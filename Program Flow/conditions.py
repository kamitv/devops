age = int(input("How old are you?"))

#if age >= 16 and age <= 60:     #for this to evaluate to true, both parts need to be true
#if 16 <= age <= 65:
if age in range (16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

#AND TRUTH TABLE:
    #True & True = True
    #True & False = False
    #False & True = False
    #false & False = False

#OR TRUTH TABLE:
    ##True or True = True
    #True or False = True
    #False or True = True
    #False or False = False

#When comparing conditions with and, python will stop as soon as it finds something false, but when comparing
#conditions using or, it will stop as soon as it finds true