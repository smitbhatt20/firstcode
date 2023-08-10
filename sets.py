set1 = {"smit","shivanshi"}
set2 = {"smit"}

intersect = set1 & set2
print(intersect)

mod = set1 | set2
print(mod) # it will add the both the items from different sets as it will not add only one time the item is repeated it will print only one time
#set is case sensitive

mod = set1 > set2
print(mod)
print(len(set1))
print(len(set2))
print(list(set1)) #set does not print the two same item it will add only one time no matters how many time does it is repeated.
