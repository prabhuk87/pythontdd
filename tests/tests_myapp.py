import unittest
from myapp.myapp import Myapp


class MyappTest(unittest.TestCase):
    def test_addition(self):
        app = Myapp()
        self.assertEqual(app.addition(2, 2), 4)

    def test_subtraction(self):
        app = Myapp()
        self.assertEqual(app.subtraction(4, 2), 2)

    def test_multiplication(self):
        app = Myapp()
        self.assertEqual(app.multiplication(2, 2), 4)

    def test_division(self):
        app = Myapp()
        self.assertEqual(app.division(2, 2), 1)
