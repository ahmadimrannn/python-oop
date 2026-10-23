from typing import Literal

class Person:

    number_of_persons = 0
    family_head = "Muhammad Imran (Father)"

    def __init__(self, first_name: str, last_name: str, age: int, gender: Literal["male", "female"], occupation: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation

        # This is a class variable which can't be overriden by the instance.
        Person.number_of_persons += 1

    # Regular methods automatically take the self instance
    def get_information_about_the_person(self):
        information = f"The person is a {self.age} years old {self.gender}. The name of the person is {self.first_name} {self.last_name}. The person's occupation is {self.occupation}."

        return information

    # Class methods automatically take the class
    @classmethod
    def set_family_head(cls, head):
        cls.family_head = head

    @classmethod 
    def form_person(cls, person_str):
        first, last, age, gender, occupation = person_str.split(",")
        return cls(first, last, age, gender, occupation)

    # Static methods don't take anything automatically like self or cls

person1 = Person("Ahmad", "Imran", 18, "male", "AI Engineer")
person2 = Person("George", "Kyle", 21, "male", "Full Stack Engineer")

person1.set_family_head("Ahmad Imran")

print(Person.family_head)
print(person1.family_head)
print(person2.family_head)

person_string = "Talha, Irfan, 18, male, ai engineer"
person3 = Person.form_person(person_string)
print(person3.first_name)