from tkinter import *
from tkinter import ttk
import sqlite3
import utility_functions as uf


class App():
    def __init__(self):
        root = Tk()

        frame1 = Frame(root)
        frame2 = Frame(root,relief=RAISED,borderwidth=1)   
        frame3 = Frame(root,relief=SUNKEN,borderwidth=1)
        frame4 = Frame(root,relief=RAISED,borderwidth=1)
        frame5 = Frame(root,relief=SUNKEN,borderwidth=1)
        frame5 = Frame(root,relief=RAISED,borderwidth=1) 

        frame1.pack(fill=X,side=TOP)
        frame2.pack(fill=X,side=TOP)
        frame3.pack(fill=X,side=TOP)       
        frame4.pack(side=TOP)
        frame5.pack(fill=X,side=TOP)


        lbName = Label(frame1,text='Name',anchor=W)
        lbName.pack(side=LEFT)
        etName = Entry(frame1)
        etName.pack(side=LEFT)

        lbType = Label(frame2,text='Type').pack(side=LEFT)
        j = IntVar()
        rbCanh = Radiobutton(frame2,text="Canh",value=1,variable=j).pack(side=LEFT)
        rbMan = Radiobutton(frame2,text="Man",value=2,variable=j).pack(side=LEFT)
        rbXao = Radiobutton(frame2,text="Xao",value=3,variable=j).pack(side=LEFT)
        rbTuDo = Radiobutton(frame2,text="Tu do",value=4,variable=j).pack(side=LEFT)
                
        lbDifficulty = Label(frame3,text='Difficulty').pack(side=LEFT)
        i = IntVar()
        rbEasy = Radiobutton(frame3,text="Easy",value=1,variable=i).pack(side=LEFT)
        rbIntermediate = Radiobutton(frame3,text="Intermediate",value=2,variable=i).pack(side=LEFT)
        rbHard = Radiobutton(frame3,text="Hard",value=3,variable=i).pack(side=LEFT)


        bAdd = Button(frame4,text='Add dish',command=lambda:self.addDish(etName.get(),j.get(),i.get()))
        bAdd.pack(side=LEFT)

        bUpdate = Button(frame4,text='Update dish',command=self.deletetree)
        bUpdate.pack(side=LEFT)


        ##################################################
        
        self.treeview = ttk.Treeview(frame5,columns=(1,2,3,4),show='headings',height='5')
        self.treeview.pack()

        self.treeview.heading(1,text='Name')
        self.treeview.heading(2,text='Age')
        self.treeview.heading(3,text='Email')
        self.treeview.heading(4,text='ID')

        self.loadtreeview()
                                                
        root.mainloop()

    def deletetree(self):
        self.treeview.delete(*self.treeview.get_children())
    def loadtreeview(self):
        path = 'D:/8570w/Python Projects/Foodapp/foodhunt.db'
        conn = sqlite3.connect(path)
        c = conn.cursor()

        sql = "SELECT * FROM dishes"
        c.execute(sql)
        rows = c.fetchall()
        total = c.rowcount

        for row in rows:
            self.treeview.insert('',END,values=row)


    def addDish(self,name,j,i):
        self.deletetree()
        name = name
        #type
        switcher = {
            1: "canh",
            2: "man",
            3: "xao",
            4: "tu do"
        }
        type = switcher.get(j,"Invalid type")
        #Difficulty
        switcher = {
            1: "easy",
            2: "intermediate",
            3: "hard"
        }
        difficulty = switcher.get(j,"Invalid difficulty")
        list = [name,type,difficulty]

        print("{}\t{}\t{}".format(name,type,difficulty))

        path = 'D:/8570w/Python Projects/Foodapp/foodhunt.db'
        conn = sqlite3.connect(path)
        c = conn.cursor()

        c.execute("""INSERT INTO dishes(name,type,difficulty)
                VALUES (?,?,?)""",list)

        conn.commit()

        conn.close()
        self.loadtreeview()


app = App()
