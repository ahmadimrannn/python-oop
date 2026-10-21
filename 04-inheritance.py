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
    pass


emp_1 = Developer("Ahmad", "Imran", 60000)
emp_2 = Employee("Corey", "Schafer", 120000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)