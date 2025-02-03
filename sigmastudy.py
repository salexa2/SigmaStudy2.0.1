
import tkinter as tk
from tkinter import * 
from YoutubeTranscript import get_Tran
import customtkinter
from tkinter import filedialog
import gallary 
from gallary import *
import month
from month import * 
import datetime
import WeeklyRoutinePlanner
from WeeklyRoutinePlanner import  *
import Year
from Year import *
import atexit
import threading
from threading import *
from googletrans import Translator
import asyncio




#study app that aids students in studying
#testing added 1/24/2025 

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


 # configure window
root = customtkinter.CTk() 
root.title("Sigma Study")
root.geometry(f"{1350}x{700}")


# configure grid layout (4x4)
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=3)
                


#---------------------variables-------------------

saveName = "data.json"
current_time = datetime.datetime.now()
c_language  = 0
language_list = ["en", "es", "ko"]


#----------Frames-------------
upload_frame = customtkinter.CTkFrame(root, width = 1150, height =700)
upload_frame.grid(column = 1,row =0, columnspan = 2, rowspan = 2 ,sticky = "NSEW",padx=5)

calander_frame = customtkinter.CTkFrame(root, width = 1150, height = 700) 
calander_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)
plan_frame = customtkinter.CTkScrollableFrame(root, width = 1150, height =700) 
plan_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)
settings_frame = customtkinter.CTkFrame(root, width = 1150, height = 700) 
settings_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)
home_frame = customtkinter.CTkFrame(root, width = 1150, height = 700) 
home_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)

#---------buttons/labels---------
sidebar_button_1 = None
sidebar_button_2 = None
sidebar_button_3 = None
sidebar_button_4 = None
sidebar_button_5 = None
sidebar_button_6 = None
appearance_mode_optionemenu = None
language_optionemenu = None
create_set_button = create_set_button = customtkinter.CTkButton(upload_frame, text= "Create Set", fg_color= "#279400", hover_color="#1C6B00", command = lambda: gally.create_Set(upload_frame, create_set_button))
link_button  =  link_button = customtkinter.CTkButton(upload_frame, text= "Enter", fg_color= "#279400", hover_color="#1C6B00", width = 50, height = 28)
upload_file_button =  customtkinter.CTkButton(upload_frame, text= "Text Upload", fg_color= "#279400", hover_color="#1C6B00")
gen_button = customtkinter.CTkButton(plan_frame, text = "Generate", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: RequiredForm(plan_frame,planner, gen_button))
settings_label = customtkinter.CTkLabel(settings_frame, text="Settings", font=customtkinter.CTkFont(size=20, weight="bold"))
scale_label = customtkinter.CTkLabel(settings_frame, text="Change window size:")
side_label = customtkinter.CTkLabel( calander_frame, text="Events", font=customtkinter.CTkFont(size=20, weight="bold"))
home_txt = "Thank you for using Study Sigma! Study Sigma is an innovative app that aims to revolutionize the way students study by providing a set of tools that enable to study effeciently. The data is stored when you close the program, so no need to worry about losing your data! This is our first app and it was created for a college software engineering project, any feedback is greatly appreaciated!\n\nHere's a list of the tools at your disposal:\n\n\nSummary - This allows you to upload text and Youtube links which then enable you to summarize a video and or create flashcards. The Longer the video, the longer it takes to get a summary.\n\nFlashcard Gallary - Display and modify your flashcard sets. \n\n\nCalender - Keep track of upcoming deadlines by adding and removing events from an automatically up to date calender.\n\n\nRoutine Planner - Generate a weekly routine by inputing required tasks such as a class or job and/or hobbies.\nOnce the generate button is clicked, a new routine will be created and showed.\n\n\nSettings - Change the Scaling of the objects on the screen (For those with bigger/smaller devices.\n\nFAQ:\n'Why is the Page Not Refresing?'\n~Click on the Page button to refresh it's contents!\n'What Languages Are there?'\n~Languages: English, Spanish, Korean\n~It takes a second to change the language, please wait...\n'My Card is not adding to a set?'\n~Click the '+' to add a card to a set, then done when you're finished.\n'I am missing an extra hobby?'\n~If a Hobby is not added, it's because the time of day it was meant to be added to was full and it was removed.\n'I Changed the language and switched back, but now the text is different?'\n~Warning: Google Translate is used to translate the text, the text will be different from orignal as Google Translate is not perfect. Don't worry, the language will reset to default when you close the app.\n_________________________________________________________________________________________________________________\n\nDevelopers: "
home_label = customtkinter.CTkLabel(home_frame, text= "HOME", justify = "left", font=customtkinter.CTkFont(size=40, weight="bold"))
developers = "Shadai Alexander (Git:https://github.com/salexa2), Chase Walters (Git:https://github.com/ChaseWalters)\n\nContact: salexa2@gmu.edu\n\nReleased 2023"
monthmenu = customtkinter.CTkOptionMenu(calander_frame, fg_color = "#279400",  button_color = "#279400", dropdown_hover_color = "#1C6B00" , width = 40,
     height = 25,values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
     font=customtkinter.CTkFont(size=20))
    
 
