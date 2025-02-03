from youtube_transcript_api import YouTubeTranscriptApi as yta
import re





def get_Tran(vid_url):
    import re

def get_Tran(vid_url):
    if not vid_url:
        raise ValueError("Video URL is empty or None")
    
    # Perform the regex search
    match = re.search(r"v=([^&]+)", vid_url)
    
    if match:
        vid_id = match.group(1)
        print("Video ID:", vid_id)
    else:
        raise ValueError("Could not extract video ID from the URL")

    # Extract the transcript using the video ID
    data = yta.get_transcript(vid_id)
    
    # Clean up the transcript a little
    transcript = ''
    for value in data:
        for key, val in value.items():
            if key == 'text':
                transcript += val
                
    # Clean up the transcript further
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

    