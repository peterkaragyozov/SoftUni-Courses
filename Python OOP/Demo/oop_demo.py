class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        if self.brand == "Peugeot":
            return f"My personal car is a {self.brand} {self.model} from the {self.year} year."
        elif self.brand == "Mazda":
            return f"Mila's car is a {self.brand} {self.model} from the {self.year} year."
        return f"Some other person's car is a {self.brand} {self.model} from the {self.year} year."


print(Car("Peugeot", "3008", 2020))
print(Car("Mazda", "3", 2011))
print(Car("Mercedes-Benz", "S-class", 2018))
print(Car("BMW", "3er", 2008))
print(Car("Mitsubishi", "Lancer", 2006))
