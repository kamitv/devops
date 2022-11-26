shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
                   #0       #1       #2      #3       #4      #5
item_2_find = "spam"
found_at = None     #none= something doesnt have a value

#for index in range(6):
#for index in range (len(shopping_list)):    #len is short for length & lets us know how many items are in a sequence
#   if shopping_list[index] == item_2_find:  #this will index the list
#        found_at = index
#       break

if item_2_find in shopping_list:
    found_at = shopping_list.index(item_2_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_2_find))

