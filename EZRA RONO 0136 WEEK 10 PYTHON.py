from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, fname, initial, lname):
        self.fname = fname
        self.initial = initial
        self.lname = lname

    @abstractmethod
    def getSalary(self):
        pass

    def display(self):
        print(f"{self.fname} {self.initial}. {self.lname}")


class SalaryEmployee(Employee):
    def __init__(self, fname, initial, lname, salary):
        super().__init__(fname, initial, lname)
        self.salary = salary

    def getSalary(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, fname, initial, lname, hours, rate):
        super().__init__(fname, initial, lname)
        self.hours = hours
        self.rate = rate

    def getSalary(self):
        return self.hours * self.rate


# Test polymorphism
e1 = SalaryEmployee("John", "A", "Doe", 50000)
e2 = HourlyEmployee("Jane", "B", "Smith", 160, 300)

for emp in (e1, e2):
    emp.display()
    print("Salary:", emp.getSalary())
    print()