import sqlite3
#######################
def addDish(name,j,i):
    #name
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

##########################
