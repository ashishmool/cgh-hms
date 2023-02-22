#Import Library
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

#Creating GUI for Application
root = Tk()
root.title('Login')


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
# root.eval('tk::PlaceWindow . center')
root.configure(bg='#fff')
root.resizable(False,False)
root.iconbitmap('D://cgh-hms-main/images/logo-only.ico')

#System Background Image
img = PhotoImage(file='D://cgh-hms-main/images/front-view.png')
Label(root,image=img,bg='white').place(x=0,y=0)

#Creating Frame for Login Interface
frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=300,y = 70)

#Login Header
heading = Label(frame,text='Sign In',fg='#73260E',bg='white',font=('Candara',23,'bold'))
heading.place(x=25,y=5)

#Redirect to Forgot Password Window
def forgot_password():
    root.destroy()
    import forgot_password

def verify():
    con=sqlite3.connect('cgh-hms-db.db')
    c=con.cursor() 
    c.execute("SELECT *, email, password FROM users")
    records=c.fetchall()
    found_username=''
    found_password=''
    username_check=''
    for record in records:
        username_check = str(record[1])
        if user.get() == username_check:
            found_username=username_check
            found_password = str(record[2])
    if found_username==user.get() and found_password==password.get():
        root.destroy()
        import system
    else:
        messagebox.showinfo("Incorrect Information", "Invalid Credentials!")
    con.commit()
    con.close()


def signup():
    root.destroy()
    import sign_up

def forgot_pass():
    root.destroy()
    import forgot_password

def sign_in():
    username=user.get()
    password=password.get()


#Username Entry Box and Focus Feature
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#Password Entry Box and Focus Feature
def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    name=password.get()
    if name ==' ':
        password.insert(0,'Password')

password= Entry(frame,width=25,fg='black',text='Password',show='*',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>', on_leave)

#Show Password Feature
show_pass=IntVar()
def show_pass_check():
    if show_pass.get():
        password.config(show='')
    else:
        password.config(show='*')

show_pass_checkbox = Checkbutton(frame, text = 'Show Password', variable = show_pass,bg='white', onvalue = 1, offvalue = 0, command=show_pass_check)
show_pass_checkbox.place(x=20, y=190)

#Sign In Button
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
Button(frame,width=39,pady=7,text='Sign In',bg='#73260E', fg='white',border=0, command=verify).place(x=35,y=230)

#Sign Up Label and Button
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
label.place(x=75,y=300)
sign_up=Button(frame,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#73260E', command=signup)
sign_up.place(x=215,y=300)

#Forgot Passwort Feature
label = Label(root,text="Trouble Logging In?",fg='black',bg='white',font=('Microsoft YaHei UI Light', 10))
label.place(x=750,y=30)
forgot=Button(root,width=12,text='Forgot Password',border=2,bg='white', fg='#73260E',cursor='hand2',command=forgot_pass)
forgot.place(x=760,y=60)

root.mainloop()