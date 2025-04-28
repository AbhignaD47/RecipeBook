#Manages ingredient lists using lists and for loops
ingredients = ["eggs", "flour", "sugar", "milk", "salt"]
print("First:", ingredients[0])
print("Last:", ingredients[-1])
ingredients.append("butter")
print("Pantry:")
for i in range(len(ingredients)):
    print(f"Jar {i}: {ingredients[i]}")
# Filter ingredients starting with 's'
print("Ingredients starting with s:")
for item in ingredients:
    if item[0] == "s":
        print(" -", item)
