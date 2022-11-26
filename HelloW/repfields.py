age = 24
print("My age is " + str(age) + " years")
#OR
print("My age is {0} years".format(age)) #The .format(age) basically replaces {0}

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, March: {2}, April: {1}, May: {2}, Jun: {1}, July: {2}, August: {2}, Sep: {1}, Oct: {2}"
      "Nov: {1}, Dec: {2}".format(28, 30, 31))
        #the number in the replacement field and the order of the numbers in .format() determine what will be replaced
        #The replacement feild is optional as long as the .format() are in the orders you want

#F-strings:

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

