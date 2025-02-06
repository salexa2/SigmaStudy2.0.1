

from operator import truediv
from ssl import DefaultVerifyPaths
import Weekday
from Weekday import *
import tkinter 
from tkinter import * 
import customtkinter
import random 
from datetime import *
from SaveAndLoad import *

#planner that generates a routine for a user
class WeeklyRoutinePlanner():

#------------------------------------------VARIABLES-----------------
 #---------wiget values assigned------
 savedValues = []
 task_frame = None
 taskName = ""
 taskSTime =""
 taskETime = None
 days= []
 planner = []
 #check buttons for the required task form
 Checkbutton1 = None
 Checkbutton2 = None 
 Checkbutton3 = None
 Checkbutton4 = None
 Checkbutton5 = None 
 Checkbutton6 = None
 Checkbutton7 = None
 #time we get from the required task button
 military_time = ""
 military_time2 = ""
 #tempPlanner = planner

 #Default Task values
 currentType = 0
 task_frame = None     
 hobbyName = None
 times = -1
 maxx = -1
 when = -1
 pos = -1
 present = 0
 #holds the plan frame
 mainf = None
 #Tells us if the user clicked any days for required task
 switch = -1
 #Error types 
 errorType = ['*Incomplete Task!*','!PM/AM Invalid!*', '*Invalid Time Format!-H:M AM/PM(Spaced)*', '*Conflicting Times!*']
 error = None 
 hobbysize = 0
 help_button_  = None
 help_button_2 = None
 help_button_3 = None
 help_button_4 = None


 #saved name - DO NOT TOUCH THIS
 saveName  = "PlannerData.json"

 #----------------------------VARIABLE END--------------------

 #-------------------------CONSTRUCTOR--------------------
 def __init__(self):
     if(self.loadPlanner() == False):
        self.planner = [Weekday(0),Weekday(1),Weekday(2),Weekday(3),Weekday(4),Weekday(5),Weekday(6)]

     


 #-------------------FORMS-------------------#
 
 def planner_getFrame(self,p):
     for i in self.planner:
        i.createFrames(p)

 #Displays the hobby form
 def hobbyPage(self,form_frame,nextbutton):
     self.currentType = 1
     self.hobbysize = self.hobbysize+1
     nextbutton.configure(state = "disabled")
     optionmenu_var = customtkinter.StringVar(value="Times a Week")
     optionmenu_var1 = customtkinter.StringVar(value="Max Hours a Day")
     optionmenu_var2 = customtkinter.StringVar(value="Time of Day")
     optionmenu_var3 = customtkinter.StringVar(value="When Would You  Want to do your Hobbies?")
 

     hobby_frame = customtkinter.CTkFrame(form_frame, fg_color = "#279400", width = 1000, height = 100) 
     hobby_frame.pack(side = TOP)

     self.help_button_3 = customtkinter.CTkLabel(hobby_frame, text= "〶", text_color = "#FFFFFF",font=customtkinter.CTkFont(size=28, weight="bold"))
     self.help_button_3.place(x = 190, y = 10)
     self.help_button_4 = customtkinter.CTkLabel(hobby_frame, text= "", text_color = "#FFFFFF",width = 40)
     self.help_button_4.place(x =250, y = 10)


     self.help_button_3.bind("<Enter>", self.on_enterh)
     self.help_button_3.bind("<Leave>", self.on_leaveh)

     self.taskName = customtkinter.CTkEntry(master=hobby_frame, placeholder_text="Hobby Name")
    
     self.taskName.place(x = 10, y = 10)

     combobox1 = customtkinter.CTkOptionMenu(hobby_frame, fg_color = "#FFFFFF", text_color = "#000000", dropdown_text_color = "#000000",button_color= "#E3E3E3" , button_hover_color = "#E3E3E3", dropdown_fg_color = "#FFFFFF", dropdown_hover_color = "#E3E3E3",font = ("Helvetica",18),  width = 20, height = 25,values=['1','2','3','4','5','6','7'] ,command = self.optionmenu_callbackT ,variable = optionmenu_var)
     combobox1.place(x=10,y=55)

     combobox2 = customtkinter.CTkOptionMenu(hobby_frame,   fg_color = "#FFFFFF", text_color = "#000000",dropdown_text_color = "#000000",button_color= "#E3E3E3", button_hover_color = "#E3E3E3",dropdown_fg_color = "#FFFFFF",dropdown_hover_color = "#E3E3E3",font = ("Helvetica",18) , width = 30, height = 25,values=['1','2','3','4','5','6','7'], command = self.optionmenu_callbackM,variable = optionmenu_var1)
     combobox2.place(x=190,y=55)

     combobox3 = customtkinter.CTkOptionMenu(hobby_frame,  fg_color = "#FFFFFF", text_color = "#000000",dropdown_text_color = "#000000", button_color= "#E3E3E3",button_hover_color = "#E3E3E3",dropdown_fg_color = "#FFFFFF", dropdown_hover_color = "#E3E3E3",font = ("Helvetica",18) , width = 30, height = 25,values=["Morning", "Afternoon", "Evening"], command = self.optionmenu_callbackW,variable = optionmenu_var2)
     combobox3.place(x=390,y=55)

     combobox4 = customtkinter.CTkOptionMenu(hobby_frame ,  fg_color = "#FFFFFF", text_color = "#000000", dropdown_text_color = "#000000",button_color= "#E3E3E3", button_hover_color = "#E3E3E3",dropdown_fg_color = "#FFFFFF", dropdown_hover_color = "#E3E3E3",font = ("Helvetica",18) , width = 30, height = 25,values=["Before", "After", "Between"], command = self.optionmenu_callbackP, variable = optionmenu_var3)
     combobox4.place(x= 550,y=55)
    
     divider = customtkinter.CTkLabel(master = form_frame, text="___________________________________________________________________________________________________________________________________________________________________________________________", font=customtkinter.CTkFont(size=20, weight="bold"))
     divider.pack()
  
 def on_enter(self, event):
        self.help_button_2.configure(text="*Time Fomat:[H:M AM/PM], Required Tasks have an assigned time.\n Add Your Required Tasks first! Tasks are unsorted.")

 def on_leave(self, enter):
        self.help_button_2.configure(text="")
 
 def on_enterh(self, event):
        self.help_button_4.configure(text="*Hobbies are not mandatory and will be assigned a random time.")

 def on_leaveh(self, enter):
        self.help_button_4.configure(text="")


 def loadPlanner(self):
    loader = SaveAndLoad.load_data(self.saveName);
    if loader is None:
        print("no saved data found")
        return False
    self.planner = loader.copy();
    return True

 def savePlanner(self):
    SaveAndLoad.save_data(self.planner,self.saveName)

 #Displays the Requirement form
 def formPage(self,form_frame):
     self.switch = -1
     self.currentType = 0
     #task boxes 

   
     
     

     self.task_frame = customtkinter.CTkFrame(form_frame, fg_color = "#279400", width = 1000, height = 100) 
     self.task_frame.pack(side = TOP)
     
     self.help_button_ = customtkinter.CTkLabel(self.task_frame, text= "〶", font=customtkinter.CTkFont(size=28, weight="bold"), text_color = "#FFFFFF")
     self.help_button_.place(x = 550, y = 10)
     self.help_button_2 = customtkinter.CTkLabel(self.task_frame, text= "", width = 40, text_color = "#FFFFFF")
     self.help_button_2.place(x =595, y = 10)


     self.help_button_.bind("<Enter>", self.on_enter)
     self.help_button_.bind("<Leave>", self.on_leave)

     self.taskName = customtkinter.CTkEntry(master=self.task_frame, placeholder_text="Required Task Name")
     self.taskName.place(x = 10, y = 10)

     self.error = customtkinter.CTkLabel(master = self.task_frame, text="", text_color ="#FF0000",font=customtkinter.CTkFont(size=10, weight="bold")) 

     self.taskSTime = customtkinter.CTkEntry(master=self.task_frame, placeholder_text="Task Start Time")
     self.taskSTime.place(x = 200, y = 10)
     self.taskETime = customtkinter.CTkEntry(master=self.task_frame, placeholder_text="Task End Time")
     self.taskETime.place(x = 400, y = 10)

     

     self.Checkbutton1 =  BooleanVar(form_frame)
     self.Checkbutton1.set(False)
     self.Checkbutton2 =  BooleanVar(form_frame)
     self.Checkbutton2.set(False)
     self.Checkbutton3 =  BooleanVar(form_frame)
     self.Checkbutton3.set(False)
     self.Checkbutton4 =  BooleanVar(form_frame)
     self.Checkbutton4.set(False)
     self.Checkbutton5 =  BooleanVar(form_frame)
     self.Checkbutton5.set(False)
     self.Checkbutton6 =  BooleanVar(form_frame)
     self.Checkbutton6.set(False)
     self.Checkbutton7 =  BooleanVar(form_frame)
     self.Checkbutton7.set(False)
     

  
     Button1 = customtkinter.CTkCheckBox(self.task_frame, text = "Sunday", 
                          variable = self.Checkbutton1,
                          onvalue = True,
                          offvalue = False,
                          height = 2, 
                          width = 10, text_color = "#FFFFFF", font = ("Helvetica",18))
  
     Button2 = customtkinter.CTkCheckBox(self.task_frame, text = "Monday",
                          variable = self.Checkbutton2,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10,  text_color = "#FFFFFF", font = ("Helvetica",18))
  
     Button3 = customtkinter.CTkCheckBox(self.task_frame, text = "Tuesday",
                          variable = self.Checkbutton3,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10,   text_color = "#FFFFFF", font = ("Helvetica",18))
     Button4 = customtkinter.CTkCheckBox(self.task_frame, text = "Wednesday",
                          variable = self.Checkbutton4,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10,   text_color = "#FFFFFF", font = ("Helvetica",18))
     Button5 = customtkinter.CTkCheckBox(self.task_frame, text = "Thursday",
                          variable = self.Checkbutton5,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10,  text_color = "#FFFFFF", font = ("Helvetica",18))  
     Button6 = customtkinter.CTkCheckBox(self.task_frame, text = "Friday",
                          variable = self.Checkbutton6,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10, text_color = "#FFFFFF", font = ("Helvetica",18))  
     Button7 = customtkinter.CTkCheckBox(self.task_frame, text = "Saturday",
                          variable = self.Checkbutton7,
                          onvalue = True,
                          offvalue = False,
                          height = 2,
                          width = 10,text_color = "#FFFFFF", font = ("Helvetica",18))

     Button1.place(x = 10, y = 60)
     Button2.place(x = 120, y = 60)
     Button3.place(x = 220, y = 60)
     Button4.place(x = 330, y = 60)
     Button5.place(x = 460, y = 60)
     Button6.place(x = 570, y = 60)
     Button7.place(x = 680, y = 60)

     
     
     divider = customtkinter.CTkLabel(master = form_frame, text="___________________________________________________________________________________________________________________________________________________________________________________________", font=customtkinter.CTkFont(size=20, weight="bold"))
     divider.pack()

