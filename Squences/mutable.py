shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]     # add cookies to shopping_list
print(shopping_list)
print(id(shopping_list))        # the id will remain the same because python was able to add a new item to the list without changing it
print(another_list)

a = b = c = d = e = f = another_list
# this can also be written as:
# a = another_list
# b = another_list
# c = another_list
# d = another_list
# e = another_list
# f = another_list
print(a)

print("Adding cream")
b.append("cream")      # adding cream to the list called 'b' b.append("cream") is a method
print(c)
print(d)

# how to write method = start with the name of the object you are using, then a dot, then the name of the method,
# then paranthesis, then an argument