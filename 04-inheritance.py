class Employee:
    raise_amt = 1.15

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@gmail.com"
        self.pay = pay   

    def full_name(self):
        full_name = f"{self.first} {self.last}"

        return full_name

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.20

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def list_employees(self):
        for emp in self.employees:
            print(f"--> {emp.full_name()}")



emp_1 = Developer("Ahmad", "Imran", 60000, "Python")
emp_2 = Developer("Corey", "Schafer", 120000, "C++")

manager = Manager("Hassan", "Umer", 80000, [emp_1])

manager.list_employees()

print("-" * 20)

manager.add_emp(emp_2)
manager.list_employees()

print("-" * 20)

manager.remove_emp(emp_1)
manager.list_employees()

print("-" * 20)

print(isinstance(emp_1, Employee))
print(issubclass(Manager, Employee))