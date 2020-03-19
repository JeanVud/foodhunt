from tkinter import *
import sqlite3
import random

path = 'foodhunt.db'
conn = sqlite3.connect(path)
c = conn.cursor()


class Dish:
    def __init__(self, name, ingredients, price, frequency, description,instruction, category):
        self.name = name                #string
        self.ingredients = ingredients  #list of ingredient()
        self.price = price              #int derived 
        self.frequency = frequency      #int
        self.note = note                #string
        self.instruction = instruction  #
        self.category = category        
        self.tags = tags                #list of tags
                                        # can be salads, fishes, soups...
                                        # TODO: figure out wtf to do with this
        self.prep = prep                #TODO: preparation 
        self.calories = calories
    def display_short(self):
        pass
        print(self.name)
    def display_basic(self):
        pass
        print('{} : {} : {}'.format(self.name,self.ingredients,self.price))

class Ingredient:
    def __init__(self):
        self.name = name                #string
        self.frequency = frequency      #int

class EatOut():
    def __init__(self):
        self.name = name
        self.restaurant = restaurant

def getCourse(category):
    command = "select * from dishes where category = '{}' ".format(category)
    c.execute(command)
    return c.fetchall()


def updateTextWithList(result,framebottom):
    for widget in framebottom.winfo_children():
        widget.destroy()

    frame_left = Frame(framebottom)
    frame_left.pack(side=LEFT)
    frame_right = Frame(framebottom)
    frame_right.pack(side=LEFT,padx=10)
    for dish in result:
        lbname = Label(frame_left,text=dish[0],borderwidth=2,relief='ridge')
        lbname.pack(side=TOP, anchor=E)
        thisthing = dish[1]
        lbUhhh = Label(frame_right,text=thisthing[1])
        lbUhhh.pack(side=TOP, anchor=W)
def generateMeal(framebottom):
    


    ###################################################################
    man = getCourse('mặn')
    canh = getCourse('canh')
    xao = getCourse('xào')
    freestyle = getCourse('free style')
    uong = getCourse('uống')

    result = []
    result.append( ['man',random.choice(man)] )
    result.append( ['canh',random.choice(canh)] )
    result.append( ['xào',random.choice(xao)] )
    #result.append( ['free style',random.choice(freestyle)] )
    result.append( ['uống',random.choice(uong)] )
 
    updateTextWithList(result,framebottom)
def TkMealRecEngine():
    root = Tk()
    root.title = 'Meal Recommendation Engine'

    frametop = Frame(root)
    frametop.pack(side=TOP)
    framebottom = Frame(root)
    framebottom.pack(side=TOP)

    bGenerate = Button(frametop,text="Generate",command = lambda : generateMeal(framebottom))
    bGenerate.pack()
    



    root.mainloop()
    





TkMealRecEngine()


#DON'T TOUCH
conn.commit()
conn.close()
