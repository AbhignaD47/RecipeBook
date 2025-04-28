#Stores recipes in a dictionary
recipes = {
    "cake": ["eggs", "flour", "sugar"],
    "pie": ["apple", "sugar"],
    "soup": ["water", "salt"]
}
recipe_name = input("Enter a recipe name: ")
if recipe_name in recipes:
    print(f"{recipe_name} ingredients:", recipes[recipe_name])
else:
    print("Recipe not found!")
new_recipe = input("Add a new recipe name: ")
ingredients = input("Enter ingredients (comma-separated): ").split(", ")
recipes[new_recipe] = ingredients
print("Updated recipes:")
for name, ingredients in recipes.items():
    print(f"{name}: {ingredients}")
