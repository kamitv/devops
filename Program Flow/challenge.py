
choice = "-"
while True:

    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose one option from the ones below:" )
        print("1:\tLearn Swimming")
        print("2:\tLearn Hindi")
        print("3:\tGo to bed")
        print("4:\tWatch TV")
        print("5:\tListen to music")
        print("0:\texit")

    choice = input()