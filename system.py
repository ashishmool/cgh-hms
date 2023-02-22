#Import Library
from tkinter import *
from tkinter import ttk
import datetime
import time
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
#Import Date Time for Bill Operations
now = datetime.datetime.now()
date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")


#Importing Sqlite for Server-side operations
con = sqlite3.Connection('cgh-hms-db.db')
c = con.cursor()


# # #setting all rooms to available Administration Use Only
# # con=sqlite3.connect('cgh-hms-db.db')
# # c=con.cursor()
# c.execute("SELECT res_room_no from room")
# avrooms=c.fetchall()
# for i in avrooms:
# 	c.execute("""UPDATE room SET
# 	room_status=:st""",{'st': 'Available'})



#For Table Deletion:
c.execute("create table if not exists guests(first_name text,middle_name text,last_name text, contact_number integer, email text, g_address text, child integer, adult integer, no_nights integer, res_room_no integer PRIMARY KEY)")
c.execute("create table if not exists bill(cust_id integer,rate integer, qty integer, amount integer)")
c.execute("create table if not exists room(res_room_no number,room_type text,room_status text,rate integer)")

# Close Open Database Connection
con.commit()
con.close()

# con=sqlite3.connect('cgh-hms-db.db')
# c=con.cursor()
# c.execute("SELECT res_room_no from room")
# avrooms=c.fetchall()
# for i in avrooms:
# 	c.execute("""UPDATE room SET
# 	room_status=:st""",{'st': 'Available'})

# c.execute("DROP TABLE bill;")


#Room Data for Administration Use Only
# c.execute("INSERT INTO room VALUES (:res_room_no, :room_type, :room_status, :rate)", {
#         'res_room_no':'301',
#         'room_type':'Double',
#         'room_status':'Available',
#         'rate':'2000',
#     })

# c.execute("INSERT INTO room VALUES (:res_room_no, :room_type, :room_status, :rate)", {
#         'res_room_no':'302',
#         'room_type':'Double',
#         'room_status':'Available',
#         'rate':'2100',
#     })

# c.execute("INSERT INTO room VALUES (:res_room_no, :room_type, :room_status, :rate)", {
#         'res_room_no':'303',
#         'room_type':'Twin',
#         'room_status':'Available',
#         'rate':'2300',
#     })

# c.execute("INSERT INTO room VALUES (:res_room_no, :room_type, :room_status, :rate)", {
#         'res_room_no':'304',
#         'room_type':'Family',
#         'room_status':'Available',
#         'rate':'2500',
#     })

# c.execute("INSERT INTO room VALUES (:res_room_no, :room_type, :room_status, :rate)", {
#         'res_room_no':'305',
#         'room_type':'Economy',
#         'room_status':'Available',
#         'rate':'1500',
#     })
	# #--------------seperator-------------------------------------------------------------------------------------------------------------------

	# sep = Frame(height=500,bd=1,relief='sunken',bg='white')
	# sep.place(x=20,y=0)

	# b_frame = Frame(root,height=400,width=1080,bg='white')
			# path = "D://cgh-hms-main/images/footer.png"
			# img = ImageTk.PhotoImage(Image.open(path))
			# label = Label(b_frame,image = img ,height=400,width=1280)
			# label.image=img
			# label.place(x=0,y=0)

			# b_frame.place(x=0,y=120+6+20+60+11)
			# b_frame.pack_propagate(False)
			# b_frame.tkraise()
		
			#setting all rooms to available
			

			# updating rooms to occupied according to users

