#Dictionaries allows to make Key:Value pair)

dog = { "name":"Roger", "age":8 , "color":"brown"}

print(dog['age'])
print(dog.get("color","brown"))
print(dog.pop("name"))
print(dog)
print(dog.keys())
print(dog.values())
dog["favourite food"] = "Biscuits" #add the another key:vlaue pair in the dictionaries.
print(dog)
del dog['color']
dogCopy = dog.copy()