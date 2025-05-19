class Employee:
    #constructor hai init self pehlay
    def __init__(self, name, salary, ssn):
        self.name = name # public variable
        self._salary = salary #protected kay liay _ use karna(only in class) also outside but not recomended
        self.__ssn = ssn #private kay liay double__ use karna hai(only in class not outide)


if __name__ == "__main__":
    emp = Employee("Asad", 50000 ,"123-4556-454444")

    print("public:", emp.name)
    print("protected variable:", emp._salary)
    # private will not shw

    try:      
        print("private variable:", emp.__ssn)
    except AttributeError:
        print("can not access private")


    


