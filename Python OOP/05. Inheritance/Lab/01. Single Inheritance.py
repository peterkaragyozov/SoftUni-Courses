class Animal:
    def eat(self):
        return "eating..."


class Dog(Animal):
    def bark(self):
        return "barking..."


d = Dog()
print(d.eat())
print(d.bark())