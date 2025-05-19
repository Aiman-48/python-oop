class Engine:
    def start(self):

        print("engine is ready")


class Car: ##constructor
    def __init__(self):

        self.engine = Engine() ##make object of the class in the class its composition ([trong relation of two class)

    def start_car(self):
            self.engine.start() ##method in this  we will acesses engine method


if __name__ =="__main__":
     my_car = Car()
     my_car.start_car()
               
            
