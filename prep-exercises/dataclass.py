from  dataclasses import dataclass
import datetime as dt

@dataclass(frozen=True)
class Person:
    name: str 
    preferred_operating_system: str
    date_of_birth: dt.date
    
    def is_adult(self) -> bool:
        today = dt.date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age >= 18
imran = Person("Imran", "Ubuntu", dt.date(2009, 1, 24))
print(f"Is Imran an adult? {imran.is_adult()}")


