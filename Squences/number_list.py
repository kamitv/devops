# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# print(min(even))
# print(max(even))
#
# print(min(odd))
# print(max(odd))
# print()
#
# print(len(even))
# print(len(odd))
#
# print()
#
# print("Mississippi".count("issi"))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

    # extend method takes all the items from the iterable list and adds it to the list we passed it
# even.extend(odd)    # in this case we pass the list odd to the extend method, this adds each item from odd to even
# print(even)
# another_even = even
# print(even)
#
# even.sort(reverse=True) #reverses the order of the list, sort method rearranges the items in the list without copying it
# print(even)
# print(another_even)

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)