#Main System Tkinter GUI
def mainroot():
	
	root = Tk()

	window_height = 500
	window_width = 1080
	
	def center_screen():
		""" gets the coordinates of the center of the screen """
		global screen_height, screen_width, x_cordinate, y_cordinate
	
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()
			# Coordinates of the upper left corner of the window to make the window appear in the center
		x_cordinate = int((screen_width/2) - (window_width/2))
		y_cordinate = int((screen_height/2) - (window_height/2))
		root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
	
	center_screen()
	# root.geometry('1080x500')
	root.minsize(width=1080,height=550)
	root.maxsize(width=1080,height=550)
	root.configure(bg='white')
	root.title("City Guest House - Hotel Booking Management System")
	root.iconbitmap('images/logo-only.ico')
	
	#Bottom Frame
	b_frame = Frame(root,height=400,width=1080,bg='gray91')
	b_frame.place(x=0,y=120+6+20+60+11)
	b_frame.pack_propagate(False)
	path = "images/front.jpg"
	img = ImageTk.PhotoImage(Image.open(path))
	label = Label(b_frame,image = img ,height=400,width=1080)
	label.image=img
	label.place(x=0,y=0)
	b_frame.tkraise()
	
	
	def hotel_status():
		con = sqlite3.Connection('cgh-hms-db.db')
		c = con.cursor()

		global b_frame
		b_frame = Frame(root,height=400,width=1080,bg='gray91')
		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		path = "images/newbg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=400,width=1080)
		label.image=img
		label.place(x=0,y=0)

		path6='images/guest-list.png'
		img6 = ImageTk.PhotoImage(Image.open(path6))
		b7 = Button(b_frame,image=img6,text='b2',bg='white',width=180,height=100, command=display_guests)
		b7.image = img6
		b7.place(x=870,y=20)

		def table():
			#updating rooms to occupied according to users
			con=sqlite3.connect('cgh-hms-db.db')
			c=con.cursor()
			c.execute("SELECT res_room_no from guests")
			rnum=c.fetchall()
			for i in rnum:
				c.execute("""UPDATE room SET
				room_status=:st
				WHERE res_room_no=:rn""",{
					'st': 'Available',
					'rn': i[0]
				})
			c.execute("SELECT res_room_no from room")
			rnum=c.fetchall()
			for i in rnum:
				c.execute("""UPDATE room SET
				room_status=:st
				WHERE res_room_no=:rn""",{
					'st': 'Occupied',
					'rn': i[0]
				})
			#creating a table
			table=Frame(b_frame,height=580,width=950,bg='white')
			table.place(x=50,y=20)

			#connection with database
			con=sqlite3.connect('cgh-hms-db.db')
			c=con.cursor()
			c.execute("SELECT * from room")
			lst=c.fetchall()

			#table heading
			lst.insert(0,('Room Number','Room Type','Status','Price'))

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
					jus=CENTER
					state=(lst[i][2])
					if state=="Occupied":
						bgc='#f79b9b'
					else:
						bgc='#a8d08d'
				for j in range(total_columns):
					#setting colomn width
					if j==0:
						wid=15
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

		table()

		#website label
		nl = Label(b_frame,text='www.cityguesthouse.com.np',fg='black',bg='gray91',font='msserif 8')
		nl.place(x=900,y=310)
		nl.tkraise()

	def display_guests():
		
		#creating window
		display_screen = Tk()
		#setting width and height for window
		display_screen.geometry("1000x400")
		#setting title for window
		display_screen.title("Guest List at City Guest House")
		global tree
		#creating frame
		TopViewForm = Frame(display_screen, width=600, bd=0, relief=SOLID)
		TopViewForm.pack(side=TOP, fill=X)
		LeftViewForm = Frame(display_screen, width=600)
		LeftViewForm.pack(side=LEFT, fill=Y)
		MidViewForm = Frame(display_screen, width=600)
		MidViewForm.pack(side=RIGHT)
		lbl_text = Label(TopViewForm, text="Guest Records", font=('arial', 18), width=600,bg="#73260E",fg="white")
		lbl_text.pack(fill=X)
		lbl_txtsearch = Label(LeftViewForm, text="", font=('arial', 15))
		lbl_txtsearch.pack(side=TOP, anchor=W)
		#setting scrollbar
		scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
		scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
		tree = ttk.Treeview(MidViewForm,columns=("First Name", "Middle Name", "Last Name", "Contact","Email","Address",
							"No. Child","No. Adults", "No. Nights","Room No."),
							selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
		scrollbary.config(command=tree.yview)
		scrollbary.pack(side=RIGHT, fill=Y)
		scrollbarx.config(command=tree.xview)
		scrollbarx.pack(side=BOTTOM, fill=X)
		#setting headings for the columns
		tree.heading('First Name', text="First Name", anchor=W)
		tree.heading('Middle Name', text="Middle Name", anchor=W)
		tree.heading('Last Name',text="Last Name", anchor=W)
		tree.heading('Contact', text="Contact", anchor=W)
		tree.heading('Email', text="Email", anchor=W)
		tree.heading('Address', text="Address", anchor=W)
		tree.heading('No. Child', text="No. Child", anchor=W)
		tree.heading('No. Adults', text="No. Adults", anchor=W)
		tree.heading('No. Nights', text="No. Nights", anchor=W)
		tree.heading('Room No.', text="Room No.", anchor=W)
		#setting width of the columns
		tree.column('#0', stretch=NO, minwidth=0, width=0)
		tree.column('#1', stretch=NO, minwidth=0, width=80)
		tree.column('#2', stretch=NO, minwidth=0, width=80)
		tree.column('#3', stretch=NO, minwidth=0, width=80)
		tree.column('#4', stretch=NO, minwidth=0, width=80)
		tree.column('#5', stretch=NO, minwidth=0, width=200)
		tree.column('#6', stretch=NO, minwidth=0, width=100)
		tree.column('#7', stretch=NO, minwidth=0, width=50)
		tree.column('#8', stretch=NO, minwidth=0, width=50)
		tree.column('#9', stretch=NO, minwidth=0, width=50)
		tree.pack()
		DisplayData()
		#defining function to access data from SQLite database
	def DisplayData():
		# open databse
		con = sqlite3.connect('cgh-hms-db.db')
		#select query
		c=con.execute("SELECT * FROM guests")
		fetch = c.fetchall()
		for data in fetch:
			tree.insert('', 'end', values=(data))
		c.close()
		con.close()


		

	# n2 = Label(root,text='www.cityguesthouse.com.np',fg='black',bg='gray91',font='msserif 8').place(x=500,y=500)



		#hline = Frame(b_frame,height=10,width=960,bg='cyan4')
		#hline.place(x=122,y=27)

	

#Book and Unbook Rooms
	def reserve():
		b_frame = Frame(root,height=420,width=1080,bg='gray89')
		path = "D://cgh-hms-main/images/newbg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=420,width=1080)
		label.image=img
		label.place(x=0,y=0)
		
		vline = Frame(b_frame,height=400,width=7,bg='#73260E')
		vline.place(x=700,y=0) 

		Label(b_frame,text='Personal Information',font='msserif 15',bg='gray93').place(x=225,y=0)

		fnf = Frame(b_frame,height=1,width=1)
		fn = Entry(fnf)
		
		mnf = Frame(b_frame,height=1,width=1)
		mn = Entry(mnf)

		lnf = Frame(b_frame,height=1,width=1)
		ln = Entry(lnf)

		fn.insert(0, 'First Name *')
		mn.insert(0, 'Middle Name')
		ln.insert(0, 'Last Name *')
		
		def on_entry_click1(event):
			if fn.get() == 'First Name *' :
				fn.delete(0,END)
				fn.insert(0,'')
		def on_entry_click2(event):
			if mn.get() == 'Middle Name' :
				mn.delete(0,END)
				mn.insert(0,'')
		def on_entry_click3(event):
			if ln.get() == 'Last Name *' :
				ln.delete(0,END)
				ln.insert(0,'')
		def on_exit1(event):
			if fn.get()=='':
				fn.insert(0,'First Name *')
		def on_exit2(event):
			if mn.get()=='':
				mn.insert(0,'')
		def on_exit3(event):
			if ln.get()=='':
				ln.insert(0,'Last Name *')

		fn.bind('<FocusIn>', on_entry_click1)
		mn.bind('<FocusIn>', on_entry_click2)
		ln.bind('<FocusIn>', on_entry_click3)
		fn.bind('<FocusOut>',on_exit1)
		mn.bind('<FocusOut>',on_exit2)
		ln.bind('<FocusOut>',on_exit3)

		fn.pack(ipady=4,ipadx=15)
		mn.pack(ipady=4,ipadx=15)
		ln.pack(ipady=4,ipadx=15)
		fnf.place(x=20,y=42)
		mnf.place(x=235,y=42)
		lnf.place(x=450,y=42)

		Label(b_frame,text='Contact Information',font='msserif 15',bg='gray93').place(x=225,y=90)

		cnf = Frame(b_frame,height=1,width=1)
		cn = Entry(cnf)
		
		emf = Frame(b_frame,height=1,width=1)
		em = Entry(emf)

		adf = Frame(b_frame,height=1,width=1)
		ad = Entry(adf)

		cn.insert(0, 'Contact Number *')
		em.insert(0, 'Email *')
		ad.insert(0, "Guest's Address *")
		
		def on_entry_click4(event):
			if cn.get() == 'Contact Number *' :
				cn.delete(0,END)
				cn.insert(0,'')
		def on_entry_click5(event):
			if em.get() == 'Email *' :
				em.delete(0,END)
				em.insert(0,'')
		def on_entry_click6(event):
			if ad.get() == "Guest's Address *" :
				ad.delete(0,END)
				ad.insert(0,'')
		def on_exit4(event):
			if cn.get()=='':
				cn.insert(0,'Contact Number *')
		def on_exit5(event):
			if em.get()=='':
				em.insert(0,'Email *')
		def on_exit6(event):
			if ad.get()=='':
				ad.insert(0,"Guest's Address *")

		cn.bind('<FocusIn>', on_entry_click4)
		em.bind('<FocusIn>', on_entry_click5)
		ad.bind('<FocusIn>', on_entry_click6)
		cn.bind('<FocusOut>',on_exit4)
		em.bind('<FocusOut>',on_exit5)
		ad.bind('<FocusOut>',on_exit6)

		cn.pack(ipady=4,ipadx=15)
		em.pack(ipady=4,ipadx=15)
		ad.pack(ipady=4,ipadx=15)
		cnf.place(x=20,y=130)
		emf.place(x=235,y=130)
		adf.place(x=450,y=130)

		Label(b_frame,text='Reservation Information',font='msserif 15',bg='gray93').place(x=210,y=175)
		
		nocf = Frame(b_frame,height=1,width=1)
		noc = Entry(nocf)
		
		noaf = Frame(b_frame,height=1,width=1)
		noa = Entry(noaf)

		nodf = Frame(b_frame,height=1,width=1)
		nod = Entry(nodf)

		noc.insert(0, 'Number of Children *')
		noa.insert(0, 'Number of Adults *')
		nod.insert(0, 'Number of Days of Stay *')
		
		def on_entry_click7(event):
			if noc.get() == 'Number of Children *' :
				noc.delete(0,END)
				noc.insert(0,'')
		def on_entry_click8(event):
			if noa.get() == 'Number of Adults *' :
				noa.delete(0,END)
				noa.insert(0,'')
		def on_entry_click9(event):
			if nod.get() == 'Number of Days of Stay *' :
				nod.delete(0,END)
				nod.insert(0,'')
		def on_exit7(event):
			if noc.get()=='':
				noc.insert(0,'Number of Children *')
		def on_exit8(event):
			if noa.get()=='':
				noa.insert(0,'Number of Adults *')
		def on_exit9(event):
			if nod.get()=='':
				nod.insert(0,'Number of Days of Stay *')

		noc.bind('<FocusIn>', on_entry_click7)
		noa.bind('<FocusIn>', on_entry_click8)
		nod.bind('<FocusIn>', on_entry_click9)
		noc.bind('<FocusOut>',on_exit7)
		noa.bind('<FocusOut>',on_exit8)
		nod.bind('<FocusOut>',on_exit9)

		noc.pack(ipady=4,ipadx=15)
		noa.pack(ipady=4,ipadx=15)
		nod.pack(ipady=4,ipadx=15)
		nocf.place(x=20,y=220)
		noaf.place(x=235,y=220)
		nodf.place(x=450,y=220)
		
		roomnf = Frame(b_frame,height=1,width=1)
		roomn = Entry(roomnf)
		roomn.insert(0, 'Enter Room Number *')
		def on_entry_click10(event):
			if roomn.get() == 'Enter Room Number *' :
				roomn.delete(0,END)
				roomn.insert(0,'')
		def on_exit10(event):
			if roomn.get()=='':
				roomn.insert(0,'Enter Room Number *')	
		roomn.bind('<FocusIn>', on_entry_click10)
		roomn.bind('<FocusOut>',on_exit10)
		roomn.pack(ipady=4,ipadx=15)
		roomnf.place(x=20,y=270)

		def unbook_room():
			con=sqlite3.connect('cgh-hms-db.db')
			c=con.cursor()

			if (roomn.get() == 'Enter Room Number') or (roomn.get()==''):
				messagebox.showerror('Entries not filled','Kindly Enter room Number')
			else :
				c.execute("update room set room_status='Available' where res_room_no = ? ",(roomn.get(),))
				messagebox.showinfo("Successful","Room Unreserved successfully")
				


			# c.execute("SELECT res_room_no from guests")
			# rnum=c.fetchall()
			# room_no=''
			# for i in rnum:
			# 	c.execute("""UPDATE room SET
			# 	room_status=:st
			# 	WHERE res_room_no=:rn""",{
			# 		'st': 'Available',
			# 		'rn': i[0]
			# 	})

				c.execute("DELETE from guests WHERE res_room_no = " + roomn.get())
				c.execute("SELECT *, oid FROM guests")
				records = c.fetchall()
				roomn.delete(0,END)
				print ('Deleted Successfully')

			con.commit()
			con.close()
			# messagebox.showinfo("Reservation Information", "Guest has been unreserved successfully!")
			# reserve()

		def book_room():
			if (roomn.get() == 'Enter Room Number') or (roomn.get()=='' or fn.get() == 'First Name *') or (fn.get()=='' or ln.get() == 'Last Name *') or (ln.get()=='' or cn.get() == 'Contact Number *') or (cn.get()=='' or em.get() == 'Email *') or (em.get()=='' or noc.get() == 'Number of Children *') or (noc.get()=='' or noa.get() == 'Number of Adults *') or (noa.get()=='' or nod.get() == 'Number of Days of Stay *') or (nod.get()==''):
				messagebox.showerror('Entries not filled','Kindly Enter Required Details')
			else :
				con=sqlite3.connect('cgh-hms-db.db')
				c=con.cursor()
				
				c.execute("SELECT *, rowid, res_room_no, no_nights FROM guests")
				records=c.fetchall()
				global no_nights_f
				found_room=''
				room_id=''
				# no_nights_f=''
				for record in records:
					room_id = str(record[9])
					if roomn.get() == room_id:
						found_room=room_id
						found_name = str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2])
						global guest_row_id
						guest_row_id = str(record[10])
						
				if found_room==roomn.get():
						messagebox.showerror("Error","Room Already Assigned - Choose another Room!")

						# fn.insert(0,'First Name')
						# mn.insert(0,'Middle Name')
						# ln.insert(0,'Last Name')
						# cn.insert(0,'Contact Number')
						# em.insert(0,'Email')
						# ad.insert(0,'Address')
						# noc.insert(0,'No. of Children')
						# noa.insert(0,'No. of Adults')
						# nod.insert(0,'No. of Nights')
				else:
				
					c.execute("INSERT INTO guests VALUES (:first_name, :middle_name, :last_name, :contact_number, :email, :g_address, :child, :adult, :no_nights, :res_room_no)", {
							'first_name':fn.get(),
							'middle_name':mn.get(),
							'last_name':ln.get(),
							'contact_number':cn.get(),
							'email':em.get(),
							'g_address': ad.get(),
							'child': noc.get(),
							'adult': noa.get(),
							'no_nights': nod.get(),
							'res_room_no': roomn.get(),
							
						})

					#updating rooms to occupied according to users
					c.execute("SELECT res_room_no from guests")
					rnum=c.fetchall()
					for i in rnum:
						c.execute("""UPDATE room SET
						room_status=:st
						WHERE res_room_no=:rn""",{
							'st': 'Occupied',
							'rn': i[0]
						})

					messagebox.showinfo("Reservation Information", "Guest has been reserved successfully!")
				
			# #clear text boxes
					fn.delete(0,END)
					mn.delete(0,END)
					ln.delete(0,END)
					cn.delete(0,END)
					em.delete(0,END)
					ad.delete(0,END)
					noc.delete(0,END)
					noa.delete(0,END)
					nod.delete(0,END)

			# #insert labels in text boxes
					fn.insert(0,'First Name')
					mn.insert(0,'Middle Name')
					ln.insert(0,'Last Name')
					cn.insert(0,'Contact Number')
					em.insert(0,'Email')
					ad.insert(0,'Address')
					noc.insert(0,'No. of Children')
					noa.insert(0,'No. of Adults')
					nod.insert(0,'No. of Nights')

				con.commit()
				con.close()
			
		reserve=Button(b_frame,width=21,pady=7,text='Book Room',bg='#73260E', fg='white',border=0, command=book_room)
		reserve.place(x=235,y=270)

		unreserve=Button(b_frame,width=21,pady=7,text='Unbook Room',bg='#73260E', fg='white',border=0, command=unbook_room)
		unreserve.place(x=450,y=270)

		unreserve_lbl=Label(b_frame,text='**Room Number required or Quick Select above...',font='msserif 9')
		unreserve_lbl.place(x=630,y=280)


		
		
		# show_booking=Button(b_frame,width=21,pady=7,text='Show Booking',bg='#73260E', fg='white',border=0, command=edit)
		# show_booking.place(x=800,y=70)

		#--------------------------------------------------------right side---------------------------------------------------
		
		
		Label(b_frame,text='Quick Select Room Number',font='msserif 14',bg='gray93').place(x=800,y=0)
	
		# roomn_b = Button(b_frame,width=15,pady=7,text='Show Booking',bg='#73260E', fg='white',border=0).place(x=800, y=70)
		def r_201():
			roomn.delete(0,END)
			roomn.insert(0,'201')
		def r_202():
			roomn.delete(0,END)
			roomn.insert(0,'202')
		def r_203():
			roomn.delete(0,END)
			roomn.insert(0,'203')
		def r_204():
			roomn.delete(0,END)
			roomn.insert(0,'204')
		def r_205():
			roomn.delete(0,END)
			roomn.insert(0,'205')
		def r_301():
			roomn.delete(0,END)
			roomn.insert(0,'301')
		def r_302():
			roomn.delete(0,END)
			roomn.insert(0,'302')
		def r_303():
			roomn.delete(0,END)
			roomn.insert(0,'303')
		def r_304():
			roomn.delete(0,END)
			roomn.insert(0,'304')
		def r_305():
			roomn.delete(0,END)
			roomn.insert(0,'305')
		
		# fname_l=Label(b_frame,text="Full Name").place(x=730, y=80)
		# fname_e=Entry(b_frame,width=25, state=DISABLED).place(x=700,y=80)
		# noa_l=Label(b_frame,text="No. of Adults").place(x=730, y=120)
		# noa_e=Entry(b_frame,width=5).place(x=810,y=120)
		# noc_l=Label(b_frame,text="No. of Child").place(x=730, y=140)
		# noc_e=Entry(b_frame,width=5).place(x=810,y=140)
		# non_l=Label(b_frame,text="No. of Nights").place(x=730, y=160)
		# non_e=Entry(b_frame,width=5).place(x=810,y=160)
		# rnn_l=Label(b_frame,text="Room No").place(x=730, y=180)
		# rno_e=Entry(b_frame,width=5).place(x=810,y=180)
		
	

		r_201=Button(b_frame,width=10,pady=7,text='201',bg='#73260E', fg='white',border=0, command=r_201).place(x=730,y=80)
		r_202=Button(b_frame,width=10,pady=7,text='202',bg='#73260E', fg='white',border=0, command=r_202).place(x=820,y=80)
		r_203=Button(b_frame,width=10,pady=7,text='203',bg='#73260E', fg='white',border=0, command=r_203).place(x=910,y=80)
		r_204=Button(b_frame,width=10,pady=7,text='204',bg='#73260E', fg='white',border=0, command=r_204).place(x=1000,y=80)
		r_205=Button(b_frame,width=10,pady=7,text='205',bg='#73260E', fg='white',border=0, command=r_205).place(x=730,y=150)
		r_301=Button(b_frame,width=10,pady=7,text='301',bg='#73260E', fg='white',border=0, command=r_301).place(x=820,y=150)
		r_302=Button(b_frame,width=10,pady=7,text='302',bg='#73260E', fg='white',border=0, command=r_302).place(x=910,y=150)
		r_303=Button(b_frame,width=10,pady=7,text='303',bg='#73260E', fg='white',border=0, command=r_303).place(x=1000,y=150)
		r_304=Button(b_frame,width=10,pady=7,text='304',bg='#73260E', fg='white',border=0, command=r_304).place(x=730,y=220)
		r_305=Button(b_frame,width=10,pady=7,text='305',bg='#73260E', fg='white',border=0, command=r_305).place(x=820,y=220)

		

		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()

		nl = Label(b_frame,text='www.cityguesthouse.com.np',fg='black',bg='gray91',font='msserif 8')
		nl.place(x=900,y=310)
		nl.tkraise()

