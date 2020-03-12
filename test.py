from tkinter import *

root = Tk()


e = Entry(root)
e.pack()

def printResult(text):
    temp = Label(root, text=text).pack()

button = Button(root,text='click me',
command=lambda: printResult(e.get()) )
button.pack()

root.mainloop()

####################
import sqlite3

path = 'D:/8570w/Python Projects/Foodapp/foodhunt.db'
conn = sqlite3.connect(path)
c = conn.cursor()

#c.execute("delete  from dishes where difficulty='Invalid difficulty'")
c.execute("select * from dishes")

list = c.fetchall()
for row in list:
    print(row)

conn.commit()

conn.close()
