from tkinter import*
import tkinter
from tkinter import messagebox as tkMessageBox

class teamA:
    def __init__(self):
        window = Tk()
        window.title("Select your Team")
        window.minsize(width=300,height=300)
        juv = Button(window, text="Juventus", command=self.openR).place(x=20, y=50)
        mil = Button(window, text="A C Milan", command=self.openB).place(x=100, y=50)
        window.mainloop()

    def openR(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")
        import playerlist


    def openB(self):
        tkMessageBox.showinfo("prompt", "Opening Your Player List")
        import playerlist

teamA()