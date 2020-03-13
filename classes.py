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



#r = Dish('Canh chua','fish',10000)

