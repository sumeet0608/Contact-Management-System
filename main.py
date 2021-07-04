from tkinter import *
from tkinter import messagebox as mb
from allContacts import AllContacts
from addContact import AddContact
from PIL import Image, ImageTk
import tkinter as tk

class Application(object):
    def __init__(self,master):
        self.master=master
        IMAGE_PATH = 'bg1.png'
        WIDTH, HEIGHT = 600, 500   
        #frames
        self.top=Frame(master,height=150,bg="#b35c44")  # ccffff
        self.top.pack(fill=X)
        self.bottom=Frame(master,height=450) # 006666
        self.bottom.pack(fill=X)
        self.img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        self.lbl = tk.Label(self.bottom, image=self.img)
        self.lbl.img = self.img  # Keep a reference in case this code put is in a function.
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')  
        self.heading=Label(self.top,text="My Contact Book",font="arial 15 bold",bg="#b35c44")
        self.heading.place(x=220,y=50)
        
        #buttons
        self.allContacts=Button(self.bottom,text="All Contacts",width=12,font="arial 12 bold",command=self.all_contacts)
        self.allContacts.place(x=245,y=70)
        
        self.addPeople=Button(self.bottom,text="ADD Contact",width=12,font="arial 12 bold",command=self.add_contact)
        self.addPeople.place(x=245,y=130)
        
        self.aboutUs=Button(self.bottom,text="About Us",width=12,font="arial 12 bold")
        self.aboutUs.place(x=245,y=190)
        
        self.exitBtn=Button(self.bottom,text="Exit",width=12,font="arial 12 bold",command=self.onClick)
        self.exitBtn.place(x=245,y=250)
        
    def all_contacts(self):
        contacts= AllContacts()
    def add_contact(self):
        add_page= AddContact()
    def onClick(self):
        answer = mb.askyesno('Exit Application','Are you sure that you want to quit?')
        if answer:
            self.master.destroy()

def main():
    root=Tk()
    app = Application(root)
    root.geometry("600x500+350+20")
    root.title("Phone Book Application")
    root.iconbitmap("icon.ico")
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    main()
    
