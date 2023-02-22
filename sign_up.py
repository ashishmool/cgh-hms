
#Import Library
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

#Creating GUI for Application
root = Tk()
root.title('Sign Up')

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

# Open Database Connection
con = sqlite3.connect('cgh-hms-db.db')
c = con.cursor()

# # Table Creation for Database Execution

listOfTables = c.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='users'; """).fetchall()
 
if listOfTables == []:
    c.execute ("""CREATE TABLE users (
    f_name text,
    email text PRIMARY KEY,
    password text,
    address text,
    contact integer,
    security_question text
)""")
    
    print ("Table created successfully")


#Back to Login Function

def login():
    root.destroy()
    import login

#Register Function
def register():
    if name_entry.get()!='' and email_entry.get()!='' and password_entry.get()!='' and address_entry.get()!='' and contact_entry.get()!='' and security_entry.get()!='':
        
        con=sqlite3.connect('cgh-hms-db.db')
        c=con.cursor()

        c.execute("INSERT INTO users VALUES (:f_name, :email, :password, :address, :contact, :security_question)", {
            'f_name':name_entry.get(),
            'email':email_entry.get(),
            'password':password_entry.get(),
            'address':address_entry.get(),
            'contact':contact_entry.get(),
            'security_question': security_entry.get(),
        })

        #clear text boxes
        name_entry.delete(0,END)
        email_entry.delete(0,END)
        password_entry.delete(0,END)
        address_entry.delete(0,END)
        contact_entry.delete(0,END)
        security_entry.delete(0,END)

        messagebox.showinfo("Registration Information", "Registered Successfully")

        con.commit()
        con.close()

        root.destroy()
        import login
    else:
        messagebox.showerror("Incomplete Information","Please fill in all required details and try again!")

#System Background Image
img = PhotoImage(file='D://cgh-hms-main/images/front-view.png')
Label(root,image=img,bg='white').place(x=0,y=0)

#Creating Frame for Sign Up Interface
frame = Frame(root,width=380,height=410,bg='white')
frame.place(x=300,y = 70)

#Sign Up Header
heading = Label(frame,text='Sign Up',fg='#73260E',bg='white',font=('Candara',23,'bold'))
heading.place(x=25,y=5)

#Labels
name_label = Label(frame,text="Full Name",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
name_label.place(x=10,y=50)
email_label = Label(frame,text="Email",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
email_label.place(x=10,y=90)
password_label = Label(frame,text="Password",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
password_label.place(x=10,y=130)
address_label = Label(frame,text="Address",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
address_label.place(x=10,y=170)
contact_label = Label(frame,text="Contact",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
contact_label.place(x=10,y=210)
security_question_label = Label(frame,text="Security Question: What is your mother's maiden name?",fg='black',bg='white',font=('Microsoft YaHei UI Light', 8, 'bold'))
security_question_label.place(x=10,y=250)
security_answer_label = Label(frame,text="Answer",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
security_answer_label.place(x=10,y=290)

# function to validate number entry
def only_numbers(char):
    return char.isdigit()
    
validation = frame.register(only_numbers)


#Entry Boxes
name_entry = Entry(frame,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
name_entry.place(x=80, y=50)
email_entry = Entry(frame,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
email_entry.place(x=80, y=90)
password_entry = Entry(frame,width=16,fg='black',show='*',bg='white',font=('Microsoft YaHei UI Light',11))
password_entry.place(x=80, y=130)
address_entry = Entry(frame,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
address_entry.place(x=80, y=170)
contact_entry = Entry(frame,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11),validate="key", validatecommand=(validation, '%S'))
contact_entry.place(x=80, y=210)
security_entry = Entry(frame,width=30,fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
security_entry.place(x=80, y=290)

#Show Password Feature
show_pass=IntVar()
def show_pass_check():
    if show_pass.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

show_pass_checkbox = Checkbutton(frame, text = 'Show Password', variable = show_pass,bg='white', onvalue = 1, offvalue = 0, command=show_pass_check)
show_pass_checkbox.place(x=200, y=130)



# #text box to enter marks
# t2=Entry(root,)
# t2.pack()


#Register Button

Button(frame,width=40,pady=7,text='Register',bg='#73260E', fg='white',border=0, command=register).place(x=35,y=350)

#Back to Login
label = Label(root,text="Already Registered?",fg='black',bg='white',font=
('Microsoft YaHei UI Light', 9))
label.place(x=750,y=30)
back=Button(root,width=12,text='Back to Login',border=0,bg='#73260E', fg='white',cursor='hand2',command=login)
back.place(x=760,y=60)

# Close Open Database Connection
con.commit()
con.close()

root.mainloop()