from tkinter import *
from PIL import Image, ImageTk

class main:
    def __init__(self, main):
        self.root = main
        self.root.geometry('1920x1080')
        self.root.resizable(False, False)
        self.root.title("JDK Railway Reservation System   -main")
        self.bg=ImageTk.PhotoImage(file="images/bg.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)


        mainframe=Frame(root, bg="#38548c", relief=GROOVE, border=20).place(x=300, y=250, height=600, width=800)

        label1 = Label(text="JDK Railway Reservation System", font=("Comic Sans MS", 33, "bold"), bg="#38548c", fg="White").place(x=350,y=350)
        register = Button(mainframe,text="Register",font=("Comic Sans MS", 20, "bold"),bd=0,cursor="hand2", width=30,relief=GROOVE,border=10,command=self.registerbtn,bg="#E078B6").place(x=450,y=500)
        login = Button(mainframe, text="Login", font=("Comic Sans MS", 20, "bold"), bd=0, cursor="hand2", width=30,relief=GROOVE,border=10,command=self.loginbtn,bg="#E078B6").place(x=450, y=620)

    def registerbtn(self):
        self.root.destroy()
        import Register
    def loginbtn(self):
        self.root.destroy()
        import Login



root = Tk()
obj = main(root)
root.mainloop()



