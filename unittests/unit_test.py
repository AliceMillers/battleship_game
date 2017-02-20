import unittest
from class_field import *

class MyTest(unittest.TestCase):
    def test(self):
        field = Field()
        field.add_ship(1, 10, 10, "v")