if 0:
    print("True")
else:
    print("False")      #0 elvatuates to false in boolean expersions

name = input("Please enter your name: ")
#if name:
if name != "":
    print("Hello, {0}".format(name))
else:
    print("Are you the man with no name?")      #empty strings = false
