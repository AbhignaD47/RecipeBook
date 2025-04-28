#Searches instructions using regular expressions
import re
instructions = input("Enter recipe instructions: ")
mix_steps = re.findall(r"\b[mM]ix\b", instructions)
print("Mix steps found:", mix_steps)
numbers = re.findall(r"\d+", instructions)
print("Quantities found:", numbers)
if re.match(r"[mM]ix", instructions):
    print("Recipe starts with mixing!")
verbs = re.findall(r"\b\w+\b", instructions)
print("Words:", verbs)
ingredients = re.findall(r"add\s+([a-z]+)", instructions, re.IGNORECASE)
print("Ingredients after 'add':", ingredients)
