#Processes recipe instructions using string manipulation
instruction = input("Enter recipe instruction: ")
print("Shouted:", instruction.upper())
words = instruction.split()
print("First word:", words[0])
print("Number of words:", len(words))
ingredients = input("Enter ingredients (comma-separated): ").split(", ")
print("Formatted:", f"Recipe: {instruction}. Ingredients: {', '.join(ingredients)}")
# Check if recipe starts with mixing
verb = instruction.split()[0]
if verb.lower() == "mix":
    print("This is a mixing recipe!")
