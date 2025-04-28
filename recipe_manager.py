#integrating all files
import re
from collections import deque

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Completed {func.__name__}")
        return result
    return wrapper

class RecipeManager:
    def __init__(self):
        self.recipes = {}
    
    @logger
    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {"ingredients": ingredients, "instructions": instructions}
    
    @logger
    def save_recipes(self, filename):
        with open(filename, "w") as file:
            for name, data in self.recipes.items():
                file.write(f"{name}: {', '.join(data['ingredients'])} | {data['instructions']}\n")
    
    @logger
    def load_recipes(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, rest = line.split(":", 1)
                    ingredients, instructions = rest.split("|", 1)
                    self.recipes[name.strip()] = {
                        "ingredients": [i.strip() for i in ingredients.split(",")],
                        "instructions": instructions.strip()
                    }
        except FileNotFoundError:
            print("No recipes found!")
    
    def search_mixing(self, name):
        instructions = self.recipes.get(name, {}).get("instructions", "")
        return re.findall(r"\b[mM]ix\b", instructions)

# Test the manager
manager = RecipeManager()
manager.add_recipe("Cake", ["eggs", "flour"], "Mix eggs, add flour")
manager.save_recipes("recipes.txt")
manager.load_recipes("recipes.txt")
print("Mixing steps in Cake:", manager.search_mixing("Cake"))
print("Recipes:", manager.recipes)
