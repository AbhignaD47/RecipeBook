#Defines a Recipe class using OOP
class Recipe:
    def __init__(self, name, ingredients, prep_time):
        self.name = name
        self.ingredients = ingredients
        self.prep_time = prep_time
    
    def display(self):
        print(f"Recipe: {self.name} ({self.prep_time} mins)")
        print("Ingredients:")
        for item in self.ingredients:
            print(f"- {item}")
    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    
    def is_quick(self):
        return self.prep_time < 30

cake = Recipe("Cake", ["eggs", "flour"], 30)
pie = Recipe("Pie", ["apple", "sugar"], 45)
cake.display()
pie.display()
cake.add_ingredient("sugar")
print("Updated Cake:")
cake.display()
print("Is cake quick?", cake.is_quick())
