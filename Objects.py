#Objects

age = 8

print(age.real)
print(age.imag)
print(age.bit_length())

items = [1 ,2]
items.append(3)
print(items)
items.pop()
print(items)
print(id(items))

#Objects allows the methods to allowed mutable or not
age = 6
age = age + 1
print(age)

#Loops


count = 0
while count < 10:
    print("The condition is true:")
    count = count + 1

print("After the Loop")

items = ["Chocolate","Battery",1,"Senorika"]
#for item in items:
#    print(item)

for index , item in enumerate(items):
    print(index , item)
for item in range(11):
    print(item)


items = [1,2,3,4]

for item in items:
    if item == 2:
        continue
    print(item)

for item in items:
    if item == 2:
        break
    print(item)

