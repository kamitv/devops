pangram = """The quick brown 
fox jumps\t over 
the lazy dog"""

words = pangram.split()     # split returns all the items in a string
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

# replace str to int in place:
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)

# create a new list:
integer_values = []
for values in values_list:
    integer_values.append(values)
print(integer_values)

# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)

