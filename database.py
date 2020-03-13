#RESOURCES
#https://inloop.github.io/sqlite-viewer/
#https://pythontic.com/database/sqlite/alter%20table alter a table using sql_master !!!
#https://pythontic.com/database/sqlite/get%20tables%20and%20indexes Retrieve List Of Tables, Indices And The Associated SQL Statements
#https://stackoverflow.com/questions/18014894/list-the-tables-of-the-database
#https://stackoverflow.com/questions/11996394/is-there-a-way-to-get-a-schema-of-a-database-from-within-python
#https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api
#https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite/38854129

  

#IMPORTS
import sqlite3
from tkinter import *

#INTRO
path = 'foodhunt.db'
conn = sqlite3.connect(path)
c = conn.cursor()

#FUNCTIONS
createtable_dishes = """CREATE TABLE IF NOT EXISTS dishes (
                    dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name text unique,
                    category text,
                    price int,
                    frequency int,
                    note text,
                    instruction text,
                    prep text,
                    calories text) """
createtable_eatout = """CREATE TABLE IF NOT EXISTS eatout (
                    eatout_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name text,
                    restaurant text) """
def createTable(command):
    c.execute(command)

def insertData1():
    c.execute("""INSERT OR IGNORE INTO dishes(name,category,prep) 
            VALUES ('dau que xao thit bo','xao','trung binh')""")

def insertData_dishes():
    root = Tk()
    root.title = "Insert Dish"

    framel = Frame(root)
    framel.pack(side=LEFT)
    framer = Frame(root)
    framer.pack(side=LEFT)

    lbName = Label(framel,text='Name').pack(side=TOP)
    lbCategory = Label(framel,text='Category').pack(side=TOP)
    lbPrice = Label(framel,text='Price').pack(side=TOP)
    lbNote = Label(framel,text='Note').pack(side=TOP)
    lbInstruction = Label(framel,text='Instruction').pack(side=TOP)
    lbPrep = Label(framel,text='Prep').pack(side=TOP)
    lbCalories = Label(framel,text='Calories').pack(side=TOP)
    
    etName = Entry(framer,text='Name')
    etName.pack(side=TOP)
    etCategory = Entry(framer,text='Category')
    etCategory.pack(side=TOP)
    etPrice = Entry(framer,text='Price')
    etPrice.pack(side=TOP)
    etNote = Entry(framer,text='Note')
    etNote.pack(side=TOP)
    etInstruction = Entry(framer,text='Instruction')
    etInstruction.pack(side=TOP)
    etPrep = Entry(framer,text='Prep')
    etPrep.pack(side=TOP)
    etCalories = Entry(framer,text='Calories')
    etCalories.pack(side=TOP)

    def clearEntry():
        etName.delete(0,END)
        etCategory.delete(0,END)
        etPrice.delete(0,END)
        etNote.delete(0,END)
        etInstruction.delete(0,END)
        etPrep.delete(0,END)
        etCalories.delete(0,END)
    bClear = Button(framel,text='Clear',command=clearEntry)
    bClear.pack(side=TOP)

    def addDish():
        cmd = """INSERT OR IGNORE INTO dishes(name,category,price,note,instruction,prep,calories,frequency) 
                 VALUES (?,?,?,?,?,?,?,?)"""
        args = (etName.get(),etCategory.get(),etPrice.get(),etNote.get(),
                etInstruction.get(),etPrep.get(),etCalories.get(),0)
        c.execute(cmd,args)
        

    bAdd = Button(framer,text='Add',command=addDish)
    bAdd.pack(side=TOP)




    
    #########################
    datatable = Tk()
    datatable.title = 'Dish table'
    text = Text(datatable)
    text.pack()

    c.execute("select * from dishes")
    result = c.fetchall()
    here = ''
    for row in result:
        here += str(result) + "\n"

    text.insert(INSERT,here)


    datatable.mainloop()

    #########################

    root.mainloop()




def displayData():
    root = Tk()
    root.title = 'Display Data From'

    frame1 = Frame(root)
    frame1.pack(side=TOP)
    frame2 = Frame(root)
    frame2.pack(side=TOP)
    frame3 = Frame(root)
    frame3.pack(side=TOP)

    lbTable = Label(frame1,text='Table')
    lbTable.pack(side=TOP)
    etTable = Entry(frame1)
    etTable.pack(side=TOP)

    lbCustom = Label(frame2,text='Custom query')
    lbCustom.pack(side=TOP)
    etCustom = Entry(frame2)
    etCustom.pack(side=TOP)

    bExecute = Button(frame3,text='Execute',command = lambda : executeRowQuery(etTable.get(),etCustom.get()) )
    bExecute.pack()
    


    root.mainloop()

def executeRowQuery(strtable,strcustom):
    if strtable != "":
        command = 'select * from ' + strtable
        c.execute(command)
        list = c.fetchall()
        for row in list:
            print(row)
    else:
        if strcustom != "":
            command = strtable
            c.execute(command)
            list = c.fetchall()
            for row in list:
                print(row)

def executeVoidQuery():
    def onclick():
        c.execute(text.get("1.0",END))
        root.destroy()

    root = Tk()
    text = Text(root)
    text.pack(side=TOP)
    button = Button(root,text="Execute",command=onclick)
    button.pack(side=TOP)
    root.mainloop()

def sqlitemaster():
    def querysql_master_table():
        tableQuery = "select * from sqlite_master"
        c.execute(tableQuery)
        tableList = c.fetchall()
        print()
        return tableList

    # Print the updated listed of tables
    def printListOfTablesinsql_master(tableList):
        for table in tableList:
            print("Database Object Type: %s"%(table[0]))
            #print("Name of the database object: %s"%(table[1]))
            print("Name of the table: %s"%(table[2]))
            #print("Root page: %s"%(table[3]))
            print("SQL Statement: %s"%(table[4]))
            print()

    
    #print(querysql_master_table())
    printListOfTablesinsql_master(querysql_master_table())

def tableColumns(table):
    #c.execute('select * from ' + table)
    #method 1
    #names = list(map(lambda x: x[0], c.description)) 

    #method 2
    #names = [description[0] for description in c.description]
    #print(names)

    #method 3
    for row in c.execute("PRAGMA table_info("+table+")").fetchall():
        print(row)



 


createTable(createtable_dishes)
#insertData1()
#displayData()
c.execute("DELETE FROM dishes WHERE frequency is null")
executeRowQuery('dishes','')
#sqlitemaster()
tableColumns('dishes')
#executeVoidQuery()
#insertData_dishes()



#DON'T TOUCH
conn.commit()
conn.close()
