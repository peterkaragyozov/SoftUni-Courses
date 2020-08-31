import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("LEKO", 20)
        self.paint_factory.add_ingredient("red", 1)

    def test_add_ingredient_if_ingredient_not_allowed(self):
        with self.assertRaises(TypeError):
            self.paint_factory.add_ingredient("BMW", 10)

    def test_add_ingredient_if_space(self):
        with self.assertRaises(ValueError):
            self.paint_factory.add_ingredient("green", 100)

    def test_add_non_existing_ingredient(self):
        self.paint_factory.add_ingredient("green", 1)
        result = self.paint_factory.products
        self.assertEqual(result, {"red": 1, "green": 1})

    def test_add_existing_ingredient(self):
        self.paint_factory.add_ingredient("green", 1)
        self.paint_factory.add_ingredient("green", 1)
        result = self.paint_factory.ingredients
        self.assertEqual(result, {"red": 1, "green": 2})

    def test_remove_ingredient_key_error(self):
        with self.assertRaises(KeyError):
            self.paint_factory.remove_ingredient("Sony", 100)

    def test_remove_ingredient_value_error(self):
        self.paint_factory.add_ingredient("green", 1)
        with self.assertRaises(ValueError):
            self.paint_factory.remove_ingredient("green", 100)

    def test_remove_ingredient(self):
        self.paint_factory.add_ingredient("green", 1)
        self.paint_factory.add_ingredient("green", 1)
        self.paint_factory.remove_ingredient("green", 1)
        result = self.paint_factory.ingredients
        self.assertEqual(result, {"red": 1, "green": 1})
        pass

    def test_return_ingredients_property(self):
        self.paint_factory.add_ingredient("green", 1)
        result = self.paint_factory.products
        self.assertEqual(result, {"red": 1, "green": 1})

