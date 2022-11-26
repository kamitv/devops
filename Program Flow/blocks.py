name = input("Please enter your name")
age = int(input("How old are you {0}?".format(name)))
print(age)

# if age >= 18:
#     print("YAY! You are old enough to vote!")
#     print("Please put an X in the box.")
# else:
#     print("Please come back in {} years.".format(18-age))
#OR:
if age < 18:
    print("Please come back in {} years.".format(18-age))
elif age == 900:
    print("Sorry Yoda, you died in Return of Jedi")
else:
    print("YAY! You are old enough to vote!")
    print("Please put an X in the box.")