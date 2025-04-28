#Calculates recipe cost using functions and while loops
def recipe_cost(eggs, flour_cups):
    egg_price = 0.2  # $ per egg
    flour_price = 0.5  # $ per cup
    total = eggs * egg_price + flour_cups * flour_price
    return total

def is_ready(eggs, flour):
    return eggs >= 2 and flour >= 1

eggs = 0
flour = 0
while not is_ready(eggs, flour):
    eggs = int(input("Eggs? "))
    flour = float(input("Flour (cups)? "))
    print("Status:", is_ready(eggs, flour))
print("Ready to bake! Cost: $", recipe_cost(eggs, flour))
