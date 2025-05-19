#cls represent class and self represent object

class Counter:
    count = 0 #  common class variable

    def __init__(self):
        Counter.count +=1

    @classmethod
    def show_count(cls):
        print(f"total obj created: {cls.count}")


if __name__ == "__main__":

    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    Counter.show_count()


