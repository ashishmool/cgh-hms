import tkinter as tk
from tkinter import *
from tkinter import ttk
from my_connect import my_conn
from  datetime import date
from my_invoice import my_invoice
from config import *
sb=[]
my_w = tk.Tk()
my_w.geometry("1000x800") 
my_w.columnconfigure(0,weight=8)
my_w.columnconfigure(1,weight=2)
my_w.rowconfigure(0, weight=1) 
my_w.rowconfigure(1, weight=14) # change weight to 4
my_w.rowconfigure(2, weight=2)

frame_top=tk.Frame(my_w,bg='white')
frame_bottom=tk.Frame(my_w,bg='white')

frame_m_right=tk.Frame(my_w,bg='#f8fab4')
frame_m_left=tk.Frame(my_w,bg='#284474')

#placing in grid
frame_top.grid(row=0,column=0,sticky='WENS',columnspan=2)
frame_m_left.grid(row=1,column=0,sticky='WENS')
frame_m_right.grid(row=1,column=1,sticky='WENS')
frame_bottom.grid(row=2,column=0,sticky='WENS',columnspan=2)
trv = ttk.Treeview(frame_m_right, selectmode ='browse')
trv.grid(row=0,column=0,columnspan=2,padx=3,pady=2)

# column identifiers 
trv["columns"] = ("1", "2","3")
trv.column("#0", width = 80, anchor ='w')
trv.column("1", width = 60, anchor ='w')
trv.column("2", width =50 , anchor ='c')
trv.column("3", width = 50, anchor ='c')
  
# Headings  
# respective columns
trv.heading("#0", text ="Item",anchor='w')
trv.heading("1", text ="Price",anchor='w')
trv.heading("2", text ="qty",anchor='c')
trv.heading("3", text ="Total",anchor='c')
def my_reset():
    global total, tax
    for item in trv.get_children():
        trv.delete(item)
    l1=[]
    for i in range(8):
        l1.append(tk.IntVar(value=0))
    for i in range(len(sb)):
        sb[i].config(textvariable=l1[i])

    for w in frame_m_right.grid_slaves(1):
        w.grid_remove()
    for w in frame_m_right.grid_slaves(2):
        w.grid_remove()    
    for w in frame_m_right.grid_slaves(3):
        w.grid_remove()
    dt=date.today().strftime('%Y-%m-%d') # todays date
    query="INSERT INTO  plus2_bill (total,tax,`bill_date`) \
                  VALUES (%s,%s,%s)"
    data=[total,tax,dt]
    id=my_conn.execute(query,data)
    #print(total, tax)
    bill_no=id.lastrowid
    for i in dl:
        i.insert(3,bill_no)
        i.insert(4,dt)
    query="INSERT INTO plus2_sell(p_id,price,quantity,bill_no,bill_date)\
                  VALUES(%s,%s,%s,%s,%s)"
    id=my_conn.execute(query,dl)
    #print("Rows Added  = ",id.rowcount)  
    lr1=tk.Button(frame_m_right,text='Bill',font=font1,command=lambda:my_invoice(my_w,bill_no,img_top))
    lr1.grid(row=1,column=0,sticky='nw')                
dl=[]    
total,tax,final=0,0,0
def my_bill():
    global dl,total,tax,final 
    total,tax,final=0,0,0
    dl.clear()
    for item in trv.get_children():
        trv.delete(item)
    
    for i in range(len(sb)):
        if(int(sb[i].get())>0): 
            price=int(sb[i].get())*my_menu[i][2]
            total=round(total+price,2)
            my_str1=(str(my_menu[i][2]), str(sb[i].get()), str(price))
            trv.insert("",'end',iid=i,text=my_menu[i][1],values=my_str1)
            dl.append([my_menu[i][0],my_menu[i][2],int(sb[i].get())])
    lr1=tk.Label(frame_m_right,text='Total',font=font1)
    lr1.grid(row=1,column=0,sticky='nw')
    lr2=tk.Label(frame_m_right,text=str(total),font=font1)
    lr2.grid(row=1,column=1,sticky='nw')
    lr21=tk.Label(frame_m_right,text='Tax 10%',font=font1)
    lr21.grid(row=2,column=0,sticky='nw')
    tax=round(0.1*total,2)
    lr22=tk.Label(frame_m_right,text=str(tax),font=font1)
    lr22.grid(row=2,column=1,sticky='nw')
    lr31=tk.Label(frame_m_right,text='Total',font=font2)
    lr31.grid(row=3,column=0,sticky='nw')
    final=round(total+tax,2)
    lr32=tk.Label(frame_m_right,text=str(final),font=font2)
    lr32.grid(row=3,column=1,sticky='nw')
    # add data to to database table plus2_bill 
    
    #print(dt)
    
        
# Layout is over , sart placing buttons 
#path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
font1=('Times',14,'normal')
font2=('Times',32,'bold')
pdx,pdy=1,5
img_top = tk.PhotoImage(file = path_image+"restaurant-3.png")
bg=tk.PhotoImage(file=path_image+'bg2.png')

c1 = tk.Canvas(frame_m_left,width=1000,height=500)
c1.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='nw',padx=0)
c1.create_image(0,0,image=bg,anchor='nw')

img_l1 = tk.Label(frame_top,  image=img_top)
img_l1.grid(row=0,column=0,sticky='nw',pady=1)
img_l1.image=img_top
my_menu={} # Dictionary to store items with price
sb=[]
r,c,i=0,0,0
def show_items(cat):
    global r,c,i,my_menu
    my_menu.clear() # remove all items
    sb.clear() 
    r,c,i=0,0,0
    r_set=my_conn.execute("SELECT * FROM plus2_products WHERE \
       available=1 and  p_cat="+str(cat))
    
    for item in r_set: 
        menu=tk.Label(frame_m_left,text=item[1]+'('+str(item[3])+')',font=font1)
        menu.grid(row=r,column=c,padx=pdx,pady=0)    
        r1=r+1
        sbox = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font2,width=1)
        sbox.grid(row=r1,column=c,padx=pdx,pady=0)
        sb.append(sbox)  
        my_menu[i]=[item[0],item[1],item[3]]
        i=i+1
        if(c>2): # add one more row 
            c=0
            r=r+2
        else:
            c=c+1

show_items(1)
r=r+1
r1_v = tk.IntVar(value=1) # We used integer variable here 

r1 = tk.Radiobutton(frame_bottom, text='Breakfast', variable=r1_v, value=1,command=lambda:show_items(1))
r1.grid(row=r,column=0) 

r2 = tk.Radiobutton(frame_bottom, text='Lunch', variable=r1_v, value=0,command=lambda:show_items(2))
r2.grid(row=r,column=1) 

r3 = tk.Radiobutton(frame_bottom, text='Dinner', variable=r1_v, value=5,command=lambda:show_items(3))
r3.grid(row=r,column=2)

b1=tk.Button(frame_bottom,text='Get Bill',command=my_bill)
b1.grid(row=r,column=3,padx=10)
b2=tk.Button(frame_bottom,text='Confirm ( Reset)',command=my_reset)
b2.grid(row=r,column=4,padx=10)
my_w.mainloop()