class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p = Person("Peter", "Karagyozov", 27)
print(p.__dict__)