#Functions

def hello(name):
    print("Hello " + name)

hello("Smit")

def who_am_i(): #this is a function without the parameters
    name = "Smit" #local variables
    age = 20
    print("My name is " + name + "I am "+ str(age) + "years old.")

who_am_i()

def party(age,money):
    a = int(input("Enter your age:"))
    m = int(input("Enter the money you have:"))

    if (age>=18 and money>6):
        print("You are eligible to drink the alcohol!")
    elif (age>=18 and money<6):
        print("Sorry! You can not drink alcohol as you do not have enough money!")
    elif (age<18 and money>6):
        print("Sorry!You can not drink alcohol as your age is below the drinking criteria!")
    else:
        print("Sorry!You can not drink alcohol as your age is less and you do not have enough money too!! ")

party(1,11)


#Variable Scope
age = 20 #Global Variable

def test():
    print(age)

print(age)
test()

#Nested Functions
def items():
    items = 5


    def price():
        price = items * 20
        print(price)

    price()

items()

def count():
    count = 0

    def increment():
        nonlocal count #To access the count vsriable from inside the function
        count = count + 2
        print(count)

    increment()
count()

def marks():
    marks = 40

    def firstclass():
        nonlocal marks
        marks = marks + 20
        print(marks)

        firstclass()

        def firstclasswithdistinction():
        marks = marks + 25
        print(marks)

        firstclasswithdistinction()

pass()

