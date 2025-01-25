from flashcard import * 
import tkinter 
from tkinter import * 
import customtkinter
from SaveAndLoad import *


#changes
#play page 

#Holds a list of flashcards
class flashcardset:

    #-------------GLOBAL VARIABLE------------------

    #WARNING: we use global so that way the flashsets do not merge. Do not remove global in this set.

    #list of flashcards
    global flashset 
    #set name
    global flash_name  
    #keeps track of current set index
    global index
    #reference to gallary object
  
    #flashcard set creation frame.
    global flashframe

 



    #constructor
    def __init__(self, uploadf):
        self.flash_frame = customtkinter.CTkFrame(uploadf, width = 550, height = 375, fg_color= "#279400")
        self.flash_frame.place(x =700,y=100)
        self.flashset = []
        self. flash_name = ""
        self.index = 0
        self.recycling = []
 
      

     #-----------------FUNCTIONS---------------------- 

    #Gets the size of a set
    def get_Size(self):
        return len(self.flashset)
    #Gets a sets name
    def get_Name(self):
        return self.flash_name
    #sets a sets name
    def set_Name(self, name):
        self.flash_name = name

    #print oiut all the cards of a set 
    def printAll(self):
        print("---FlashCard Set---\n")
        print(self.get_Name())
        for x in self.flashset :
           x.printFront()
           x.printBack()

        print("---FlashCard End---\n")
    #displays a card
    def displayCard(self,root,index):
        cardIndex = index
        print("Unit Testing 3.4: display current card\n")
        self.flashset[cardIndex].printFront()
        self.flashset[cardIndex].printBack()
        self.flashset[cardIndex].displayCard(root)


     #helps move to the next card
    def updateCount(self,play_f, button, prev):
          self.index = self.index + 1

          
          print("Unit Testing 3.5: Gallary: next card should show\n")
          if(self.index == self.get_Size()-1):
               print("disabled")
               button.configure(state = "disabled") 
           
          prev.configure(state = "Normal") 
           
          self.displayCard(play_f,self.index)
    
    #helps move to previous card
    def decreaseCount(self, play_f, button, nextb):
        self.index= self.index - 1
        if(self.index == 0):
              button.configure(state = "disabled") 

        if(self.index <self.get_Size()-1 ):
            nextb.configure(state = "Normal")
        self.displayCard(play_f,self.index)


           
    #takes us back to gallary by removing the frame that's displaying the flashcards and resets index back to 0       
    def removepframes(self,play_f):

        print("Unit Testing 3.n: Gallary: flashcard should be closed \n")
        self.index = 0
        play_f.destroy()
        return
    
     
       
   #page that holds each flashcard- called once 
    def play_Page(self,galf):
        #bug fix -------------displaying empty flash card sets
        if(len(self.flashset) >0):
            #0----------------------------
         print("Unit Testing 3.2: Gallary: Flashcard should display \n")
         play_f = customtkinter.CTkFrame(galf, fg_color="#279400" ,width =1200 ,height = 700) 
         play_f.place(x= 0, y= 0)
       
         done_button = customtkinter.CTkButton(play_f, text = "✓" , text_color ="#000000", fg_color= "#FFFFFF", hover_color = "#CFCFCF" ,corner_radius = 200, width = 25, height = 30, font = ("Helvetica",18), anchor="center", command = lambda:self.removepframes(play_f))
         done_button.place(x=1100, y= 650)

         if (self.get_Size()>1):

             if(self.index == 0):
                 prev_card = customtkinter.CTkButton(play_f, text =  "back", width = 25,height = 30, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center",state = "disabled", command = lambda:self.decreaseCount(play_f,prev_card,next_card))
                 prev_card.place(x = 5, y = 650)

             next_card = customtkinter.CTkButton(play_f, text =  "next", width = 25,height = 30, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda:self.updateCount(play_f,next_card, prev_card))
             next_card.place(x = 1000, y = 650)
       
            
      
         self.displayCard(play_f,self.index)
    
    #deletes a set 
    def delete_Set(self,setframe,galObject):
        galObject.remove_Set(self)
        setframe.destroy()
        SaveAndLoad.save_data(galObject.returnGal(), galObject.return_saveN())
        galObject.reload_Gal()
        
    def remove_Frame(self,setframe):
       setframe.destroy()


    #delete page 
    def delete_Page(self,galObject,setframe):
        
        print("Testing Testing Case 5.1: Modifying a set  - Set should be deleted")

        warningframe = customtkinter.CTkFrame(setframe, width = 100, height = 100)
        warningframe.place(x = 0, y = 0)

       

        w_label = customtkinter.CTkLabel(warningframe, text = "Are you sure you\n want to delete?",font=customtkinter.CTkFont(size=10, weight="bold"))
        w_label.place(x = 50, y = 30, anchor = "center")
        yes_b = customtkinter.CTkButton(warningframe, text = "yes",width = 5,height = 5, border_width=0, hover_color= "#279400", fg_color= "#279400", font=customtkinter.CTkFont(size=10), command = lambda: self.delete_Set(setframe,galObject))
        yes_b.place(x = 10, y = 85, anchor = "center")
        no_b = customtkinter.CTkButton(warningframe, text = "no",width = 5,height = 5, border_width=0, hover_color= "#279400", fg_color= "#279400", font=customtkinter.CTkFont(size=10), command = lambda: warningframe.destroy())
        no_b.place(x = 90, y = 85, anchor = "center")

    #finalizes and saves changes to set 
    def finalizeChange(self,scrollframe,galObject): 
       print("Unit Testing Case 6.3: Modifying set - finalizing changes")
       for i in self.flashset:
           i.saveEditedCard()
           
       SaveAndLoad.save_data(galObject.returnGal(), galObject.return_saveN());
       scrollframe.destroy()
       galObject.reload_Gal()
      
       


    #edit card page
    def edit_Page (self,galObject):
         print("Unit Testing Case 6.1: Modifying set - Edit Page should show")

         scrollframe = customtkinter.CTkFrame(galObject.get_galFrame(), width = 1300, height = 750) 
         scrollframe.place(x = 0, y= 0)

         scrollable_frame = customtkinter.CTkScrollableFrame(master=scrollframe, width=1200, height=700)
         scrollable_frame.place(x = 10, y = 10)

         logo_label = customtkinter.CTkLabel(master = scrollable_frame, text="Edit Flash cards Here", font=customtkinter.CTkFont(size=20, weight="bold"))
         logo_label.pack()

         
        
            
         for i in self.flashset:

               i.editCard(scrollable_frame,self,galObject)


        
         addCard_button = customtkinter.CTkButton(scrollable_frame, text = "Add Card", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: add_Card(addCard_button,doneEdit_button) )
         addCard_button.pack(side=LEFT)
         doneEdit_button = customtkinter.CTkButton(scrollable_frame, text = "Done", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: self.finalizeChange(scrollframe,galObject) )
         doneEdit_button.pack(side=RIGHT)
        

         def add_Card(add,doneEdit_button):
             print("Adding Card to edit page")
             newCard = flashcard()
             self.flashset.append(newCard)

             newCard.editCard(scrollable_frame,self,galObject)
             
             addCard_button.destroy()
             doneEdit_button.destroy()

             add = customtkinter.CTkButton(scrollable_frame, text = "Add Card", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: add_Card() )
             add.pack(side=LEFT)
             doneEdit_button = customtkinter.CTkButton(scrollable_frame, text = "Done", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center", command = lambda: self.finalizeChange(scrollframe,galObject) )
             doneEdit_button.pack(side=RIGHT)
             
         


    #deletes a flashcard
    def delete_card(self,card):
        self.flashset.remove(card)
        

    #option menu choices for each set 
    def optionmenu_callback(self, choice, galObject,setframe):
   

        if(choice == "Edit"):  
            print("Unit Testing Case 6.0: Modifying set - Edit")
            self.edit_Page(galObject)
        
        if(choice == "Delete"):
            print("Unit Testing Case 5.0: Modifying a set  - Delete a set")
            self.delete_Page(galObject,setframe)
          
   
    #finishes making a visual set and associates each play button with it's own set
    def displaySet(self,set_frame,galf, galObject):
         optionmenu_var = customtkinter.StringVar(value="✍")

         set_label = customtkinter.CTkLabel(set_frame, text = self.get_Name(),font=customtkinter.CTkFont(size=16, weight="bold"))
         set_label.place(x = 50, y = 30, anchor = "center")
         play_b = customtkinter.CTkButton(set_frame, text = "▶️",width = 3,height = 3, hover_color= "#279400", fg_color= "transparent", font=customtkinter.CTkFont(size=12), command = lambda: self.play_Page(galf))
         play_b.place(x = 16, y = 85, anchor = "center")
         combobox = customtkinter.CTkOptionMenu(set_frame, fg_color = "#279400",  button_color = "#279400", dropdown_hover_color = "#1C6B00" , width = 18, height = 19,values=["Edit", "Delete"], font=customtkinter.CTkFont(size=12), command = lambda choice: self.optionmenu_callback(choice,galObject,set_frame), variable = optionmenu_var)
         combobox.place(x= 33,y=75)
       
              

         return

    #creates a flashcard  and inserts it into set after + is hit
    def create_a_Card(self,front,back,galObject,button):
        print("Unit Testing 2.3: Creates a card\n")
        new = flashcard()
        new.setFront(front)
        new.setBack(back)
        self.insertCard(new,galObject,button)
    
    #inserts card into set
    def insertCard(self,card,galObject, button):
        print("Unit Testing 2.4: Inserts a card into a set\n")
        self.flashset.append(card)
        print("Unit Testing 2.5: Calls the creating set page.n")
        self.creating_set_page(galObject,button)


    #adds a flashcard set to the gallary object
    def addtoGal(self,galObject,button):
        
        #creats a name for set otherwise no name
        galObject.loadSets()
        dialog = customtkinter.CTkInputDialog(text="What would you like to name your set?", title= "New FlashCard Set")
        self.set_Name(dialog.get_input())
        #adds set to gallary object.
        galObject.add_Set(self)
        SaveAndLoad.save_data(galObject.returnGal(), galObject.return_saveN());
        #destroys the create frame
        galObject.reload_Gal()
       
        self.flash_frame.destroy()
        
        self.printAll()
        
    #UI for creating a new set 
    def creating_set_page(self, galObject, button):
         print("Unit Testing 2.2: Flashcard Page should show\n")
     
        #frontinput, 
         front_card_input= customtkinter.CTkEntry(self.flash_frame, width= 500,height=50,  font = ("Helvetica", 20), placeholder_text = "Enter Term")
         front_card_input.place(x = 25,y=15) 
         #backinput 
         back_input = customtkinter.CTkTextbox(self.flash_frame,width=500,height= 250,  font = ("Helvetica", 18))
         back_input.place(x= 25, y=85) 
         back_input.insert(END,"Enter Definition")
 
         #creates another card, inserts previous card, doesn't insert a card till the "+" button is hit.
         next_button = customtkinter.CTkButton(self.flash_frame, text= "➕", text_color ="#000000", fg_color= "#FFFFFF",hover_color = "#CFCFCF" , corner_radius = 200, width = 30, height = 30, font = ("Helvetica",18), anchor="center", command = lambda:self.create_a_Card(front_card_input.get(), back_input.get("1.0",END),galObject,button))
         next_button.place(x=420, y= 338)

         #creates a set
         done_button = customtkinter.CTkButton(self.flash_frame, text = "✔️" , text_color ="#000000", fg_color= "#FFFFFF", hover_color = "#CFCFCF" ,corner_radius = 200, width = 25, height = 30, font = ("Helvetica",18), anchor="center", command = lambda: self.addtoGal(galObject,button))
         done_button.place(x=480, y= 338)

         cancel_button = customtkinter.CTkButton(self.flash_frame, text= "❌", text_color ="#FFFFFF", fg_color= "transparent" , corner_radius = 200, width = 30, height = 30, font = ("Helvetica",18), anchor="center", command = lambda: self.activateButton(button))
         cancel_button.place(x=5, y= 338)

    def activateButton(self,button):
        button.configure(state = "normal")
        self.flash_frame.destroy()
