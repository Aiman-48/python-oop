class Car:
    def __init__(self, brand):
        self.brand = brand # public variablr

    def start(self):
        print(f"{self.brand} is starting ") #public method

if __name__ == "__main__":

    my_car = Car("Toyota")
    print(my_car.brand) #access public variable from obj
    my_car.start() #accssess public method
        