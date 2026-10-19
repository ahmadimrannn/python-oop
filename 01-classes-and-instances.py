from typing import Literal

class Person:
    def __init__(self, first_name: str, last_name: str, age: int, gender: Literal["male", "female"], occupation: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def get_information_about_the_person(self):
        information = f"The person is a {self.age} years old {self.gender}. The name of the person is {self.first_name} {self.last_name}. The person's occupation is {self.occupation}."

        return information

person1 = Person("Ahmad", "Imran", 18, "male", "AI Engineer")
person2 = Person("George", "Kyle", 21, "male", "Full Stack Engineer")

print(person1.first_name)
print(person1.get_information_about_the_person())

print(person2.first_name)
print(person2.get_information_about_the_person())