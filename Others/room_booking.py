from tkinter import *
from tkinter import ttk
import datetime
import time
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
now = datetime.datetime.now()

con = sqlite3.Connection('cgh-hms.db')
c = con.cursor()


c.execute("create table if not exists room(sno integer, room_no integer, room_type text, room_status text, rate integer)")


# Close Open Database Connection
con.commit()
con.close()

root = Tk()
root.geometry('1080x500')
root.minsize(width=1080,height=800)
root.maxsize(width=1080,height=800)
root.configure(bg='white')
root.title("City Guest House - Hotel Booking Management System")
root.iconbitmap('images/logo-only.ico')

#---------------Top Background Frame------------------------------------------------------------------------------------------------------------------

top_frame = Frame(root,height=70,width=1080,bg='orange')
path = "images/newestbg6.png"
img = ImageTk.PhotoImage(Image.open(path))
label = Label(top_frame,image = img ,height=70,width=1080)
label.image=img
label.place(x=0,y=0)
top_frame.place(x=0,y=0)
tf_label = Label(top_frame,text='Hotel Management System',font='BritannicBold',fg='black',bg='gray89',height=70)
tf_label.pack(anchor='center')
top_frame.pack_propagate(False)

	#-------------exit module----------------------------------------------------------------------------------------------------------------------
def exit():
	q = messagebox.askyesno("Exit","Do you really want to exit ?")
	if(q):
		root.destroy()

