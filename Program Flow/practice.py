while True:
    number = int(input("Please enter a number"))
    if (number % 2) == 0:
        print("{} is an even number".format(number))
    else:
        print("{} is an odd number".format(number))
    question = input("Do you want to continue?")
    answer = "yes"
    if answer == "yes":
        print("Al right!")
    number = int(input("Please enter a number"))
    if (number % 2) == 0:
        print("{} is an even number".format(number))
    else:
        print("{} is an odd number".format(number))