#----------------Object-------------------
gally = gallary(root)
year = Year(current_time.month)
planner = WeeklyRoutinePlanner()



def exit_handler():
    year.saveCall()
    gally.saveSets()
    planner.savePlanner()

#On exit Function caller
atexit.register(exit_handler)

#-------------------functions-----------------------
def change_appearance_mode_event( new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
 

def file_open():
    #gets the video
    root.filename = filedialog.askopenfilename(title="Select Video", filetypes=(("txt files", "*.txt"),))
    if (len(root.filename) == 0): 
        return None
        
    return root.filename


       

#opens a text file and displays it in text field.
def openf(default_text):
   
    text_File = file_open()
    if(text_File != None):
         text_temp = open(text_File, 'r')
         text = text_temp.read()
         default_text.insert(END,text)
         text_temp.close()

#takes in a link to a video, gets a transcript from it, converts it to text 
def getLink(linkbar, default_text):
    script = get_Tran(linkbar)
    default_text.delete( "0.0", END)
    default_text.insert(END,script)
   
    #use openf to open the newly created text file

def summarize(url,default_text,button):
    print("summary")
    



    
def optionmenu_callback(choice):
    customtkinter.deactivate_automatic_dpi_awareness()
    customtkinter.set_widget_scaling(float(choice))  

def optionmenu_callback(choice):
    customtkinter.deactivate_automatic_dpi_awareness()
    customtkinter.set_widget_scaling(float(choice))  

def config(sum_button):
    print("configure the buttons\n")

   
    sum_button.configure(state = "disabled")
    sum_button.configure(text = "Summarizing...Please Wait")
    sidebar_button_1.configure(state = "disabled")
    sidebar_button_2.configure(state = "disabled")
    sidebar_button_3.configure(state = "disabled")
    sidebar_button_4.configure(state = "disabled")
    sidebar_button_5.configure(state = "disabled")
    sidebar_button_6.configure(state = "disabled")
    appearance_mode_optionemenu.configure(state = "disabled")
    language_optionemenu.configure(state = "disabled")
    create_set_button.configure(state = "disabled")
    link_button.configure(state = "disabled")
    upload_file_button.configure(state = "disabled")
    
    print("button configured\n")
    return 
def configOn(sum_button):
    sum_button.configure(state = "enabled")
    sum_button.configure(text = "Summarize")
    sidebar_button_1.configure(state = "enabled")
    sidebar_button_2.configure(state = "enabled")
    sidebar_button_3.configure(state = "enabled")
    sidebar_button_4.configure(state = "enabled")
    sidebar_button_5.configure(state = "enabled")
    sidebar_button_6.configure(state = "enabled")
    appearance_mode_optionemenu.configure(state = "enabled")
    language_optionemenu.configure(state = "enabled")
    create_set_button.configure(state = "enabled")
    link_button.configure(state = "enabled")
    upload_file_button.configure(state = "enabled")
    

#-------------------pages---------------



async def upload_page():
   
   upload_frame.lift()
 
   default_text = customtkinter.CTkTextbox(upload_frame,width=600,height= 650, font = ("Helvetica", 16))
   default_text.place(x= 50, y=100)

   upload_file_button.place(x=100, y=50)
   upload_file_button.configure(command = lambda:openf(default_text))

   #LINK ENTRY 
   link_entry = customtkinter.CTkEntry(master=upload_frame, placeholder_text="Youtube Link")
   link_entry.place(x = 250, y =50)

   link_button.place(x= 390, y=50)
   link_button.configure(command = lambda:getLink(link_entry.get(),default_text))
   #----------------------

   print("Unit Testing 2.0: Gallary should create a set\n")
   create_set_button.place(x=450, y=50)


   #CREATE ENTRY BUTTON 
   summarize_button = customtkinter.CTkButton(upload_frame, text="Summarize", fg_color="#279400", hover_color="#1C6B00", command=lambda:summarize(link_entry.get(),default_text,summarize_button))
   summarize_button.place(x=600, y=50)

   translator = Translator()
   print("Unit Testing 1.0: Upload page: upload page should show\n")
   l = [upload_file_button,link_button,create_set_button,summarize_button]
   print(c_language)
   
   for child in l:
        text = child.cget("text")
        if text is not None:
            translated_text =  await translator.translate(text, dest= language_list[c_language])
            print(translated_text.text)
            child.configure(text= translated_text.text)
   

def on_upload_button_click():

    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if asyncio.get_event_loop().is_running():
        root.after(100, lambda: asyncio.create_task(upload_page()))  # Schedule async task
    else:
        asyncio.run(upload_page())


def on_plan_page_click():
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if asyncio.get_event_loop().is_running():
        root.after(100, lambda: asyncio.create_task(plan_page()))  # Schedule async task
    else:
        asyncio.run(plan_page())




gallary_frames = []
def gallary_page(): 
   for g in gallary_frames:
       g.destroy()
   gallary_frame = customtkinter.CTkFrame(root, width = 1150, height = 700) 
   gallary_frame.grid(column = 1,row =0 ,sticky = "NSEW",padx=5)
   gallary_frames.append(gallary_frame)
   gally.set_galFrame(gallary_frame)
  
   gally.loadSets()                       

   print("Unit Testing 3.0: Gallary page: gallary page should show\n")
   gally.print_size()
   gally.print_Gal()
   gally.createButtons(gallary_frame)

  
   if(gally.getSize()>0):
       gally.display(gallary_frame)
  

  


def calander_page():  
     calander_frame.lift()
    
     side_label.place(x=1150,y=70)
    
     
     side_taskframe = customtkinter.CTkFrame(calander_frame, width = 250, height = 650) 
     side_taskframe.place(x = 1060, y = 100)

     year.setMonthFrame(calander_frame)
     year.showMonth(side_taskframe)
     #year.loadCall()

     optionmenu_var = customtkinter.StringVar(value=year.getCurrMonth())
     #display month 
     monthmenu.place(x = 500, y = 50)
     monthmenu.configure(command = lambda choice: year.setMonth(choice,side_taskframe))
     monthmenu.configure(variable = optionmenu_var)

     translator = Translator()
     l = [side_label]
     for child in l:
        text = child.cget("text")
        if text is not None:
            translated_text = translator.translate(text, dest= language_list[c_language])
            print(translated_text.text)
            child.configure(text= translated_text.text)



def helperP(planner,form_frame):
    if(planner.checkV()==False):
        if(planner.getValues()==False):
         planner.formPage(form_frame)


def helperP2(planner,form_frame,next_button):
    if(planner.checkV()==False):
        if(planner.getValues()==False):
            if(planner.getValuesH() == False):
              print("hobby show")
              planner.hobbyPage(form_frame,next_button)
           
           


def RequiredForm(plan_frame,planner,gen):

     planner.reset()
     print("form should show")
     gen.configure(state = "disabled")
     temp_frame = customtkinter.CTkFrame(plan_frame, width = 1150, height =750) 
     temp_frame.pack()

     next_button = customtkinter.CTkButton(temp_frame, text = "add Task", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: helperP(planner,form_frame))
     next_button.pack(anchor= "n", pady = 15)
     hobby_button = customtkinter.CTkButton(temp_frame, text = "Add Hobbies", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda:helperP2(planner,form_frame,next_button))
     hobby_button.pack(anchor= "n", pady = 15)
     done_button = customtkinter.CTkButton(temp_frame, text = "Done", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: planner.printPlan(temp_frame, gen))
     done_button.pack(anchor = "n", pady = 15)
     
     form_frame = customtkinter.CTkScrollableFrame(temp_frame, width = 1150, height = 700) 
     form_frame.pack(side=TOP)

   
     
     planner.formPage(form_frame)
   


async def plan_page():
     
     plan_frame.lift()
     planner.planner_getFrame(plan_frame)
     planner.displayPlan()
     gen_button.pack(pady = 19)
     planner.show_All()
     translator = Translator()
     l = [gen_button]
     for child in l:
        text = child.cget("text")
        if text is not None:
            translated_text = await translator.translate(text, dest= language_list[c_language])
            print(translated_text.text)
            child.configure(text= translated_text.text)

     
     
def settings_page():
     settings_frame.lift()
     settings_label.place(x=40,y=30)
     scale_label.place(x=40,y=80)
     scaling = customtkinter.CTkOptionMenu(settings_frame, fg_color = "#279400",  button_color = "#279400", dropdown_hover_color = "#1C6B00" , width = 140, height = 25,values=[".2", ".4",".5", ".6", ".8","1", "1.2","1.3","1.4",  "1.5" , "1.6" , "1.8", "1.9", "2"], command =  optionmenu_callback)
     scaling.place(x= 40,y=125)

     translator = Translator()
     n = [settings_label,scale_label]
     for child in n:
        text = child.cget("text")
        if text is not None:
            translated_text = translator.translate(text, dest= language_list[c_language])
            child.configure(text = translated_text.text)
     
            
            

async def home_Page():
    home_frame.lift()
    home_label.place(x = 550, y = 40)
    default_text = customtkinter.CTkTextbox(home_frame, width=1115,height= 650, font = ("Helvetica", 18))
    default_text.place(x = 100, y = 100)
    default_text.insert("0.0",home_txt)
    
    translator = Translator()
    l = [home_label]
    n = [default_text]

    for child in l:
        text = child.cget("text")
        if text is not None:
            translated_text = await translator.translate(text, dest= language_list[c_language])
            print(translated_text.text)
            child.configure(text= translated_text.text)
    for child2 in n:
        text1 = child2.get("0.0", END)
        if text1 is not None:
            translated_text1 = await translator.translate(text1, dest= language_list[c_language])
            print(translated_text1.text)
            child2.delete("0.0", END)
            child2.insert("0.0",translated_text1.text)
    child2.insert(END,developers)
    default_text.configure(state ="disabled")





       

# create sidebar frame with widgets
sidebar_frame = customtkinter.CTkFrame(root, width=200, height = 800)
sidebar_frame.grid(column =0, row=0, sticky = "NSEW")
#sidebar_frame.grid_rowconfigure(5, weight=1)




#Menu Label 
logo_label = customtkinter.CTkLabel(sidebar_frame, text="MENU", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.place(x = 60, y =10)

sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, text= "Summary", fg_color= "#279400", hover_color="#1C6B00", command= on_upload_button_click)
sidebar_button_1.place(x = 20, y = 50)

sidebar_button_2 = customtkinter.CTkButton(sidebar_frame, text= "Flash Card Gallary",fg_color= "#279400",hover_color="#1C6B00", command=gallary_page)
sidebar_button_2.place(x = 20, y = 100)

sidebar_button_3 = customtkinter.CTkButton(sidebar_frame, text= "Calendar",fg_color= "#279400",hover_color="#1C6B00",command= calander_page)
sidebar_button_3.place(x = 20, y = 150)

sidebar_button_4 = customtkinter.CTkButton(sidebar_frame, text= "Generator",fg_color= "#279400",hover_color="#1C6B00", command = on_plan_page_click)
sidebar_button_4.place(x = 20, y = 200)

sidebar_button_5 = customtkinter.CTkButton(sidebar_frame, text= "Settings",fg_color= "#279400",hover_color="#1C6B00", command = settings_page)
sidebar_button_5.place(x = 20, y = 250)

sidebar_button_6 = customtkinter.CTkButton(sidebar_frame, text= "Home",fg_color= "#279400",hover_color="#1C6B00", command = home_Page)
sidebar_button_6.place(x = 20, y = 300)

#Appearance mode change 
appearance_mode_label = customtkinter.CTkLabel(sidebar_frame, text="Appearance Mode:",  anchor="w")
appearance_mode_label.place(x = 20, y = 600)
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame,fg_color= "#279400", button_color= "#279400",button_hover_color= "#1C6B00", values=["Light", "Dark", "Default"],command=change_appearance_mode_event)
appearance_mode_optionemenu.place(x = 20, y = 650)
language_mode_label = customtkinter.CTkLabel(sidebar_frame, text="Language Mode:",  anchor="w")
language_mode_label.place(x = 20, y = 700)


