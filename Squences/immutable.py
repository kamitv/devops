#result = True
#another_result = result
#print(id(result))       # id returns the object's memory address (aka identification)
#print(id(another_result))

#result = False
#print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))       # python attached a new variable to the string "Correctish"
print(id(another_result))
