#Manages sets and tuples
unique_ingredients = set(["salt", "sugar", "salt", "pepper"])
print("Unique ingredients:", unique_ingredients)
fixed_recipe = ("mix eggs", "add flour", "bake")
print("Recipe steps:", fixed_recipe)
user_ingredient = input("Add an ingredient to pantry: ")
unique_ingredients.add(user_ingredient)
print("Updated pantry:", unique_ingredients)
for step in fixed_recipe:
    print("Step:", step)
# Check if ingredient is in pantry
check = input("Check for ingredient: ")
if check in unique_ingredients:
    print(f"{check} is in the pantry!")
else:
    print(f"{check} not found.")
