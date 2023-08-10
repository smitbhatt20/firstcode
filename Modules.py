#MODULES
# math for math utlilities
#re or regular expressions
#json to work with JSON
#datetiem to work with dates
#sqlite3 to use SQLite
#os for Operating System Utlilities
#random for random number generation
#statistics for statistics utilities
#requests to perform HTTP network requests
#http to create HTTP Servers
#urllib to manage URLs

#lambda functions

num = lambda num : num * 2
print(num(2))

division = lambda a , b : a / b
print(division(20 , 4))

#map() , filter() ,  reduce()

numbers = [1 , 2 , 3]

result = map(lambda a : a * 2, numbers)

print(list(result))

numbers = [1 , 2 , 3]

def isEven(n):
    return n % 2 == 0

result = filter(isEven , numbers)

print(list(result))


from functools import reduce

expenses = [("Dinner", 80),("Car repair", 120)]

sum = reduce(lambda a,b : a[1] + b[1], expenses)

print(sum)

# Recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

#Decorators
def greet(fx):

    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this functions")
    return mfx

@greet
def hello():
    print("Hello!")

@greet
def add(a,b):
    print(a+b)

greet(hello)()
greet(add)(2,4)