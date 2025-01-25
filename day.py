import tkinter 
from tkinter import * 
import customtkinter
import Event
from Event import *
import datetime

#day object holda a lits of events
class day():

    #----------VARIABLES--------
    global day_name
    global events 
    global month
    global d_frame
    global currd

    def __init__(self):
       self.day_name = 1
       self.events = []
       self.month = 1
       self.d_frame = None
       self.currd = 0 
    #sets the name of a day object
    def set_name(self,name):
        self.day_name = name

    def get_events(self):
        return self.events

    def get_d_frame(self):
        return self.d_frame
    #visual representation of day object
    def day_frame(self, month_frame,posx,posy, frame, framemonth):
       d_frame = customtkinter.CTkButton(month_frame, text_color = "#FFFFFF", text = self.day_name,font=customtkinter.CTkFont(size=25, weight="bold"), hover_color="#DBDBDB", fg_color="transparent",width = 50,height = 50, command =lambda: self.event_display(frame , d_frame) ) 
       d_frame.place(x = posx, y= posy)
       current_time = datetime.datetime.now()
       self.month = framemonth
       if(self.day_name == current_time.day and self.month == current_time.month):
           d_frame.configure(fg_color = "#31FF6D")
           d_frame.configure(corner_radius = 10)
           self.currd = 1
       self.d_frame = d_frame
       if(len(self.events)>0):
           self.d_frame.configure(fg_color = "#167030")
       

    #displays the events in side bar
    def event_display(self,frame, day_frame):
        
       side_taskframe = customtkinter.CTkScrollableFrame(frame, width = 230, height = 650, fg_color = "transparent") 
       side_taskframe.place(x = 0, y = 0)
       label = customtkinter.CTkLabel(side_taskframe, text="Day " + str(self.day_name), font=customtkinter.CTkFont(size=20, weight="bold"))
       label.pack(anchor = CENTER)
       add_button = customtkinter.CTkButton(side_taskframe, text = "Add Event", text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF",font = ("Helvetica",18), command= lambda:self.add_page(side_taskframe,frame, day_frame, add_button))
       add_button.pack(fill = X, pady = 2)
 
       
       for e in self.events:

           e.eventpage(self.events,side_taskframe,day_frame)
           
    #displays a page to add an event to a day
    def add_page(self,frame, basefr, day_frame, add):
        add.configure(state = "disabled")
        eventframe = customtkinter.CTkFrame(frame, width =250, height = 100, fg_color = "transparent") 
        eventframe.pack(side = TOP,anchor = "nw", pady = 15 )
        entry = customtkinter.CTkEntry(eventframe, width = 150, height = 20, placeholder_text="Event Name")
        entry.pack(side = TOP, anchor = "nw")
        textbox = customtkinter.CTkTextbox(eventframe, width=250, height  = 90, corner_radius=0)
        textbox.pack()
        textbox.insert(END,"Enter Definition")
        done_button = customtkinter.CTkButton(eventframe, text = "Done", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: self.add_event(entry,textbox,eventframe, basefr, day_frame))
        done_button.pack(side = TOP,fill = X, expand = True, padx = 10, pady = 10)
    #addds event to events list 
    def add_event(self,entry, textbox, frame,basefr, day_frame):
        day_frame.configure(fg_color = "#167030")
        self.events.append(Event(entry.get(),textbox.get("1.0",END), self.getCurrD()))
        frame.destroy()
        self.event_display(basefr, day_frame)
        self.d_frame = day_frame
        
    def getCurrD(self):
        return self.currd
        

   
