from tkinter import *
from tkinter import messagebox as mb
import mysql.connector
from mysql.connector import Error

class AddContact(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x500+350+20")
        self.title("ADD Contact")
        self.iconbitmap("D:\VS PYTHON\ContactBook\icon.ico")
        self.resizable(False,False)
        
        #frames
        self.top=Frame(self,height=150,bg="#aca48a")
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=450,bg="#d8d8d8")
        self.bottom.pack(fill=X)
        
        self.heading=Label(self.top,text="ADD Contact",font="arial 15 bold",bg="#aca48a")
        self.heading.place(x=240,y=60)
        
        #-----------------------------------------------------------------#
        self.label_fName=Label(self.bottom,text="First Name:",font="arial 15",bg="#d8d8d8")
        self.label_fName.place(x=49,y=20)
        
        self.entry_fName=Entry(self.bottom,font="arial 10",width=30,bd=2)
        self.entry_fName.insert(0, "First Name")
        self.entry_fName.place(x=164,y=20,height=30)
        #-----------------------------------------------------------------#
        self.label_lName=Label(self.bottom,text="Last Name:",font="arial 15",bg="#d8d8d8")
        self.label_lName.place(x=49,y=70)
        
        self.entry_lName=Entry(self.bottom,font="arial 10",width=30,bd=2)
        self.entry_lName.insert(0, "Last Name")
        self.entry_lName.place(x=164,y=70,height=30)
        #-----------------------------------------------------------------#
        self.label_eMail=Label(self.bottom,text="E-mail:",font="arial 15",bg="#d8d8d8")
        self.label_eMail.place(x=49,y=120)
        
        self.entry_eMail=Entry(self.bottom,font="arial 10",width=30,bd=2)
        self.entry_eMail.insert(0, "email@example.com")
        self.entry_eMail.place(x=164,y=120,height=30)
        #-----------------------------------------------------------------#
        self.label_contactNo=Label(self.bottom,text="Mobile:",font="arial 15",bg="#d8d8d8")
        self.label_contactNo.place(x=49,y=170)
        
        self.entry_contactNo=Entry(self.bottom,font="arial 10",width=30,bd=2)
        self.entry_contactNo.insert(0, "1234567890")
        self.entry_contactNo.place(x=164,y=170,height=30)
        #-----------------------------------------------------------------#
        self.label_city=Label(self.bottom,text="City:",font="arial 15",bg="#d8d8d8")
        self.label_city.place(x=49,y=210)
        
        self.entry_city=Entry(self.bottom,font="arial 10",width=30,bd=2)
        self.entry_city.insert(0, "Bangalore")
        self.entry_city.place(x=164,y=210,height=30)
        #-----------------------------------------------------------------#
        addBtn=Button(self.bottom,text="Save Contact",width=12,font="lucida 12 bold",command=self.add_contact)
        addBtn.place(x=150,y=270)
        
        backbtn=Button(self.bottom,text="Back",width=12,font="lucida 12 bold",command=self.onBack)
        backbtn.place(x=310,y=270)
        
        #self.entry_fName.bind("<Button-1>",self.click)   disappear placeholder
        #self.entry_fName.bind("<Leave>", self.leave)      disappear placeholder
    
    # def click(self,*args):         #disappear placeholder
       # self.entry_fName.delete(0, 'end')
    # def leave(self,*args):          #disappear placeholder
        #self.entry_fName.delete(0, 'end')
       # self.entry_fName.insert(0, 'First Name')
    def onBack(self):
        self.destroy()
    def add_contact(self):
        fName=self.entry_fName.get()
        lName=self.entry_lName.get()
        eMail=self.entry_eMail.get()
        phoneNo=self.entry_contactNo.get()
        city=self.entry_city.get()
        
        if fName=="" or fName=="First Name" or lName=="" or fName=="Last Name" or eMail=="" or eMail=="email@example.com" or phoneNo=="" or city=="":
            mb.showwarning("Insert Status","All fields required",icon="warning")
        else:
            mydb=mysql.connector.connect(host='localhost',user="root",passwd="@Sumeet06",db="contactdb",autocommit=True)
            mycursor=mydb.cursor()
            sql = "INSERT INTO addressbook (FName, LName, Email, Phone_Number, City) VALUES (%s, %s, %s, %s, %s)"
            val = (fName, lName, eMail, phoneNo, city)
            mycursor.execute(sql, val)
            mb.showinfo("Insert Status","Contact Added")
            mydb.commit()
            mydb.close()