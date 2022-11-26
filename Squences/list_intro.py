computer_parts = ["computer",   # 0
                  "monitor",    # 1
                  "keyboard",   # 2
                  "mouse",      # 3
                  "mouse mat"   # 4
                  ]

# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2])
#
# print(computer_parts[0:3])
# print(computer_parts[-1])   # returns last item
#
# # strings are immutable, which means they cannot be changed
# # lists are mutable, which means you can change the contents of a list

print(computer_parts)
# computer_parts[3] = "trackball"
# print(computer_parts)

print(computer_parts[3:])

computer_parts[3: ] = ["trackball"]     # replace mouse & mouse mat with trackball, trackball must be a list
print(computer_parts)