numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are rejected")
        break
else:
    print("These numbers are acceptable")
    # if the code did not terminate from the if loop, it goes to else. Else is associated with the for loop instead of
    #if because of the indentation
