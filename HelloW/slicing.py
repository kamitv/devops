parrot = "Norwegian Blue"
#produce a slice using 3 numbers with colons- start:stop:step
print(parrot[0:6])  #here we are telling python to start at position 6 and slice up to but not including position 6
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])   #you dont need to put a 0, just a colon

print(parrot[10:14])
#OR
print(parrot[10:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

#NEGATIVE NUMBERS:

print(parrot[-4:-2])
print(parrot[-4:])
print(parrot[-11:-9])

#Steps:

print(parrot[0:6:2])    #starts at 0, ends at 6 (but not including), and we step in multiples of 2
print(parrot[0:6:3])    #so only positions that are a mulitple of 3 will be in the output

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)


