for i in range (1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
    #'**' is exponent operator & is used to put exponents on #s

print()

for i in range (1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    #The added :# is the width of the section, it looks tidier than before

print()

for i in range (1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    #to left align the values, we place a less than symbol after the colon

print()

for i in range (1, 13):
    print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
    #the carrot symbol centers the values

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
