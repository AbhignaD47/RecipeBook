#Handles input errors using try/except
try:
    eggs = int(input("How many eggs? "))
    sugar = float(input("Cups of sugar? "))
    print(f"Got {eggs} eggs and {sugar} cups sugar")
except ValueError:
    print("Invalid input! Use numbers.")
