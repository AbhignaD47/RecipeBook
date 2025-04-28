#Checks ingredient quantities using conditionals
eggs = int(input("How many eggs? "))
sugar = float(input("How many cups of sugar? "))
if eggs >= 2 and sugar >= 0.5:
    print("You can bake a cake!")
elif eggs == 1:
    print("Make a small cake instead.")
else:
    print("Missing ingredients.")
