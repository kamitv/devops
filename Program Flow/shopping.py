shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

#for item in shopping_list:
    #if item != "spam":
        #print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue    #continue causes the specific code in the block to be skipped, and continues on
    print("Buy " + item)
print("--------------------")
for item in shopping_list:
    if item == "spam":
        break    #break causes the code to terminate after the specified string
    print("Buy " + item)

