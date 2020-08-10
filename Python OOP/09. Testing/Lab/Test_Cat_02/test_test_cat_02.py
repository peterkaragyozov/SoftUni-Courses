import unittest

from Testing.Test_Cat_02.test_cat_02 import Cat


class TestCat(unittest.TestCase):
    def test_catEat_shouldIncreaseSizeBy1(self):
        name = 'Gosho'

        cat = Cat(name)
        cat.eat()

        self.assertEqual(1, cat.size)

    def test_catEat_shouldSetFedToTrue(self):
        name = 'Gosho'

        cat = Cat(name)
        cat.eat()

        self.assertTrue(cat.fed)

    def test_catEat_whenFed_shouldRaiseException(self):
        name = 'Gosho'

        cat = Cat(name)
        cat.eat()

        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertIsNotNone(context.exception)

    def test_catSleep_whenNotFed_shouldRaiseException(self):
        name = 'Gosho'

        cat = Cat(name)
        with self.assertRaises(Exception) as context:
            cat.sleep()

        self.assertIsNotNone(context.exception)

    def test_cat_when_should(self):
        name = 'Gosho'

        cat = Cat(name)

        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
