class Person:
    def __init__(self , fname ,lname):
        self.first_name = fname
        self.last_name = lname

    def print_details(self):
        print(f"First Name is : {self.first_name}")
        print(f"Last Name is : {self.last_name}")
        print("---------")


class Student(Person):
    def __init__(self, fname ,lname , course , year):
        super().__init__(fname,lname)
        self.course = course
        year = int(year)
    def print_other_details(self):
        print(f"Course is : {self.course}")
        print(f"year is : {self.year}")

s1 = Student("Apollo" , "Carter" , "Data Science" ,2020)
s1.print_details()
s1.print_other_details()








