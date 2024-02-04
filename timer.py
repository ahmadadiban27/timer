from tkinter import*
from tkinter import messagebox
timer = int()
#==========================win main==========================
win = Tk()
win.title('Timer')
win.geometry('400x500+400+200')
win.config(bg = '#A49DA9')

#==========================general==========================
def adout ():
    messagebox.showinfo('About', 'program name: Timer \nWritten by: Ahmad Adiban \n    Data : 12/20/2023')

def exit ():
    ask1= messagebox.askyesno('Exit', 'Are you sure:')
    if ask1 ==1:
        win.destroy()
#-----------------------------------------------------------------------------------------
b_about = Button(win , text = 'About' , font = ('Wide Latin' , 5) ,fg= "white" , bg = 'black', width= 6, command=adout)
b_exit = Button(win , text = 'Exit' , font = ('Wide Latin' , 5) ,fg= "white" , bg = 'black', width= 6 , command=exit)

b_about.place( x=20 , y = 450)
b_exit.place( x=300 , y = 450)

#==========================function==========================
def set():
   global timer
   if time_entry.get().isdigit():
       timer = int(time_entry.get())
       num_timer.config(text = timer)
       b_start.config(state=NORMAL)
       time_entry.delete(0 ,END)
   else:
       messagebox.showerror('Error', 'please enter the number ')
       time_entry.delete(0, END)
def start():
    global timer
    time_entry.config(state=DISABLED)
    if timer >0 :
        timer -=1
        num_timer.config(text=timer)
        num_timer.after(1000 , start)
    if timer==0:
        b_rset.config(state=NORMAL)
    b_set.config(state=DISABLED)
    b_start.config(state=DISABLED)

def rset():
    num_timer.config(text = '')
    time_entry.config(state=NORMAL)
    b_set.config(state=NORMAL)


#==========================widget==========================
num_timer = Label(win ,text ='' , font = ('titr' , 80), fg = 'red', bg = '#A49DA9' )
time_entry = Entry(win , font = ('papyrus' , 15,'bold'),bd =10  )
b_set = Button(win , text = 'set' , font = ('Wide Latin' , 10) ,fg= "white" , bg = 'black' , width= 10 , command=set)
b_start = Button(win , text = 'Start' ,state=DISABLED, font = ('Wide Latin' , 10) ,fg= "white" , bg = 'black', width= 10 , command= start)
b_rset = Button(win , text = 'Rset' , state=DISABLED,font = ('Wide Latin' , 10) ,fg= "white" , bg = 'black', width= 10 , command=rset )
#*********************************************************************************
num_timer.place( x=135 , y = 45)
time_entry.place( x=62 , y = 250)
time_entry.focus()
b_set.place( x=110 , y = 320)
b_start.place( x=110 , y = 360)
b_rset.place( x=110 , y = 400)
#***********************************************************************************

win.mainloop()