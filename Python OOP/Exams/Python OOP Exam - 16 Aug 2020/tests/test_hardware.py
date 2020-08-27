import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("SSD", "Heavy", 100, 120)

    def test_set_attr(self):
        self.assertEqual(self.hardware.name, "SSD")
        self.assertEqual(self.hardware.type, "Heavy")
        self.assertEqual(self.hardware.memory, 120)
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.software_components, [])

    def test_successful_install(self):
        soft = Software("Skype", "Express", 60, 40)
        self.hardware.install(soft)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_unsuccessful_install(self):
        soft = Software("NotSkype", "Express", 200, 240)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(soft)
            self.assertEqual(str(ex), "Software cannot be installed")

    def test_uninstall(self):
        soft = Software("Skype", "Express", 60, 40)
        self.hardware.install(soft)
        self.hardware.uninstall(soft)
        self.assertEqual(self.hardware.software_components, [])

    def test_unsuccessful_uninstall(self):
        soft = Software("Skype", "Express", 60, 40)
        softy = Software("Discord", "Express", 20, 20)
        self.hardware.install(soft)
        with self.assertRaises(Exception) as ex:
            self.hardware.uninstall(softy)
            self.assertEqual(str(ex), "Some of the components do not exist")

    def test_not_working_install_message(self):
        software = Software("Skype", "Express", 100, 10)
        self.hardware = Hardware("SSD", "Heavy", 10, 12)
        try:
            self.hardware.install(software)
        except Exception as ex:
            self.assertEqual(str(ex), "Software cannot be installed")


if __name__ == "__main__":
    unittest.main()
