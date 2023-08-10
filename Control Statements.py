#condition = True
#if  condition == True:
 #   print("The Condition")
  #  print("Is True")

#else:
 #   print("The Condition")
  #  print("Is False")

#age = int(input("Enter your age:"))
#dollars = int(input("Enter the amount you have:"))
#if (age >= 18 and dollars >= 6):
#    print("You are allowed to drink alcohol")
#elif (age >= 18 and dollars < 6):
#    print("You are not allowed to drink alocohol as you don't have enough money")
#elif (age < 18 and dollars > 6):
#    print("you can not drink alcohol as you are not eligible")
#else:
#    print("You are not allowed to drink alcohol as you are not eligible and you do not have noeny too")


dogs = ["Roger" , "Syd" , "Alpha" , 1] #we can add any data types in the list[

print("Roger" in dogs)
print(dogs[2])
dogs[2] = "Beta" #update tbe list by replacing the list index items
print(dogs)
print(dogs[-2])
print(dogs[1:3])

dogs.append("Jack Daniels") # to add the new itmes in the list
print(dogs)
print(len(dogs))

dogs.extend(["Beta" , 5]) #To extend the list
print(dogs)

dogs.remove("Syd") #to remove the item from the list
print(dogs)

print(dogs.pop()) # rmeoves the last item in the list
print(dogs)

dogs.insert(2 , "Jacky") #To insert the item at particular index you enter with a particular new item.
print(dogs)

dogs[1:1] = ["Test1","Test2"]
print(dogs)

items = ["Jack daniels" , "Jacky" , "Sheru" , "Alpha"]
items.sort() # TO sort the items
print(items)
