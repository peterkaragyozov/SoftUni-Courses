from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)
        self.ingredients = dict()
        self.recipes = dict()
        self.products = dict()

    def add_ingredient(self, ingredient_type, quantity):
        if ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"] and quantity <= self.capacity:
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = 0
            self.ingredients[ingredient_type] += quantity
            self.capacity -= quantity
        elif ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"] and quantity > self.capacity:
            raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type, quantity):
        if ingredient_type in self.ingredients and quantity <= self.ingredients[ingredient_type]:
            self.ingredients[ingredient_type] -= quantity
        elif ingredient_type in self.ingredients and quantity > self.ingredients[ingredient_type]:
            raise ValueError("Ingredient quantity cannot be less than zero")
        elif ingredient_type not in self.ingredients:
            raise KeyError("No such product in the factory")

    def add_recipe(self, recipe_name, recipe: dict):
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = 0
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name):
        if recipe_name in self.recipes:
            if recipe_name not in self.products:
                self.products[recipe_name] = 0
            self.products[recipe_name] += 1
            # del self.ingredients
        else:
            raise TypeError("No such recipe")

