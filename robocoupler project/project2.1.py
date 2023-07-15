from tkinter import *
import tkinter as tk
import pyqrcode
from tkinter import font
from PIL import ImageTk,Image

count=0
cnt=0
# Function to add an item to the cart
def add_to_cart(val):
    slt_itm= val
    #sel_prc=val[slt_itm]
    cart_listbox.insert(tk.END,slt_itm)

    #actin of button
def action(val):
    add_to_cart(val)
    #code exe start
root = tk.Tk()
root.title("Royal Enfield Accessories")
root.geometry('1336x768')
bg=PhotoImage(file="bg.png")
relogo=PhotoImage(file="rename.png")
renme=PhotoImage(file="relogo.png")
menu=PhotoImage(file="menu.png")
l=Canvas(root,width=1366,height=768,highlightthickness=0)
l.place(x=0,y=0)
head=PhotoImage(file="head.png")


l.create_image(0,70,image=bg,anchor='nw')
l.create_image(0,0,image=head,anchor='nw')
l.create_image(570,20,image=relogo,anchor='nw')
l.create_image(515,15,image=renme,anchor='nw')
l.create_image(90,25,image=menu,anchor='nw')


l.create_text(690,210,fill="white",text='Accessories Available',font=('Book Antiqua',25,'bold'))
l.create_text(1170,40,fill="white",text='Help',font=('Sans',10))
l.create_text(680,100,fill="white",text='"Made Like A Gun... Goes Like A Bullet"',font=('Century Schoolbook',13 ,"bold italic"))

    # Cart
def cart():
    crt_lb=tk.Toplevel(root)
    crt_lb.title('My Cart')
    bl=Label(crt_lb,image=bg)
    bl.place(x=0,y=0)
    #crt_lb.create_image(0,0,image=bg,anchor='nw')
    crt_lb.geometry("400x300")
    goods= cart_listbox.get(0, tk.END)
    cart_lb = tk.Listbox(crt_lb, width=40,height=7)
    root.bind("<Escape>",lambda event:crt_lb.destroy())
    cart_lb.pack()
    
        #details
    '''d1=tk.Label(crt_lb,text='Name:',font=('Comic Sans MS',12))
    d1.place(x=90,y=190)
    e1=Entry(crt_lb,width=30,bg='white')
    e1.place(x=150,y=200)
    d1=tk.Label(crt_lb,text='phone no:',font=('Comic Sans MS',12))
    d1.place(x=70,y=230)
    e2=Entry(crt_lb,width=30,bg='white')
    e2.place(x=150,y=240)
    d1=tk.Label(crt_lb,text='Email Id:',font=('Comic Sans MS',12))
    d1.place(x=70,y=270)
    e3=Entry(crt_lb,width=30,bg='white')
    e3.place(x=150,y=280)

    
    d1=tk.Label(crt_lb,text='Address:',font=('Comic Sans MS',12))
    d1.place(x=420,y=190)
    e4=Entry(crt_lb,width=30,bg='white')
    e4.place(x=500,y=200)
    d1=tk.Label(crt_lb,text='Land Mark:',font=('Comic Sans MS',12))
    d1.place(x=400,y=230)
    e5=Entry(crt_lb,width=30,bg='white')
    e5.place(x=500,y=240)
    d1=tk.Label(crt_lb,text='Pincode:',font=('Comic Sans MS',12))
    d1.place(x=425,y=270)
    e5=Entry(crt_lb,width=30,bg='white')
    e5.place(x=500,y=280)'''
    def remove_from_cart():
        selected_item = cart_lb.curselection()
        if selected_item:
            cart_lb.delete(selected_item)
    def checkout():
        items = cart_lb.get(0, tk.END)
        if items:
            total_price = sum(float(item) for item in items)
            checkout_window = tk.Toplevel(root)
            checkout_window.title("Checkout")
            total_label = tk.Label(checkout_window, text="Total items: " + str(len(items)))
            total_label.pack(pady=10)
            items_label = tk.Label(checkout_window, text="Items:")
            for item in items:
                item_label = tk.Label(checkout_window, text=item)
                item_label.pack()
                #qr code
            amount=f"{total_price:.2f}"
            mer_id="charangadamsetty1608@okicici"
            name="GadamsettyCharan"
            qr_data = f"upi://pay?pa={mer_id}&pn={name}&am={amount}&cu=INR&mc=0000&aid=uGICAgICzjqOeSw"       
            qr=pyqrcode.create(qr_data)
            qr_image=qr.png("qr_code.png",scale=4)
            def img():
                qr_image=Image.open("qr_code.png")
                qr_photo=ImageTk.PhotoImage(qr_image)
                qr_label=tk.Label(checkout_window,image=qr_photo)
                qr_label.image=qr_photo
                qr_label.pack()
                        # Pay button
            pay_button = tk.Button(checkout_window, text="Pay With QR",command=lambda:img())
            pay_button.pack(pady=10)
        
        total_price_label = tk.Label(checkout_window, text="Total Price: rs " + f"{total_price:.2f}")
        total_price_label.pack(pady=10)

    
                   #remove from cart button
    remove_button = tk.Button(crt_lb, text="Remove from Cart", command=(remove_from_cart))
    remove_button.pack()
                        # checkout button
    checkout_button = tk.Button(crt_lb,text="Checkout", command=checkout)
    checkout_button.pack() 
    for itm in goods:
            #item_label = tk.Label(checkout_window, text=itm)
            cart_lb.insert(tk.END,itm)
  
