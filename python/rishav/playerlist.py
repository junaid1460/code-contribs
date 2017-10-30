import sqlite3 as sql

import tkinter as tk
from tkinter.ttk import *
from tkinter import *


class App(tk.Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        # self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('id', 'name', 'number', 'team')
        tv.heading('id', text='ID')
        tv.column('id', anchor='center', width=100)
        tv.heading('name', text='Name')
        tv.column('name', anchor='center', width=100)
        tv.heading('number', text='Number')
        tv.column('number', anchor='center', width=100)
        tv.heading('team', text='Team')
        tv.column('team', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

  

connection = sql.connect("localdb")
cursor = connection.cursor()
res = cursor.execute("select * from Player")
data = res.fetchall()
window = tk.Tk()
window.geometry("600x500")
app = App(window)
for i in data:
    app.treeview.insert('', 'end', text = str(hash(i)) ,values=i)
window.mainloop()
