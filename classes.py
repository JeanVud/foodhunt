class Recipe:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price
    def display(self):
        print('{} : {} : {}'.format(self.name,self.ingredients,self.price))


r = Recipe('Canh chua','fish',10000)
r.display()
