activity = input("What would you like to do today?: ")

if "cinema" not in activity.casefold():     #casefold makes strings lowercase
    print("But I want to go to the cinema")

print("-" * 80)

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age and age < 31:
    print("Welcome to your vacation")
else:
    print("Sorry, but this vacation isn't for you")
