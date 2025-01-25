
#from ast import Lambda  i commented this out 4/9, if program acts up uncomment it 
from tkinter import * 
import customtkinter
from SaveAndLoad import *

#holds front and back input
class flashcard:
 
   #front card text
   front_card = ""
   #back card text 
   back_card = ""
   #helps flip a card
   state = 0

   #when a user edits a card, the values will be saved in this entry and text box - edit front and back.
   editfront = None
   editback = None
  

   #gets the front of card
   def getFront(self):
       return self.front_card
   #gets the back of card
   def getBack(self):
       return self.back_card
   #sets the front of card
   def setFront(self,front_input):
       self.front_card = front_input
   #sets the back of card
   def setBack(self,back_input):
       self.back_card = back_input
   #prints the front of a card
   def printFront(self):
       print("\nfront:", self.front_card)
   #prints the back of a card
   def printBack(self):
       print("\nback:", self.back_card)
   #flips the card
   def flip(self, card_frame, state):
       if(state==0):
        
           card_frame.configure(text=self.getBack())
           self.state = 1
         

       else:
         
           card_frame.configure(text =self.getFront())
           self.state = 0
         
   #displays the flash card
   def displayCard(self, root):
       print("Unit Testing 4.0: Card should show\n")
       card_frame = customtkinter.CTkButton(root, text_color = "#000000", text = self.getFront(), hover_color="#DBDBDB", fg_color="#FFFFFF",width = 1000,height = 400, command = lambda: self.flip(card_frame,self.state)) 
       card_frame.place(x = 100, y= 100)

   #removes this card from a given set 
   def remove (self,fset,galObject,divider):
       fset.delete_card(self)
       #changed----------------edit card bug
       self.editfront.destroy()
       self.editback.destroy()
       self.del_button.destroy()
       divider.destroy()
       

       SaveAndLoad.save_data(galObject.returnGal(), galObject.return_saveN())
    
     #--------------------bug end 
       print("Unit Testing Case 6.2: Modifying set - card should be deleted, new edit page should show")

   #edits card
   def editCard(self, scrollable_frame,fset,galObject):
        #frontinput, 
                self.editfront = customtkinter.CTkEntry(scrollable_frame, width= 750,height=100, font = ("Helvetica", 20), placeholder_text = self.getFront(), placeholder_text_color= "#000000")
                self.editfront.pack(side=TOP, anchor=N)
                self.editfront

                #backinput 
                self.editback = customtkinter.CTkTextbox(scrollable_frame,width=750,height= 100, font = ("Helvetica", 18))
                self.editback.pack(side=TOP, anchor=N)
                self.editback.insert(END,self.getBack())
                self.del_button = customtkinter.CTkButton(scrollable_frame, text = "Delete", width = 25,height = 25, text_color ="#000000",  fg_color= "#FFFFFF",hover_color = "#CFCFCF", corner_radius = 200,font = ("Helvetica",18),  anchor="center" ,command = lambda:self.remove(fset,galObject,divider)) #command = lambda:fset.remove(self)
                self.del_button.pack(side=TOP, anchor=NE)
                #removed from set ------------
                divider = customtkinter.CTkLabel(master = scrollable_frame, text="___________________________________________________________________________________________________________________________________________________________________________________________", font=customtkinter.CTkFont(size=20, weight="bold"))
                divider.pack()
   
   #saves edited changes 
   def saveEditedCard(self):
       print("Unit Testing 6.4: print saved set")

       #you cant insert anything into an entry box like textbox so if self.editfront is not touched, all it had is "", the placeholder text is the flashcard front but i didnt initially set the entrys value like i did with the text box, where i inserted the bac input 
       if(self.editfront.get() != ""):
           print("front: \n", self.editfront.get())
           self.setFront(self.editfront.get())
       else:
           print("front was not changed\n")
      
         
       print("back: \n", self.editback.get("1.0",END))
       self.setBack(self.editback.get("1.0",END))
      

   
       
        
    


