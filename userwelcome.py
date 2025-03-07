from tkinter import *
from tkinter import messagebox, ttk
import pymysql
from PIL import Image, ImageTk





class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.resizable(False, False)
        self.root.title("JDK Railway Reservation System ")

        self.verifytext=StringVar()
        self.verifytext.set("Verify")
        self.emailTb_text = StringVar()

        lbl_heading = Label(self.root, text="JDK Railway Reservation System", font=("Comic Sans MS", 28, "bold"),
                            bg="#cbd4cd", fg="black", bd=10, relief=RIDGE).pack(side=TOP, fill=X)
        mainframe = Frame(self.root, bg='black', relief=GROOVE, bd=10).place(x=650, y=150, width=600, height=600)

        bookticketBtn = Button(text="Book  Ticket", font=("Comic Sans MS", 20, "bold"), width=32,
                               command=self.bookticket).place(x=672, y=250)
        cancelticketBtn = Button(text="Cancel Ticket", font=("Comic Sans MS", 20, "bold"), width=32,
                                 command=self.cancelticket).place(x=672, y=350)
        generateticketBtn = Button(text="Generate Ticket", font=("Comic Sans MS", 20, "bold"), width=32,
                                  command=self.generateticket).place(x=672, y=450)

        deleteaccountBtn = Button(text="Delete Account", font=("Comic Sans MS", 20, "bold"), width=32,command=self.deleteaccount).place(x=672,
                                                                                                             y=550)


        logoutBtn = Button(text="Logout", font=("Comic Sans MS", 20, "bold"), command=self.logoutbtnclick, bg="black",
                           fg="white", bd=10, relief=GROOVE, width=10).place(x=1700, y=960)

        emailLabel = Label(self.root, text="Email:", font=("Times new Romon", 20, "bold"), fg='black',
                           bg='white').place(x=600, y=108)
        emailTb = Entry(self.root, textvariable=self.emailTb_text, font=("Times new Romon", 20, "bold"), bg="white",fg='black',
                        width=30)
        emailTb.place(x=690, y=108)
        self.checkmail = Button(self.root, textvariable=self.verifytext, font=("Georgia", 13, "bold"), bd=0,
                                cursor="hand2", width=10,
                                relief=GROOVE, border=3, bg="white", fg="black", command=self.verify_mail).place(x=1150,
                                                                                                                 y=108)




    def logoutbtnclick(self):
        msg = messagebox.askquestion("Logout", "Are you sure want to logout?", parent=self.root)
        if msg == "yes":
            self.root.destroy()
            import main

    def bookticket(self):
        msg = messagebox.askquestion("Book Ticket", "Are you sure want to Book Ticket?", parent=self.root)
        if msg == "yes":
            self.root.destroy()
            import bookticket

    def cancelticket(self):
        msg = messagebox.askquestion("Cancel Ticket", "Are you sure want to Cancel Ticket?", parent=self.root)
        if msg == "yes":
            self.root.destroy()
            import cancelticket

    def generateticket(self):
        msg = messagebox.askquestion("Generate ticket", "Are you sure want to Generate Ticket?", parent=self.root)
        if msg == "yes":
            self.root.destroy()
            import generateticket


    def verify_mail(self):
        if self.emailTb_text.get()=="":
            messagebox.showerror("Error","Email must be Entered",parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost",user="root",password="",database="Railway")
                c = conn.cursor()
                c.execute("Select * from users where Email=%s",(self.emailTb_text.get()))
                row = c.fetchone()
                if row==None:
                    messagebox.showerror("Error","Email is not registered",parent=self.root)
                else:
                    messagebox.showinfo("Success","Email is Verifed")
                    self.verifytext.set("Verifed")

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def deleteaccount(self):

        if self.verifytext.get()=="Verify":
            messagebox.showerror("Error","Email must be Verifed",parent=self.root)
        else:
            try:
                msg = messagebox.askquestion("Delete Account","Are you sure want to Delete Account",parent=self.root)
                if msg =="yes":
                    conn = pymysql.connect(host="localhost", user="root", password="", database="Railway")
                    c = conn.cursor()
                    c.execute("Delete from users where Email=%s", (self.emailTb_text.get()))
                    c.execute("Delete from nooftickets where email=%s", (self.emailTb_text.get()))
                    messagebox.showinfo("Success", "User Deleted Successfully", parent=self.root)
                    conn.commit()
                    conn.close()
                    self.root.destroy()
                    import main




            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)



root = Tk()
obj = Main(root)
root.mainloop()
