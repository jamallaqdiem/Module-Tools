import datetime as dt # we import the datetime module

# this is similar to new Date() object in js, but only getting the date not hours etc.

class Person:
    def __init__(self, name: str, preferred_os: str, dob: dt.date):
        self.name = name
        self.preferred_operating_system = preferred_os 
        self.date_of_birth = dob

    def is_adult(self) -> bool:
        today = dt.date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            # if the birthday date did not happened yet ad  -1 else skip it, we use full age
            age -= 1
        return age >= 18

imran_dob = dt.date(1986, 12, 24)
imran = Person("Imran", "Ubuntu", imran_dob) 

print(f"{imran.name} is adult: {imran.is_adult()}")
