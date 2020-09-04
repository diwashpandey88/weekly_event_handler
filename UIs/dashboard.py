from tkinter import *
from eventui import *
from tkinter import ttk
from todoui import *

class Dashboard:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('400x300')
        self.window.title("Weekly Event Handler")

        self.text1 = Label(self.window, text="Weekly Event Handler", width='28', bg='#D8737F', font=('Arieal',20))
        self.text1.grid(columnspan = 4)

        self.text2 = Label(self.window, text="What do you want see?", width='25', font=('Arieal',15))
        self.text2.grid( columnspan=4)

        self.button1 = Button(self.window, text='Events', command=self.hello, height='4', width =8)
        self.button1.grid(row=2,column =1)

        self.button2 = Button(self.window, text='To-do', command=self.to_do, height = '4', width = 8)
        self.button2.grid(row=2, column= 2)




        self.window.mainloop()

    def hello(self):
        EventA()
    def to_do(self):
        Todoui()

Dashboard()