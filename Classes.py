#Class is the type of object.
#In object-oriented programming, a class is a template definition of the methods and variables in a particular kind of object.



class Employee:

    def __init__(self):               #The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.03
        self.name = "Vishwa"
        self.age = 21
        self.occupation = "Python Developer"
        self.salary = 600000
        self.experience = 2

    def win(self):
       print(f"{self.name} has won gold medal in Swimming")

    def talk(self):
        print(f"{self.name} is a fluent public speaker")

    def vote(self):
        if self.experience > 4:
            print("You can vote")
        else:
            print("You can not vote!")

obj = Employee()
obj.win()
obj.talk()
obj.vote()



class Person:

    def __init__(self):
        self.name = "Smit"
        self.age = 20
        self.occupation = "Information Security Engineer"
        self.company = "Amazon Web Services"
        self.experience = 15
        self.salary = 48,87,999
        self.networth = 3,32,122,989

    def talk(self):
        print("Hi! I am ", self.name)
        print(f"I am an {self.occupation} working in {self.company}")

    def vote(self):
        if self.experience > 12:
            print("Then you can vote")
        else:
            print("You are not eligible to vote")




obj = Person()
#obj.name = "Harry"                if you wan to change the properties of a object in the class then you can do this by example shown in adjacent
#obj.occupation = "Software Developer"
#obj.networth = "4,44,441,433"

obj.talk()
obj.vote()

