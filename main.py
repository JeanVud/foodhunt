from tkinter import *
import utility_functions as uf

root = Tk()


width = 1000
height = 500

def hello():
    print("hello!")
# ROOT SPECS
root.title('Food Hunt')
#root.geometry('%dx%d+%d+%d'%(width,height,250,180))

lbName = Label(root,text='Name').grid(row=0)
etName = Entry(root)
etName.grid(row=0,column=1,columnspan=3)

lbType = Label(root,text='Type').grid(row=1)
j = IntVar()
rbCanh = Radiobutton(root,text="Canh",value=1,variable=j).grid(row=1,column=1)
rbMan = Radiobutton(root,text="Man",value=2,variable=j).grid(row=1,column=2)
rbXao = Radiobutton(root,text="Xao",value=3,variable=j).grid(row=1,column=3)
rbTuDo = Radiobutton(root,text="Tu do",value=4,variable=j).grid(row=1,column=4)

lbDifficulty = Label(root,text='Difficulty').grid(row=2)
i = IntVar()
rbEasy = Radiobutton(root,text="Easy",value=1,variable=i).grid(row=2,column=1)
rbIntermediate = Radiobutton(root,text="Intermediate",value=2,variable=i).grid(row=2,column=2)
rbHard = Radiobutton(root,text="Hard",value=3,variable=i).grid(row=2,column=3)


bAdd = Button(root,text='Add dish',command=lambda:uf.addDish(etName.get(),j.get(),i.get())).grid(row=3,columnspan=4)



root.mainloop()
