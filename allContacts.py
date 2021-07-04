from tkinter import *
from tkinter import messagebox as mb
import mysql.connector
from mysql.connector import Error
from updateContact import UpdateContacts
from displayContact import Display
from searchContact import Search

mydb=mysql.connector.connect(host='localhost',user="root",passwd="",db="contactdb",autocommit=True)
mycursor=mydb.cursor()

class AllContacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x500+350+20")
        self.title("All Contacts")
        self.iconbitmap("D:\VS PYTHON\ContactBook\icon.ico")
        self.resizable(False,False)
        
        #frames
        self.top=Frame(self,height=150,bg="#878a61")
        self.top.pack(fill=X)
        self.bottom=Frame(self,height=450,bg="#d6d6d6")
        self.bottom.pack(fill=X)
        
        self.heading=Label(self.top,text="All Contacts",font="arial 15 bold",bg="#878a61")
        self.heading.place(x=240,y=60)
        
        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        self.listBox=Listbox(self.bottom,font=("lucida ",10),width=40,height=27)
        self.listBox.grid(row=0,column=0,padx=(40,0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)
        
        mycursor.execute("select * from addressbook order by FNAME")
        contacts=mycursor.fetchall()
        count=0
        
        for contact in contacts:
            self.listBox.insert(count,str(contact[1]+" "+ contact[2]))
            count+=1
        self.scroll.grid(row=0,column=0,sticky=N+S)
        
        #buttons
        updatebtn=Button(self.bottom,text="Update",width=12,font="sans 12 bold",command=self.alterContact)
        updatebtn.grid(row=0,column=2,padx=20,pady=10,sticky=N)
        
        displaybtn=Button(self.bottom,text="Display",width=12,font="sans 12 bold",command=self.display)
        displaybtn.grid(row=0,column=2,padx=20,pady=60,sticky=N)
        
        deletebtn=Button(self.bottom,text="Delete",width=12,font="sans 12 bold",command=self.delete_contact)
        deletebtn.grid(row=0,column=2,padx=20,pady=110,sticky=N)
        
        searchbtn=Button(self.bottom,text="Search",width=12,font="sans 12 bold",command=self.search_contact)
        searchbtn.grid(row=0,column=2,padx=20,pady=160,sticky=N)
        
        backbtn=Button(self.bottom,text="Back",width=12,font="sans 12 bold",command=self.onBack)
        backbtn.grid(row=0,column=2,padx=20,pady=210,sticky=N)
        
    def alterContact(self):
        try:
            select=self.listBox.curselection()
            contact=self.listBox.get(select)
            firstName=contact.split()[0]
            lastName=contact.split()[1]
            update=UpdateContacts(firstName,lastName)
        except :
            mb.showerror('Error','Select a contact to update')
        
    def display(self):
        try:
            select=self.listBox.curselection()
            contact=self.listBox.get(select)
            firstName=contact.split()[0]
            lastName=contact.split()[1]
            disp=Display(firstName,lastName)
        except:
            mb.showerror('Error','Select a contact to display')
    
    def delete_contact(self):
        select=self.listBox.curselection()
        contact=self.listBox.get(select)
        firstName=contact.split()[0]
        lastName=contact.split()[1]
        
        sql='DELETE FROM addressbook WHERE FName=%s AND LName=%s'
        val=(firstName,lastName)
        answer = mb.askyesno('Delete Contact','Are you sure that you want to delete '+contact.split()[0]+' '+contact.split()[1]+'?')
        if answer:
            mycursor.execute(sql, val)
            mb.showinfo("Delete Status","Contact Deleted")
            mydb.commit()
            self.destroy()
        
    def search_contact(self):
        search=Search()
          
    def onBack(self):
        self.destroy()
