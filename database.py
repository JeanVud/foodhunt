#https://inloop.github.io/sqlite-viewer/



import sqlite3
#D:\8570w\Python Projects\Foodapp\foodhunt.db
path = 'D:/8570w/Python Projects/Foodapp/foodhunt.db'
conn = sqlite3.connect(path)
#conn = sqlite3.connect('/Foodapp/foodhunt.db')
c = conn.cursor()
#
c.execute("""CREATE TABLE dishes (
                dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text unique,
                type text,
                difficulty text) """)

c.execute("""CREATE TABLE eatout (
                eatout_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                restaurant text) """)

c.execute("INSERT INTO dishes(name,type,difficulty) VALUES ('canh ca rieu hong','canh','kho')")

c.execute('select * from dishes')
list = c.fetchall()

for row in list:
    print(row)



conn.commit()

conn.close()
