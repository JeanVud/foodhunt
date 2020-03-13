import sqlite3
from tkinter import *
#######################


def loadtree():
    path = 'D:/8570w/Python Projects/Foodapp/foodhunt.db'
    conn = sqlite3.connect(path)
    c = conn.cursor()
    
    sql = "SELECT * FROM dishes"
    c.execute(sql)
    rows = c.fetchall()
    total = c.rowcount

    for row in rows:
        treeview.insert('',END,values=row)

##########################

def datagrid(root):
    path = 'D:/8570w/Python Projects/Foodapp/foodhunt.db'
    conn = sqlite3.connect(path)
    c = conn.cursor()

    sql = "SELECT * FROM dishes"
    c.execute(sql)
    rows = c.fetchall()
    total = c.rowcount
    print('total data entries: '+str(total))

    frame = Frame(root)
    frame.pack(side=LEFT,padx=20)

    treeview = Treeview(frame,columns=(1,2,3),show='headings',height='5')
    treeview.pack()

    treeview.heading(1,text='Name')
    treeview.heading(2,text='Age')
    treeview.heading(3,text='Email')

    conn.commit()

    conn.close()


