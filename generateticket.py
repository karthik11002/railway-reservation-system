from tkinter import *
from tkinter import messagebox, ttk
import pymysql
from PIL import Image, ImageTk, ImageDraw, ImageFont



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
        self.fromtext=StringVar()
        self.totext=StringVar()
        self.name=StringVar()
        self.phone=StringVar()
        self.age=StringVar()
        self.gender=StringVar()
        self.date=StringVar()
        self.email=StringVar()
        self.cost=StringVar()
        self.pincode=StringVar()
        self.address=StringVar()
        self.status=StringVar()
        self.bookingdate=StringVar()
        self.ticketidsave = StringVar()





        self.bg = ImageTk.PhotoImage(file="images/ticketframeimg.png")





        lbl_heading = Label(self.root, text="JDK Railway Reservation System", font=("Comic Sans MS", 28, "bold"),
                            bg="#cbd4cd", fg="black", bd=10, relief=RIDGE).pack(side=TOP, fill=X)

        mainframe=Frame(root, bg="black", relief=GROOVE, bd=10).place(x=250, y=80, width=1400, height=900)

        mainmenuBtn = Button(self.root, text="Main menu", command=self.mainmenuclick,
                             font=("Comic Sans MS", 18, "bold"), bd=1,
                             relief=GROOVE, bg="black", fg="White", width=125, cursor="hand2").place(x=15, y=985)

        emailLabel = Label(self.root, text="Email:", font=("Times new Romon", 20, "bold"), fg='white',
                           bg='black').place(x=600, y=100)
        emailTb = Entry(self.root, textvariable=self.emailTb_text, font=("Times new Romon", 20, "bold"), fg='Black',
                        width=30)
        emailTb.place(x=690, y=100)
        self.checkmail = Button(self.root, textvariable=self.verifytext, font=("Georgia", 13, "bold"), bd=0,
                                cursor="hand2", width=10,
                                relief=GROOVE, border=3, bg="black", fg="white", command=self.verify_mail).place(x=1150,
                                                                                                                 y=100)






        ticketframe = Frame(mainframe,bd=4,relief=RIDGE,bg="Black")
        ticketframe.place(x=700, y=600, width=458, height=208)
        ticketbg=Label(ticketframe, image=self.bg).place(x=0, y=0)

        ticketIdTxt = Entry(ticketframe, text="XXXXXXX", textvariable=self.ticketid,
                            font=("Sylfaen", 9),
                            fg='black',bg="#c3c3c3", bd=0, width=10)
        ticketIdTxt.place(x=90, y=43)

        FromTxt = Entry(ticketframe,  text="XXXXXXX", textvariable=self.fromtext,
                            font=("Sylfaen", 9),
                            fg='black', bg="#c3c3c3", bd=0, width=30)
        FromTxt.place(x=66, y=66)

        ToTxt = Entry(ticketframe,  text="XXXXXXX", textvariable=self.totext,
                        font=("Sylfaen", 9),
                        fg='black', bg="#c3c3c3", bd=0, width=30)
        ToTxt.place(x=50, y=86)

        nameTxt = Entry(ticketframe, text="XXXXXXX",  textvariable=self.name,
                        font=("Sylfaen", 9),
                        fg='black', bg="#c3c3c3", bd=0, width=25)
        nameTxt.place(x=70, y=106)

        phoneTxt = Entry(ticketframe, text="XXXXXXX",  textvariable=self.phone,
                        font=("Sylfaen", 9),
                        fg='black', bg="#c3c3c3", bd=0, width=15)
        phoneTxt.place(x=129, y=126)

        ageTxt = Entry(ticketframe, text="XXXXXXX",  textvariable=self.age,
                      font=("Sylfaen", 9),
                      fg='black', bg="#c3c3c3", bd=0, width=15)
        ageTxt.place(x=60, y=147)

        genderTxt = Entry(ticketframe, text="XXXXXXX",  textvariable=self.gender,
                        font=("Sylfaen", 9),
                        fg='black', bg="#c3c3c3", bd=0, width=15)
        genderTxt.place(x=80, y=167)

        dateTxt = Entry(ticketframe,  text="XXXXXXX", textvariable=self.date,
                        font=("Sylfaen", 9),
                        fg='black', bg="#c3c3c3", bd=0, width=15)
        dateTxt.place(x=210, y=44)


        Downloadticket=Button(self.root, text="Download Ticket", font=("Georgia", 13, "bold"), bd=0,
                                cursor="hand2", width=20,
                                relief=GROOVE, border=3, bg="black", fg="white",command=self.downloadticket).place(x=805,y=850)


        detailsframe2 = Frame(mainframe, bd=4, relief=RIDGE, bg="black")
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
        msg=messagebox.askquestion("JDK Railway reservation System","Are you sure want to go Main Menu",parent=self.root)
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

    def get_cursor(self,event):
        row_cursor = self.Tickets_table.focus()
        contents = self.Tickets_table.item(row_cursor)
        self.row = contents['values']
        self.ticketid.set(self.row[0])
        self.email.set(self.row[1])
        self.name.set(self.row[2])
        self.totext.set(self.row[3])
        self.fromtext.set(self.row[4])
        self.cost.set(self.row[5])
        self.phone.set(self.row[6])
        self.pincode.set(self.row[7])
        self.address.set(self.row[8])
        self.gender.set(self.row[9])
        self.age.set(self.row[10])
        self.status.set(self.row[11])
        self.date.set(self.row[12])
        self.bookingdate.set(self.row[13])


        self.ticket = Image.open("images/ticketframeimg.png")
        ticketfont = ImageFont.truetype("sylfaen.ttf", 15)
        tickettype=ImageDraw.Draw(self.ticket)
        tickettype.text((90, 42), self.ticketid.get(), (0, 0, 0), font=ticketfont)
        tickettype.text((210, 43), self.date.get(), (0, 0, 0), font=ticketfont)
        tickettype.text((50, 86), self.totext.get(), (0, 0, 0), font=ticketfont)
        tickettype.text((66, 66), self.fromtext.get(), (0, 0, 0), font=ticketfont)
        tickettype.text((70, 106), self.name.get(), (0, 0, 0), font=ticketfont)
        tickettype.text((128, 126), self.phone.get(), (0, 0, 0), font=ticketfont)
        tickettype.text((60, 147), self.age.get(), (0, 0, 0), font=ticketfont)
        tickettype.text((80, 167), self.gender.get(), (0, 0, 0), font=ticketfont)



    def downloadticket(self):
        self.ticketidsave.set(self.ticketid.get()+".png")
        self.ticket.save(self.ticketidsave.get())
        messagebox.showinfo("Success","Ticket Download Successfully",parent=self.root)


















root = Tk()
obj = Main(root)
root.mainloop()