cart_listbox = tk.Listbox(root, width=1,height=1)
cart_listbox.place(x=1100,y=1100)

            #cart button

imagecrt=PhotoImage(file="llll.png")
crt_lb = tk.Button(root, image=imagecrt,bg="black",activebackground="black",command=lambda:cart())
crt_lb.place(x=1210,y=20)

        #timer pics
hel_pic=[ PhotoImage(file="hel1.png"),PhotoImage(file="hel2.png"),PhotoImage(file="hel3.png"),PhotoImage(file="hel4.png")]
bot_pic=[ PhotoImage(file="bot1.png"),PhotoImage(file="bot2.png"),PhotoImage(file="bot3.png"),PhotoImage(file="bot4.png")]
glv_pic=[ PhotoImage(file="glv1.png"),PhotoImage(file="glv2.png"),PhotoImage(file="glv3.png"),PhotoImage(file="glv4.png")]
jak_pic=[ PhotoImage(file="jak1.png"),PhotoImage(file="jak2.png"),PhotoImage(file="jak3.png"),PhotoImage(file="jak4.png")]


        

'''def login():
    def val_login():
        usrnme=e1.get()
        pswrd=e2.get()
        if usrnme in vaid_cred and valid_cred[usrnme]=pswrd:
            
    login=tk.Toplevel(root)
    login.title('My Cart')
    login.geometry("300x200")
    l1=tk.Label(login,text='Username:',font=('Comic Sans MS',12))
    l1.place(x=10,y=70)
    e1=Entry(login,width=30,bg='white')
    e1.place(x=100,y=70)
    l2=tk.Label(login,text='Paasword:',font=('Comic Sans MS',12))
    l2.place(x=10,y=110)
    e2=Entry(login,width=30,bg='white')
    e2.place(x=100,y=110)
    btn=tk.Button(login,text="Enter",command=lambda:login.destroy())
    btn.pack()
    

log_btn = tk.Button(root, text="Loggin",font=('Sitka Banner',13,), command=lambda:login())
log_btn.place(x=110,y=50)'''

        #counter
def cont():
    global count
    count=count+1
    cnt1.config(text=str(count))
cnt1=tk.Label(root,text=str(count),bg="black",fg='white',font=(10))
cnt1.place(x=1265,y=25)


