print(1 + 1) #2
print(8 - 3) #5
print(20 * 1) #20
print(20 / 5) #4
print(8 ** 2) #64
print(5 // 2) #2
print(50 % 10) #0

age = 10
age += 8
print(age)

print("Smit S Bhatt" + " is an Information Security Engineer")#we can concanetate the strings or add the strings

#Comparater Operators
a = 1
b = 2
print(a)
print(b)
print(a == b) #False
print(a != b) #True
print(a > b) #False
print(a < b) #True


#condition1 = True
#condition2 = False
#not condition1 #False
#condition1 and condition2 #False
#condition1 or condition2 #True

print(0 or 1) ##1
print(False or 'hey') ## 'hey'
print('hi'or False) ##'False
print([] or False) ##False
print(False or [1]) ##[]      #print(first operand or second operand) if any one is true it will print that operand otherwise it will print the last or second operand by default


#Bitwise Operators

# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR Operations
# ~ performs a binary NOT operations
# << shift left operation
# >> shift right operation

#Ternary Operators

def is_adult(age):
    if age > 18:
        return True
    else:
        return False

def is_adult2(age):
    return True if age > 18 else False



