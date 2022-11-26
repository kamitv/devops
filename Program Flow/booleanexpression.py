day = "Saturday"
Temperature = 30
raining = True

if (day == "Saturday" and Temperature > 27) or not raining:   #and has a higher precedence than or
    print("Go swimming")
else:
    print("Learn Python")

#always use paranthesis when using "and" and "or" in one condition, doing this helps it make clear what you intended

