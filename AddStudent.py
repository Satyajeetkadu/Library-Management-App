from tkinter import *
from tkinter import messagebox
import mysql.connector as my


con= my.connect(host = 'localhost',
                  user= 'root',
                  password='',
                  database='db')

if con:
    print("Connection was succesful...")
else:
    print ("Connection failed...")

cur = con.cursor()

'''try:
    cur.execute("Create table student(sid varchar(20), name varchar(30))")
except Exception as e:
    print(e)
'''
def bookRegister():
    #data entry of the variables
    sid = bookInfo1.get()
    name = bookInfo2.get()
    
    #UPDATE TO THE DATABASE HERE
    insertStudents = "insert into student values ('"+sid+"','"+name+"')"
    try:
        cur.execute(insertStudents)
        con.commit()
        messagebox.showinfo('Success',"Student added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")

   
    print(sid)
    print(name)

#page gets closed
    root.destroy()
   
def addStu(): 
    
    global bookInfo1,bookInfo2,root
    
    root = Tk()
    root.title("Library Management system: Add Book")
    root.minsize(width=600,height=600)
    root.geometry("800x650")
    
    # Enter Table Names here
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Student ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Student Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
      
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
