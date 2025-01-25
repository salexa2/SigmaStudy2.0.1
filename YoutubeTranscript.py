from typing import Final, final
from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead






def get_Tran(vid_url):
    vid_id = re.search(r"v=([^&]+)", vid_url).group(1)
    print("Video ID:",vid_id)
    #extract the text
    data = yta.get_transcript(vid_id)
    #clean up transcript alittle
    transcript = ''
    for value in data:
        for key,val in value.items():
            if key == 'text':
                transcript += val
    l = transcript.splitlines()
    final_tra = " ".join(l)
    final_tra = clean_Script(final_tra)
    return final_tra

def clean_Script(transcript):
    # Remove timestamps
    transcript = re.sub(r'\[\d+:\d+\]', '', transcript)
    # Remove non-textual elements
    transcript = re.sub(r'\[.*?\]', '', transcript)
    # Remove extra spaces
    transcript = re.sub(r'\s+', ' ', transcript)
    # Remove leading and trailing spaces
    transcript = transcript.strip()
    #Remove padding keyword
    transcript = re.sub(r'\<.*?\>', '', transcript)
    return transcript

def summarizing(script):
    tokenizer = AutoTokenizer.from_pretrained('t5-base', model_max_length = 1024)
    model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict = True)
    sequence = (script)
    inputs = tokenizer.encode("summarize: "+ sequence,return_tensors = 'pt', max_length= 1024, truncation = True)
    outputs = model.generate(inputs,max_length = 600, min_length = 500 ,length_penalty = 2.,num_beams = 2)
    summary = tokenizer.decode(outputs[0])
    summary = clean_Script(summary)
    return summary
    