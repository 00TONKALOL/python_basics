from datetime import datetime


from dictionary import student

class Student:
    def __init__(self,name, age , DOB , gender):
        self.name=name
        self.age=age
        self.date_of_birth=DOB
        self.gender=gender

    def name(self):
        return self.name
    def age(self):
        return self.age
    def date_of_birth(self):
        return self.date_of_birth
    def gender(self):
        return self.gender
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Gender: {self.gender}")
student1 = Student("Ernest Maina" , 18 , 2007/4/10 , )
print(f"student1.name: {student1.name} is student1.age: {student1.calculate_age}years old")
age=datetime.today() - datetime.strptime("2007/4/10","%Y-%m-%d")
print(age.days//365)
