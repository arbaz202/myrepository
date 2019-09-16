from sqlite3 import *
from tkinter import *
from tkinter import ttk

from tkinter import messagebox
from PIL import Image,ImageTk
class Login:
    def __init__(sf):
        sf.c=connect("mydata.db")
        sf.cur=sf.c.cursor()
        try:
            sf.cur.execute("create table staff(user varchar(50),passw varchar(50))")
        except:
            pass
        sf.scr=Tk(className="Pizza Management System")
        sf.scr.state('zoomed')
        sf.scr.geometry('1280x840+400+400')

        

        sf.f=Frame(sf.scr,bg="steelblue")
        sf.f.pack(fill=BOTH,expand=1)
          
        
        sf.l=Label(sf.f,bg='steelblue',fg='white',font=('times',40,'italic'),text='Pizza Mania')
        sf.l.place(x=0,y=10)
        sf.l=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='user name')
        sf.l.place(x=0,y=110)
        sf.user=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'))
        sf.user.place(x=200,y=110)
        sf.l1=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='password')
        sf.l1.place(x=0,y=170)
        sf.passw=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'),show='*')
        sf.passw.place(x=200,y=170)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',25,'bold'),text='Order')
        sf.l2.place(x=10,y=400)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Pizza')
        sf.l2.place(x=10,y=450)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Sides')
        sf.l2.place(x=10,y=500)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Meals')
        sf.l2.place(x=10,y=550)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Order')
        sf.l2.place(x=10,y=600)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',25,'bold'),text='PizzaMania in India')
        sf.l2.place(x=250,y=400)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Contact us at:')
        sf.l2.place(x=250,y=450)
        sf.l21=Label(sf.f,bg='steelblue',fg='white',font=('times',20),text='0522 226518')
        sf.l21.place(x=250,y=500)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',25,'bold'),text='Order Pizza IN')
        sf.l2.place(x=650,y=400)
        
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Mumbai')
        sf.l2.place(x=650,y=450)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Delhi')
        sf.l2.place(x=650,y=500)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Agra')
        sf.l2.place(x=650,y=550)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Lucknow')
        sf.l2.place(x=650,y=600)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Your city')
        sf.l2.place(x=650,y=650)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',25,'bold'),text='Connect With Pizza Mania')
        sf.l2.place(x=950,y=400)
        sf.l2=Button(sf.f,bg='steelblue',fg='white',font=('times',15,'bold'),text='Give us \nyour valuable feedback',command=sf.feedback)
        sf.l2.place(x=950,y=450)

        sf.l3 =Text(sf.f,bg='white',bd=10,fg='black', width = 40, height = 10, font = ('Arial', 20,'bold','italic'), padx=5, pady=5)
        sf.l3.place(x=700,y=10)
        sf.l3.configure(state='normal')
        sf.l3.insert('end', 'Welcome to PizzaMania.Order a delicious pizza on the go, anywhere, anytime',
                     '\nPizza Hut is happy to assist you with your home delivery.',
                     '\nEvery time you order, you get a hot and fresh pizza',
                     '\ndelivered at your doorstep in less than thirty minutes.',
                     '\nT&C Apply.Hurry up and place your order now.')
        
        sf.l3.configure(state='disabled',relief=RIDGE)

        
        
        sf.b=Button(sf.f,text="submit",bg='blue',fg='white',font=('times',20,'bold'),command=lambda :sf.result("login"))
        sf.b.place(x=50,y=230)
        sf.b1=Button(sf.f,text="register",bg='green',fg='white',font=('times',20,'bold'),command=sf.register)
        sf.b1.place(x=300,y=230)
        sf.scr.mainloop()
    def register(sf):
        try:
            sf.scr.destroy()
        except:
            try:
                sf.scr1.destroy()
            except:
                pass
        sf.scr1=Tk(className="Pizza Management System Register")
        sf.scr1.state('zoomed')
        sf.scr1.geometry('1280x840+400+400')

        sf.f=Frame(sf.scr1,bg="steelblue")
        sf.f.pack(fill=BOTH,expand=1)
        sf.l=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='user name')
        sf.l.grid(row=10,column=0)
        sf.user=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'))
        sf.user.grid(row=10,column=1)
        sf.l1=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='password')
        sf.l1.grid(row=12,column=0)
        sf.passw=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'),show='*')
        sf.passw.grid(row=12,column=1)
        sf.l2=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='retype password')
        sf.l2.grid(row=14,column=0)
        sf.passw1=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'),show='*')
        sf.passw1.grid(row=14,column=1)
        sf.b=Button(sf.f,text="submit",bg='yellow',fg='white',font=('times',20,'bold'),command=lambda :sf.result("register"))
        sf.b.grid(row=16,column=0)
        sf.b1=Button(sf.f,text="clear",bg='red',fg='white',font=('times',20,'bold'))
        sf.b6=Button(sf.f,text="Login",bg='green',fg='white',font=('times',20,'bold'),command=lambda:sf.logout())
        sf.b1.grid(row=16,column=1)
        sf.b6.grid(row=16,column=3)
        sf.scr1.mainloop()
    
        
    def result(sf,val):
        if val=="login":
            try:
                sf.username=sf.user.get()
                sf.passd=sf.passw.get()
                sf.scr.destroy()
                x=sf.cur.execute("select count(*) from staff where user=%r and passw=%r"%(sf.username,sf.passd))
                if list(x)[0][0]==0:
                    sf.__init__()
                else:
                    sf.scr12=Tk(className="menu")
                    sf.scr12.state('zoomed')

                    #scrollbar =Scrollbar(sf.scr12)
                    #scrollbar.pack(side = RIGHT, fill=Y)
                    
                    

                    
                    sf.frame_header = Frame(sf.scr12, bg="steelblue", relief = RIDGE)
                    sf.frame_header.pack(fill=BOTH,expand=1)
                    
                    sf.mi = PhotoImage(file="pizza_trad_pepperonibeef (1).png")
                    sf.tmi=sf.mi.subsample(2,2)
                    sf.b1=Label(sf.frame_header, image= sf.mi).grid(row=0, column=0, rowspan = 1, columnspan=1)
                    sf.b5=Label(sf.frame_header, text='Pizza Mania',bg='red',fg='white',font=('times',20,'bold'),
                                 padx = 30, pady=10).place(x=0, y=10)
                    
                    
                    
                    
                    sf.scr12.geometry('1280x840+400+400')
                    
                    sf.b1=Button(sf.frame_header,text="Pizza",bg='red',fg='white',font=('times',20,'bold'), padx = 30, pady=10)
                    sf.b1.place(x=0, y=100)
                    sf.b1.config(command=sf.pizza)
                    
                    sf.b2=Button(sf.frame_header,text="Side",bg='red',fg='white',font=('times',20,'bold'),padx = 30, pady=10)
                    sf.b2.place(x=0, y=200)
                    sf.b2.config(command=sf.sides)
                    sf.b27=Button(sf.frame_header,text="Desserts",bg='red',fg='white',font=('times',20,'bold'),padx = 30, pady=10)
                    sf.b27.place(x=0, y=300)
                    sf.b27.config(command=sf.dessert)
                    sf.b29=Button(sf.frame_header,text="Drinks",bg='red',fg='white',font=('times',20,'bold'),padx = 30, pady=10)
                    sf.b29.place(x=0, y=400)
                    sf.b29.config(command=sf.drink)
                    sf.b3=Button(sf.frame_header,text="Burger",bg='red',fg='white',font=('times',20,'bold'),padx = 30, pady=10)
                    sf.b3.place(x=0, y=500)
                    sf.b3.config(command=sf.offer)

                    
                    sf.b31=Button(sf.frame_header,text="Start your delivery",bg='blue',fg='white',font=('times',20,'bold'),padx = 60, pady=10)
                    sf.b31.place(x=0, y=600)
                    sf.b31.config(command=sf.location)
                    sf.b32=Button(sf.frame_header,text="Home",bg='red',fg='white',font=('times',20,'bold'),command=lambda :sf.logout())
                    sf.b32.place(relx = 1.0, x=-5, y = 5, anchor = 'ne')
    

                                                           
            except:
                pass
   
        
        elif val=='register':
            if sf.passw.get()==sf.passw1.get():
                x=sf.cur.execute("select count(*) from staff where user=%r"%(sf.user.get()))
                if list(x)[0][0]!=0:
                    messagebox.showinfo("pizza","username allready exists")
                    sf.register()
                else:
                    sf.cur.execute("insert into staff values(%r,%r)"%(sf.user.get(),sf.passw.get()))
                    sf.c.commit()
                try:
                    sf.scr1.destroy()
                except:
                    pass
                sf.__init__()
            else:
                try:
                    sf.scr1.destroy()
                except:
                    pass
                sf.register()
                sf.scr11.mainloop()

    def pizza(sf):
        
        sf.scr2=Tk(className="Pizza")
        sf.scr2.state('zoomed')
                    
                    
        sf.frame_header2 = Frame(sf.scr2, bg="blue", relief = RIDGE)
        sf.frame_header2.pack()
        sf.b5=Label(sf.frame_header2, text='Pizza Mania',bg='red',fg='white',font=('times',20,'bold'),
                    padx = 30, pady=10).place(x=0, y=10)
                    
                    
        sf.f=Frame(sf.scr2,bg="steelblue")
        sf.f.pack(fill=BOTH,expand=1)
        sf.scr2.geometry('1480x840+400+400')
        
        sf.bu=Button(sf.f,text="Home",bg='red',fg='white',font=('times',20,'bold'),command=lambda :sf.logout())
        sf.bu.place(relx = 1.0, x=-5, y = 5, anchor = 'ne')          
        sf.b12=Button(sf.f,text="Vegetarian",bg='red',fg='white',font=('times',20,'bold'), padx = 60, pady=10)
        sf.b12.place(x=127, y=100)
        sf.b12.config(command=sf.pizza)
        sf.b22=Label(sf.f,text="Veggie Italiano",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=250)
        sf.b23=Label(sf.f,text="Rs 500",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=250)
        sf.b33=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=250)
        sf.b25=Label(sf.f,text="Veggie Supreme",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=350)
        sf.b24=Label(sf.f,text="Rs 500",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=350)
        sf.b34=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=350)

        sf.b26=Label(sf.f,text="Veg Exotica",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=450)
        sf.b27=Label(sf.f,text="Rs 500",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=450)
        sf.b30=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=450)

        sf.b28=Label(sf.f,text="Paneer Soya \nSupreme",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=550)
        sf.b29=Label(sf.f,text="Rs 500",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=550)
        sf.b31=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=550)

        sf.b32=Label(sf.f,text="Chicken Supreme",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=250)
        sf.b36=Label(sf.f,text="Rs 600",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=250)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=250)

        sf.b32=Label(sf.f,text="Chicken Exotica",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=350)
        sf.b36=Label(sf.f,text="Rs 600",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=350)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=350)

        sf.b32=Label(sf.f,text="Chicken Italiano",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=450)
        sf.b36=Label(sf.f,text="Rs 500",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=450)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=450)

        sf.b32=Label(sf.f,text="Triple Chicken Feasr",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=550)
        sf.b36=Label(sf.f,text="Rs 500",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=550)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=550)
        sf.b38=Button(sf.f,text="Non Vegeterian",bg='blue',fg='white',font=('times',20,'bold'),padx = 60, pady=10).place(x=830, y=100)
    

        sf.scr12.destroy()
        
        sf.scr2.mainloop()



    def dessert(sf):
        
                 
        sf.scr26=Tk(className="Desert")
        sf.scr26.state('zoomed')
                    
                    
        
                    
                    
        sf.f=Frame(sf.scr26,bg="steelblue")
        sf.f.pack(fill=BOTH,expand=1)
        sf.scr26.geometry('1480x840+400+400')
        
        sf.bu=Button(sf.f,text="Home",bg='red',fg='white',font=('times',20,'bold'),command=lambda :sf.logout())
        sf.bu.place(relx = 1.0, x=-5, y = 5, anchor = 'ne')          
        sf.b12=Label(sf.f,text="Choco Truffle \nCake",bg='steelblue',fg='black',font=('arial',20))
        sf.b12.place(x=10, y=100)
        sf.b41=Label(sf.f,text="Rs 30",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=100)
        sf.b42=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=100)
    

        sf.b22=Label(sf.f,text="Choco Vacano \nCake",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=250)
        sf.b23=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=250)
        sf.b33=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=250)

        sf.scr12.destroy()
        
        sf.scr26.mainloop()



    def sides(sf):
        
        sf.scr24=Tk(className="Sides")
        sf.scr24.state('zoomed')
                    
                    
        sf.frame_header2 = Frame(sf.scr24, bg="blue", relief = RIDGE)
        sf.frame_header2.pack()
        sf.b5=Label(sf.frame_header2, text='Pizza Mania',bg='red',fg='white',font=('times',20,'bold'),
                    padx = 30, pady=10).place(x=5, y=10)
                    
                    
        sf.f=Frame(sf.scr24,bg="steelblue")
        sf.f.pack(fill=BOTH,expand=1)
        sf.scr24.geometry('1480x840+400+400')
        
        sf.bu=Button(sf.f,text="Home",bg='red',fg='white',font=('times',20,'bold'),command=lambda :sf.logout())
        sf.bu.place(relx = 1.0, x=-5, y = 5, anchor = 'ne')          
        sf.b12=Button(sf.f,text="Vegetarian",bg='red',fg='white',font=('times',20,'bold'), padx = 60, pady=10)
        sf.b12.place(x=127, y=100)
        sf.b12.config(command=sf.pizza)
        sf.b22=Label(sf.f,text="Spanish Tomato \nVeg Pasta",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=250)
        sf.b23=Label(sf.f,text="Rs 200",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=250)
        sf.b33=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=250)
        sf.b25=Label(sf.f,text="Cheese Garlic \nbread",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=350)
        sf.b24=Label(sf.f,text="Rs 130",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=350)
        sf.b34=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=350)

        sf.b26=Label(sf.f,text="Tandoori Pocket \nPaneer",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=450)
        sf.b27=Label(sf.f,text="Rs 90",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=450)
        sf.b30=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=450)

        sf.b28=Label(sf.f,text="Garlic Bread \nSpicy Supreme",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=550)
        sf.b29=Label(sf.f,text="Rs 180",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=550)
        sf.b31=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=550)

        sf.b32=Label(sf.f,text="Spanish Tomato \nNon Veg Pasta",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=250)
        sf.b36=Label(sf.f,text="Rs 160",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=250)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=250)

        sf.b32=Label(sf.f,text="Spicy Backed \nChicken Wings",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=350)
        sf.b36=Label(sf.f,text="Rs 160",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=350)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=350)

        sf.b32=Label(sf.f,text="Chicken Rosted",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=450)
        sf.b36=Label(sf.f,text="Rs 140",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=450)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=450)

        sf.b32=Label(sf.f,text="Tandoori Pocket \nchicken",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=550)
        sf.b36=Label(sf.f,text="Rs 90",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=550)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=550)
        sf.b38=Button(sf.f,text="Non Vegeterian",bg='blue',fg='white',font=('times',20,'bold'),padx = 60, pady=10).place(x=830, y=100)
    

        sf.scr12.destroy()
        
        sf.scr24.mainloop()



    def drink(sf):
                 
        sf.scr25=Tk(className="Drinks")
        sf.scr25.state('zoomed')
                    
                    
    
                    
        sf.f=Frame(sf.scr25,bg="steelblue")
        sf.f.pack(fill=BOTH,expand=1)
        sf.scr25.geometry('1480x840+400+400')
        
        sf.bu=Button(sf.f,text="Home",bg='red',fg='white',font=('times',20,'bold'),command=lambda :sf.logout())
        sf.bu.place(relx = 1.0, x=-5, y = 5, anchor = 'ne')          
        sf.b12=Label(sf.f,text="Mineral Water \nBottle",bg='steelblue',fg='black',font=('arial',20))
        sf.b12.place(x=10, y=100)
        sf.b41=Label(sf.f,text="Rs 30",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=100)
        sf.b42=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=100)
    

        sf.b22=Label(sf.f,text="Sprite",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=250)
        sf.b23=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=250)
        sf.b33=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=250)
        sf.b25=Label(sf.f,text="7Up",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=350)
        sf.b24=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=350)
        sf.b34=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=350)

        sf.b26=Label(sf.f,text="Thums up",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=450)
        sf.b27=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=450)
        sf.b30=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=450)

        sf.b28=Label(sf.f,text="Mirenda",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=550)
        sf.b29=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=550)
        sf.b31=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=550)

        sf.b32=Label(sf.f,text="Appy fiz",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=250)
        sf.b36=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=250)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=250)

        sf.b32=Label(sf.f,text="Maaza",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=350)
        sf.b36=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=350)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=350)

        sf.b32=Label(sf.f,text="Dew",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=450)
        sf.b36=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=450)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=450)

        sf.b32=Label(sf.f,text="Pepsi",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=550)
        sf.b36=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=550)
        sf.b37=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=550)
        sf.b38=Label(sf.f,text="Real juice",bg='steelblue',fg='black',font=('arial',20)).place(x=700, y=100)
        sf.b39=Label(sf.f,text="Rs 70",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=1000, y=100)
        sf.b40=Button(sf.f,text="Add to cart",bg='blue',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=1150, y=100)
    

        sf.scr12.destroy()
        
        sf.scr25.mainloop()






        

    def location(sf):
        sf.cn=connect("mydata.db")
        sf.curs=sf.cn.cursor()
        try:
            sf.scr2.destroy()
        except:
            
            try:
                sf.scr12.destroy()
                
            except:
                try:
                    sf.curs.execute("create table location(city varchar(50),street varchar(50))")
                except:
                    pass
        sf.scr3=Tk(className="Pizza Management System")
        sf.scr3.state('zoomed')
        sf.scr3.geometry('1280x840+400+400')
        

        

        sf.f=Frame(sf.scr3,bg="steelblue")
        sf.f.pack(fill=BOTH,expand=1)

        sf.l56=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Please re-verify the details \nand then click on confirm to \nsuccesfully place order')
        sf.l56.grid(row=0,column=4, rowspan=2,columnspan=4)
       
        sf.l5=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Name')
        sf.l5.grid(row=0,column=0)
        sf.user1=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'), relief='raised')
        sf.user1.grid(row=1,column=1)
        sf.l6=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text=' Mobile')
        sf.l6.grid(row=2,column=0)
        sf.user=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'), relief='raised')
        sf.user.grid(row=3,column=1)
        




        
        sf.l1=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='   pin code')
        sf.l1.grid(row=4,column=0)
        sf.lmob=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='   Email id')
        sf.lmob.grid(row=6,column=0)
        sf.pin=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'), relief='raised',show='*')
        sf.pin.grid(row=5,column=1)
        sf.mob=Entry(sf.f,bg='white',fg='black',font=('times',20,'bold'), relief='raised')
        sf.mob.grid(row=7,column=1)

        sf.piz=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='Pizza')
        sf.piz.grid(row=8,column=0)
        pizza = StringVar()

        sf.combobox =ttk.Combobox(sf.f, textvariable = pizza,width=35, height=5)
        sf.combobox.grid(row=9,column=1)
        sf.combobox.config(values = ('Veggie Italiano', 'Veggie Supreme', 'Veg Exotica', 'Paneer Soya Supreme','Chicken Italiano',
                                     'Chicken Supreme', 'Chicken Exotica', 'Chicken Soya Supreme' ))

        sf.lad=Label(sf.f,bg='steelblue',fg='white',font=('times',20,'bold'),text='   Address')
        sf.lad.grid(row=10,column=0)

        sf.lbl=Label(sf.f,bg='steelblue',bd=5,fg='white',font=('times',20,'bold'),text=' ')
        sf.lbl.grid(row=13,column=0)
        sf.l32 =Text(sf.f,bg='white',fg='black', width = 25, height = 4, font = ('Arial', 20,'bold','italic'), padx=5, pady=5)
        sf.l32.grid(row=11,column=1, columnspan=3)
        sf.l32.configure(state='normal', relief='raised')


       
        #sf.l32.configure(state='disabled')
        sf.l33=StringVar()
        sf.l33 =Text(sf.f,bg='white',bd=10,fg='black', width = 30, height = 10, font = ('Arial', 20,'bold','italic'))
        sf.l33.grid(row=2,column=15, rowspan=8, columnspan=12,sticky='N')
        sf.l33.configure(state='normal', relief=RIDGE)
        sf.bt=Button(sf.l33,text="clear",bg='red',fg='white',font=('times',20,'bold'),command=lambda :sf.reset())
        sf.l33.window_create('insert',window=sf.bt)
        sf.bt.place(relx = 1.0, x=-5, y = 5, anchor = 'ne')
        sf.btn=Button(sf.l33,text="Confirm",bg='red',fg='white',font=('times',15,'bold'),command=lambda :sf.payment())
        sf.l33.window_create('insert',window=sf.btn)
        sf.btn.place(relx = 1.0, x=-5, y = 80, anchor = 'ne')


       
        

    


   



        
        sf.b=Button(sf.f,text="submit",bg='green',fg='white',font=('times',20,'bold'),command=lambda :sf.confirm())
        sf.b8=Button(sf.f,text="clear",bg='red',fg='white',font=('times',20,'bold'),command=lambda :sf.clr())
        sf.b9=Button(sf.f,text="Home",bg='green',fg='white',font=('times',20,'bold'),command=lambda :sf.logout())
        sf.b.grid(row=15,column=0)
        sf.b8.grid(row=15,column=1)
        sf.b9.place(relx = 1.0, x=-5, y = 5, anchor = 'ne')
        sf.l33.configure(state='disabled')
        
        
        sf.scr3.mainloop()

    def digit(inStr,acttyp):
        if acttype == '1':
            if not inStr.isdigit():
                return False
            return True
    def reset(sf):
        sf.l33.configure(state='normal')
        sf.l33.delete(1.0, 'end')
        sf.l33.configure(state='disabled')

        

   

    def confirm(sf):
        sf.l33.configure(state='normal')
        print('Name: {}'.format(sf.user1.get()))
        print('Mobile: {}'.format(sf.user.get()))
        print('Pin: {}'.format(sf.pin.get()))
        print('Email: {}'.format(sf.mob.get()))
        print('Pizza: {}'.format(sf.combobox.get()))
        print('Address: {}'.format(sf.l32.get(1.0, 'end')))
        sf.l33.insert(END, ('Name: {}'.format(sf.user1.get())))
        sf.l33.insert(END, ('\nMobile: {}'.format(sf.user.get())))
        sf.l33.insert(END, ('\nPin: {}'.format(sf.pin.get())))
        
        sf.l33.insert(END, ('\nEmail: {}'.format(sf.mob.get())))
        sf.l33.insert(END, ('\nPizza: {}'.format(sf.combobox.get())))
        sf.l33.insert(END, ('\nAddress: {}'.format(sf.l32.get(1.0, 'end'))))
        
        messagebox.showinfo("details","submitted")
        sf.l33.configure(state='disabled')
        
        

    def clr(sf):
        sf.l33.configure(state='normal')
        sf.user1.delete(0, 'end')
        sf.user.delete(0, 'end')
        sf.pin.delete(0, 'end')
        sf.mob.delete(0, 'end')
        sf.l32.delete(1.0, 'end')
        sf.combobox.delete(0, 'end')
        sf.l33.configure(state='disabled')



    
    def logout(sf):
        try:
            sf.scr1.destroy()
        except:
            try:
                sf.scr12.destroy()
                sf,scr2.destroy()
            except:
                try:
                    sf.scr2.destroy()
                    
                    
                except:
                    try:
                        sf.scr3.destroy()
                        
                    except:
                        try:
                           sf.scr24.destroy()
                        except :
                            try:
                                sf.scr25.destroy()
                            except:
                                try:
                                    sf.scr26.destroy()
                                except:
                                    try:
                                        sf.scr27.destroy()
                                    except:
                                        pass
        x=Login()
        
        
        
        sf.scr.mainloop()
    def feedb(sf):
        try:
            sf.scr1.destroy()
        except:
            try:
                sf.scr12.destroy()
                sf,scr2.destroy()
            except:
                try:
                    sf.scr2.destroy()
                    
                    
                except:
                    try:
                        sf.scr3.destroy()
                    except:
                        pass
        x=Feedback()
        
        
        
        sf.scr.mainloop()




    
        
    

    def payment(sf):

            
        
        sf.root1=Tk(className="Payment option")
        sf.frame_header5 = Frame(sf.root1, bg="#e1d8b9", relief = RIDGE)
        sf.frame_header5.pack()
        #sf.resizable(False, False)
        
        

        sf.style = ttk.Style()
        sf.style.configure('TFrame', background = '#e1d8b9')
        sf.style.configure('TButton', background = '#e1d8b9')
        sf.style.configure('TLabel', background = '#e1d8b9',font=('Arial',11))
        #sf.style.configure('Header.TLabel',font=('Arial',18,'bold'))
        
                    
        
        #sf.b1=Label(sf.frame_header5, image= sf.mi).grid(row=0, column=0, rowspan = 1, columnspan=1)
        sf.b5=Label(sf.frame_header5, text='Pizza \nMania', background = '#e1d8b9',font=('Arial',14), padx=12, pady=12).grid(row = 0, column = 0, rowspan = 1)
        sf.bs1=Label(sf.frame_header5, text = 'Thanks for Exploring!',background = '#e1d8b9',font=('Arial',18,'bold') ).grid(row = 0, column = 1)
        sf.bs2=Label(sf.frame_header5, wraplength = 300, text = ("Please enter your debit card"
                                          "or credit card no to confirm your order.Thanks you"), background = '#e1d8b9',font=('Arial',12)).grid(row = 1, column = 1)


        sf.frame_content = Frame(sf.root1, bg="#e1d8b9", relief = RIDGE)
        
        sf.frame_content.pack()

        sf.l11=Label(sf.frame_content, text = 'Card no:', background = '#e1d8b9',font=('Arial',11)).grid(row = 3, column = 0, padx = 5, sticky = 'sw')
        sf.l12=Label(sf.frame_content, text = 'Valid thru:', background = '#e1d8b9',font=('Arial',11)).grid(row = 5, column = 0, padx = 5, sticky = 'sw')
        sf.l13=Label(sf.frame_content, text = 'Cvv:', background = '#e1d8b9',font=('Arial',11)).grid(row = 7, column = 0, padx = 5, sticky = 'sw')
        sf.l14=Label(sf.frame_content, text = 'Name:', background = '#e1d8b9',font=('Arial',11)).grid(row = 1, column = 0, padx = 5, sticky = 'sw')
        
        sf.entry_name=Entry(sf.frame_content, width = 40, font = ('Arial', 10))
        sf.entry_cardno =Entry(sf.frame_content, width = 42, font = ('Arial', 10))
        sf.entry_doe =Entry(sf.frame_content, width = 42, font = ('Arial', 10))
        sf.entry_cvv =Entry(sf.frame_content, width = 42, font = ('Arial', 10))

        sf.check=Checkbutton(sf.frame_content,width = 5, text='Debit',background = '#e1d8b9')
        sf.check.grid(row = 0, column = 0, sticky = 'sw')
        sf.debit=StringVar()
        sf.debit.set('Debit')
        sf.check1=Checkbutton(sf.frame_content,width = 5, text='Credit',background = '#e1d8b9')
        sf.check1.grid(row = 0, column = 1, sticky = 'sw')
        sf.credit=StringVar()
        sf.credit.set('Credit')

        
        sf.entry_name.grid(row = 2, column = 0, padx = 5)
        sf.entry_cardno.grid(row = 4, column = 0, padx = 5)
        sf.entry_doe.grid(row = 6, column = 0, padx = 5, sticky = 'sw')
        sf.entry_cvv.grid(row = 8, column = 0, padx = 5, sticky = 'sw')
        
        sf.bs3=Button(sf.frame_content, text = 'Submit', background = '#e1d8b9',
                   command = sf.submit1).grid(row = 9, column = 0, padx = 5, pady = 5, sticky = 'e')
        sf.bs4=Button(sf.frame_content, text = 'Clear', background = '#e1d8b9',
                   command = sf.clear1).grid(row = 9, column = 1, padx = 5, pady = 5, sticky = 'w')
        sf.reset()

    def submit1(sf):
        print('Name: {}'.format(sf.entry_name.get()))
        print('Card No: {}'.format(sf.entry_cardno.get()))
        print('Doe: {}'.format(sf.entry_doe.get()))
        print('Debit: {}'.format(sf.debit.get()))
        print('Credit: {}'.format(sf.credit.get()))
        print('Cvv: {}'.format(sf.entry_cvv.get()))
        messagebox.showinfo("Order status","Order placed successfully.Thanks You")
        sf.clear1()
        
    
    def clear1(sf):
        sf.entry_name.delete(0, 'end')
        sf.entry_cardno.delete(0, 'end')
        sf.entry_doe.delete(0, 'end')
        #sf.debit.delete(0, 'end')
        #sf.credit.delete(0, 'end')
        sf.entry_cvv.delete(0, 'end')
        sf.root1.mainloop()






    def feedback(sf):
        sf.root=Tk(className="Explore Feedback")
        sf.frame_header5 = Frame(sf.root, bg="#e1d8b9", relief = RIDGE)
        sf.frame_header5.pack()
        #sf.resizable(False, False)
        
        

        sf.style = ttk.Style()
        sf.style.configure('TFrame', background = '#e1d8b9')
        sf.style.configure('TButton', background = '#e1d8b9')
        sf.style.configure('TLabel', background = '#e1d8b9',font=('Arial',11))
        #sf.style.configure('Header.TLabel',font=('Arial',18,'bold'))
        
                    
        sf.b5=Label(sf.frame_header5, text='Pizza \nMania', background = '#e1d8b9',font=('Arial',12), padx=7, pady=7).grid(row = 0, column = 0, rowspan = 1)
        sf.bs1=Label(sf.frame_header5, text = 'Thanks for Exploring!',background = '#e1d8b9',font=('Arial',18,'bold') ).grid(row = 0, column = 1)
        sf.bs2=Label(sf.frame_header5, wraplength = 300, text = ("We're glad you to chose Pizza Maniya."
                                          "Please tell us what you thought about the service of pizza.Thanks you"), background = '#e1d8b9',font=('Arial',11)).grid(row = 1, column = 1)


        sf.frame_content = Frame(sf.root, bg="#e1d8b9", relief = RIDGE)
        
        sf.frame_content.pack()

        sf.l11=Label(sf.frame_content, text = 'Name:', background = '#e1d8b9',font=('Arial',11)).grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        sf.l12=Label(sf.frame_content, text = 'Email:', background = '#e1d8b9',font=('Arial',11)).grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        sf.l13=Label(sf.frame_content, text = 'Comments:', background = '#e1d8b9',font=('Arial',11)).grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        
        sf.entry_name=Entry(sf.frame_content, width = 24, font = ('Arial', 10))
        sf.entry_email =Entry(sf.frame_content, width = 24, font = ('Arial', 10))
        sf.text_comments =Text(sf.frame_content, width = 50, height = 10, font = ('Arial', 10))
        
        sf.entry_name.grid(row = 1, column = 0, padx = 5)
        sf.entry_email.grid(row = 1, column = 1, padx = 5)
        sf.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
        
        sf.bs3=Button(sf.frame_content, text = 'Submit', background = '#e1d8b9',
                   command = sf.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        sf.bs4=Button(sf.frame_content, text = 'Clear', background = '#e1d8b9',
                   command = sf.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')



    
    def submit(sf):
        print('Name: {}'.format(sf.entry_name.get()))
        print('Email: {}'.format(sf.entry_email.get()))
        print('Comments: {}'.format(sf.text_comments.get(1.0, 'end')))
        messagebox.showinfo("Explore PizzaMania Feedback","Comments Submitted!")
        sf.clear()
        
    
    def clear(sf):
        sf.entry_name.delete(0, 'end')
        sf.entry_email.delete(0, 'end')
        sf.text_comments.delete(1.0, 'end')
        sf.root.mainloop()

    def offer(sf):
        sf.scr27=Tk(className="Desert")
        sf.scr27.state('zoomed')
                    
                    
        
                    
                    
        sf.f=Frame(sf.scr27,bg="steelblue")
        sf.f.pack(fill=BOTH,expand=1)
        sf.scr27.geometry('1480x840+400+400')
        
        sf.bu=Button(sf.f,text="Home",bg='red',fg='white',font=('times',20,'bold'),command=lambda :sf.logout())
        sf.bu.place(relx = 1.0, x=-5, y = 5, anchor = 'ne')          
        sf.b12=Label(sf.f,text="Cheese burger",bg='steelblue',fg='black',font=('arial',20))
        sf.b12.place(x=10, y=100)
        sf.b41=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=100)
        sf.b42=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=100)
    

        sf.b22=Label(sf.f,text="Chicken Burgur",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=250)
        sf.b23=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=250)
        sf.b33=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=250)

        sf.b24=Label(sf.f,text="Paneer Burgur ",bg='steelblue',fg='black',font=('arial',20)).place(x=10, y=400)
        sf.b25=Label(sf.f,text="Rs 60",bg='steel blue',fg='white',font=('arial',20,'bold')).place(x=250, y=400)
        sf.b39=Button(sf.f,text="Add to cart",bg='red',fg='white',font=('times',20,'bold'), relief='raised',command=sf.location).place(x=400, y=400)



        sf.scr12.destroy()
        
        sf.scr27.mainloop()
            

def main():
    x=Login()
    


if __name__ == "__main__": main()


    






        
        
        
