class Person:
    __slots__ = ['name', 'city']
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
class User(Person):
    def __init__(self, name, city, age):
        super().__init__(name, city)
        self.age  = age

if __name__ == '__main__':
    p1 = Person('vishwas','bangalore')
    print(p1.name)
    p2 = User('Arjun', 'bangalore', 23)
    print(p2.name)
    p1.salary = 25000
    print(p1.salary)
    print(p1.__dict__)