#-------------------------FUNCTIONS---------------------------
 #clears the weekdays                     
 def clearA(self):
     for i in self.planner:
         i.cleartypes()
 

 #Displays planner at start 
 def displayPlan(self)  :
     if(self.present == 0):
         for i in self.planner:
             i.getweekFrame()
     return
 #randomizes the hobbies- LEFT OUT
 def randomGen(self):
     for h in self.planner:
         h.randomize()
     self.savePlanner()
#prints plan to terminal
 def printValues(self):

     for i in self.savedValues:
         print("weekday num:",i)

     print ("name", self.taskName.get())
     print ("taskSTime", self.taskSTime.get())
     print("taskETime", self.taskETime.get())
#Displays plan in planner
 def printPlan(self,frame,gen):
     self.present = 0
     self.savePlanner()
     if(self.currentType == 0):
          self.getValues()
     else:
         if(self.times>0):  # if user even entered anything 
            self.getValuesH() #saves any h values
    
     print("WEEKLY ROUTINE\n")
     self.show_All()
     
     frame.destroy()
     gen.configure(state = "normal")


 def show_All(self):
     if(self.present == 0):
         for m in self.planner:
              m.showAll()
         self.present = 1
 #Clears a planner
 def reset(self):
    self.clearA()
    self.present = 0
    #self.savePlanner()
 #Hobby-gets the times of day from a hobby
 def optionmenu_callbackT(self,choice):#times a day
    #print("optionmenuT dropdown clicked:", choice)
    self.times = int(choice)
 
 #Hobby-gets the max hours for a hobby 
 def optionmenu_callbackM(self,choice):
  #  print("optionmenu dropdown clicked:", choice)
    self.maxx = int(choice)
