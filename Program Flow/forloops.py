parrot = "Norwegian Blue"

for character in parrot:    #you can call the variable anything you want (character)
    print(character)

#a for loop starts with "for"
#next we provide the name of one or more variables
#next we have "in," our variable will be bound to each of the items in the sequence
#fianlly we specify where the values are in

number = input("Please enter a series of numbers using any separators you like")
separators = ""

for char in number:
    if not char.isnumeric():    #isnumeric() will return true if the char is a number and false otherwise
        separators = separators + char
#print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

string = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans done for us?"
capitals = ""

for char in string:
    if not char.isupper():
        capitals = capitals + char
print(capitals)

