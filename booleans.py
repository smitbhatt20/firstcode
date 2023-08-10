done = True   #string is false only when it is empty and number is always false when it is 0.

if done:
    print("yes")
else:
    print("no")

name = "Smit is a Handsome Boy"
if (type(name) == str):
    print("True")
else:
    print("False")

pass_Firstclass = False
pass_Firstclasswithdistinction = True

pass_marks = any([pass_Firstclass , pass_Firstclasswithdistinction])
#any is  the global function that is the any of the one is true is printed True

pass_marks = all([pass_Firstclass , pass_Firstclasswithdistinction])

num1 = 2+3j
num2 = complex(2,3)
print(num2.real , num2.imag)

print(abs(5.5)) #prints the absolute value
print(round(5.77))

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)

#User Input
age = input("Enter your age: ")
print("Your age is " + age)