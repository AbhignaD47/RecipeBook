#Uses kitchen_utils module
import kitchen_utils
import random
import math

recipes = ["cake", "pie", "soup"]
print("Suggested recipe:", kitchen_utils.suggest_recipe(recipes))
ingredients = ["eggs", "flour", "sugar"]
kitchen_utils.list_ingredients(ingredients)
print("Weight of 2.5 units:", kitchen_utils.ingredient_weight(2.5))
print("Random recipe:", random.choice(recipes))
random.shuffle(recipes)
print("Shuffled recipes:", recipes)
print("Square root of 16:", math.sqrt(16))
