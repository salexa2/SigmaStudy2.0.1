import month
from month import *
from SaveAndLoad import *

class Year():
    
    global months 
    global monthnames 
    global currmonth

    #saved name
    saveName  = "Callendata.json"

    def __init__(self, mon):
        if(self.loadCall() == False):
            self.months = [month(0),month(1),month(2),month(3),month(4), month(5), month(6), month(7), month(8) , month(9), month(10) , month(11)]
     
        self.currmonth= mon

    def setMonthFrame(self, calandar_fr):
        for m in self.months:
            m.setMonthFrame(calandar_fr)

    def showMonth(self, sideframe):
            self.months[self.currmonth-1].createMonth(sideframe)
    def getCurrMonth(self):
        month_n  = ['January','February','March','April', 'May', 'June', 'July','August', 'September','October','November','December']
   
        return month_n[self.currmonth-1]
    def setMonth(self, choice,sideframe):
        if(choice == "January"):
           self.currmonth = 1 
        elif(choice == "February"):
            self.currmonth = 2 
        elif(choice == "March"):
            self.currmonth = 3
        elif(choice == "April"):
           self.currmonth = 4       
        elif(choice == "May"):               
            self.currmonth = 5
        elif(choice == "June"):
           self.currmonth = 6 
        elif(choice == "July"):
            self.currmonth= 7    
        elif(choice == "August"):
           self.currmonth= 8
        elif(choice == "September"):
            self.currmonth = 9    
        elif(choice == "October"):
            self.currmonth = 10                  
        elif(choice == "November"):
           self.currmonth = 11          
        elif(choice == "December"):
            self.currmonth = 12     

        #self.dayStart = self.weekDay(self.current_time.year, self.currentMonth, 1)
        #print("the 1 of the set month starts on:", self.dayStart)
        print("The month is now:")
        self.showMonth(sideframe)

    def loadCall(self):
        loader = SaveAndLoad.load_data(self.saveName);
        if loader is None:
            print("no saved data found")
            return False
        self.months = loader.copy();
        return True

    def saveCall(self):
        SaveAndLoad.save_data(self.months,self.saveName)

           
        
        
       
      
