print(5+6)
print("5"+"6")

#Polymorphism:
#the above expression is example of polymorphism
#the plus opertor add the two strings and give the different value
#the plus operator add the two strings and give the different value


#Getter and Setter
class Fruit:
    def __init__(self,name: str):
        self._name = name

    @property
    def fruit_name(self):
        print("f")

if __name__ == "__main__"
    fruit = Fruit('Banana')
