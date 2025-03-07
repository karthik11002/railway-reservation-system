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

        self.emailTb_text = StringVar()
        self.verifytext = StringVar()
        self.verifytext.set("Verify")

        self.ticketid=StringVar()

        self.email=StringVar()

        self.name=StringVar()

        self.number=StringVar()

        self.fromaddress = StringVar()

        self.toaddress=StringVar()

        self.gender = StringVar()

        self.age = StringVar()

        self.bookingdate=StringVar()

        self.traveldate=StringVar()

        self.address=StringVar()

        self.pincode=StringVar()

        self.status = StringVar()

        self.cost = StringVar()




        lbl_heading = Label(self.root, text="JDK Railway Reservation System", font=("Comic Sans MS", 28, "bold"),
                            bg="#cbd4cd", fg="black", bd=10, relief=RIDGE).pack(side=TOP, fill=X)

        detailsframe = Frame(root, bg="black", relief=GROOVE, bd=10).place(x=250, y=80, width=1400, height=900)

        mainmenuBtn = Button(self.root, text="Main menu", command=self.mainmenuclick, font=("Comic Sans MS", 18, "bold"), bd=1,
                             relief=GROOVE, bg="black", fg="White", width=125, cursor="hand2").place(x=15, y=985)

        emailLabel = Label(self.root, text="Email:", font=("Times new Romon", 20, "bold"), fg='white', bg='black').place(x=600, y=100)
        emailTb = Entry(self.root, textvariable=self.emailTb_text, font=("Times new Romon", 20, "bold"), fg='Black',width=30)
        emailTb.place(x=690, y=100)
        self.checkmail = Button(self.root, textvariable=self.verifytext, font=("Georgia", 13, "bold"), bd=0,cursor="hand2", width=10,
                                relief=GROOVE, border=3, bg="black", fg="white",command=self.verify_mail).place(x=1150,y=100)

        ticketIdlbl=Label(self.root,text="Ticket Id:",font=("Times new Romon", 20, "bold"), fg='white', bg='black').place(x=300, y=550)
        ticketIdTxt = Entry(self.root,text="XXXXXXX",textvariable=self.ticketid,font=("Times new Romon", 20, "bold"), fg='white', bg='black',bd=0)
        ticketIdTxt.place(x=500, y=550)

        emaillbl = Label(self.root, text="Email:", font=("Times new Romon", 20, "bold"), fg='white',
                            bg='black').place(x=960, y=550)
        emailTxt = Entry(self.root, text="XXXXXXX", font=("Times new Romon", 20, "bold"),
                            fg='white', bg='black',textvariable=self.email,bd=0)
        emailTxt.place(x=1180, y=550)

        namelbl = Label(self.root, text="Name:", font=("Times new Romon", 20, "bold"), fg='white',
                         bg='black').place(x=300, y=600)
        nameTxt =Entry(self.root, text="XXXXXXX",  font=("Times new Romon", 20, "bold"),textvariable=self.name,
                         fg='white', bg='black',bd=0)
        nameTxt.place(x=500, y=600)

        numberlbl = Label(self.root, text="Phone Number:", font=("Times new Romon", 20, "bold"), fg='white',
                        bg='black').place(x=960, y=600)
        numberTxt =Entry(self.root, text="XXXXXXX", font=("Times new Romon", 20, "bold"),textvariable=self.number,
                        fg='white', bg='black',bd=0)
        numberTxt.place(x=1180, y=600)

        fromaddresslbl = Label(self.root, text="From:", font=("Times new Romon", 20, "bold"), fg='white',
                        bg='black').place(x=300, y=650)
        fromaddressTxt = Entry(self.root, text="XXXXXXX",  font=("Times new Romon", 20, "bold"),textvariable=self.fromaddress,
                        fg='white', bg='black',bd=0)
        fromaddressTxt.place(x=500, y=650)

        toaddresslbl = Label(self.root, text="To:", font=("Times new Romon", 20, "bold"), fg='white',
                          bg='black').place(x=960, y=650)
        toaddressTxt = Entry(self.root, text="XXXXXXX", font=("Times new Romon", 20, "bold"),textvariable=self.toaddress,
                          fg='white', bg='black',bd=0)
        toaddressTxt.place(x=1180, y=650)

        genderlbl = Label(self.root, text="Gender:", font=("Times new Romon", 20, "bold"), fg='white',
                               bg='black').place(x=300, y=700)
        genderTxt = Entry(self.root, text="XXXXXXX",
                               font=("Times new Romon", 20, "bold"),textvariable=self.gender,
                               fg='white', bg='black',bd=0)
        genderTxt.place(x=500, y=700)

        agelbl = Label(self.root, text="Age:", font=("Times new Romon", 20, "bold"), fg='white',
                          bg='black').place(x=960, y=700)
        ageTxt = Entry(self.root, text="XXXXXXX",  font=("Times new Romon", 20, "bold"),textvariable=self.age,
                          fg='white', bg='black',bd=0)
        ageTxt.place(x=1180, y=700)

        bookingdatelbl = Label(self.root, text="Booking Date:", font=("Times new Romon", 20, "bold"), fg='white',
                          bg='black').place(x=300, y=750)
        bookingdateTxt = Entry(self.root, text="XXXXXXX",
                          font=("Times new Romon", 20, "bold"),textvariable=self.bookingdate,
                          fg='white', bg='black',bd=0)
        bookingdateTxt.place(x=500, y=750)


        traveldatelbl = Label(self.root, text="Travel Date:", font=("Times new Romon", 20, "bold"), fg='white',
                               bg='black').place(x=960, y=750)
        traveldateTxt = Entry(self.root, text="XXXXXXX",
                               font=("Times new Romon", 20, "bold"),textvariable=self.traveldate,
                               fg='white', bg='black',bd=0)
        traveldateTxt.place(x=1180, y=750)

        addresslbl = Label(self.root, text="Address:", font=("Times new Romon", 20, "bold"), fg='white',
                               bg='black').place(x=300, y=800)
        addressTxt = Entry(self.root, text="XXXXXXX",
                               font=("Times new Romon", 20, "bold"),textvariable=self.address,
                               fg='white', bg='black',bd=0)
        addressTxt.place(x=500, y=800)

        pincodebl = Label(self.root, text="Pincode:", font=("Times new Romon", 20, "bold"), fg='white',
                              bg='black').place(x=960, y=800)
        pincodeTxt = Entry(self.root, text="XXXXXXX",
                              font=("Times new Romon", 20, "bold"),textvariable=self.pincode,
                              fg='white', bg='black',bd=0)
        pincodeTxt.place(x=1180, y=800)

        statuslbl = Label(self.root, text="Status:", font=("Times new Romon", 20, "bold"), fg='white',
                           bg='black').place(x=300, y=850)
        statusTxt = Entry(self.root, text="XXXXXXX",
                           font=("Times new Romon", 20, "bold"),textvariable=self.status,
                           fg='white', bg='black',bd=0)
        statusTxt.place(x=500, y=850)

        costlbl = Label(self.root, text="Cost:", font=("Times new Romon", 20, "bold"), fg='white',
                          bg='black').place(x=960, y=850)
        costTxt = Entry(self.root, text="XXXXXXX",
                          font=("Times new Romon", 20, "bold"), textvariable=self.cost,
                          fg='white', bg='black',bd=0)
        costTxt.place(x=1180, y=850)


        cancelticket = Button(self.root, text="Cancel Ticket", font=("Georgia", 15, "bold"), bd=0,cursor="hand2", width=30,
                                relief=GROOVE, border=3, bg="black", fg="white",command=self.cancelticket).place(x=750,y=910)

        detailsframe2 = Frame(detailsframe, bd=4, relief=RIDGE, bg="black")
        detailsframe2.place(x=270, y=150, width=1365, height=400)
        scrollY = Scrollbar(detailsframe2, orient=VERTICAL)
        self.Tickets_table = ttk.Treeview(detailsframe2, columns=(
            "ticketid", "email", "name", "from", "to", "cost", "pnumber", "pincode", "address", "gender", "age",
            "status", "traveldate"), yscrollcommand=scrollY)

        scrollY.pack(side=RIGHT, fill=Y)

        scrollY.config(command=self.Tickets_table.yview_scroll)
        self.Tickets_table.heading("ticketid", text="Ticket Id")
        self.Tickets_table.heading("email", text="Email")
        self.Tickets_table.heading("name", text="Name")
        self.Tickets_table.heading("from", text="From")
        self.Tickets_table.heading("to", text="To")
        self.Tickets_table.heading("cost", text="Cost")
        self.Tickets_table.heading("pnumber", text="Phone Number")
        self.Tickets_table.heading("pincode", text="Pincode")
        self.Tickets_table.heading("address", text="Address")
        self.Tickets_table.heading("gender", text="Gender")
        self.Tickets_table.heading("age", text="Age")
        self.Tickets_table.heading("status", text="Status")
        self.Tickets_table.heading("traveldate", text="Date")
        self.Tickets_table['show'] = 'headings'

        self.Tickets_table.column("ticketid", width=50)
        self.Tickets_table.column("email", width=50)
        self.Tickets_table.column("name", width=50)
        self.Tickets_table.column("from", width=50)
        self.Tickets_table.column("to", width=50)
        self.Tickets_table.column("cost", width=50)
        self.Tickets_table.column("pnumber", width=50)
        self.Tickets_table.column("pincode", width=50)
        self.Tickets_table.column("address", width=50)
        self.Tickets_table.column("gender", width=50)
        self.Tickets_table.column("age", width=10)
        self.Tickets_table.column("status", width=50)
        self.Tickets_table.column("traveldate", width=50)
        self.Tickets_table.pack(fill=BOTH, expand=1)
        self.Tickets_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.getTickets()

    def mainmenuclick(self):
        msg=messagebox.askquestion("JDK Railway reservation System","Aru you sure want to go Main Menu",parent=self.root)
        if msg=="yes":
            self.root.destroy()
            import userwelcome


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

    def getTickets(self):
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



    def get_cursor(self, event):
        row_cursor = self.Tickets_table.focus()
        contents = self.Tickets_table.item(row_cursor)
        self.row = contents['values']
        self.ticketid.set(self.row[0])
        self.email.set(self.row[1])
        self.name.set(self.row[2])
        self.toaddress.set(self.row[3])
        self.fromaddress.set(self.row[4])
        self.cost.set(self.row[5])
        self.number.set(self.row[6])
        self.pincode.set(self.row[7])
        self.address.set(self.row[8])
        self.gender.set(self.row[9])
        self.age.set(self.row[10])
        self.status.set(self.row[11])
        self.traveldate.set(self.row[12])
        self.bookingdate.set(self.row[13])

    def cancelticket(self):
        if self.ticketid.get()=="":
            messagebox.showerror("Error","Select a ticket",parent=self.root)
        else:
            try:
                msg=messagebox.askquestion("Confirm",f"Are you sure want to cancel the Ticket of {self.ticketid.get()}",parent=self.root)
                if msg=="yes":
                    conn = pymysql.connect(host="localhost", user="root", password="", database="railway")
                    c = conn.cursor()
                    c.execute("Delete from nooftickets WHERE ticketid=%s", self.ticketid.get())
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Ticket cancelled Successfully",parent=self.root)
                    self.getTickets()
                    self.clearall()



            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def clearall(self):
        self.ticketid.set("")
        self.name.set("")
        self.email.set("")
        self.traveldate.set("")
        self.bookingdate.set("")
        self.number.set("")
        self.gender.set("")
        self.age.set("")
        self.address.set("")
        self.toaddress.set("")
        self.fromaddress.set("")
        self.status.set("")
        self.cost.set("")
        self.pincode.set("")










root = Tk()
obj = Main(root)
root.mainloop()