#Utility functions as a module
import random
import math

def list_ingredients(ingredients):
    for item in ingredients:
        print("Ingredient:", item)

def suggest_recipe(recipes):
    return random.choice(recipes)

def ingredient_weight(quantity):
    return math.ceil(quantity * 100)  # grams
