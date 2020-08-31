from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name, chocolate_factory: ChocolateFactory, egg_factory: EggFactory, paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = dict()

    def add_chocolate_ingredient(self, type_c, quantity):
        self.chocolate_factory.add_ingredient(type_c, quantity)

    def add_egg_ingredient(self, type_i, quantity):
        self.egg_factory.add_ingredient(type_i, quantity)

    def add_paint_ingredient(self, type_i, quantity):
        self.paint_factory.add_ingredient(type_i, quantity)

    def make_chocolate(self, recipe):
        self.chocolate_factory.make_chocolate(recipe)
        if recipe not in self.storage:
            self.storage[recipe] = 0
        self.storage[recipe] += 1

    def paint_egg(self, color, egg_type):
        try:
            self.egg_factory.remove_ingredient(egg_type, 1)
            self.paint_factory.remove_ingredient(color, 1)
            painted_egg = f"{color} {egg_type}"
            if painted_egg not in self.storage:
                self.storage[painted_egg] = 0
            self.storage[painted_egg] += 1
        except ValueError:
            raise ValueError("Invalid commands")

    def __repr__(self):
        storage_list = [f"{{{k}}}: {{{v}}}" for k, v in self.storage.items()]
        x = "\n".join(storage_list)
        return f"Shop name: {self.name}\nShop Storage:\n{x}"