def next():
    global cnt
    if cnt==3:
        t1.create_image(0,0,image=hel_pic[0],anchor='nw')
        t2.create_image(0,0,image=bot_pic[0],anchor='nw')
        t3.create_image(0,0,image=jak_pic[0],anchor='nw')
        t4.create_image(0,0,image=glv_pic[0],anchor='nw')
        cnt=0
    else:
        t1.create_image(0,0,image=hel_pic[cnt+1],anchor='nw')
        t2.create_image(0,0,image=bot_pic[cnt+1],anchor='nw')
        t3.create_image(0,0,image=jak_pic[cnt+1],anchor='nw')
        t4.create_image(0,0,image=glv_pic[cnt+1],anchor='nw')
        cnt += 1
    root.after(3000,next)



'''t=Canvas(root,width=1399,height=50)
t.create_image(0,0,image=head,anchor='nw')
t.place(x=100,y=100)'''
    #helmet
'''count=0
def cont1():
    global count
    count+=1
    cnt1.config(text=str(count))    
cnt1=tk.Label(root,text=str(count))
cnt1.place(x=400,y=510)'''
bg1=tk.PhotoImage(file="hel1.png")
t1=Canvas(root,width=150,height=150,highlightthickness=0)
t1.create_image(0,0,image=hel_pic[0],anchor='nw')
l.create_text(330,465,fill="white",text='Helmet',font=('Comic Sans MS',15))
l.create_text(330,490,fill="white",text='Rs.2,700/-',font=('Gill Sans MT',10))
t1.place(x=250,y=300)
btn2=Button(root,text="Add To Cart",font=('Gill Sans MT',10,'bold'),command=lambda:(action(2700),cont()))
btn2.place(x=280,y=500)
    #boots
'''count1=0
def cont2():
    global count1
    count1+=1
    cnt2.config(text=str(count1))    
cnt2=tk.Label(root,text=str(count1))
cnt2.place(x=600,y=510)'''
bg2=PhotoImage(file="bot1.png")
t2=Canvas(root,width=149,height=149,highlightthickness=0 )
t2.create_image(0,0,image=bot_pic[0],anchor='nw')
t2.place(x=480,y=300)
l.create_text(550,465,fill="white",text='Boots',font=('Comic Sans MS',15))
l.create_text(550,490,fill="white",text='Rs.4,400/-',font=('Gill Sans MT',10))
btn1=Button(root,text="Add To Cart",font=('Gill Sans MT',10,'bold'),command=lambda:(action(4400),cont()))
btn1.place(x=510,y=500)

    #jacket
'''count3=0
def cont3():
    global count3
    count3+=1
    cnt3.config(text=str(count3))    
cnt3=tk.Label(root,text=str(count3))
cnt3.place(x=800,y=510)'''
bg3=PhotoImage(file="jak1.png")
t3=Canvas(root,width=149,height=149,highlightthickness=0)
t3.create_image(0,0,image=jak_pic[0],anchor='nw')
t3.place(x=700,y=300)
l.create_text(780,465,fill="white",text='Jacket',font=('Comic Sans MS',15))
l.create_text(780,490,fill="white",text='Rs.13,125/-',font=('Gill Sans MT',10))
btn3=Button(root,text="Add To Cart",font=('Gill Sans MT',10,'bold'),command=lambda:(action(13125),cont()))
btn3.place(x=730,y=500)
    #glove
'''count4=0
def cont4():
    global count4
    count4+=1
    cnt4.config(text=str(count4))    
cnt4=tk.Label(root,text=str(count4))
cnt4.place(x=1000,y=510)'''
bg4=PhotoImage(file="glv1.png")
t4=Canvas(root,width=149,height=149,highlightthickness=0)
t4.create_image(0,0,image=glv_pic[0],anchor='nw')
t4.place(x=915,y=300)
l.create_text(990,465,fill="white",text='Glove',font=('Comic Sans MS',15))
l.create_text(990,490,fill="white",text='Rs.5,200/-',font=('Gill Sans MT',10))
btn4=Button(root,text="Add To Cart",font=('Gill Sans MT',10,'bold'),command=lambda:(action(5200),cont()))
btn4.place(x=950,y=500)

# Run the main event loop
next()
root.mainloop()
