class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())
print(person1.get_full_name())
person1.change_last_name("Tyurina")
print(person1.get_name())
print(person1.get_full_name())

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())
#print(person2.get_full_name())
#person2.change_last_name("Tyurina")
print(person2.get_name())
#print(person2.get_full_name())

# Output for person1:
#1. line 26 it call the method get_name() from the Parent class the output will be "Elizaveta Alekseeva" as the Child class in inheriting the properties from the Parent class.
#2. line 27 it call the get_full_name() method from the Child class the output will be "Elizaveta Alekseeva " as the check statement will get skip entirely.
#3. line 28 we call the change_last_name() method to change last name of person1, the method started as an empty array then it append (end of the array)to it the new parameter value given output "Elezaveta Tyurina". CORRECTION: it will append the old last_name
#4. I think that line 29 and 30 will print as the 26 and 27, as they do not interact with the new array created by change_last_name method(). CORRECTION:  line 30 the list now have leng 1, means it will add suffix value at the end.

#Output for person2:
#1. line 33 and 36 the output will be similar to line 26
#2. lines 34, 35, 37 all they will throw an error  as the inheritance work as waterfall a child can access parent methods, however a parent class can not.
