class Student:
     # init constructor jab class ka object banayay jab use hoga
    def __init__(self , name, marks):# selfcurrent obj ko reffer karta hai

        self.name = name
        self.marks = marks

    def display(self): # yhan self use kia matlab kay yeh name  or marks dono ko use kar rha hai

# jab string kay sath variable use karna ho tw string ka method use kartay hain
        print(f"name : {self.name} , marks :{ self.marks}")

if __name__ == "__main__": # yeh aik speacial condition hai jo check karei agar program direct run horha ya kkahin say import
    student1 = Student("aiman" ,90)
    student1.display()






        