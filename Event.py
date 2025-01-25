import tkinter 
from tkinter import * 
import customtkinter


#an event in a day  which holds a brief description and name
class Event():


    #-------------variables----------
    event_names = ""
    event_description = ""
    switch = 0
    dayObj = None
    
    #constructor
    def __init__(self,names,description, dayOb):
            self.event_names = names
            self.event_description = description
            self.dayObj = dayOb
       
    #visual display of events 
    def eventpage(self, events, sideframe,dayframe):
          eventframe = customtkinter.CTkFrame(sideframe, width =250, height = 100, fg_color = "transparent") 
          eventframe.pack(pady= 15)
          entry = customtkinter.CTkEntry(eventframe, width = 150, height = 20, placeholder_text=self.event_names)
          entry.pack(side = TOP, anchor = "nw")
          textbox = customtkinter.CTkTextbox(eventframe, width=250, height  = 90, corner_radius=0)
          textbox.pack()
          textbox.insert(END,self.event_description)
          entry.configure(state = "disabled")
          textbox.configure(state = "disabled")
          del_button = customtkinter.CTkButton(eventframe, text = "X", text_color ="#000000",width = 20, height = 15, fg_color= "#FFFFFF",hover_color = "#CFCFCF",font = ("Helvetica",18), command= lambda:self.delete_Event(eventframe, events, dayframe))
          del_button.pack(anchor = "se")
          divider = customtkinter.CTkLabel(master = eventframe, text="__________________________________", font=customtkinter.CTkFont(size=20, weight="bold"))
          divider.pack()
           
           
         

    #delets an event from a day 
    def delete_Event(self,button, events,dayframe):
        button.destroy()
        events.remove(self)
        if( len(events) == 0):
            dayframe.configure(fg_color = "transparent")
        if(self.dayObj == 1):
          dayframe.configure(fg_color = "#31FF6D")
          dayframe.configure(corner_radius = 10)

    




