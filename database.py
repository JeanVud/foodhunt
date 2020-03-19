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
from tkinter import messagebox

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





def TkDatabase():

    def updateTextWithList(result):
        columns = []
        for row in c.execute("PRAGMA table_info(dishes)").fetchall():
            columns.append(row[1])
    
        text.delete('1.0', END)
        for row in result:
            for i in range(len(columns)):
                if str(row[i])!='' and str(row[i])!=str(0):
                    temp = str(columns[i] + 
                            ':\t\t'+
                            str(row[i])+'\n')
                    text.insert(END, temp)
    
            text.insert(END, '\n')
        text.see(END)
    def updateText():
        c.execute("select * from dishes")
        result = c.fetchall()
        updateTextWithList(result)
    def clearEntry():
        etIden.delete(0,END)
        etName.delete(0,END)
        etCategory.delete(0,END)
        etIngredients.delete(0,END)
        etPrice.delete(0,END)
        etNote.delete(0,END)
        etInstruction.delete(0,END)
        etPrep.delete(0,END)
        etCalories.delete(0,END)
    def addDish():
        #validation
        if etName.get().strip() == '':
            messagebox.showerror(message = 'Điền tên món vào')
            return
        
        cat = etCategory.get().strip()
        if cat!='' and (cat!='canh' and cat!='mặn' and cat!='xào' and cat!='free style' and cat!='uống'):
            if cat=='c' or cat=='m' or cat=='x' or cat=='f' or cat=='u':
                switcher = {
                    'c': 'canh',
                    'm': 'mặn',
                    'x': 'xào',
                    'f': 'free style',
                    'u': 'uống'                
                    }
                etCategory.delete(0,END)
                etCategory.insert(0,switcher.get(cat,'invalid'))
            else:
                messagebox.showerror(message = "Điền 'canh', 'mặn', 'xào', 'free style' hoặc 'uống'")
                return

        prep = etPrep.get().strip()
        if prep!='' and prep!='nhanh' and prep!='trung bình' and prep!='lâu':
            messagebox.showerror(message = "Điền 'nhanh', 'trung bình' hoặc 'lâu'")
            return

        calories = etCalories.get().strip()
        if calories!='' and calories!='thấp' and calories!='trung bình' and calories!='cao':
            messagebox.showerror(message = "Điền 'thấp', 'trung bình' hoặc 'cao'")
            return

        #add dish
        cmd = """INSERT OR IGNORE INTO dishes(name,category,ingredients,price,note,
                                                instruction,prep,calories,frequency) 
                    VALUES (?,?,?,?,?,?,?,?,?)"""
        args = (etName.get().strip(),etCategory.get().strip(),etIngredients.get().strip(),0,etNote.get().strip(),
                etInstruction.get().strip(),etPrep.get().strip(),etCalories.get().strip(),0)
        c.execute(cmd,args)
        clearEntry()
        updateText()
    def findDish():
        def findDish_byID(command):
            
            c.execute(command)
            result = c.fetchone()
            clearEntry()
                    
            etIden.insert(0,result[0])
            etName.insert(0,result[1])
            etCategory.insert(0,result[2])
            etPrice.insert(0,result[3])
            etNote.insert(0,result[5])
            etInstruction.insert(0,result[6])
            etPrep.insert(0,result[7])
            etCalories.insert(0,result[8])
            etIngredients.insert(0,result[9])
        def findDish_byNameorCat(column,search_term):
            command = "select * from dishes where {} like '%{}%'".format(column,search_term)
            c.execute(command)
            result = c.fetchall()
            updateTextWithList(result)


        if etIden.get()!='':
            command = 'select * from dishes where dish_id= {}'.format(str(etIden.get()))
            findDish_byID(command)
            return
        else:
            if etName.get().strip()!='':
                findDish_byNameorCat('name',etName.get().strip())
                return
        if etCategory.get().strip()!='':
            findDish_byNameorCat('category',etCategory.get().strip())
    def editDish():
        thisbitch = str(etIden.get())
        x =  int(etPrice.get()) if etPrice.get() !='' else 0

        command = """
        UPDATE dishes  
        SET     name = '{}' , 
                category = '{}' ,
                ingredients = '{}' ,
                price = {} ,
                note = '{}' ,
                instruction = '{}' ,
                prep = '{}' ,
                calories = '{}'  
        WHERE dish_id={} """.format(    etName.get(),
                                        etCategory.get(),
                                        etIngredients.get(),
                                        x,
                                        etNote.get(),
                                        etInstruction.get(),
                                        etPrep.get(),
                                        etCalories.get(),
                                        etIden.get())

        c.execute(command)
        updateText()
    def deleteDish():
        thisbitch = str(etIden.get())
        c.execute('select * from dishes where dish_id= {}'.format(thisbitch))
        result = c.fetchall()
        if len(result) == 0:
            messagebox.showerror(message = 'Món không tồn tại')
            return

        thisbitch = str(etIden.get())
        c.execute('delete from dishes where dish_id= {}'.format(thisbitch))
        updateText()
    def refreshText():
        updateText()

    ###############################
    root = Tk()
    root.title = "Insert Dish"
   
    frametop = Frame(root)
    frametop.pack(side=TOP)
    framel = Frame(frametop)
    framel.pack(side=LEFT)
    framer = Frame(frametop)
    framer.pack(side=LEFT)

    framemiddle = Frame(root)
    framemiddle.pack(side=TOP)

    framebottom = Frame(root)
    framebottom.pack(side=TOP)

    
    lbID = Label(framel,text='ID').pack(side=TOP)
    lbName = Label(framel,text='Name').pack(side=TOP)
    lbCategory = Label(framel,text='Category').pack(side=TOP)
    lbIngredients = Label(framel,text='Ingredients').pack(side=TOP)
    lbPrice = Label(framel,text='Price').pack(side=TOP)
    lbNote = Label(framel,text='Note').pack(side=TOP)
    lbInstruction = Label(framel,text='Instruction').pack(side=TOP)
    lbPrep = Label(framel,text='Prep').pack(side=TOP)
    lbCalories = Label(framel,text='Calories').pack(side=TOP)
        
    etIden = Entry(framer)
    etIden.pack(side=TOP,pady=1)
    etName = Entry(framer)
    etName.pack(side=TOP,pady=1)
    etCategory = Entry(framer)
    etCategory.pack(side=TOP,pady=1)    
    etIngredients = Entry(framer,)
    etIngredients.pack(side=TOP,pady=1)
    etPrice = Entry(framer)
    etPrice.pack(side=TOP,pady=1)
    etNote = Entry(framer)
    etNote.pack(side=TOP,pady=1)
    etInstruction = Entry(framer)
    etInstruction.pack(side=TOP,pady=1)
    etPrep = Entry(framer)
    etPrep.pack(side=TOP,pady=1)
    etCalories = Entry(framer)
    etCalories.pack(side=TOP,pady=1)
    
    bClear = Button(framemiddle,text='Clear',command=clearEntry)
    bClear.pack(side=LEFT, padx = 2)
    bAdd = Button(framemiddle,text='Add',command=addDish)
    bAdd.pack(side=LEFT, padx = 2)
    bFind = Button(framemiddle,text='Find',command=findDish)
    bFind.pack(side=LEFT, padx = 2)
    bEdit = Button(framemiddle,text='Edit',command=editDish)
    bEdit.pack(side=LEFT, padx = 2)
    bDelete = Button(framemiddle,text='Delete',command=deleteDish)
    bDelete.pack(side=LEFT, padx = 2)
    bRefresh = Button(framemiddle,text='Refresh',command=refreshText)
    bRefresh.pack(side=LEFT, padx = 2)
    
    #########################
    text = Text(framebottom)
    text.pack()    
    updateText()
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
    #for row in c.execute("PRAGMA table_info("+table+")").fetchall():
    #    print(row)

    #method 4
    columns = []
    for row in c.execute("PRAGMA table_info("+table+")").fetchall():
        columns.append(row[1])

    line =''
    for column in columns:
        line += str(column)
        line += '\t'

    print(line)









#tableColumns('dishes')
#insertData1()



#displayData()

#executeRowQuery('dishes','')
#sqlitemaster()

#executeVoidQuery()
#tableColumns('dishes')

TkDatabase()



#DON'T TOUCH
conn.commit()
conn.close()
