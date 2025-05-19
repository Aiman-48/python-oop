## any class object is instancence 

##object kay through call karna instance method
class Dog: #instance class
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed #instance var

    def bark(self): #instance method
        print(f"{self.name} is barking!")

if __name__ == "__main__":
    my_dog = Dog("tommy", "labrador") #instance obj (calling class)
    my_dog.bark() #calling instance method

