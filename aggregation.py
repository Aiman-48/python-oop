class Employee:
    def __init__(self, name):
        self.name = name ## constructor


class Department:
    def __init__(self, employee):
        self.employee = employee ## both classes are independent

    def show_employee(self):
        print(f"Employee in department: {self.employee.name}")

if __name__ == "__main__":

    emp = Employee("Aiman")  
    dept = Department(emp)  ## passes the emp obj 
    dept.show_employee()    


