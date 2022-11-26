split_string = "This line has been\nsplit over\nseveral\nlines\n"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print("The pet shop owner said \"No, no, no, he's resting.\"")

print('The pet shop owner said "No, no, no \'e\'s resting."')

#you can use 3 quotes so you won't need to use escape char

another_string= ("""This line has been
split over
several
lines""")
print(another_string)

#when you put a backslash with spaces ( \ ) it undoes escape char

print("""The pet show owner said "No, no \
'e's uh... he's resting'""")

#how to make a backslash character in your output: put 2 backslashes OR use a raw string
# #\U, \t, \n all have special meanings, so when you run it, it won't include the \ in the output
#2 backslashes
print("C:\\Users\\timachaluka\\notes.txt")

#raw string (just ad r at the beginning)
print(r"C:\Users\timachaluka\notes.txt")