def status_main():
    b_frame = Frame(root,height=400,width=1080,bg='white')
    path = "images/newbg6lf.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    label = Label(b_frame,image = img ,height=400,width=1080)
    label.image=img
    label.place(x=0,y=0)

    try:
        #creating a customer table
        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("""CREATE TABLE customers(
            fname text,
            lname text,
            gender text,
            dob int,
            mob text,
            email text,
            address text,
            nationality text,
            days int,
            Room_Number text
        )""" )
        con.commit()
        con.close()
    except:
        pass

    #reset function
    def reset():
        fn.delete(0,END)
        ln.delete(0,END)
        gen.delete(0,END)
        dob.delete(0,END)
        mob.delete(0,END)
        eml.delete(0,END)
        add.delete(0,END)
        nat.delete(0,END)
        cod.delete(0,END)
        rno.delete(0,END)

    #teble function
    def table():
        #setting all rooms to available
        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("SELECT Room_Number from room")
        avrooms=c.fetchall()
        for i in avrooms:
            c.execute("""UPDATE room SET
            Room_Status=:st""",{'st': 'Available'})
            con.commit()
        con.close()

        #updating rooms to occupied according to users
        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("SELECT Room_Number from customers")
        rnum=c.fetchall()
        for i in rnum:
            c.execute("""UPDATE room SET
            Room_Status=:st
            WHERE Room_Number=:rn""",{
                'st': 'Occupied',
                'rn': i[0]
            })
            con.commit()
        con.close()

        #creating a table
        table=Frame(root,height=580,width=950,bg='white')
        table.place(x=400,y=300)

        #connection with database
        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("SELECT * from room")
        lst=c.fetchall()

        #table heading
        lst.insert(0,('S.No.','Room Number','Room Type','Status','Price'))

        #table
        total_rows =len(lst)
        total_columns=len(lst[1])
        for i in range(total_rows):
            #table heading
            if i==0:
                fontt=('Arial',16,'bold')
                jus=CENTER
                bgc='#9cc2e5'
            else:
                #table data
                fontt=('Arial',16)
                jus=LEFT
                state=(lst[i][3])
                if state=="Occupied":
                    bgc='#f79b9b'
                else:
                    bgc='#a8d08d'
            for j in range(total_columns):
                #setting colomn width
                if j==0:
                    wid=7
                else:
                    wid=16
                e=Entry(
                    table,
                    width=wid,
                    font=fontt,
                    justify=jus,
                    disabledforeground='black',
                    disabledbackground=bgc
                )
                e.grid(row=i,column=j)
                e.insert(0,lst[i][j])
                e.config(state=DISABLED)
        con.commit()
        con.close()

    #fetch data function
    def fetch():
        a=cid.get()
        if a=="":
            messagebox.showerror("Fetch","Enter CustomerID")
        else:
            try:
                #database connection
                con=sqlite3.connect('cgh-hms.db')
                c=con.cursor()
                c.execute("SELECT * from customers where oid=:cid",{'cid':a})
                rec=c.fetchall()
                
                reset()
                #inserting values into entry boxes
                fn.insert(0,rec[0][0])
                ln.insert(0,rec[0][1])
                gen.insert(0,rec[0][2])
                dob.insert(0,rec[0][3])
                mob.insert(0,rec[0][4])
                eml.insert(0,rec[0][5])
                add.insert(0,rec[0][6])
                nat.insert(0,rec[0][7])
                cod.insert(0,rec[0][8])
                rno.insert(0,rec[0][9])
                cnn.commit()
                con.close()
                #update button status to normal
                upd.config(state=NORMAL)
            except:
                messagebox.showerror("Fetch","Invalid CustomerID")

    #submit function
    def submit():
        #add values to database
        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("INSERT INTO customers VALUES (:fn, :ln, :gen, :dob, :mob, :email, :address, :nationality, :cod, :number)",
            {
                'fn':fn.get(),
                'ln':ln.get(),
                'gen':gen.get(),
                'dob':dob.get(),
                'mob':mob.get(),
                'email':eml.get(),
                'address':add.get(),
                'nationality':nat.get(),
                'cod':cod.get(),
                'number':rno.get()
            })
        con.commit()

        #get customer id for just booked customer
        c.execute("SELECT oid from customers where mob=:phn",{'phn':mob.get()})
        cid=c.fetchall()

        #display customer id
        messagebox.showinfo("Booking","Room Booked Successfully, CustomerID: {}".format(cid[0][0]))
        con.commit()
        con.close()

        #update table
        table()
        #reset entries
        reset()

        try:
            #create bill for new customer
            con=sqlite3.connect('cgh-hms.db')
            c=con.cursor()
            c.execute("""CREATE TABLE bill(
                cid int,
                particular text,
                rate int,
                qty int,
                price int
            )""")
            con.commit()
            con.close()
        except:
            pass

        #get room number and number of days from customers table
        con=sqlite3.connect('booking.db')
        c=con.cursor()
        c.execute("SELECT Room_Number,days from customers where oid=:cid",{'cid':cid[0][0]})
        room=c.fetchall()
        con.commit()
        con.close()

        #get price and room type from room table
        con=sqlite3.connect('booking.db')
        c=con.cursor()
        c.execute("SELECT Price,Room_Type from room where Room_Number=:cid",{'cid':room[0][0]})
        price=c.fetchall()
        con.commit()
        con.close()
        days=room[0][1]
        rtype=price[0][1]
        prc=price[0][0]
        
        #inserting values to bill for room
        con=sqlite3.connect('booking.db')
        c=cnn.cursor()
        c.execute("INSERT INTO bill VALUES (:cid, :particular, :rate, :qty, :prc)",
        {
            'cid':cid[0][0],
            'particular':rtype,
            'rate':prc,
            'qty':days,
            'prc':prc*days
        })
        con.commit()
        con.close()

    #verification for customer update
    def verifyforupdate():
        #getting all occupied rooms and adding to a list
        con=sqlite3.connect('booking.db')
        c=con.cursor()
        c.execute("SELECT Room_Number from room WHERE Room_Status=:oc",{'oc':"Occupied"})
        list1=c.fetchall()
        y=[]
        for i in list1:
            y.append(i[0])
        con.commit()
        con.close()

        #getting values to verify
        a=fn.get()
        b=ln.get()
        c=gen.get()
        d=dob.get()
        e=mob.get()
        f=eml.get()
        g=add.get()
        h=nat.get()
        i=cod.get()
        j=rno.get()

        #verification
        if a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" or i=="" or j=="":
            messagebox.showerror("Booking","One or More Fields Empty!")
        elif len(d)!=4:
            messagebox.showerror("Booking","Invalid Date")
        elif len(e)!=10:
            messagebox.showerror("Booking","Invalid Phone Number")
        elif "@" and ".com" not in f:
            messagebox.showerror("Booking","Invalid Email")
        elif j!="T1" and j!="T2" and j!="T3" and j!="C1" and j!="C2" and j!="R1" and j!="R2" and j!="R3" and j!="R4":
            messagebox.showerror("Booking","Invalid Room Number")
        elif d[0].isalpha() or d[1].isalpha() or d[2].isalpha() or d[3].isalpha():
            messagebox.showerror("Booking","Invalid Date")
        elif e[0].isalpha() or e[1].isalpha() or e[2].isalpha() or e[3].isalpha() or e[4].isalpha() or e[5].isalpha() or e[6].isalpha() or e[7].isalpha() or e[8].isalpha() or e[9].isalpha():
            messagebox.showerror("Booking","Invalid Phone Number")
        elif i[0].isalpha() or i[len(i)-1].isalpha() or len(i)>2:
            messagebox.showerror("Booking","Invalid Number of Days")
        else:
            #occupied room verification 
            if j in y:
                con=sqlite3.connect('booking.db')
                c=cnn.cursor()
                c.execute("SELECT Room_Number from customers where mob=:phn",{'phn':e})
                rn=c.fetchall()
                con.commit()
                con.close()
                if j==rn[0][0]:
                    update()
                else:
                    messagebox.showerror("Booking","Room Full")
            else:
                update()

    #update function           
    def update():
        a=rno.get()
        days=cod.get()
        
        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("""UPDATE customers SET
            fname=:a,
            lname=:b,
            gender=:d,
            dob=:e,
            mob=:f,
            email=:g,
            address=:h,
            nationality=:i,
            days=:k,
            Room_Number=:l
            WHERE oid=:cid""",{
                'a':fn.get(),
                'b':ln.get(),
                'd':gen.get(),
                'e':dob.get(),
                'f':mob.get(),
                'g':eml.get(),
                'h':add.get(),
                'i':nat.get(),
                'k':cod.get(),
                'l':rno.get(),
                'cid':cid.get()
            })
        con.commit()
        con.close()
        reset()
        table()

        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("SELECT Price, Room_Type from room WHERE Room_Number=:number",{'number':a})
        price=c.fetchall()
        con.commit()
        con.close()
        rtype=price[0][1]
        prc=price[0][0]
        summ=int(days)*int(prc)
        print(summ)

        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("""UPDATE bill SET
        particular=:newroom,
        rate=:price,
        qty=:days,
        price=:money WHERE cid=:cid""",{'newroom':rtype,'price':prc,'days':days,'money':summ,'cid':cid.get()})
        con.commit()
        con.close()

        messagebox.showinfo("Update","Data Updated Successfully")

    #verification for submitting
    def verifyforsubmit():
        con=sqlite3.connect('cgh-hms.db')
        c=con.cursor()
        c.execute("SELECT Room_Number from room WHERE Room_Status=:oc",{'oc':"Occupied"})
        list1=c.fetchall()
        y=[]
        for i in list1:
            y.append(i[0])
        con.commit()
        con.close()
        
        a=fn.get()
        b=ln.get()
        c=gen.get()
        d=dob.get()
        e=mob.get()
        f=eml.get()
        g=add.get()
        h=nat.get()
        i=cod.get()
        j=rno.get()
        if a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" or i=="" or j=="":
            messagebox.showerror("Booking","One or More Fields Empty!")
        elif len(d)!=4:
            messagebox.showerror("Booking","Invalid Date")
        elif len(e)!=10:
            messagebox.showerror("Booking","Invalid Phone Number")
        elif "@" and ".com" not in f:
            messagebox.showerror("Booking","Invalid Email")
        elif j!="T1" and j!="T2" and j!="T3" and j!="C1" and j!="C2" and j!="R1" and j!="R2" and j!="R3" and j!="R4":
            messagebox.showerror("Booking","Invalid Room Number")
        elif j in y:
            messagebox.showerror("Booking","Room Full")
        elif d[0].isalpha() or d[1].isalpha() or d[2].isalpha() or d[3].isalpha():
            messagebox.showerror("Booking","Invalid Date")
        elif i[0].isalpha() or i[len(i)-1].isalpha() or len(i)>2:
            messagebox.showerror("Booking","Invalid Number of Days")
        elif e[0].isalpha() or e[1].isalpha() or e[2].isalpha() or e[3].isalpha() or e[4].isalpha() or e[5].isalpha() or e[6].isalpha() or e[7].isalpha() or e[8].isalpha() or e[9].isalpha():
            messagebox.showerror("Booking","Invalid Phone Number")
        else:
            submit()

        #Labels for data entry
        Frame(b_frame,bg='white',height=31,width=870).place(x=350,y=228)

        Frame(b_frame,bg='white',width=253,height=270).place(x=75,y=180)
        Label(b_frame,text='\u00BB       Book a Room',bg='white',font=('Agency FB',16,'bold')).place(x=80,y=220)
        Label(b_frame,text="Customer ID:",bg='white',font=('Agency FB',12)).place(x=80,y=275)
        Label(b_frame,text="First Name:",bg='white',font=('Agency FB',12)).place(x=80,y=300)
        Label(b_frame,text="Last Name:",bg='white',font=('Agency FB',12)).place(x=80,y=325)
        Label(b_frame,text="Gender:",bg='white',font=('Agency FB',12)).place(x=80,y=350)
        Label(b_frame,text="Year of Birth:",bg='white',font=('Agency FB',12)).place(x=80,y=375)
        Label(b_frame,text="Mobile:",bg='white',font=('Agency FB',12)).place(x=80,y=400)
        Label(b_frame,text="Email:",bg='white',font=('Agency FB',12)).place(x=80,y=425)
        Label(b_frame,text="Address:",bg='white',font=('Agency FB',12)).place(x=80,y=450)
        Label(b_frame,text="Nationality:",bg='white',font=('Agency FB',12)).place(x=80,y=475)

        #Entry boxes
        cid=Entry(b_frame,relief=SOLID)
        fn=Entry(b_frame,relief=SOLID)
        ln=Entry(b_frame,relief=SOLID)
        gen=Entry(b_frame,relief=SOLID)
        dob=Entry(b_frame,relief=SOLID)
        mob=Entry(b_frame,relief=SOLID)
        eml=Entry(b_frame,relief=SOLID)
        add=Entry(b_frame,relief=SOLID)
        nat=Entry(b_frame,relief=SOLID)

        cid.place(x=150,y=275,height=25,width=155)
        fn.place(x=150,y=300,height=25,width=155)
        ln.place(x=150,y=325,height=25,width=155)
        gen.place(x=150,y=350,height=25,width=155)
        dob.place(x=150,y=375,height=25,width=155)
        mob.place(x=150,y=400,height=25,width=155)
        eml.place(x=150,y=425,height=25,width=155)
        add.place(x=150,y=450,height=25,width=155)
        nat.place(x=150,y=475,height=25,width=155)

        #entries for booking room
        Frame(b_frame,bg='white',width=253,height=130).place(x=80,y=600)
        Label(b_frame,text="No. of Nights:",bg='white',font=('Agency FB',12)).place(x=80,y=525)
        Label(b_frame,text="Room No.:",bg='white',font=('Agency FB',12)).place(x=80,y=550)

        cod=Entry(b_frame,relief=SOLID)
        rno=Entry(b_frame,relief=SOLID)

        cod.place(x=150,y=525,height=25,width=155)
        rno.place(x=150,y=550,height=25,width=155)

        #buttons
        Button(b_frame,text="FETCH DATA",font=('Arial',8,'bold'),fg='white',bg="black",width=9,height=1,cursor='hand2',command=fetch).place(x=320, y=275)
        Button(b_frame,text="SAVE",font=('Arial',8,'bold'),fg='white',bg="black",width=6,height=1,cursor='hand2',command=verifyforsubmit).place(x=80, y=590)
        upd=Button(b_frame,text="UPDATE",font=('Arial',8,'bold'),fg='white',bg="black",width=6,height=1,cursor='hand2',state=DISABLED,command=verifyforupdate)
        upd.place(x=150, y=590)
        Button(b_frame,text="RESET",font=('Arial',8,'bold'),fg='white',bg="black",width=6,height=1,cursor='hand2',command=reset).place(x=220, y=590)

        table()

    b_frame.place(x=0,y=120+6+20+60+11)
    b_frame.pack_propagate(False)
    b_frame.tkraise()
    nl = Label(b_frame,text='Made by Ashish Mool',fg='black',bg='gray91',font='msserif 8')
    nl.place(x=955,y=310)
    nl.tkraise()


