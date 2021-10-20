
import pymysql
from AddBook import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *
from ViewBooks import *
from AddStudent import *

from tkinter import *
from tkinter import messagebox


class Login:

    def __init__(self, root):

        self.root = root
        self.root.title("Login and registration ")
        self.root.geometry("1366x700+0+0")
        self.root.resizable(False, False)
        self.loginform()

    def loginform(self):

        Frame_login = Frame(self.root, bg="#006B38")
        Frame_login.place(x=0, y=0, height=700, width=1366)


        frame_input = Frame(self.root, bg="#006B38")
        frame_input.place(x=320, y=130, height=450, width=350)

        headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="Login Here", bg='black', fg='white', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


        label2 = Label(frame_input, text="Username", font=("times new roman", 20, "bold"),

                       fg='white', bg='black')
        label2.place(x=5, y=95)


        self.email_txt = Entry(frame_input, font=("times new roman", 15, "bold"),

                               bg='lightgray')
        self.email_txt.place(x=5, y=145, width=270, height=35)


        label3 = Label(frame_input, text="Password", font=("times new roman", 20, "bold"),

                       fg='white', bg='black')
        label3.place(x=5, y=195)


        self.password = Entry(frame_input, font=("times new roman", 15, "bold"),

                              bg='lightgray')
        self.password.place(x=5, y=245, width=270, height=35)



        btn1 = Button(frame_input, text="Login", command=self.login, cursor="hand2",

                      font=("times new roman", 15), fg="black", bg='#f7f1e3',

                      bd=0, width=15, height=1)
        btn1.place(x=70, y=340)



        btn2 = Button(frame_input, command=self.Register, text="Not Registered?Register Here"

                      , cursor="hand2",  font=("times new roman", 15), fg="black", bg='#f7f1e3', bd=0)

        btn2.place(x=75, y=390)

    def login(self):

        if self.email_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:

                con = pymysql.connect(host='localhost', user='root', passwd='',
                                      database='db')

                cur = con.cursor()

                cur.execute('select * from register where emailid=%s and password=%s'
                            , (self.email_txt.get(), self.password.get()))

                row = cur.fetchmany()

                if row == None:
                    messagebox.showerror('Error', 'Invalid Username And Password'
                                         , parent=self.root)

                    self.email_txt.focus()

                else:
                    self.appscreen()
                    con.close()

            except Exception as es:
                messagebox.showerror('Error', f'Error Due to : {str(es)}'
                                     , parent=self.root)

    def Register(self):

        Frame_login1 = Frame(self.root, bg="#006B38")
        Frame_login1.place(x=0, y=0, height=700, width=1366)


        frame_input2 = Frame(self.root, bg="#006B38")
        frame_input2.place(x=320, y=130, height=450, width=630)

        headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="Register Here", bg='black', fg='white', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


        label2 = Label(frame_input2, text="Username", font=("times new roman", 20, "bold"),

                       fg='white', bg='black')
        label2.place(x=5, y=95)


        self.entry = Entry(frame_input2, font=("times new roman", 15, "bold"),
                           bg='lightgray')
        self.entry.place(x=5, y=145, width=270, height=35)


        label3 = Label(frame_input2, text="Password", font=("times new roman", 20, "bold"),
                       fg='white', bg='black')
        label3.place(x=5, y=195)


        self.entry2 = Entry(frame_input2, font=("times new roman", 15, "bold"),
                            bg='lightgray')
        self.entry2.place(x=5, y=245, width=270, height=35)


        label4 = Label(frame_input2, text="Email-id", font=("times new roman", 20, "bold"),
                       fg='white', bg='black')
        label4.place(x=330, y=95)


        self.entry3 = Entry(frame_input2, font=("times new roman", 15, "bold"),
                            bg='lightgray')
        self.entry3.place(x=330, y=145, width=270, height=35)


        label5 = Label(frame_input2, text="Confirm Password",
                       font=("times new roman", 20, "bold"), fg='white', bg='black')
        label5.place(x=330, y=195)


        self.entry4 = Entry(frame_input2, font=("times new roman", 15, "bold"),
                            bg='lightgray')
        self.entry4.place(x=330, y=245, width=270, height=35)



        btn2 = Button(frame_input2, command=self.register, text="Register"

                      , cursor="hand2",  font=("times new roman", 15), fg="black", bg='#f7f1e3', bd=0, width=15, height=1)
        btn2.place(x=205, y=340)


        btn3 = Button(frame_input2, command=self.loginform,
                      text="Already Registered?Login", cursor="hand2",
                      font=("times new roman", 15), fg="black", bg='#f7f1e3', bd=0)
        btn3.place(x=205, y=390)


    def register(self):

        if self.entry.get() == "" or self.entry2.get() == "" or self.entry3.get() == "" or self.entry4.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        elif self.entry2.get() != self.entry4.get():
            messagebox.showerror("Error", "Password and Confirm Password Should Be Same"
                                 , parent=self.root)

        else:
            try:

                con = pymysql.connect(host='localhost', user='root', passwd='',
                                      database='db')

                cur = con.cursor()


                cur.execute("select * from register where emailid=%s"

                            , self.entry3.get())
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error"

                                         , "User already Exist,Please try with another Email"

                                         , parent=self.root)
                    self.entry.focus()

                else:

                    cur.execute("insert into register values(%s,%s,%s,%s)"

                                , (self.entry.get(), self.entry3.get(),

                                   self.entry2.get(),

                                   self.entry4.get()))

                    con.commit()
                    con.close()

                    messagebox.showinfo("Success", "Registered Successfully"
                                        , parent=self.root)


            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}"
                                     , parent=self.root)

    def appscreen(self):




        root.title("Library Management System")
        root.minsize(width=600, height=600)
        root.geometry("800x650")
        same = True
        n = 0.25
        Canvas1 = Canvas(root)

        Canvas1.config(bg="#006B38")
        Canvas1.pack(expand=True, fill=BOTH)
        headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="MPSTME Library", bg='black', fg='white', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        btn1 = Button(root, text="Add Book ", bg='#f7f1e3', fg='black', command=addBook)
        btn1.place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.1)
        btn2 = Button(root, text="Delete Book", bg='#f7f1e3', fg='black', command=delete)
        btn2.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.1)
        btn3 = Button(root, text="View Books", bg='#f7f1e3', fg='black', command=View)
        btn3.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)
        btn4 = Button(root, text="Issue Book", bg='#f7f1e3', fg='black', command=issueBook)
        btn4.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)
        btn5 = Button(root, text="Return Book", bg='#f7f1e3', fg='black', command=returnBook)
        btn5.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)
        btn6 = Button(root, text="Add Student", bg='#f7f1e3', fg='black', command=addStu)
        btn6.place(relx=0.28, rely=0.85, relwidth=0.45, relheight=0.1)


root = Tk()
ob = Login(root)
root.mainloop()
