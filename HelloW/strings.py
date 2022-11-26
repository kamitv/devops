print('Today is a good day to learn Python')
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " world")
print("Nidhi" + " Amit" + " Kulkarni")
greeting= "Hello"
Name= input("Please enter your name ")
what= input("What are you doing? ")

#if we want a space, we can add that too
print(greeting + ' ' + Name + ' ' + what)

age = 24
print(age)
print("My age is " + str(age) + " years old.")

#how to make python figure out what type of code it is? remember: the value is with the value rather than the variable
print(type(greeting))
print(type(age))

age = "2 years"
#age is no longer reffered to an int value, it is now a str value
print(type(age))