#-------------- Important Contact Information --------------------------------------------------------------------------------------------------------------------------
def staff():
		b_frame = Frame(root,height=400,width=1080,bg='white')
		path = "images/newbg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=400,width=1080)
		label.image=img
		label.place(x=0,y=0)
		
		emp1f = Frame(b_frame)
		path1 = "images/newman.jpg"
		img1 = ImageTk.PhotoImage(Image.open(path1))
		emp1 = Label(emp1f,image = img1)
		emp1.image=img1
		emp1.pack()
		emp1f.place(x=0,y=0)
		emp1inf = Frame(b_frame,bg='White',height=122,width=350)
		Label(emp1inf,text="General Manager",bg='white',font='msserif 17 bold').place(x=60,y=0)
		Label(emp1inf,text="Kajesh Mool",bg='white',fg="Grey",font='msserif 10').place(x=60,y=37)
		Label(emp1inf,text="Contact: +977 9803685830",bg='white',fg="Grey",font='msserif 10').place(x=60,y=59)
		Label(emp1inf,text="Email: kajesh.mool@cityguesthouse.com.np",bg='white',fg="Grey",font='msserif 10').place(x=60,y=83)
		emp1inf.pack_propagate(False)
		emp1inf.place(x=117,y=1)

		emp1f = Frame(b_frame)
		path2 = "D://cgh-hms-main/images/receptionnew.jpg"
		img2 = ImageTk.PhotoImage(Image.open(path2))
		emp1 = Label(emp1f,image = img2)
		emp1.image=img2
		emp1.pack()
		emp1f.place(x=580,y=0)
		emp1inf = Frame(b_frame,bg='White',height=122,width=350)
		Label(emp1inf,text="Receptionist",bg='white',font='msserif 17 bold').place(x=45,y=0)#pack(side='top')
		Label(emp1inf,text="Ms. Sumira Shrestha",bg='white',fg="Grey",font='msserif 10').place(x=45,y=37)
		Label(emp1inf,text="Contact: +977 9847112122",bg='white',fg="Grey",font='msserif 10').place(x=45,y=59)
		Label(emp1inf,text="Email: hello@citygueshouse.com.np",bg='white',fg="Grey",font='msserif 10').place(x=45,y=83)	
		emp1inf.pack_propagate(False)
		emp1inf.place(x=690,y=2)

		emp1f = Frame(b_frame)
		path3 = "D://cgh-hms-main/images/fchefnew.jpg"
		img3 = ImageTk.PhotoImage(Image.open(path3))
		emp1 = Label(emp1f,image = img3)
		emp1.image=img3
		emp1.pack()
		emp1f.place(x=0,y=152)
		emp1inf = Frame(b_frame,bg='White',height=122,width=350)
		Label(emp1inf,text="Restaurant Manager",bg='white',font='msserif 17 bold').place(x=72,y=0)#pack(side='top')
		Label(emp1inf,text="Mr. Dinesh Kiju",bg='white',fg="Grey",font='msserif 10').place(x=72,y=37)
		Label(emp1inf,text="Phone: +977 9841912893",bg='white',fg="Grey",font='msserif 10').place(x=72,y=59)
		Label(emp1inf,text="Email: food@cityguesthouse.com.np",bg='white',fg="Grey",font='msserif 10').place(x=72,y=83)	
		emp1inf.pack_propagate(False)
		emp1inf.place(x=99,y=153)
		emp1inf.tkraise()

		emp1f = Frame(b_frame)
		path4 = "D://cgh-hms-main/images/roomservicenew.jpg"
		img4 = ImageTk.PhotoImage(Image.open(path4))
		emp1 = Label(emp1f,image = img4)
		emp1.image=img4
		emp1.pack()
		emp1f.place(x=580,y=152)
		emp1inf = Frame(b_frame,bg='White',height=122,width=350)
		Label(emp1inf,text="Housekeeping",bg='white',font='msserif 17 bold').place(x=55,y=0)#pack(side='top')
		Label(emp1inf,text="Ms. Subha Laxmi Ranjitkar",bg='white',fg="Grey",font='msserif 10').place(x=55,y=37)
		Label(emp1inf,text="Phone: +977 9843887541",bg='white',fg="Grey",font='msserif 10').place(x=55,y=59)
		Label(emp1inf,text="Email: housekeeping@cityguesthouse.com.np",bg='white',fg="Grey",font='msserif 10').place(x=55,y=83)	
		emp1inf.pack_propagate(False)
		emp1inf.place(x=690,y=153)
		
		# Frame(b_frame,height=13,width=250,bg='white').place(x=410,y=2)
		# Frame(b_frame,height=13,width=250,bg='white').place(x=410,y=153)
		#Frame(b_frame,height=180,width=13,bg='white').place(x=406,y=20)



		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()
		nl = Label(b_frame,text='Made by Ashish Mool',fg='black',bg='gray91',font='msserif 8')
		nl.place(x=955,y=310)
		nl.tkraise()










