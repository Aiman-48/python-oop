class MathUtils:
    @staticmethod #aisa method js main logic ho no use of cls ,self
    def add(a, b):
        return a + b
    
if __name__ == "__main__":
    result = MathUtils.add(3, 5)
    print("sum: ", result)


