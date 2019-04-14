'''
from Tkinter import *

master = Tk()
def callback():
    print "click"


f=Frame(master,height=32,width=64)
f.pack_propagate(0)
f.pack()

b=Button(master,text=" LED ON ",command=callback)

b.pack(fill=BOTH,expand=1)

#b.config(relief=SUNKEN)
mainloop()
'''

'''
from Tkinter import *

master = Tk()


var = IntVar()

c = Checkbutton(master, text="LED ON", variable=var)
c.pack()


v = IntVar()
c = Checkbutton(master, text=" LED ON ", variable=v)
c.pack()
c.var = v
mainloop()
'''
from time import sleep
import piface.pfio as pfio
pfio.init()

from Tkinter import *

class App:

 def __init__(self, master): 
    frame = Frame(master)
    frame.pack()
    Label(frame, text='Turn LED ON').grid(row=0, column=0)

    Label(frame, text='Turn LED OFF').grid(row=1, column=0)

    button = Button(frame, text='LED 0 ON', command=self.convert0)
    button.grid(row=2, columnspan=2)

    button = Button(frame, text='LED 1 ON', command=self.convert1)
    button.grid(row=3, columnspan=2)

    button = Button(frame, text='LED 2 ON', command=self.convert2)
    button.grid(row=4, columnspan=2)

    button = Button(frame, text='LED 3 ON', command=self.convert3)
    button.grid(row=5, columnspan=2)

    button = Button(frame, text='LED 4 ON', command=self.convert4)
    button.grid(row=6, columnspan=2)

    button = Button(frame, text='LED 5 ON', command=self.convert5)
    button.grid(row=7, columnspan=2)

    button = Button(frame, text='LED 6 ON', command=self.convert6)
    button.grid(row=8, columnspan=2)

    button = Button(frame, text='LED 7 ON', command=self.convert7)
    button.grid(row=9, columnspan=2)


 def convert0(self):
    if pfio.read_output():
        pfio.digital_write(0,0)
        print('LED 0 OFF')
        sleep(0.5)
    else:
        pfio.digital_write(0,1)
        print('LED 0 ON')
        sleep(0.5)

    def convert1(self):
     if pfio.read_output():
        pfio.digital_write(1,0)
        print('LED 1 OFF')
        sleep(0.5)
     else:
        pfio.digital_write(1,1)
        print('LED 1 ON')
        sleep(0.5)

 def convert2(self):
    print('LED 2 ON')
    pfio.digital_write(2,1) #turn on
    #sleep(0.5)
    #pfio.digital_write(2,0) #turn off
    #sleep(0.5)

 def convert3(self):
    print('LED 3 ON')
    pfio.digital_write(3,1) #turn on
    #sleep(0.5)
    #pfio.digital_write(3,0) #turn off
    #sleep(0.5)

 def convert4(self):
    print('LED 4 ON')
    pfio.digital_write(4,1) #turn on
    #sleep(0.5)
    #pfio.digital_write(4,0) #turn off
    #sleep(0.5)

 def convert5(self):
    print('LED 5 ON')
    pfio.digital_write(5,1) #turn on
    #sleep(0.5)
    #pfio.digital_write(5,0) #turn off
    #sleep(0.5)

 def convert6(self):
    print('LED 6 ON')
    pfio.digital_write(6,1) #turn on
    #sleep(0.5)
    #pfio.digital_write(6,0) #turn off
    #sleep(0.5)

 def convert7(self):
    print('LED 7 ON')
    pfio.digital_write(7,1) #turn on
    #sleep(0.5)
    #pfio.digital_write(7,0) #turn off
    #sleep(0.5)

root = Tk()
root.wm_title('LED on & off program')
app = App(root)
root.mainloop()
 
