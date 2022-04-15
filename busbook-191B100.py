from tkinter import *
import sqlite3
from tkcalendar import *
import tkinter.messagebox
from tkinter import messagebox
from PIL import Image, ImageTk
conn = sqlite3.connect('busbook.db')
curr = conn.cursor()

def home():
    global window
    window= Tk()
    window.geometry('1920x1080')
    load=Image.open('./unsplash.jpg')
    render=ImageTk.PhotoImage(load)
    img=Label(window,image=render).place(x=0,y=0)

    window.title("BUS BOOKING SYSTEM")
    Label(window, text="Bus booking").pack()

    Label(window,text="Terminus BUS Service", font=("Comic Sans MS Bold",60)).pack()
    Label(window,text="To Add Bus click on OPERATOR Button",font=("Comic Sans MS Bold",20)).place(x=150,y=420)

    Button(window,text="OPERATOR",font=("Comic Sans MS Bold",20),command=fun1).place(x=400,y=500)

    Label(window,text="To book bus click on PASSENGER Button ",font=("Comic Sans MS Bold",20)).place(x=780,y=420)
    Button(window,text="PASSENGER",font=("Comic Sans MS Bold",20),command=fun3).place(x=1000,y=500)


    Button(window,text="EXIT",font=("Comic Sans MS Bold",10),command= window.destroy).place(x=700,y=700)
    window.mainloop()

def fun7():
    window.destroy()
    home()

def showdata():
    curr.execute('SELECT * FROM Buses')#to fetch the data from the database
    ans = str(curr.fetchall())
    messagebox.showinfo("Alert",ans)
def add():
    arr = [(x.get(),y.get(),z.get(),p.get(),q.get())]
    try:
        curr.execute('CREATE TABLE Buses (num text,source text,des text,seat text,fare text)')
        curr.executemany('INSERT INTO Buses VALUES (?,?,?,?,?)',arr)
        conn.commit()
    except:
        curr.executemany("INSERT INTO Buses VALUES (?,?,?,?,?)",arr)
        conn.commit()
        messagebox.showinfo("INFO","BUS ADDED")
        # window.destroy()


def fun1():
    window.destroy()
    fun2()

def fun2():
    global window,x,y,z,p,q
    window=Tk()
    window.geometry('1920x1080')
    window.title("BUS BOOKING SYSTEM")
    Label(window,text="Welcome to operator portal",font=("Comic Sans MS Bold",55)).pack()
    Label(window,text="of Terminus BUS service",font=("Comic Sans MS Bold",55)).pack()
    x=StringVar()
    y=StringVar()
    z=StringVar()
    p=StringVar()
    q=StringVar()
    Button(window,text="Add BUS",font=("Comic Sans MS Bold",13),command=add).place(x=720,y=630)
    Button(window,text="Show data",font=("Comic Sans MS Bold",13),command=showdata).place(x=720,y=680)
    Label(window,text="BUS NUMBER",font=("Comic Sans MS Bold",20)).place(x=430,y=310)
    Entry(window,textvariable=x,font=("Comic Sans MS Bold",16)).place(x=630,y=315)
    Label(window,text="Source",font=("Comic Sans MS Bold",20)).place(x=430,y=370)
    Entry(window,textvariable=y,font=("Comic Sans MS Bold",16)).place(x=630,y=370)
    Label(window,text="Destination",font=("Comic Sans MS Bold",20)).place(x=430,y=430)
    Entry(window,textvariable=z,font=("Comic Sans MS Bold",16)).place(x=630,y=430)
    Label(window,text="Seat available",font=("Comic Sans MS Bold",20)).place(x=430,y=490)
    Entry(window,textvariable=p,font=("Comic Sans MS Bold",16)).place(x=630,y=490)
    Label(window,text="Fare",font=("Comic Sans MS Bold",20)).place(x=430,y=550)
    Entry(window,textvariable=q,font=("Comic Sans MS Bold",16)).place(x=630,y=550)
    Button(window,text="Home",font=("Comic Sans MS Bold",16),command=fun7).place(x=1200,y=700)


#BOOKING LOGS
def fun5():
    lst = (x.get(),y.get(),)
    curr.execute('SELECT * FROM Buses WHERE source = (?) AND des = (?)',lst)
    temp = curr.fetchall()
    if(len(temp)>0):
        messagebox.showinfo("INFO","BUS FOUND")
        window.destroy()
        fun6()
    else:
        messagebox.showinfo("INFO","No Buses Found")


def fun6():
    global window
    window = Tk()
    b = Application(window)
    window.geometry("1500x1080")
    window.resizable(False, False)

# PASSENGER LOGS
def fun3():
    window.destroy()
    fun4()
def grab_date():
        my_label.config(text=cal.get_date())
        bt=Button(window,text="get date", command=grab_date)

def checkifempty():
    if(x.get()=='' or y.get()==''):
        messagebox.showinfo("Error","Please Fill Boxes")
    else:
        fun5()

