import datetime
from datetime import time
from pdb import pm
import random
import tkinter 
from tkinter import * 
import customtkinter

#task in planner, either a required task or a hobby.Required tasks are mandatory, hobbies are not and are assigned random times. 
class Task():

    now = datetime.datetime.now()
   
  
    weekdays=['Sun','Mon','Tues,','Wed','Thurs','Fri','Sat']
    dayTypesName = ['morning','afternoon','evening']
    taskTypeName = ['required','hobby','free']
     
    
    taskName = ""
    taskType = 0   
    dayType =  0 #morning 
    tempFrame = None


    #-----------Required----------
    startTime = None
    #endTime = None
    day = 0  #mon,tues,wed
    #------------Hobbies----------
    timesaWeek = 0
    maxHours = float(0)
    position  = 0 #before after, inbetween
    taskFrame = None

   
    def __init__(self,name,weekd,Ttype,start,end,times,maxH,dayType,pos):
     print("task created")



     self.taskName = name
     self.day = int(weekd)
     self.taskType = Ttype
   
     startN = ""
     endN = ""

     sub_list = ["PM", "AM"]
 
     # Remove substring list from String
     # Using loop + replace()
     for sub in sub_list:
        startN = start.replace(' ' + sub + ' ', ' ')
        endN = end.replace(' ' + sub + ' ', ' ')
     
     h, m = map(int, startN.split(':'))
     h1, m2 = map(int, endN.split(':'))
    
    
     

     res = time(hour=h, minute=m)
     self.startTime = res
     res2 = time(hour=h1, minute=m2)
     self.endTime = res2

     self.timesaWeek = int(times)
     self.maxHours = float(maxH)
     self.position = int(pos)
    

     if(self.taskType == 0):
         
        # print('timeeeeeee', self.startTime.hour)
         if(int(self.startTime.hour)>=12 and int(self.startTime.hour < 17)):
             self.dayType = 1
            # print ("day type is",  self.dayType )
         elif(int(self.startTime.hour>=17)):
             self.dayType = 2
             #print ("day type is",  self.dayType )
     else:
         self.dayType = int(dayType)
      
    def setName(self,name_new):
        self.taskName = name_new

    def getName(self):
        return self.taskName
           
    def returnPos(self):
        return self.position
    def setPos(self,pos):
        self.position = pos
    def printTask(self):
        if(self.taskType == 0):
            print("Task name:", self.taskName)
            print("\n")
            print("Task Type:", self.taskTypeName[self.taskType])
            print("\n")
            print("Task Day:", self.weekdays[self.day])
            print("\n")
            print("Task Start:", self.startTime)
            print("\n")
            print("Task End:", self.endTime)
            print("\n")
            print("Task day type:", self.dayTypesName[self.dayType])


        elif(self.taskType ==1):
            print("Task name:", self.taskName)
            print("\n")
            print("Task Type:", self.taskTypeName[self.taskType])
            print("\n")
            print("Task Times a Week:",self.timesaWeek)
            print("\n")
            print("Task Max Hours:",self.maxHours)
            print("\n")
            print("Task day type:", self.dayTypesName[self.dayType])
            print("\n")
            print("Task Start:", self.startTime)
            print("\n")
            print("Task End:", self.endTime)
        else:
             print("Task day type:", self.dayTypesName[self.dayType])
             print("\n")
    def getMax(self):
        return self.maxHours
    def getName(self):
         return self.taskName
    def getDay(self):
        return self.day
    def getType(self):
        return self.taskType
    def getDayType(self):
        return self.dayType
    def getEndTime(self):
        return self.endTime
    def getStartTime(self):
        return self.startTime
    def setStartTime(self,sTime):
        self.startTime = sTime
    def setEndTime(self,eTime):
        self.endTime = eTime
        #military time 

    def getFrame(self):
        return self.tempFrame

    def taskPage(self,frame):
        hours = self.startTime.hour 
        hourE = self.endTime.hour

        if self.startTime.hour >= 12:

          cycle = "pm"
          
          hours %= 12
          if self.startTime.hour  == 12:
           hours = 12
        else:
            if self.startTime.hour  == 0:
             hours = 12
            cycle = "am"
        

        if self.endTime.hour >= 12:
          cycle2 = "pm"
          hourE %= 12
          if self.endTime.hour  == 12 :
           hourE = 12
        else:
            if self.endTime.hour  == 0:
             hourE = 12
            cycle2 = "am"
        
        mins = self.getStartTime().minute
        mine = self.getEndTime().minute
        minsstr = str(self.getStartTime().minute)
        minestr = str(self.getEndTime().minute)

        
        if(mins == 0):
            minsstr  = "00"

        if(mine == 0):
            minestr = "00"
         
        

        sname = "{0}:{1} {2}-".format(hours,minsstr, cycle)
        ename = "{0}:{1} {2}".format(hourE, minestr, cycle2)
        self.descript= self.taskName +"\n" + sname + ename
        
        if(self.taskType == 0):
            self.tempFrame = customtkinter.CTkFrame(frame, fg_color = "transparent",width = 500, height =50)
            self.tempFrame.pack(side = TOP)

            task_frame = customtkinter.CTkButton(self.tempFrame, text = self.descript, text_color = "#000000",font=customtkinter.CTkFont(size=25,family = "Segoe Print" ,weight="bold"), hover_color="#279400", fg_color="transparent",width = 500,height = 100 ) 
            task_frame.pack()
        else:
            self.tempFrame = customtkinter.CTkFrame(frame, fg_color = "transparent",width = 500, height =50)
            self.tempFrame.pack(side = TOP)

            self.taskframe = customtkinter.CTkButton(self.tempFrame, text_color = "#000000", text = self.descript,font=customtkinter.CTkFont(size=25,family = "Segoe Print", weight="bold"), hover_color="#279400", fg_color="transparent",width = 500,height = 100 ) 
            self.taskframe.pack()
    def getTaskButton(self):
        return self.taskFrame
    def getDescript(self):
        return self.descript
    


 
       
