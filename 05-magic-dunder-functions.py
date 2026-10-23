class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@gmail.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        return int(self.pay * self.raise_amount)
    
    # Dunder Functions in OOP
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.first} {self.last}, {self.email}"

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee("ahmad", "butt", 58934)
emp_2 = Employee("saeed", "khan", 98493)

print(emp_1)
print(repr(emp_1))
print(emp_1.__repr__())

print(str(emp_1))
print(emp_1.__str__())

print(emp_1 + emp_2)