#Hobby- Gets the time of day for a hobbu
 def optionmenu_callbackP(self,choice):
   # print("optionmenuP dropdown clicked:", choice)

    if(choice == "Before"):
         self.pos ='0'
    elif(choice == "After"):
         self.pos ='1'
    elif(choice == "Between"):
         self.pos = '2'
#Hobby- Gets times a week hobby is done
 def optionmenu_callbackW(self,choice):
    #print("optionmenuW dropdown clicked:", choice)
    if(choice == "Morning"):
         self.when ='0'
    elif(choice == "Afternoon"):
         self.when ='1'
    elif(choice == "Evening"):
         self.when = '2'
 
  #--------------------------VERFICIATION/ADD VALUE FUNCTIONS----------
 #Checks if the task name is empty
 def checkV(self):
     if(self.taskName.get()==""):
           print("Unit Testing: Task Name is Empty!--CheckV function\n")
           self.error.place(x = 880, y= 5)
           self.error.configure(text = self.errorType[0])
           return True
     
     return False
      

 #Checks for incorrect format in time
 def addRValues(self): # 0, 1, 3
                #verification
               print("Unit Testing: Verification started\n")
               if(self.currentType == 1):
                   print("Unit Testing: This task is a hobby, bypass verification!!\n")
                   return False
               try:
                   #If user enters AM-PM, error will occur.
                   if("PM" in self.taskSTime.get()):
                        if("AM" in self.taskETime.get()):
                            print("Unit Testing: AM/PM ERROR--AddRValues function")
                            self.error.place(x = 880, y= 5)
                            self.error.configure(text = self.errorType[1])
                            return True
                   self.military_time = datetime.strptime(self.taskSTime.get(), '%I:%M %p').strftime('%H:%M')
                   self.military_time2 = datetime.strptime(self.taskETime.get(), '%I:%M %p').strftime('%H:%M')
                   
               except:
                            print("Unit Testing: Invalid Time Formats")
                            self.error.place(x = 750, y= 5)
                            self.error.configure(text = self.errorType[2])
                            return True    
               else:
                   #checks for time conflicts and then adds to planner
                    return self.verifyTwo()        
                   
                
                    
                   
                
 # Final Checks for time conflicts or any wonky business with        
 def  verifyTwo(self):
                    #User did not put in any days
                    if(self.switch == -1):
                     print("Unit Testing: Days is Empty!--verifyTwo function\n")
                     self.error.place(x = 880, y= 5)
                     self.error.configure(text = self.errorType[0])
                     return True

                    sub_list = ["PM", "AM"]
                    for sub in sub_list:
                        startN = self.military_time.replace(' ' + sub + ' ', ' ')
                        endN = self.military_time2.replace(' ' + sub + ' ', ' ')
     
                    h, m = map(int, startN.split(':'))
                    h1, m2 = map(int, endN.split(':'))

                    #if start hour greater than second or if equal check the minute
                  #  print("h:",h)
                  #  print("h1:",h1)
                    if(h>h1):
                         self.error.place(x = 880, y= 5)
                         self.error.configure(text = self.errorType[3])
                         return True
                    elif(h==h1):
                        if(m >m2 or m == m2):
                            self.error.place(x = 880, y= 5)
                            self.error.configure(text = self.errorType[3])
                            return True

                    #Checks for time conflicts
                    for c in self.savedValues:
                       check = self.planner[c].checkTimeConflict(self.taskName.get(), self.military_time,self.military_time2)
                       if(check == True):
                         self.error.place(x = 880, y= 5)
                         self.error.configure(text = self.errorType[3])
                         return True
                        #self.printValues()

                    #If no conflicts adds the task to planner and returns false.
                    for d in self.savedValues:
                        self.planner[d].createARequiredTask(self.taskName.get(),self.military_time,self.military_time2)
                    self.savePlanner()
                    
                    return False


 #Adds hobbies to planner by picking n random numbers(n is given by user)      
 def addHValues(self,value):
     if(value == 1):
          if self.times == -1 or self.maxx == -1 or self.pos == -1:
              print("Unit Testing: Hobby Task Incomplete")
              self.error.place(x = 800, y= 5)
              self.error.configure(text = self.errorType[0])
              return True
     
    # picks random days for times
     count = 0
     temp  = []
     while(count<self.times):
         var = random.randrange(7)
         while(var in temp):
             var = random.randrange(7)
         temp.append(var) 
         count = count + 1
     
    # for b in temp:
    #    print("value got:",b)

    #Adds a hobby to the list 
     for v in temp :
        #print("value got:",v)
        self.planner[v].createAHobby(self.taskName.get(),self.times,float(self.maxx),self.when,self.pos)
     self.savePlanner()
     return False
         
    
 #Gets the values from the day widgets
 def getValues(self): 
     self.present = 0
     
     self.days.append(self.Checkbutton1)
     self.days.append(self.Checkbutton2)
     self.days.append(self.Checkbutton3)
     self.days.append(self.Checkbutton4)
     self.days.append(self.Checkbutton5)
     self.days.append(self.Checkbutton6)
     self.days.append(self.Checkbutton7)

     counter = 0
     for e in self.days:
         if(e.get() == True):
             #print("found a True\n")
             self.switch = 1
             #print("here:",counter\n)
             self.savedValues.append(counter)
         counter = counter + 1
     #self.printValues()
     checkingTime = self.addRValues()
     if(checkingTime == True):
         print("Unit Testing: There was an error the verification process")
         #resets the values in the form
         self.days.clear()
         self.savedValues.clear()
         return True

     #if the user is able to add th etask, clear the saved values
     self.savedValues.clear()
     self.days.clear()
     
     return False
 #Gets H's values
 def getValuesH(self):  
     self.present = 0
     if(self.switch == -1):
       print("Unit Testing: No Days selected --getValuesH funtion")
       self.error.place(x = 880, y= 5)
       self.error.configure(text = self.errorType[0])
       return True

     self.combobox1 = None #times a day
     self.combobox2 = None # max hours
     self.combobox3  =None # time of day
     self.combobox4 = None  # before or after tasks
     #if done adding required tasks, and adding a hobby, it doesn't flag the default hobby values
     if(self.hobbysize >0):
        self.addHValues(0)
    
     return False
     



    




