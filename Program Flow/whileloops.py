#basic form of a while loop:
# while <condition>:
#   execute block of code
# the condition can be anything that can evaluate to true or false
# as long as the condition if true, the code will be executed, otherwise, it will terminate

#for i in range(10):
#    print("i is now {}".format(i))

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1      # i = i + 1