## parent class hai jiss say data use or inherit
## abc python main aik module jo abstract class banany main help karta hai
## abstract class ka structure fixed hota hai implementation baad mai hota uss main nahi hoti
## jo class inherit karegi wohi implement karega child class
from abc import ABC, abstractmethod #abstract base class(abc)

class Shape(ABC): #abstract class(parent)
    @abstractmethod # iss kay baad method ya function sirf structure hoga no implentation
    def area(self): 
        pass # nothing here 

class Reactangle(Shape): #child
    def __init__(self, width, height):
        self.width = width #var
        self.height = height   

    def area(self): #implement
        return self.width * self.height
    
if __name__ == "__main__":
    rect = Reactangle(4,5)
    print("Area of reactangle :", rect.area())




