#from ast import Delete
#from tkinter.tix import COLUMN

import tkinter 
from tkinter import * 
import customtkinter

import flashcardset 
from flashcardset import *
from SaveAndLoad import *
 
#gallary holds the flashcard sets for use
class gallary():


    #list of flashcard sets - a list of lists
    lib = []
    #base number of rows and columns that hold each set 
    row_num = 0
    column_num = 0 
    #saved name - DO NOT TOUCH THIS
    saveName  = "data.json"
    #gallarys main frame
    galframe = None
    # main root
    mainr = None
   


    #constructor
    def __init__(self,root):
       self.mainr = root

    #return gallerys set - a list of lists 
    def returnGal(self):
        return self.lib

    def setLib(self,newlib):
        self.lib = newlib

    #prints the num of sets
    def print_size(self):
        print("Count:", len(self.lib))
        print("\n")
   
    #gets the size of the set 
    def getSize(self):
        return len(self.lib)

    #call to create a set
    def create_Set(self,upload_frame, button):
        button.configure(state = "disabled")
        print("Unit Testing 2.1: Flashcard set created\n")
        flashset = flashcardset(upload_frame)
        flashset.creating_set_page(self, button)
       # return

     #adds a set to the gallary
    def add_Set(self,flset):
         self.lib.append(flset)

    #removes a set 
    def remove_Set(self,cardset):
        self.lib.remove(cardset)

    #returns the saveName - DO NOT TOUCH 
    def return_saveN(self):
        return self.saveName

    #prints all the sets of a gallary 
    def print_Gal(self):
        print("__________________\n")
        for x in self.lib:
         print(x.printAll())
        print("__________________\n")
    
    #gets the gallarys main frame
    def get_galFrame(self):
        return self.galframe
    
    #sets the gal frame for use later
    def set_galFrame(self,frame):
       self.galframe = frame


  
    #displays all the flashcard sets on the gallary page
    def display(self, galf):
        count = 0
        posx = 50
        posy = 100

        print("Unit Testing 3.1: Gallary: shows all the sets\n")
       

        for i in self.lib:   
           # print("count var: ",count)
            if(count < len(self.lib)):
                set_frame = customtkinter.CTkFrame(galf, width = 100, height = 100)
                set_frame.place(x = posx, y = posy)
                i.displaySet(set_frame,galf,self)
               
                posx+=150
               
            if(posx > 1100):
                posx = 50
                posy+= 150
            count+=1
        return

    def createButtons(self,galf):
        #BUTTON TO CREATE NEW SET IN GALLERY
        create_set_button = customtkinter.CTkButton(galf, text= "Create Set", fg_color= "#279400", hover_color="#1C6B00", command = lambda: self.create_Set(galf, create_set_button))
        create_set_button.place(x=10, y=10)
   

        #BUTTON TO CLEAR ALL SETS
        create_clear_button = customtkinter.CTkButton(galf, text= "Clear All Sets", fg_color= "#279400", hover_color="#1C6B00", command = lambda: self.clearSets())
        create_clear_button.place(x=200, y=10)





    def reload_Gal(self):
        if(self.galframe !=None):
            for i in self.galframe.winfo_children():
                i.destroy()
            self.display(self.galframe)
            self.createButtons(self.galframe)
    #loads flashcard sets (called on program launch) 
    def loadSets(self):
        loader = SaveAndLoad.load_data(self.saveName);
        if loader is None:
            print("no saved data found")
            return
       
        self.lib = loader.copy();

    def saveSets(self):
        SaveAndLoad.save_data(self.lib,self.saveName)


    def clearSets(self):
        print("prompting to clear all sets")
        warningframe = customtkinter.CTkFrame(self.galframe, width = 400, height = 150)
        warningframe.place(x=0, y=10)


        w_label = customtkinter.CTkLabel(warningframe, text = "Are you sure you\n want to delete all sets?",font=customtkinter.CTkFont(size=20, weight="bold"))
        w_label.place(x = 200, y = 30, anchor = "center")
        yes_b = customtkinter.CTkButton(warningframe, text = "yes",width = 30,height = 30, border_width=0, hover_color= "#279400", fg_color= "#279400", font=customtkinter.CTkFont(size=20), command = lambda: removeAllSets())
        yes_b.place(x = 50, y = 85, anchor = "center")
        no_b = customtkinter.CTkButton(warningframe, text = "no",width = 30,height = 30, border_width=0, hover_color= "#279400", fg_color= "#279400", font=customtkinter.CTkFont(size=20), command = lambda: warningframe.destroy())
        no_b.place(x = 350, y = 85, anchor = "center")

        def removeAllSets():
            self.lib = []
            SaveAndLoad.save_data(self.lib,self.saveName)
            warningframe.destroy()





    



       
   


             



        




       








   





    





