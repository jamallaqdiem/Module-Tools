class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
#print(imran.address) # Person class do not have address attribute.

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
#print(eliza.address) # again here Person class do not have address attribute.

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))

# This method will crash the program as there is no occupation attribute in the Person class
#def is_student(person: Person) -> bool:
#    return person.occupation =="Software Engineer" 
