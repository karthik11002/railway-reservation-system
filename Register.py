from tkinter import *
from tkinter import messagebox, ttk
import pymysql
from PIL import Image, ImageTk
from tkcalendar import DateEntry


class Register:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.resizable(False, False)
        self.root.title("JDK Railway Reservation System  -Register")
        self.bg = ImageTk.PhotoImage(file="images/bg.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)


        registerframe = Frame(self.root, bg="#38548c", relief=GROOVE, border=20).place(x=300, y=250, height=600, width=800)


        self.fname_text = StringVar()
        self.lname_text = StringVar()
        self.phonenumber_text = StringVar()
        self.email_text = StringVar()
        self.gender_text = StringVar()
        self.dob_text = StringVar()
        self.password_text = StringVar()
        self.cpassword_text = StringVar()


        label1 = Label(text="JDK Railway Reservation System", font=("Comic Sans MS", 33, "bold"), bg="#38548c",fg="White").place(x=350, y=280)

        self.firstnameLabel = Label(registerframe,text="First Name", font=("Georgia", 15), bg="#38548c", fg="White").place(x=350, y=380)
        firstnameTb = Entry(registerframe,textvariable=self.fname_text, font=("Georgia", 20), width=18, border=3, relief=GROOVE)
        firstnameTb.place(x=353, y=410)

        self.lastnameLabel = Label(registerframe, text="Last Name", font=("Georgia",15), bg="#38548c", fg="White").place(x=700,y=380)
        lastnameTb = Entry(registerframe,textvariable=self.lname_text,font=("Georgia", 20), width=18, border=3, relief=GROOVE)
        lastnameTb.place(x=703,y=410)

        self.phonenumberLabel = Label(registerframe, text="Phone Number", font=("Georgia", 15), bg="#38548c", fg="White").place(x=350, y=470)
        phonenumberTb = Entry(registerframe,textvariable=self.phonenumber_text,font=("Georgia", 20), width=18, border=3, relief=GROOVE)
        phonenumberTb.place(x=353, y=500)

        self.emailLabel = Label(registerframe, text="Email", font=("Georgia", 15), bg="#38548c",fg="White").place(x=703, y=470)
        emailTb = Entry(registerframe,textvariable=self.email_text, font=("Georgia", 20), width=18, border=3, relief=GROOVE)
        emailTb.place(x=703, y=500)

        self.genderLabel = Label(registerframe, text="Gender", font=("Georgia", 15), bg="#38548c",fg="White").place(x=350, y=560)
        genderChoice = ttk.Combobox(registerframe,textvariable=self.gender_text, width=20, font=("Georgia", 19), state="readonly")
        genderChoice['values'] = ("Select", "Male", "Female", "other")
        genderChoice.place(x=350,y=590)
        genderChoice.current(0)

        self.dobLabel = Label(registerframe, text="D O B", font=("Georgia", 15), bg="#38548c",fg="White").place(x=703, y=560)
        dobTb = DateEntry(registerframe,textvariable=self.dob_text,width=20, year=2019, month=12, day=31, background='darkblue', foreground='white', borderwidth=20, font=("Georgia", 18))
        dobTb.place(x=703, y=590)

        self.passwordLabel = Label(registerframe, text="Password", font=("Georgia", 15), bg="#38548c", fg="White").place( x=350, y=650)
        passwordTb = Entry(registerframe,textvariable=self.password_text, font=("Georgia", 20), width=18, border=3, relief=GROOVE)
        passwordTb.place(x=350, y=680)

        self.cpasswordLabel = Label(registerframe, text="Confirm Password", font=("Georgia", 15), bg="#38548c", fg="White").place(x=703, y=650)
        cpasswordTb = Entry(registerframe,textvariable=self.cpassword_text, font=("Georgia", 20), width=18, border=3, relief=GROOVE)
        cpasswordTb.place(x=703, y=680)

        register = Button(registerframe, text="Register", font=("Georgia", 15, "bold"), bd=0, cursor="hand2", width=22, relief=GROOVE, border=3, bg="#38548C",fg="white",command=self.registerClick).place(x=520,y=740)
        loginBtn = Button(registerframe,text="Existing user? Login here", font=("Georgia", 10), bg="#38548C",fg="white",bd=0,cursor="hand2",command=self.loginbtnclick).place(x=600,y=795)


    def loginbtnclick(self):
        self.root.destroy()
        import Login

    def registerClick(self):
        if(self.fname_text.get() == "" or self.lname_text.get() == "" or self.password_text.get() == "" or self.email_text.get() == "" or self.gender_text.get() == "Select" or self.dob_text.get() == "12/31/19" or self.password_text.get() == "" or self.cpassword_text.get() == ""):
            messagebox.showerror("Error", "All Fields Must be Required", parent=self.root)
        elif (self.password_text.get() != self.cpassword_text.get()):
            messagebox.showerror("Error", "Password not mached", parent=self.root)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="Railway")
                c = con.cursor()
                c.execute("Insert into users(Fname, Lname, PhoneNumber, Email, Gender, DOB, Password) values(%s,%s,%s,%s,%s,%s,%s)",
                               (self.fname_text.get(),
                                self.lname_text.get(),
                                self.phonenumber_text.get(),
                                self.email_text.get(),
                                self.gender_text.get(),
                                self.dob_text.get(),
                                self.password_text.get()))
                con.commit()
                con.close()
                MsgBox = messagebox.showinfo("Success", "Successfully Registered", parent=self.root)
                if MsgBox == 'ok':
                    self.root.destroy()
                    import main

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)

root = Tk()
obj = Register(root)
root.mainloop()
