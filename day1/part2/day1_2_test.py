import unittest

from day1_2 import fuelRequired

class fuelRequiredTest(unittest.TestCase):
    def test_mass_0(self):
        self.assertEqual(fuelRequired("0"), 0)

    def test_mass_8(self):
        self.assertEqual(fuelRequired("8"), 0)

    def test_mass_9(self):
        self.assertEqual(fuelRequired("9"), 1)

    def test_mass_12(self):
        self.assertEqual(fuelRequired("12"), 2)

    def test_mass_14(self):
        self.assertEqual(fuelRequired("14"), 2)

    def test_mass_1969(self):
        self.assertEqual(fuelRequired("1969"), 966)

    def test_mass_100756(self):
        self.assertEqual(fuelRequired("100756"), 50346)

from day1_2 import totalFuelFromFile

class totalFuelTest(unittest.TestCase):
    def test_file_1(self):
        self.assertEqual(totalFuelFromFile("test1.txt"), 5)
    def test_file_2(self):
        self.assertEqual(totalFuelFromFile("test2.txt"), 967)

if __name__ == "__main__":
    unittest.main()