def fun4():
    global window,x,y,img
    window = Tk()
    window.geometry('1920x1080')
    window.title("BUS BOOKING SYSTEM")
    Label(window,text="Search buses to your Terminus",font=("Comic Sans MS Bold",50)).pack()
    canvas = Canvas(window, width = 1500, height = 1080)
    canvas.place(x=360,y=240)
    img = ImageTk.PhotoImage(Image.open("./bus img.png"))
    canvas.create_image(20, 20, anchor=NW, image=img)

    x=StringVar()
    y=StringVar()
    Label(window,text="Source",font=("Comic Sans MS Bold",20)).place(x=500,y=300)
    Entry(window,textvariable=x,font=("Comic Sans MS Bold",20)).place(x=600,y=300)
    Label(window,text="Destination",font=("Comic Sans MS Bold",20)).place(x=440,y=360)
    Entry(window,textvariable=y,font=("Comic Sans MS Bold",20)).place(x=600,y=360)
    cal=Calendar(window,selectmode="day",year=2020,month=12,day=14).place(x=620,y=500)
    Label(window,text="Journey date ",font=("Comic Sans MS Bold",20)).place(x=640,y=430)
    bt=Button(window,text="Search",font=("Comic Sans MS Bold",10),command=checkifempty).place(x=730,y=690)
    Button(window,text="Home",font=("Comic Sans MS Bold",16),command=fun7).place(x=1200,y=700)

    # Button(window,text="Show data",font=("Comic Sans MS Bold",10),command=showdata).place(x=720,y=730)
class Application:
    def __init__(self, windows):
        self.windows = windows
        # window.geometry("1920x1080")
        window.title("BUS BOOKING SYSTEM")


        self.left = Frame(windows, width=1920, height=1080,bg="#3572d4")
        self.left.place(x=0,y=0)

        self.wel=Label(window,text="Welcome to Bus Booking portal ",font=("Comic Sans MS Bold",50))
        self.wel.pack()

        self.ter=Label(window,text="of Terminus Bus Service ",font=("Comic Sans MS Bold",50))
        self.ter.pack()
        self.title = Label(self.left, text="BUS Booking", font=(
            'Verdana 30 bold'))
        self.title.place(x=500, y=250)

        self.n = Label(self.left, text="Passanger Name", font=(
            'Verdana 16 bold'))
        self.n.place(x=380, y=340)


        self.a = Label(self.left, text="Age", font=(
            'Verdana 16 bold'))
        self.a.place(x=400, y=380)


        self.gen = Label(self.left, text="Gender", font=(
            'Verdana 16 bold'))
        self.gen.place(x=400, y=420)

        self.loc = Label(self.left, text="From", font=(
            'Verdana 16 bold'))
        self.loc.place(x=400, y=460)

        self.t = Label(self.left, text="To", font=(
            'Verdana 16 bold'))
        self.t.place(x=400, y=500)
        self.s=Label(self.left,text="Seats you want to book",font=(
            'Verdana 16 bold'))
        self.s.place(x=300,y=590)

        self.phoneNumber = Label(self.left, text="Phone Number", font=(
            'Verdana 16 bold'))
        self.phoneNumber.place(x=400, y=540)

        self.nametextentry = Entry(self.left, width=30)
        self.nametextentry.place(x=600, y=340)

        self.agetextentry = Entry(self.left, width=30)
        self.agetextentry.place(x=600, y=380)

        self.gendertextentry = Entry(self.left, width=30)
        self.gendertextentry.place(x=600, y=420)

        self.fromtextentry = Entry(self.left, width=30)
        self.fromtextentry.place(x=600, y=460)

        self.totextentry = Entry(self.left, width=30)
        self.totextentry.place(x=600, y=500)

        self.phonetextentry = Entry(self.left, width=30)
        self.phonetextentry.place(x=600, y=540)
        self.num_seats = Entry(self.left,width=30)
        self.num_seats.place(x=600,y=600)
        self.submit = Button(self.left, text="Add Booking", width=20,
                             height=2, bg='white',font=("Comic Sans MS Bold",10), command=self.add_appointment)
        self.submit.place(x=500, y=650)
        Button(window,text="Home",font=("Comic Sans MS Bold",16),command=fun7).place(x=1200,y=700)
    def livecounter(self):
        lst = (self.value4,self.value5,)
        curr.execute('SELECT seat FROM Buses WHERE source = (?) AND des = (?)',lst)
        info = str(curr.fetchall())
        messagebox.showinfo("Alert","Seats Avalilable in Buses are "+info)
    def add_appointment(self):
        self.value_1 = self.nametextentry.get()
        self.value_2 = self.agetextentry.get()
        self.value_3 = self.gendertextentry.get()
        self.value4 = self.fromtextentry.get()
        self.value5 = self.totextentry.get()
        self.value6 = self.phonetextentry.get()
        self.value7 = self.num_seats.get()
        self.livecounter()

        if self.value_1 == '' or self.value_2 == '' or self.value_3 == '' or self.value4 == '' or self.value5 == '' or self.value7=='0':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            lst = (self.value7,)
            curr.execute('UPDATE Buses SET seat = seat - (?)',lst)
            conn.commit()
            tkinter.messagebox.showinfo(
                "Success", "Booking for " + str(self.value_1) + " has been created")
            self.box.insert(END, 'Booking fixed for ' +
                            str(self.value_1) + ' at ' + str(self.value5))





global window
window= Tk()
window.geometry('1920x1080')
load=Image.open('./unsplash.jpg')
render=ImageTk.PhotoImage(load)
img=Label(window,image=render).place(x=0,y=0)

window.title("BUS BOOKING SYSTEM")
Label(window, text="Bus booking").pack()

Label(window,text="Terminus BUS Service", font=("Comic Sans MS Bold",60)).pack()
Label(window,text="To Add Bus click on OPERATOR Button",font=("Comic Sans MS Bold",20)).place(x=150,y=420)

Button(window,text="OPERATOR",font=("Comic Sans MS Bold",20),command=fun1).place(x=400,y=500)

Label(window,text="To book bus click on PASSENGER Button ",font=("Comic Sans MS Bold",20)).place(x=780,y=420)
Button(window,text="PASSENGER",font=("Comic Sans MS Bold",20),command=fun3).place(x=1000,y=500)


Button(window,text="EXIT",font=("Comic Sans MS Bold",10),command= window.destroy).place(x=700,y=700)




window.mainloop()
