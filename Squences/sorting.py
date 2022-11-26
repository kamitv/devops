pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)   # the sorted function returns a list containing all the items in order, with the captial letter first
print(letters)

numbers = [2.3, 4.5, 8.7, 9.2, 1.6, 3.7]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)

# 'sorted' returns a new list, but 'sort' sorts the list in its place

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key = str.casefold)     # use key=str.casefold when you dont want the captial letters to appear first
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)