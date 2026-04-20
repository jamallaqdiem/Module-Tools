from dataclasses import dataclass
from enum import Enum
from typing import List
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
    Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH)
]


user_name = input(f"PLease enter your name: ")

user_age = input(f"PLease enter your age: ")
try :
    user_age_int = int(user_age)
except ValueError :
    sys.stderr.write(f" Error: {user_age} should be an number")
    sys.exit(1)
    
user_os = input(f"PLease enter your preferred os: ")
try: 
   os_type = OperatingSystem(user_os)
    
except ValueError :
    sys.stderr.write(f"Error: {user_os}  should be a valid OS")
    sys.exit(1)    


new_data = Person(user_name,user_age_int,os_type)
amount_os =find_possible_laptops(laptops,new_data)
len_os =len(amount_os)
print(f"we found {len_os} available")

counts ={}
for os in OperatingSystem:
    count =0
    
    for laptop in laptops:
        if laptop.operating_system ==os:
            count+=1
        counts[os]=count    
        
max_value= max(counts.values())
better_choices = [max_value]

better_choices=[]
for os, count in counts.items():
    if count == max_value:
        better_choices.append(os.value)
        

multi_options = " OR ".join(better_choices)

if max_value > len_os:
    print(f"We have better choices, you should consider: {multi_options}")
elif max_value==len_os :
    print(f"we have multiple choices: {multi_options}, however {os_type.value} is still a good choice.")
