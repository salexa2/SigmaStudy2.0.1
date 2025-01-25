
import Task
from Task import *
from datetime import *

class Weekday():
    #--------------------------VARIABLES-----------------------------
    #default days:
   weekdays=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
   #sunday
   weekdayNum = 0 
  #composed of morning,afternoon, and night tasks
   global morn 
   global after 
   global evening
   global hoursUsed 
   global minUsed 
   global hoursUsedE 
   global minUsedE 
   global weekFrame 
   global mornFrame
   global afterFrame
   global evenFrame

   global nameD 
   global state 
   global size
   global hobbies
   global startTimes 
   global endTimes
   
   #---------------------------CONSTRUCTOR----------------------
   def __init__(self,num):
       self.weekdayNum = int(num)
     #  print(self.weekdays[self.weekdayNum])
       self.nameD = self.weekdays[self.weekdayNum]
       self. morn = []
       self.after =[]
       self.evening= []
       self.startTimes = []
       self.endTimes = []
     
       self.size = 0
       self. state = -1 
       self.hobbies = 0
   #Refreshes all the day type lists

   def createFrames(self, plan_frame):
       self.weekFrame = customtkinter.CTkFrame(plan_frame, fg_color = "#CFCFCF",width = 1000, height =300)
       self.mornFrame = customtkinter.CTkScrollableFrame(self.weekFrame, fg_color = "#FFF370",width = 320, height =300)
       self.afterFrame = customtkinter.CTkScrollableFrame(self.weekFrame,fg_color = "#C1FF5E",width = 320, height =300)
       self.evenFrame = customtkinter.CTkScrollableFrame(self.weekFrame, fg_color= "#5CD9B6",width = 320, height =300)

   def cleartypes(self):
       for i in self.morn:
           i.getFrame().destroy()
       for x in self.after:
           x.getFrame().destroy()
       for y in self.evening:
          y.getFrame().destroy()
       self.morn.clear()
       self.after.clear()
       self.evening.clear()
       self.startTimes.clear()
       self.endTimes.clear()
       print("Unit Testing: Refresh")
   #checks for a time conflict
   def checkTimeConflict(self,val1,val3,val4):
        item = Task(val1,self.weekdayNum,0,val3,val4,0,0,-1,1)

        if(self.checkifused(item) == False):              
                    self.startTimes.append(item.getStartTime())
                    self.endTimes.append(item.getEndTime())
        else:
                    return True
        return False
   #create a required task
   def createARequiredTask(self,val1,val3,val4):   
        self.state = 1
        item = Task(val1,self.weekdayNum,0,val3,val4,0,0,-1,1)

        self.addTo(item)
        self.size = self.size + 1
        return True
   #create a hobby
   def createAHobby(self,name,times,maxx,when1,pos):
        self.size = self.size + 1
        self.hobbies = self.hobbies+1
        print(when1)
        self.state = 1
        #print("lululu")
        print("daytype",when1)
        item = Task(name,self.weekdayNum,1,'0:00','0:00',times,maxx,when1,pos)
        if(item.getDayType() == 0):
         
            self.insertAt(item,self.morn)
        elif(item.getDayType() == 1):
            self.insertAt(item,self.after)
          
        elif(item.getDayType()== 2):
            self.insertAt(item,self.evening)
 #add a required task
   def addTo(self,task1):
            if(task1.getDayType() == 0):
              self.morn.append(task1)
            elif(task1.getDayType() ==1):
               print("bing bong")
               self.after.append(task1)
            elif(task1.getDayType() ==2):
               self.evening.append(task1)
            return 
 #insert a hobby
   def insertAt(self,item,planner): 
      #  print("return:",item.returnPos())
        print("pso------------------------------------------------\n", item.returnPos())
        #if list is empty append to end of morn/after/or even
        if(len(planner)==0):
            #print("empty list")
            #print("name",self.nameD)
            if(item.getDayType() == 0):
                #print("append to morn")
                self.morn.append(item)
            elif(item.getDayType() == 1):
                #print("append to after")
                self.after.append(item)
            else:
                #print("append to evening")
                self.evening.append(item)
            return True

        #if the user prefers to do their hobby before their required tasks then it will insert before however if there is not enough time for thst task in the daytype it will apend after
        if(item.returnPos() == 0):
            print("Unit Testing: Hobby appended to before")
            #if(he first element is say 12 pm which is the start of afternoon, you caant put afternoon task before it)
            if( planner[0].getType() == 0):
                if(planner[0].getStartTime().hour == 12 or planner[0].getStartTime().hour == 16 or planner[0].getStartTime().hour == 0):
             
                            planner.append(item)
                else:
                    planner.insert(0,item)
            else:
                 if(item.getDayType() == 0):#morning

                    if(planner[0].getType()==0):
                        if(planner[0].getStartTime().hour - int(item.getMax())< 0 and planner[0].getType()): # 13 - 8 = 

                            if(planner[len(planner)-1].getEndTime().hour> 12 ):
                                self.evening.append(item)
                            else:
                                planner.append(item)
               
                        else:
               
                            planner.insert(0,item)
                    else:
                         planner.insert(0,item)
                 elif( item.getDayType()== 1):#after
                    if(planner[0].getStartTime().hour - int(item.getMax())< 12 ): 
                        if(planner[len(planner)-1].getEndTime().hour> 17 ):
                            self.evening.append(item)
                        else:
                            planner.append(item)
                    else:
                        planner.insert(0,item)
                 elif(item.getDayType() == 2):#evening
                    if(planner[0].getStartTime().hour - int(item.getMax()) < 17 ):
                         planner.append(item)
                    else:
                        planner.insert(0,item)
        elif(item.returnPos() == 1):
             print("Unit Testing: Hobby appended to after")          
             if(item.getDayType() == 0 ):
                 #print("length of planner",len(planner))
                 if(planner[len(planner)-1].getEndTime().hour +int(item.getMax())> 12 ):
                  self.evening.append(item)
                  
                 else:
                     planner.append(item)
             elif(item.getDayType() == 1):
                # print("length of planner",len(planner))
                 if(planner[len(planner)-1].getEndTime().hour + int(item.getMax())> 17 ):
                         self.evening.append(item)
                       
                 else:
                     planner.append(item) #doesnt break any restraints
             else:#evening
                  planner.append(item)
        elif(item.returnPos()==2):
            counter = 0
            inserted = 0
           # print("length:",len(planner))
            while (counter< len(planner)-1): #for tasks in planner
                #print("counter:",counter)
                #print("first" ,planner[counter].getName())
                #print("second", planner[counter+1].getName())
                if(planner[counter].getType() == 0 & planner[counter+1].getType() == 0  ): #if consecutive requried tasks
                    firstTime = float(planner[counter+1].getStartTime().hour) +float((planner[counter+1].getStartTime().minute) /100)
                    secondTime = float(planner[counter].getEndTime().hour) + float((planner[counter].getEndTime().minute)/100)
                    #print("first:",firstTime)
                    #print("second:",secondTime)
                    difference = firstTime- secondTime
                    diff2 =  float(item.getMax())
                    if(difference > diff2):
                       #print("difference",float(difference))
                       #print("maxHours",item.maxHours)
                        #assigns a time to the hobby, leaving 30 minute padding after 
                        new_s = time(hour=planner[counter].getEndTime().hour, minute=30) 
                        new_e = time(hour= (planner[counter].getEndTime().hour+ int(item.getMax())), minute=30)
                        item.setStartTime(new_s)
                        item.setEndTime(new_e)
                        planner.insert(counter+1,item)
                        print("inserted")
                        inserted = 1

                        break
                counter = counter +1
            #If cant append between anything, change position to after tasks and call insertAt
            if(inserted == 0):
               item.setPos(1)
               self.insertAt(item,planner)
            return True

   #checks if a time is used      
   def checkifused(self, item):
           print("LENGTH", len(self.startTimes))
           if(len(self.startTimes)== 0):
               return False

           timer = 0
           print("Unit Testing: Checking for any time conflicts")
           while(timer < len(self.startTimes)):
            print("count:", timer)
               
            print("item start:",item.getStartTime().hour)
            print("item end:",item.getEndTime().hour)
            print("other start:",self.startTimes[timer].hour)
            print("other end:",self.endTimes[timer].hour)
            print("other start min:",self.startTimes[timer].minute)
            print("item end min:",item.getEndTime().minute)

              
            if(item.getStartTime().hour<= self.startTimes[timer].hour):
                if(item.getEndTime().hour > self.startTimes[timer].hour):
                    print("end time conflict")
                    return True
                if(item.getEndTime().hour == self.startTimes[timer].hour):     
                    if(item.getEndTime().minute > self.startTimes[timer].minute):
                      print("end time conflict - equals")  
                      return True
            if(item.getEndTime().hour >=  self.endTimes[timer].hour):
                
                if(item.getStartTime().hour < self.endTimes[timer].hour):
                       print("start time conflict")
                       return True
                if(item.getStartTime().hour == self.endTimes[timer].hour):
                    
                    if(item.getStartTime().minute < self.endTimes[timer].minute):
                        print("start time conflict - equals")
                        return True
            if(item.getStartTime().hour> self.startTimes[timer].hour):
                if(item.getEndTime().hour < self.endTimes[timer].hour):
                    print("in between conflict")
                    return True
                
            timer = timer + 1
 
           print("Unit Testing: There were no conflicts")
           return False
                
 
         
   def getWeekdays(self):
     return self.weekdays
   def returweekf(self):
       return self.weekFrame
   def getweekFrame(self):
       self.weekFrame.pack(padx = .5, pady = .5, side = TOP, )
       day_label = customtkinter.CTkLabel(self.weekFrame, text_color="#000000", text=self.nameD, font=customtkinter.CTkFont(size=20, weight="bold"))
     
       day_label.pack(side = TOP)

       self.mornFrame.pack(side = LEFT)
       self.afterFrame.pack(side = LEFT)
       self.evenFrame.pack(side = LEFT)

       morn_label = customtkinter.CTkLabel(self.mornFrame, text = "Morning", text_color="#000000", font=customtkinter.CTkFont(size=20, weight="bold"))
       morn_label.pack(anchor = CENTER)

       after_label = customtkinter.CTkLabel(self.afterFrame, text = "Afternoon", text_color="#000000", font=customtkinter.CTkFont(size=20, weight="bold"))
       after_label.pack(anchor = CENTER)

       even_label = customtkinter.CTkLabel(self.evenFrame, text = "Evening", text_color="#000000",  font=customtkinter.CTkFont(size=20, weight="bold"))
       even_label.pack(anchor = CENTER)



       

   def showAll(self):
       if(self.state == 1 ):
         print("Day",self.nameD)
         ypos = 10
         count = 0
         for x in self.morn: 

            if(count == 0 and  len(self.morn) == 1 and x.getType() == 1  ):
                 x.setStartTime(time(6,0))
                 x.setEndTime(time(6+int(x.getMax()), 0))  
            elif(count == 0 and  x.getType() == 1  and len(self.morn) > 1):
                 x.setStartTime(time(0,0))
                 x.setEndTime(time(int(x.getMax()), 0))  
            else:
               if(x.getType() == 1 and len(self.morn)>1 and count >0 and count < len(self.morn)):
                 print("newwwww:",self.morn[count-1].getEndTime().hour)
                 print("count - 1",count -1)
                 minset = self.morn[count-1].getEndTime().minute + 30
                 if(self.morn[count-1].getEndTime().minute + 30  > 59) :
                         minset = self.morn[count-1].getEndTime().minute
                 x.setStartTime(time(self.morn[count-1].getEndTime().hour , minute = minset))
                 if(self.morn[count-1].getEndTime().hour+ int(x.getMax())<24):
                     x.setEndTime(time(self.morn[count-1].getEndTime().hour+ int(x.getMax()),minset ))
                 else:
                      x.setEndTime(time(int(x.getMax()),self.morn[count-1].getEndTime().minute ))

            count = count +1
            ypos = ypos+100
            x.printTask()
            x.taskPage(self.mornFrame)

         print("morn end\n")
         count = 0 
         ypos = 10

      
         for y in self.after: 
            if(count == 0 and y.getType() == 1  ):
                 y.setStartTime(time(hour = 12,minute = 0))
                 y.setEndTime(time(hour = 12+int(y.getMax()), minute =  0))
             
            else:                  
                if(y.getType() == 1  and len(self.after)>1 and count >0 and count < len(self.after)):
                     print("newwwww2:",self.after[count-1].getEndTime().hour)

                     minset = self.after[count-1].getEndTime().minute + 30
                     if(self.after[count-1].getEndTime().minute + 30  > 59) :
                         minset = self.after[count-1].getEndTime().minute

                     y.setStartTime(time(hour = self.after[count-1].getEndTime().hour , minute = minset))
                     print(y.getStartTime())
                     if(self.after[count-1].getEndTime().hour+ int(y.getMax()) <24):
                         y.setEndTime(time(hour = self.after[count-1].getEndTime().hour+ int(y.getMax()), minute =minset ))
                     else:
                          y.setEndTime(time(hour = int(x.getMax()), minute  =self.after[count-1].getEndTime().minute ))               
            ypos = ypos+100
            count = count +1
            y.taskPage(self.afterFrame)
            y.printTask() 
            
         print("after end\n")
         count = 0
         ypos = 10
         switch = 0
         for z in self.evening: 
             if(count == 0 and z.getType() == 1 ):
                 z.setStartTime(time(18,0))
                 if(18+ int(z.getMax())>23):
                     z.setEndTime(time(int(z.getMax()), 0))
                 else:
                     z.setEndTime(time(18+int(z.getMax()), 0))            
             else:
                 if(z.getType() == 1  and len(self.evening)>1 and count >0 and count < len(self.evening)):
                     minset = self.evening[count-1].getEndTime().minute + 30
                     if(self.evening[count-1].getEndTime().minute + 30  > 59) :
                         minset = self.evening[count-1].getEndTime().minute
                     z.setStartTime(time(self.evening[count-1].getEndTime().hour , minset ))
                     if(self.evening[count-1].getEndTime().hour+ z.getMax() <23):
                         z.setEndTime(time(self.evening[count-1].getEndTime().hour+ int(z.getMax()),self.evening[count-1].getEndTime().minute ))
                        # z.printTask()
                     else:
                          switch = 1
                          print("to many hobbies\n")
                          self.evening.remove(z)
                          
             ypos = ypos+100
             count = count +1
             z.printTask()
             if(switch != 1):
                z.taskPage(self.evenFrame)
             switch = 0
            
         print("even end\n")
         print("------")
       else:
           print("Day has nothing:",self.nameD)
      
     




