from tkinter import *
from tkinter import messagebox


jan = Tk()
jan.title('SilFlores - Login')
jan.geometry('600x300')
jan.configure(background='#FFB5C5')
jan.resizable(width=False, height=False)

LeftFrame = Frame(jan, width=200, height=300, bg='#FF6EB4', relief='raise')
LeftFrame.pack(side=LEFT)

jan.mainloop()
