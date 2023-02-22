#Import Library
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

#Creating GUI for Application
root = Tk()
root.title('Recover Password')

window_height = 500
window_width = 925
 
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

# root.geometry('925x500')
root.configure(bg='#fff')
root.resizable(False,False)
root.iconbitmap('D://cgh-hms-main/images/logo-only.ico')

#System Background Image
img = PhotoImage(file='D://cgh-hms-main/images/front-view.png')
Label(root,image=img,bg='white').place(x=0,y=0)

#Creating Frame for Interface
frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=300,y = 70)

#Header
heading = Label(frame,text='Recover Password',fg='#73260E',bg='white',font=('Candara',23,'bold'))
heading.place(x=25,y=5)

#Back to Login Function

def login():
    root.destroy()
    import login

def del_acc():
    messagebox.showwarning("Delete Account","Are You Sure")
    conn=sqlite3.connect('cgh-hms-db.db')
    c=conn.cursor() 
    
    c.execute("SELECT rowid FROM users")
    records = c.fetchall()
    for i in records:
        
        c.execute("DELETE from users WHERE rowid = " + row_id)
    messagebox.showinfo("Account Info","Deleted Successfully")
    root.destroy()
    import sign_up
   
    

    
    conn.commit()
    conn.close()
    
    

def save_changes():
    conn=sqlite3.connect('cgh-hms-db.db')
    c=conn.cursor() 
    
    record_id= row_id

    c.execute("""UPDATE users SET
        f_name = :f_name,
        email = :email,
        password = :password,
        address = :address,
        contact = :contact,
        security_question = :security_question
        WHERE oid = :oid""",
        {'f_name':name_entry.get(),
        'email':email_entry.get(),
        'password':password_entry.get(),
        'address':address_entry.get(),
        'contact':contact_entry.get(),
        'security_question': security_entry.get(),
        'oid' : record_id
        })

    conn.commit()
    conn.close()
    messagebox.showinfo("Account Details Update", "Your changes have been updated successfully!")
    root.destroy()
    import login

def edit():
            #Creating Frame for Interface
    frame2 = Frame(root,width=350,height=450,bg='white')
    frame2.place(x=300,y = 70)

    #Header
    heading = Label(frame2,text='Password Recovery',fg='#73260E',bg='white',font=('Candara',23,'bold'))
    heading.place(x=25,y=5)

    con=sqlite3.connect('cgh-hms-db.db')
    c=con.cursor()

    global name_entry
    global email_entry
    global password_entry
    global address_entry
    global contact_entry
    global security_entry

        #Labels
    name_label = Label(frame2,text="Full Name",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
    name_label.place(x=10,y=50)
    email_label = Label(frame2,text="Email",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
    email_label.place(x=10,y=90)
    password_label = Label(frame2,text="Password",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
    password_label.place(x=10,y=130)
    address_label = Label(frame2,text="Address",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
    address_label.place(x=10,y=170)
    contact_label = Label(frame2,text="Contact",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
    contact_label.place(x=10,y=210)
    security_question_label = Label(frame2,text="Security Question: What is your mother's maiden name?",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
    security_question_label.place(x=10,y=250)
    security_answer_label = Label(frame2,text="Answer",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
    security_answer_label.place(x=10,y=290)


    #Entry Boxes
    name_entry = Entry(frame2,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
    name_entry.place(x=80, y=50)
    email_entry = Entry(frame2,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
    email_entry.place(x=80, y=90)
    password_entry = Entry(frame2,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
    password_entry.place(x=80, y=130)
    address_entry = Entry(frame2,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
    address_entry.place(x=80, y=170)
    contact_entry = Entry(frame2,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
    contact_entry.place(x=80, y=210)
    security_entry = Entry(frame2,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
    security_entry.place(x=80, y=290)

    #Button Save
    Button(frame2,width=39,pady=7,text='Update Changes',bg='#73260E', fg='white',border=0, command=save_changes).place(x=35,y=350)

    #Button Delete Account
    Button(frame2,width=39,pady=7,text='Delete Account',bg='#73260E', fg='white',border=0, command=del_acc).place(x=35,y=400)

    c.execute("SELECT * FROM users WHERE rowid ="+ row_id)
    
    records=c.fetchall()

    for record in records:
        name_entry.insert(0, record[0])
        email_entry.insert(1, record[1])
        password_entry.insert(2, record[2])
        address_entry.insert(3, record[3])
        contact_entry.insert(4, record[4])
        security_entry.insert(5, record[5])

    con.commit()
    con.close()


def verify_update():
    con=sqlite3.connect('cgh-hms-db.db')
    c=con.cursor() 

    c.execute("SELECT *, rowid, email, security_question FROM users")

    records=c.fetchall()
    global found_username
    global row_id
    found_username=''
    found_security_question=''
    username_check=''
    found_row_id=''
    for record in records:
        username_check = str(record[1])
        
        if user.get() == username_check:
            found_username=username_check
            found_security_question = str(record[5])
            row_id = str(record[6])
    if found_username==user.get() and found_security_question==security_answer.get(): 
        edit()
    else:
        messagebox.showinfo("Incorrect Information", "Invalid Credentials!")
    con.commit()
    con.close()

#Username Entry Box and Focus Feature
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0,'Registered Email')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Registered Email')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#Security Answer Entry Box and Focus Feature
def on_enter(e):
    security_answer.delete(0,'end')

def on_leave(e):
    name=security_answer.get()
    if name =='':
        security_answer.insert(0,'Security Answer')

security_question_label = Label(frame,text="Security Question: What is your mother's maiden name?",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
security_question_label.place(x=25,y=190)
    
security_answer= Entry(frame,width=25,fg='black',text='Security Answer',show='',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
security_answer.place(x=30,y=150)
security_answer.insert(0,'Security Answer')
security_answer.bind('<FocusIn>',on_enter)
security_answer.bind('<FocusOut>', on_leave)
    
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#Button
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
Button(frame,width=39,pady=7,text='Update Password',bg='#73260E', fg='white',border=0, command=verify_update).place(x=35,y=230)

#Back to Login
label = Label(root,text="Already Registered?",fg='black',bg='white',font=
('Microsoft YaHei UI Light', 9))
label.place(x=750,y=30)
back=Button(root,width=12,text='Back to Login',border=0,bg='#73260E', fg='white',cursor='hand2',command=login)
back.place(x=760,y=60)

root.mainloop()