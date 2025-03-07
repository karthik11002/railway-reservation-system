from tkinter import *
from tkinter import messagebox, ttk
import pymysql
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import random
import datetime


class Main:
    def __init__(self, root):


        self.root = root
        self.root.geometry('1920x1080')
        self.root.resizable(False, False)
        self.root.title("JDK Railway Reservation System ")
        self.root.configure(bg='#cbd4cd')
        lbl_heading = Label(self.root, text="JDK Railway Reservation System", font=("Comic Sans MS", 28, "bold"), bg="#cbd4cd", fg="black", bd=10, relief=RIDGE).pack(side=TOP, fill=X)
        mainframe = Frame(root, bg='black', relief=GROOVE, bd=10).place(x=15, y=80, width=710, height=900)
        detailsframe = Frame(root,bg="black", relief=GROOVE,bd=10).place(x=740,y=80,width=1160,height=900)

        self.emailTb_text = StringVar()
        self.sPoint_text = StringVar()
        self.ePoint_text = StringVar()
        self.date_text = StringVar()
        self.time_text = StringVar()
        self.fname_text = StringVar()
        self.gender_text = StringVar()
        self.age_text = StringVar()
        self.address_text = StringVar()
        self.pincode_text = StringVar()
        self.phone_text = StringVar()
        self.verifytext = StringVar()
        self.verifytext.set("Verify")
        self.ticketId = StringVar()
        self.n = StringVar()
        self.cost = StringVar()
        self.status = StringVar()
        self.status.set("Pending")
        self.totalcost = StringVar()
        self.totalcost.set("0")
        self.payment = StringVar()




        sampleLabel = Label(self.root, text="Book Ticket", font=("Comic Sans MS", 28, "bold"), fg='white',
                           bg='black').place(x=290, y=95)


        emailLabel = Label(self.root, text="Email:", font=("Times new Romon", 20, "bold"), fg='white',bg='black').place(x=30,y=163)
        emailTb = Entry(self.root,textvariable=self.emailTb_text,font=("Times new Romon", 20, "bold"), fg='Black',width=30)
        emailTb.place(x=120,y=165)
        self.checkmail = Button(self.root,textvariable=self.verifytext,font=("Georgia", 13, "bold"), bd=0, cursor="hand2", width=10,
                                relief=GROOVE, border=3, bg="black",fg="white",command=self.verify_mail).place(x=580,y=165)




        self.startingPointlbl = Label(mainframe,text="From:", font=("Times new Romon", 20, "bold"), fg='white',bg='black').place(x=80,y=230)
        sPointChoice = ttk.Combobox(mainframe,textvariable=self.sPoint_text, width=25, font=("Georgia", 19), state="readonly")
        sPointChoice['values'] = ("Select", "Hyderabad", "Vijayawada", "Visakhapatnam","Guntur","Annavaram","Tirupati")
        sPointChoice.place(x=280,y=230)
        sPointChoice.current(0)

        self.endingPointlbl = Label(mainframe, text="To:", font=("Times new Romon", 20, "bold"),fg='white', bg='black').place(x=80, y=290)
        ePointChoice = ttk.Combobox(mainframe, textvariable=self.ePoint_text, width=25, font=("Georgia", 19),state="readonly")
        ePointChoice['values'] = ("Select", "Hyderabad", "Vijayawada", "Visakhapatnam","Guntur","Annavaram","Tirupati")
        ePointChoice.place(x=280, y=290)
        ePointChoice.current(0)

        self.dateLabel = Label(mainframe, text="Date:", font=("Times new Romon", 20, "bold"), bg="black", fg="White").place(x=80,y=350)
        dateTb = DateEntry(mainframe,textvariable=self.date_text,width=29, year=2021, month=4, day=19, background='darkblue',
                           foreground='white', borderwidth=20, font=("Times new Romon", 18))
        dateTb.place(x=280,y=350)

        self.Timelbl = Label(mainframe, text="Time:", font=("Times new Romon", 20, "bold"), fg='white', bg='black').place(x=80, y=410)
        timeChoice = ttk.Combobox(mainframe, textvariable=self.time_text, width=27, font=("Times new Romon", 19),state="readonly")
        timeChoice['values'] = ("9:00 AM", "12:00 PM", "4:00 PM", "7:00 PM", "10:00 PM")
        timeChoice.place(x=280, y=410)
        timeChoice.current(1)

        self.fullnameLabel = Label(mainframe, text="Full Name:", font=("Times new Romon", 20, "bold"), bg="black",fg="White").place(x=80, y=470)
        fullnameTb = Entry(mainframe, textvariable=self.fname_text, font=("Georgia", 20), width=23, border=3,relief=GROOVE)
        fullnameTb.place(x=280, y=470)

        self.genderLabel = Label(mainframe, text="Gender:", font=("Times new Romon", 20, "bold"), bg="black", fg="White").place(x=80, y=530)
        genderChoice = ttk.Combobox(mainframe, textvariable=self.gender_text, width=25, font=("Georgia", 19),state="readonly")
        genderChoice['values'] = ("Select", "Male", "Female", "other")
        genderChoice.place(x=280, y=530)
        genderChoice.current(0)

        self.ageLabel = Label(mainframe, text="Age:", font=("Times new Romon", 20, "bold"), bg="black",fg="White").place(x=80, y=590)
        AgeTb = Entry(mainframe, textvariable=self.age_text, font=("Georgia", 20), width=23, border=3,relief=GROOVE)
        AgeTb.place(x=280, y=590)



        self.addresslbl = Label(mainframe, text="Address:",font=("Times new Romon", 20, "bold"), bg="black",fg="White").place(x=80, y=650)
        addressTb = Entry(mainframe, textvariable=self.address_text, font=("Georgia", 20), width=23, border=3, relief=GROOVE)
        addressTb.place(x=280, y=650)

        self.pinLabel = Label(mainframe, text="Pincode:", font=("Times new Romon", 20, "bold"), bg="black",fg="White").place(x=80, y=710)
        AgeTb = Entry(mainframe, textvariable=self.pincode_text, font=("Georgia", 20), width=23, border=3, relief=GROOVE)
        AgeTb.place(x=280, y=710)


        self.phonenumberlbl = Label(mainframe, text="Phone Number:", font=("Times new Romon", 19, "bold"), bg="black",fg="White").place(x=80, y=770)
        phoneTb = Entry(mainframe, textvariable=self.phone_text, font=("Georgia", 20), width=23, border=3,relief=GROOVE)
        phoneTb.place(x=280, y=770)

        mainmenuBtn = Button(self.root,text="Main menu",command=self.mainmenuclick, font=("Comic Sans MS", 18, "bold"),bd=1,
                             relief=GROOVE, bg="black",fg="White",width=125,cursor="hand2").place(x=15,y=985)

        updateBtn=Button(mainframe, text="Update Details",font=("Times new Romon", 20, "bold"),bd=10,relief=GROOVE
                              , bg="black",fg="White",width=15,cursor="hand2",command=self.updatedetails).place(x=80,y=850)

        savedetails = Button(mainframe, text="Save Details", font=("Times new Romon", 20, "bold"), bd=10, relief=GROOVE
                                , bg="black", fg="White", width=15, cursor="hand2",command=self.savebook).place(x=400,y=850)

        bookticketBtn = Button(detailsframe,text="Book Tickets",font=("Times new Romon", 20, "bold"),bd=10,relief=GROOVE
                              , bg="black",fg="White",width=20,cursor="hand2",command=self.bookticket).place(x=1510,y=880)

        Totallbl=Label(detailsframe,text="Total:",font=("Times new Romon",20,"bold"),bg="Black",fg="White").place(x=1600,y=790)

        totalcost=Label(detailsframe,textvariable=self.totalcost,font=("Times new Romon",20,"bold"),bg="Black",fg="White").place(x=1680,y=790)

        paymentoption=ttk.Combobox(detailsframe,textvariable=self.payment, width=23, font=("Georgia", 19), state="readonly")
        paymentoption['values'] = ("Payment Method", "Google pay", "Phonepay", "Bank Transfer")
        paymentoption.place(x=1510,y=830)
        paymentoption.current(0)



        detailsframe2=Frame(detailsframe,bd=4, relief=RIDGE, bg="black")
        detailsframe2.place(x=760,y=100,width=1121, height=580)
        scrollY = Scrollbar(detailsframe2, orient=VERTICAL)
        self.Tickets_table = ttk.Treeview(detailsframe2, columns=(
        "ticketid","email","name","from", "to", "cost","pnumber","pincode","address","gender","age","status", "traveldate"), yscrollcommand=scrollY)
        
        scrollY.pack(side=RIGHT, fill=Y)

        scrollY.config(command=self.Tickets_table.yview_scroll)
        self.Tickets_table.heading("ticketid", text="Ticket Id")
        self.Tickets_table.heading("email", text="Email")
        self.Tickets_table.heading("name", text="Name")
        self.Tickets_table.heading("from", text="From")
        self.Tickets_table.heading("to", text="To")
        self.Tickets_table.heading("cost", text="Cost")
        self.Tickets_table.heading("pnumber",text="Phone Number")
        self.Tickets_table.heading("pincode",text="Pincode")
        self.Tickets_table.heading("address",text="Address")
        self.Tickets_table.heading("gender",text="Gender")
        self.Tickets_table.heading("age",text="Age")
        self.Tickets_table.heading("status",text="Status")
        self.Tickets_table.heading("traveldate",text="Date")
        self.Tickets_table['show'] = 'headings'

        self.Tickets_table.column("ticketid", width=50)
        self.Tickets_table.column("email", width=50)
        self.Tickets_table.column("name", width=50)
        self.Tickets_table.column("from", width=50)
        self.Tickets_table.column("to", width=50)
        self.Tickets_table.column("cost", width=50)
        self.Tickets_table.column("pnumber",width=50)
        self.Tickets_table.column("pincode",width=50)
        self.Tickets_table.column("address",width=50)
        self.Tickets_table.column("gender",width=50)
        self.Tickets_table.column("age",width=10)
        self.Tickets_table.column("status",width=50)
        self.Tickets_table.column("traveldate",width=50)
        self.Tickets_table.pack(fill=BOTH, expand=1)
        self.Tickets_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.getTickets()




    def mainmenuclick(self):
        msg=messagebox.askquestion("JDK Railway reservation System","Aru you sure want to go Main Menu",parent=self.root)
        if msg=="yes":
            self.root.destroy()
            import userwelcome

    def savebook(self):
        if (
            self.verifytext.get()=="Verify" or
            self.sPoint_text.get()=="Select" or
            self.ePoint_text.get()=="Select" or
            self.date_text.get()=="4/19/21" or
            self.time_text.get()=="" or
            self.fname_text.get()=="" or
            self.gender_text.get()=="Select" or
            self.age_text.get()=="" or
            self.address_text.get()=="" or
            self.pincode_text.get()=="" or
            self.phone_text.get()==""
            ):
            messagebox.showerror("Error","All fields must be Required",parent=self.root)
        elif self.sPoint_text.get() == self.ePoint_text.get():
            messagebox.showerror("Error","You cannot select both From and To Points as same")

        else:
            msg = messagebox.askquestion("CrossCheck Your Details Again",f"{self.sPoint_text.get()} To {self.ePoint_text.get()} On {self.date_text.get()} At {self.time_text.get()} Name: {self.fname_text.get()} Gender: {self.gender_text.get()} Age: {self.age_text.get()} PhoneNumber: {self.phone_text.get()}",parent=self.root)
            if msg=="yes":
                self.n=random.randint(10000,99999)
                try:
                    self.status.set("Pending")
                    conn=pymysql.connect(host="localhost",user="root",password="",database="railway")
                    c=conn.cursor()
                    c.execute("Select * from costs WHERE startpoint=%s and endpoint=%s",(self.sPoint_text.get(),self.ePoint_text.get()))
                    costmain=c.fetchone()
                    self.cost.set(costmain[2])
                    c.execute("Insert into nooftickets (ticketid, email, name, startpoint, endpoint, cost, pnumber, pincode, address, gender, age, status, traveldate, 	bookingdate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              ( self.n,
                                self.emailTb_text.get(),
                                self.fname_text.get(),
                                self.sPoint_text.get(),
                                self.ePoint_text.get(),
                                self.cost.get(),
                                self.phone_text.get(),
                                self.pincode_text.get(),
                                self.address_text.get(),
                                self.gender_text.get(),
                                self.age_text.get(),
                                self.status.get(),
                                self.date_text.get(),
                                datetime.datetime.now().date(),))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully added ticket",parent=self.root)
                    self.fname_text.set(" ")
                    self.age_text.set(" ")
                    self.address_text.set(" ")
                    self.pincode_text.set("")
                    self.phone_text.set(" ")
                    self.getTickets()

                except Exception as es:
                    messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)

            else:
                print("no")


    def getTickets(self):
        self.status.set("Pending")
        conn = pymysql.connect(host="localhost",user="root",password="",database="railway")
        c = conn.cursor()
        c.execute("Select * from nooftickets where email = %s",(self.emailTb_text.get()))
        rows = c.fetchall()
        if len(rows)!=0:
            self.Tickets_table.delete(*self.Tickets_table.get_children())
            for row in rows:
                self.Tickets_table.insert('', END, values=row)
            conn.commit()
            conn.close()
            self.costmain()

    def costmain(self):
        self.status.set("Pending")
        conn = pymysql.connect(host="localhost",user="root",password="",database="railway")
        c = conn.cursor()
        c.execute("Select SUM(cost) from nooftickets where email = %s and Status = %s",(self.emailTb_text.get(), self.status.get()))
        rows = c.fetchone()
        print(rows)
        if rows is None:
            self.totalcost.set("0")
        else:
            self.totalcost.set(rows)
        conn.commit()
        conn.close()



    def get_cursor(self, event):
        row_cursor = self.Tickets_table.focus()
        contents = self.Tickets_table.item(row_cursor)
        self.row = contents['values']
        self.ticketId.set(self.row[0])
        self.emailTb_text.set(self.row[1])
        self.fname_text.set(self.row[2])
        self.sPoint_text.set(self.row[3])
        self.ePoint_text.set(self.row[4])
        self.cost.set(self.row[5])
        self.phone_text.set(self.row[6])
        self.pincode_text.set(self.row[7])
        self.address_text.set(self.row[8])
        self.gender_text.set(self.row[9])
        self.age_text.set(self.row[10])




    def bookticket(self):
        if self.payment.get()=="Payment Method":
            messagebox.showerror("Error","Select the payment method",parent=self.root)
        else:
            try:
                self.status.set("Confirmed")
                conn=pymysql.connect(host="localhost",user="root",password="",database="railway")
                c=conn.cursor()
                c.execute("Update nooftickets SET status=%s  Where email=%s",(self.status.get(), self.emailTb_text.get()))
                c.execute("Update nooftickets SET Payment=%s  Where email=%s",(self.payment.get(), self.emailTb_text.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your ticket is Confirmed")
                self.getTickets()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)







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
                    self.getTickets()


            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)



    def updatedetails(self):
        if (
            self.verifytext.get()=="Verify" or
            self.sPoint_text.get()=="Select" or
            self.ePoint_text.get()=="Select" or
            self.date_text.get()=="4/19/21" or
            self.time_text.get()=="" or
            self.fname_text.get()=="" or
            self.gender_text.get()=="Select" or
            self.age_text.get()=="" or
            self.address_text.get()=="" or
            self.pincode_text.get()=="" or
            self.phone_text.get()==""
            ):
            messagebox.showerror("Error","All fields must be Required",parent=self.root)
        elif self.sPoint_text.get() == self.ePoint_text.get():
            messagebox.showerror("Error","You cannot select both From and To Points as same")

        else:
            msg = messagebox.askquestion("CrossCheck Your Details Again",f"{self.sPoint_text.get()} To {self.ePoint_text.get()} On {self.date_text.get()} At {self.time_text.get()} Name: {self.fname_text.get()} Gender: {self.gender_text.get()} Age: {self.age_text.get()} PhoneNumber: {self.phone_text.get()}",parent=self.root)
            if msg=="yes":

                try:
                    self.status.set("Pending")
                    conn=pymysql.connect(host="localhost",user="root",password="",database="railway")
                    c=conn.cursor()
                    c.execute("Select * from costs WHERE startpoint=%s and endpoint=%s",(self.sPoint_text.get(),self.ePoint_text.get()))
                    costmain=c.fetchone()
                    self.cost.set(costmain[2])
                    print(self.cost.get())


                    c.execute("Update nooftickets SET ticketid=%s, email=%s, name=%s, startpoint=%s, endpoint=%s, cost=%s, pnumber=%s, pincode=%s, address=%s, gender=%s, age=%s, status=%s WHERE ticketid=%s",
                              (
                                self.ticketId.get(),
                                self.emailTb_text.get(),
                                self.fname_text.get(),
                                self.sPoint_text.get(),
                                self.ePoint_text.get(),
                                self.cost.get(),
                                self.phone_text.get(),
                                self.pincode_text.get(),
                                self.address_text.get(),
                                self.gender_text.get(),
                                self.age_text.get(),
                                self.status.get(),
                                self.ticketId.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Updated ticket",parent=self.root)
                    self.fname_text.set(" ")
                    self.age_text.set(" ")
                    self.address_text.set(" ")
                    self.pincode_text.set("")
                    self.phone_text.set(" ")
                    self.getTickets()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)





root = Tk()
obj = Main(root)
root.mainloop()