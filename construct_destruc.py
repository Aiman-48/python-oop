#constructor special method jo hota hai init woh chalta hai 
#destructor jab kaam end ho goodbye or delete variable karo

class logger:
    def __init__(self):#constructor

        print("object created") #constructor

    def __del__(self): #destructor

        print("object is delted")

if __name__ == "__main__":

    log  = logger()
    del log