widgetshold = [logo_label,sidebar_button_1,sidebar_button_2,sidebar_button_3,sidebar_button_4,sidebar_button_5,sidebar_button_6,appearance_mode_label,language_mode_label]

c_language = 0
def changeLanguage(choice):
  global c_language
  translator = Translator()
  if choice == "English":
     
      c_language = 0
      for child in widgetshold:
        text = child.cget("text")
        if text is not None:
            translated_text = translator.translate(text, dest= language_list[c_language])
            print(translated_text.text)
            child.configure(text= translated_text.text)

  if choice == "Español": 
      c_language = 1
      for child in widgetshold:
        text = child.cget("text")
        if text is not None:
            translated_text = translator.translate(text, dest= language_list[c_language])
            print(translated_text.text)
            child.configure(text= translated_text.text)
  if choice == "한국어": 
      c_language = 2
      for child in widgetshold:
        text = child.cget("text")
        if text is not None:
            translated_text = translator.translate(text, dest= language_list[c_language])
            print(translated_text.text)
            child.configure(text= translated_text.text)

            

  


language_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame,fg_color= "#279400", button_color= "#279400",button_hover_color= "#1C6B00", values=["English", "Español", "한국어"], command = lambda choice:changeLanguage(choice))
language_optionemenu.place(x = 20, y = 750)




if __name__ == "__main__":
    asyncio.run(home_Page())


root.mainloop()
      


