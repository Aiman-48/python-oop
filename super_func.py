## base class(parent class)
class Person:
    def __init__(self, name):
        self.name = name

# step2: child class
class Teacher(Person): #inheriting person
    def __init__(self, name, subject):
        super().__init__(name) #using supper function(child class main parent ka constructor use karna ho)
        self.subject = subject

# step 3:display

    def display(self):
        print(f"Name: {self.name}, Subject:{self.subject}")

if __name__ == "__main__":

    teacher = Teacher("miss sana", "math")
    teacher.display()