#--------------- payments-----------------------------------------------------------------------------------------------------------------------

	def payments():
		b_frame = Frame(root,height=400,width=1080,bg='gray89')
		path = "images/newbg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=400,width=1080)
		label.image=img
		label.place(x=0,y=0)
		l = Label(b_frame,text='Enter Room No.',font='msserif 15',bg='#73260E',fg='white')
		l.place(x=245,y=0)
		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()
		hline = Frame(b_frame,height=42,width=1080,bg='#73260E')
		hline.place(x=0,y=23)
		ef = Frame(hline)
		p_id = Entry(ef)
		p_id.pack(ipadx=25,ipady=3)
		ef.place(x=308,y=6)

			
		fl3=Frame(b_frame,height=38,width=308,bg='#73260E')
		fl3.place(x=0,y=150)
		fl3.pack_propagate(False)
		l1=Label(fl3,text='Amount',bg='#73260E',fg='white',font='msserif 17')
		l1.pack()
		
		
		def getid(event=None):


			def check_out():
				con=sqlite3.connect('cgh-hms-db.db')
				c=con.cursor()

				if (p_id.get() ==''):
					messagebox.showerror('Entries not filled','Kindly Enter room Number')
				else :
					c.execute("update room set room_status='Available' where res_room_no = ? ",(p_id.get(),))
					messagebox.showinfo("Checkout Successful","Checked out successfully")
					


					c.execute("DELETE from guests WHERE res_room_no = " + p_id.get())
					c.execute("SELECT *, oid FROM guests")
					records = c.fetchall()
					p_id.delete(0,END)
					# print ('Deleted Successfully')

				con.commit()
				con.close()




			if p_id.get()!='':
				global amount
				global nightrec
					#connection with database
				con=sqlite3.connect('cgh-hms-db.db')
				c=con.cursor()
				c.execute("SELECT rate from room WHERE res_room_no="+p_id.get())
				payrecord=c.fetchall()

				c.execute("SELECT no_nights from guests WHERE res_room_no="+p_id.get())
				nightrec=c.fetchall()
				
				for j in nightrec:
					nights=str(nightrec[0])
					nights=nights.replace(',','')
					nights=nights.replace('(','')
					nights=nights.replace(')','')

				for i in payrecord:
					amount=str(payrecord[0])
					amount=amount.replace(',','')
					amount=amount.replace('(','')
					amount=amount.replace(')','')
					# print (amount)
				
				try:
					total = int(amount)*int(nights)
					
				except:
					messagebox.showerror("Alert","Room Not Assigned!")

				else:
					total = int(amount)*int(nights)
					
					l2=Label(b_frame,text=total,bg='#73260E',fg='white',font='msserif 17')
					l2.place(x=100,y=240)
					l4=Label(b_frame,text=nights,fg='black',font='msserif 12')
					l4.place(x=230,y=80)

					fl3=Frame(b_frame,height=38,width=308,bg='#73260E')
					fl3.place(x=0,y=150)
					fl3.pack_propagate(False)
					l1=Label(fl3,text='Amount to Pay',bg='#73260E',fg='white',font='msserif 17')
					l1.pack()
					
					l3=Label(b_frame,text='Total No. of Nights:',fg='black',font='msserif 12')
					l3.place(x=50,y=80)
					
					l5=Label(b_frame,text=date_time_str,fg='black',font='msserif 12')
					l5.place(x=730,y=80)
					l5=Label(b_frame,text='Bill Generated on:',fg='black',font='msserif 12')
					l5.place(x=600,y=80)

					pinv = Button(b_frame,text='Check Out',bg='#73260E',fg='white',command=check_out).place(x=976,y=235)
			else:
				messagebox.showwarning("Incomplete Input", "Enter Valid Data and Try Again")
			

		
		ok = Button(hline,text='Generate Bill',font='msserif 10',bg='white',activebackground='steelblue',fg='#73260E',command=getid)
		ok.place(x=530,y=5)

		nl = Label(b_frame,text='www.cityguesthouse.com.np',fg='black',bg='gray91',font='msserif 8')
		nl.place(x=900,y=310)
		nl.tkraise()
		
			
		# def pr():
		# 	con=sqlite3.connect('cgh-hms-db.db')
		# 	c=con.cursor()
		# 	c.execute("SELECT res_room_no from guests")
		# 	rnum=c.fetchall()
		# 	for i in rnum:
		# 		c.execute("""UPDATE room SET
		# 		room_status=:st
		# 		WHERE res_room_no=:rn""",{
		# 			'st': 'Available',
		# 			'rn': i[0]
		# 		})

		# 	c.execute("DELETE from guests WHERE res_room_no = " + p_id.get())

		# 	c.execute("SELECT *, oid FROM guests")
		# 	records = c.fetchall()
			
		# 	con.commit()
		# 	con.close()
		# 	messagebox.showinfo("Checkout Information", "Guest has been checked out successfully!")
		

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
		nl = Label(b_frame,text='www.cityguesthouse.com.np',fg='black',bg='gray91',font='msserif 8')
		nl.place(x=900,y=310)
		nl.tkraise()

