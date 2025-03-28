from py_class3 import Account
from py_classes2 import Cylinder


class Person:
    def __init__(self , name ,age): #constructor #providing data to your class
        self.name = name
        self.age = age
        print("Creating a person")

    def say_hello(self):
        print(f"Hello World , I am {self.name} and I am {self.age} years old")

# objects == data + functions(manipulate data)
p1 = Person("Jack ", 19) #object(any variable created from a class)
p2 = Person("Walenje", 23)
p3 = Person("Methu", 19)
p1.say_hello()
p2.say_hello()
p3.say_hello()
name = "Chad"
name.upper()
name.lower()

c1 = Cylinder(66.35 , 89)
c2 = Cylinder(45 , 875)

c1.area()
c1.volume()
c1.print_details()


acc1 = Account("0001" , "Lauryn Hill" , 90000)
acc2 = Account("0002" , "Lucien Grange" , 50000)
acc3 = Account("0003" , "Ashton Hall" , 150000)


#static methods
#inheritance
#polymorphism

acc2.deposit(1000)
acc2.check_balance()
acc2.withdraw(5000)
acc2.check_balance()


#clss student ,data ==name , dob ,gender
#calculate the age
#print details