#---------------Buttons Frame-----------------------------------------------------------------------------------------------------------------
sl_frame = Frame(root,height=130,width=1080,bg='white')
sl_frame.place(x=0,y=70+6)
path = "images/rooms.png"
img = ImageTk.PhotoImage(Image.open(path))
b1 = Button(sl_frame,image=img,text='b1',bg='white',width=180)
b1.image = img
b1.place(x=180,y=0)
path2 = "images/hotelstatus.png"
img1 = ImageTk.PhotoImage(Image.open(path2))
b2 = Button(sl_frame,image=img1,text='b2',bg='white',width=180,command=status_main)
b2.image = img1
b2.place(x=0,y=0)
path3='images/guests.png'
img3 = ImageTk.PhotoImage(Image.open(path3))
b3 = Button(sl_frame,image=img3,text='b2',bg='white',width=180,command=staff)
b3.image = img3
b3.place(x=180*4,y=0)
path4='images/payments.png'
img4 = ImageTk.PhotoImage(Image.open(path4))
b4 = Button(sl_frame,image=img4,text='b2',bg='white',width=180)
b4.image = img4
b4.place(x=180*3,y=0)
path5='images/logout.png'
img5 = ImageTk.PhotoImage(Image.open(path5))
b5 = Button(sl_frame,image=img5,text='b2',bg='white',width=180,height=100,command=exit)
b5.image = img5
b5.place(x=180*5,y=0)
path6='images/Bookroom.png'
img6 = ImageTk.PhotoImage(Image.open(path6))
b6 = Button(sl_frame,image=img6,text='b2',bg='white',width=180,height=100)
b6.image = img6
b6.place(x=180*2,y=0)
Label(sl_frame,text='Show Guest List',font='msserif 10',bg='white').place(x=35,y=106)
Label(sl_frame,text='Rooms & Availability',font='msserif 10',bg='white').place(x=248,y=106)
Label(sl_frame,text='Book & Reserve',font='msserif 10',bg='white').place(x=417,y=106)
Label(sl_frame,text='Important Contacts',font='msserif 10',bg='white').place(x=774,y=106)
Label(sl_frame,text='Payments Info',font='msserif 10',bg='white').place(x=570,y=106)
Label(sl_frame,text='Exit',font='msserif 10',bg='white').place(x=968,y=106)
sl_frame.pack_propagate(False)

status_main()
root.mainloop()