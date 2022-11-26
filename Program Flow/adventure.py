available_exits = ["North", "South", "East", "West".casefold()]
chosen_exit = ""
# chosen_exit could be anything but the available_exits because then the while loop can then evaluate to true:
# if the player inputs something that is not in the available_exits list, the while loop runs again
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("Arent you glad to get out of there")
