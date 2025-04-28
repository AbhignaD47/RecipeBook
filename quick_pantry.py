#Uses list comprehensions and lambda functions
pantry = ["salt", "flour", "sugar", "milk", "spice"]
s_ingredients = [item for item in pantry if item.startswith("s")]
print("S ingredients:", s_ingredients)
quantities = [1, 2, 3, 4]
scaled = list(map(lambda x: x * 1.5, quantities))
print("Scaled quantities:", scaled)
recipes = ["cake", "apple pie", "soup"]
sorted_recipes = sorted(recipes, key=lambda x: len(x))
print("Recipes sorted by name length:", sorted_recipes)
upper_ingredients = [item.upper() for item in pantry]
print("Uppercase ingredients:", upper_ingredients)
