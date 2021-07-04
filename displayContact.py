from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

mydb=mysql.connector.connect(host='localhost',user="root",passwd="@Sumeet06",db="contactdb",autocommit=True)
mycursor=mydb.cursor()
class Display(Toplevel):
    def __init__(self,firstName,lastName):
        Toplevel.__init__(self)
        self.geometry("600x500+350+20")
        self.title("Display Contact")
        self.iconbitmap("D:\VS PYTHON\ContactBook\icon.ico")
        self.resizable(False,False)
        self.firstName=firstName
        self.lastName=lastName
        
        #frames
        self.top=Frame(self,height=150,bg="#7b5957")
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=450,bg="#d8d8d8")
        self.bottom.pack(fill=X)
        
        self.heading=Label(self.top,text="Display Contact",font="arial 15 bold",bg="#7b5957")
        self.heading.place(x=240,y=60)
        
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        self.tree=ttk.Treeview(self.bottom, height=8, yscrollcommand=self.scroll.set)
        self.tree['columns']=("First Name","Last Name","Contact","E-mail","City")
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('First Name', anchor=CENTER, width=100)
        self.tree.column('Last Name', anchor=CENTER, width=100)
        self.tree.column('Contact', anchor=CENTER, width=120)
        self.tree.column('E-mail', anchor=CENTER, width=150)
        self.tree.column('City', anchor=CENTER, width=120) 
        self.scroll.config(command=self.tree.yview)
        self.tree.grid(row=0,column=0,padx=(4,0),sticky="n")
        self.tree.heading('#0', text='', anchor=CENTER)
        self.tree.heading('First Name', text='FirstName', anchor=CENTER)
        self.tree.heading('Last Name', text='LastName', anchor=CENTER)
        self.tree.heading('Contact', text='Contact', anchor=CENTER)
        self.tree.heading('E-mail', text='Email', anchor=CENTER)
        self.tree.heading('City', text='City', anchor=CENTER)
        
        
        sql="SELECT * FROM addressbook where FName=%s AND LName=%s"
        val = (firstName, lastName)
        mycursor.execute(sql, val)
        contact=mycursor.fetchone()
        self.tree.insert("", 'end', values=(contact[1], contact[2],str(contact[4]),contact[3],contact[5]))
        
        backbtn=Button(self.bottom,text="Back",width=12,font="sans 12 bold",command=self.onBack)
        backbtn.grid(pady=80)
        
    def onBack(self):
        self.destroy()