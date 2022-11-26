available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "HDMI cable",
                   "dvd drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
# print(valid_choices)
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # its already in, so remove it
            computer_parts.remove(chosen_part)
            print("Removing {}".format(current_choice))
        else:
            computer_parts.append(chosen_part)
            print("Adding {}".format(current_choice))
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts):         # enumerate returns an item with its index position
            print("{0}: {1}".format(available_parts.index(part) + 1, part))  # number = index position, part = item

    current_choice = input()

print(computer_parts)
