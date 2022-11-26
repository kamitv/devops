low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:  # True is always true which means the loop will go around forever
    #print("\t Guessing in the range of {} and {}".format(low,high))
    guesses = low + (high - low) // 2  # calculates midpoint, the formula to guess within 10 guesess
    high_low = input("My guess is {}. Should I guess higher or lower? Enter h, l or c if my guess was correct ".
                     format(guesses)).casefold()

    if high_low == "h":
        # Guess higher, the low end of the range becomes 1 greater than the guess
        low = guesses + 1
    elif high_low == "l":
        #Guess lower, the high end of the range becomes one less than the range
        high = guesses - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    guesses += guesses

# comments dont count as a block of code, so use pass as a place holder
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))

