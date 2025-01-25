import datetime
import tkinter 
from tkinter import * 
import customtkinter
import day
from day import *

#month holds a list of days
class month():
     #list of days- we wanna save this so when a month is displayed the eveents for that day are saved
    global daysInMonth 
    global week  
    global monthnames 
    global monthdays 
    global week_xpos 
    global monthframe
    global currentMonth
    
    global dayStart
    global current_time 



    
    #constructor
    def __init__(self, month):
        self.currentMonth = month
        self.daysInMonth = []
        self.week   = ['Sunday', 
                  'Monday', 
                  'Tuesday', 
                  'Wednesday', 
                  'Thursday',  
                  'Friday', 
                  'Saturday']
        self.monthnames  = ['January','February','March','April', 'May', 'June', 'July','August', 'September','October','November','December']
   
        self.monthdays = [32,29,32,31,32,31,32,32,31,32,31,32]
        self.week_xpos = []
        self.monthframe = None
        self.dayStart = 'Sunday'
        self. current_time = datetime.datetime.now()
        #saved name
        self.saveName  = "Callendata.json"


    def setMonthFrame(self,frame):
        self.monthframe = frame

    def numbDays(self):
        return len(self.daysInMonth)

    def weekDay(self,year, month, day):
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        afterFeb = 1
        if month > 2: afterFeb = 0
        aux = year - 1700 - afterFeb
        # dayOfWeek for 1700/1/1 = 5, Friday
        dayOfWeek  = 5
        # partial sum of days betweem current date and 1700/1/1
        dayOfWeek += (aux + afterFeb) * 365                  
        # leap year correction    
        dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
        # sum monthly and day offsets
        dayOfWeek += offset[month - 1] + (day - 1)               
        dayOfWeek %= 7
        self.dayStart = self.week[int(dayOfWeek)]
        return self.week[int(dayOfWeek)]

    def place_days(self,frame):
         posx = 50
         posy = 20
         
         for i in self.week:
            self.week_xpos.append(posx)
            print("tempx\n", posx)
            day_label = customtkinter.CTkLabel(frame, text=i[:1], text_color = "#FFFFFF", font=customtkinter.CTkFont(size=25,  weight="bold"))
            day_label.place(x = posx, y =posy)
            posx = posx + 145

    def place_dayFrames(self,frame,tempx,tempy,num,fr, month):
         counter = 1
    
         while(counter <num):
             
             if(len(self.daysInMonth)> counter-1 ):
                 print("this should show old months\n")
                 self.daysInMonth[counter-1].day_frame(frame,tempx,tempy,fr, month)
            
             else:
                n_day = day()
                n_day.set_name(counter)
                n_day.day_frame(frame,tempx,tempy,fr, month)
                self.daysInMonth.append(n_day)

             tempx= tempx+145
             
             if(tempx >= 920):
               print("limit met\n", tempx)
               tempx = self.week_xpos[0]-20
               tempy = tempy+ 90
              
             counter = counter + 1

    #checks the month and displays the page/calande
    def createMonth(self, frame):
            self.weekDay(self.current_time.year, self.currentMonth+1, 1)
        
            numdays = self.monthdays[self.currentMonth]

   
            mon_frame = customtkinter.CTkFrame(self.monthframe,width = 1000, height = 650 , fg_color = "#22B14C") 
            mon_frame.place(x = 50, y = 100)

            self.place_days(mon_frame)
           

            index = self.week.index(self.dayStart)
            tempx = self.week_xpos[index]-20
            tempy = 100
            self.place_dayFrames(mon_frame,tempx,tempy,numdays,frame, self.currentMonth+1)
         
        








    

    







