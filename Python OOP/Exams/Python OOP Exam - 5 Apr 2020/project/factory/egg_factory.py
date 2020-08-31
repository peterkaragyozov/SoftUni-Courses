from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)
        self.ingredients = dict()

    def add_ingredient(self, ingredient_type, quantity):
        if ingredient_type in ["chicken egg", "quail egg"] and quantity <= self.capacity:
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = 0
            self.ingredients[ingredient_type] += quantity
            self.capacity -= quantity
        elif ingredient_type in ["chicken egg", "quail egg"] and quantity > self.capacity:
            raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type, quantity):
        if ingredient_type in self.ingredients and quantity <= self.ingredients[ingredient_type]:
            self.ingredients[ingredient_type] -= quantity
        elif ingredient_type in self.ingredients and quantity > self.ingredients[ingredient_type]:
            raise ValueError("Ingredient quantity cannot be less than zero")
        elif ingredient_type not in self.ingredients:
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients
