letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]    #the start value MUST be greater that the stop value when using a negative slice
print(backwards)

print(letters[25::-1]) #with a negative step, the start value defaults to the end of the string & the stop to the start

print(letters[::-1]) #a python idiom to reverse a sequence

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[25:17:-1])

#the last 4 letters:
print(letters[-4:])

#the last item:
print(letters[-1:])

#the first item:
print(letters[:1])
