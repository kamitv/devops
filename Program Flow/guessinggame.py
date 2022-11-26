import random

highest = 10
answer = random.randint(1,highest)
guess = 0   #intiazle to any number that does not equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you got it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")



# an if condition begins with the keyword if, followed by a condition, and if statement will always be evaluated
# next, you will have one or more elif blocks, but elif is not necessary
# finally, you may have an else block, you also dont need this, but if you do include it, it must come after if/elif
# when testing for equality, use two equal signs, one equal sign is used to asign a variable to a value
# an if statement can include many elif parts, but only one else, else must come after elif

#less than - <
#less than or equal to - <=
#greater than - >
#greater than or equal to - >=
#equal to - ==
#not euqal to - !=


