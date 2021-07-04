from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

mydb=mysql.connector.connect(host='localhost',user="root",passwd="@Sumeet06",db="contactdb",autocommit=True)
mycursor=mydb.cursor()

class Search(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x500+350+20")
        self.title("Search Contact")
        self.iconbitmap("D:\VS PYTHON\ContactBook\icon.ico")
        self.resizable(False,False)
        
        #frames
        self.top=Frame(self,height=150,bg="#7b5957")
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=450,bg="#d8d8d8")
        self.bottom.pack(fill=X)
        
        self.heading=Label(self.top,text="Search Contact",font="arial 15 bold",bg="#7b5957")
        self.heading.place(x=240,y=60)
        
        self.myLabel1=Label(self.bottom,text="Select an option:",font="arial 14",bg="#d8d8d8").grid(row=0,column=0,padx=10,columnspan=1)
        self.myLabel2=Label(self.bottom,text="Enter the First Name:",font="arial 14",bg="#d8d8d8")
        self.entry_search=Entry(self.bottom,font="arial 10",width=30,bd=2)
        self.searchBtn=Button(self.bottom,text="Search",width=12,font="sans 12 bold",command=self.search_contact)
        
        self.option=StringVar()
        self.myComboBox=ttk.Combobox(self.bottom,textvariable=self.option,width=20,state='readonly')
        self.myComboBox['values']=('Name','Number')
        self.myComboBox.grid(row=0,column=1,columnspan=1)
        self.myComboBox.current(0)
        button1=Button(self.bottom,text="Select Option",width=12,font="sans 12 bold",command=self.select_option)
        button1.grid(row=1,column=0,padx=10,columnspan=1)
        
        #display searched contact
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        self.listBox=Listbox(self.bottom,font=("lucida ",10),width=30,height=13)
        
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)
        
    def select_option(self):
        self.option=self.myComboBox.get()
        if self.option=="Name":
            self.myLabel2.grid(row=2,column=0,padx=10,columnspan=1)
            self.myLabel2.config(text="")
            self.myLabel2.config(text="Enter First Name:")
            self.entry_search=Entry(self.bottom,font="arial 10",width=30,bd=2)
            self.entry_search.grid(row=2,column=1)
            self.searchBtn.grid(row=3,column=0,padx=10,columnspan=1)
        elif self.option=="Number":
            self.myLabel2.grid(row=2,column=0,padx=10,columnspan=1)
            self.myLabel2.config(text="")
            self.myLabel2.config(text="Enter the Number:")
            self.entry_search.grid(row=2,column=1)
            self.searchBtn.grid(row=3,column=0,padx=10,columnspan=1)
        else:
            mb.showwarning("Search Status","No option selected")
    
    def search_contact(self):
        if self.option=="Name":
            first_name=self.entry_search.get()
            if first_name=="":
                mb.showerror('Search Status','No first name entered')
                return
            sql='SELECT * from addressbook where FNAME=%s'
            val=(first_name,)
            mycursor.execute(sql,val)
            contacts=mycursor.fetchall()
            if len(contacts)==0:
                mb.showinfo('Search Status', 'No Contact found')
                return
            else:
                self.listBox.grid(row=4,column=0,padx=(29,0),columnspan=1)
                count=0
                self.listBox.delete(0,'end')        
                for contact in contacts:
                    self.listBox.insert(count,str(contact[1]+" "+ contact[2]))
                    count+=1
                self.scroll.grid(row=4,column=0,sticky=N+S)
        elif self.option=="Number":
            number=self.entry_search.get()
            if number=="":
                mb.showerror('Search Status','No number entered')
                return
            sql='SELECT * from addressbook where Phone_Number=%s'
            val=(number,)
            mycursor.execute(sql,val)
            contacts=mycursor.fetchall()
            if len(contacts)==0:
                mb.showinfo('Search Status', 'No Contact found')
                return
            else:
                self.listBox.grid(row=4,column=0,padx=(29,0),columnspan=1)
                count=0
                self.listBox.delete(0,'end')        
                for contact in contacts:
                    self.listBox.insert(count,str(contact[1]+" "+ contact[2]))
                    count+=1
                self.scroll.grid(row=4,column=0,sticky=N+S)
        else:
            mb.showwarning("Search Status","No option selected")
        