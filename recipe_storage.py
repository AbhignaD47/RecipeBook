#recipes = {
    "cake": ["eggs", "flour", "sugar"],
    "pie": ["apple", "sugar"]
}
# Save to file
try:
    with open("recipes.txt", "w") as file:
        for name, ingredients in recipes.items():
            file.write(f"{name}: {', '.join(ingredients)}\n")
    # Read and display
    with open("recipes.txt", "r") as file:
        print("Stored recipes:")
        for line in file:
            print(line.strip())
    # Append a new recipe
    name = input("New recipe name: ")
    ingredients = input("Ingredients (comma-separated): ").split(", ")
    with open("recipes.txt", "a") as file:
        file.write(f"{name}: {', '.join(ingredients)}\n")
    print("Updated recipes:")
    with open("recipes.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File error!")
