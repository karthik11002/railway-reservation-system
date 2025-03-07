from tkinter import *
from tkinter import messagebox, ttk
import pymysql
from PIL import Image,ImageTk

class login:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.resizable(False, False)
        self.root.title("JDK Railway Reservation System  -Login")
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)

        loginFrame = Frame(self.root, bg="#38548c", relief=GROOVE, border=20).place(x=350, y=350, height=400, width=600)
        label1 = Label(text="JDK Railway Reservation System", font=("Comic Sans MS", 25, "bold"), bg="#38548c",fg="White").place(x=382, y=400)






        self.email_text = StringVar()
        self.password_text = StringVar()



        self.emailLabel = Label(loginFrame, text="Email:", font=("Georgia", 20), bg="#38548c", fg="White").place(x=460, y=490)
        emailTb = Entry(loginFrame, textvariable=self.email_text, font=("Georgia", 20), width=18, border=3,relief=GROOVE)
        emailTb.place(x=550, y=490)


        self.passwordLabel = Label(loginFrame, text="Password:", font=("Georgia", 20), bg="#38548c", fg="White").place(x=420, y=560)
        passwordTb = Entry(loginFrame, textvariable=self.password_text, font=("Georgia", 20), width=18, border=3,relief=GROOVE)
        passwordTb.place(x=550, y=560)

        login = Button(loginFrame, text="Login", font=("Georgia", 15, "bold"), bd=0, cursor="hand2", width=22,relief=GROOVE, border=3, bg="#38548C", fg="white",command=self.loginbtnclick).place(x=500, y=630)
        registerbtn = Button(loginFrame, text="New User? Register Here",font=("Georgia", 10),bd=0, bg="#38548C",fg="white", width=22,cursor="hand2",command=self.registerbtnclick).place(x=565,y=685)


    def registerbtnclick(self):
        self.root.destroy()
        import Register

    def loginbtnclick(self):
        if( self.email_text.get()=="" or self.password_text.get()==""):
            messagebox.showerror("Error","All Fields Must be Required", parent=self.root)
        else:
            try:
                global emailtransfer
                emailtransfer=self.email_text.get()
                con = pymysql.connect(host="localhost",user="root",password="",database="Railway")
                c = con.cursor()
                c.execute("select * from users where Email=%s and Password=%s", (self.email_text.get(), self.password_text.get()))
                row=c.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Details", parent=self.root)
                else:
                    self.root.destroy()
                    import userwelcome




            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)





root = Tk()
obj = login(root)
root.mainloop()