#---------------Top Background Frame------------------------------------------------------------------------------------------------------------------

	top_frame = Frame(root,height=70,width=1080,bg='orange')
	path = "D://cgh-hms-main/images/newestbg6.png"
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
    
	#-------------exit module----------------------------------------------------------------------------------------------------------------------
	def food_order():
		root.destroy()
		import main
    

    #---------------Buttons Frame-----------------------------------------------------------------------------------------------------------------

	sl_frame = Frame(root,height=130,width=1080,bg='white')
	sl_frame.place(x=0,y=70+6)
	path = "images/rooms.png"
	img = ImageTk.PhotoImage(Image.open(path))
	b1 = Button(sl_frame,image=img,text='b1',bg='white',width=180,command=hotel_status)
	b1.image = img
	b1.place(x=180,y=0)
	path2 = "images/online-order.png"
	img1 = ImageTk.PhotoImage(Image.open(path2))
	b2 = Button(sl_frame,image=img1,text='b2',bg='white',width=180,command=food_order)
	b2.image = img1
	b2.place(x=0,y=0)
	path3='images/guests.png'
	img3 = ImageTk.PhotoImage(Image.open(path3))
	b3 = Button(sl_frame,image=img3,text='b2',bg='white',width=180, command=staff)
	b3.image = img3
	b3.place(x=180*4,y=0)
	path4='images/payments.png'
	img4 = ImageTk.PhotoImage(Image.open(path4))
	b4 = Button(sl_frame,image=img4,text='b2',bg='white',width=180, command=payments)
	b4.image = img4
	b4.place(x=180*3,y=0)
	path5='images/logout.png'
	img5 = ImageTk.PhotoImage(Image.open(path5))
	b5 = Button(sl_frame,image=img5,text='b2',bg='white',width=180,height=100, command=exit)
	b5.image = img5
	b5.place(x=180*5,y=0)
	path6='images/Bookroom.png'
	img6 = ImageTk.PhotoImage(Image.open(path6))
	b6 = Button(sl_frame,image=img6,text='b2',bg='white',width=180,height=100, command=reserve)
	b6.image = img6
	b6.place(x=180*2,y=0)
	Label(sl_frame,text='Food/Beverage Orders',font='msserif 10',bg='white').place(x=30,y=106)
	Label(sl_frame,text='Rooms & Status',font='msserif 10',bg='white').place(x=230,y=106)
	Label(sl_frame,text='Book & Reserve',font='msserif 10',bg='white').place(x=417,y=106)
	Label(sl_frame,text='Important Contacts',font='msserif 10',bg='white').place(x=760,y=106)
	Label(sl_frame,text='Checkout',font='msserif 10',bg='white').place(x=605,y=106)
	Label(sl_frame,text='Exit',font='msserif 10',bg='white').place(x=975,y=106)
	sl_frame.pack_propagate(False)
	
    #-------------------extra frame------------------------------------------------------------------------------------------------------------------
	redf = Frame(root,height=6,width=1080,bg='#73260E')
	redf.place(x=0,y=70)
	redf1 = Frame(root,height=6,width=1080,bg='#73260E')
	redf1.place(x=0,y=210)


mainroot()
mainloop()