from dataclasses import dataclass
from pydantic import BaseModel

# @dataclass
# class Person:
#     name: str
#     city: str

class Person(BaseModel):
    name: str
    city: str
    age: int


if __name__ == '__main__':
    p1 = Person(name='vishwas',city='Bangalore',age='23')
    print(f'The Person is {p1.name}, his age is {p1.age}')