import unittest
from class_field import *


class FieldTest(unittest.TestCase):
    field = Field()

    def test_in_rigth_down_corner(self):
        self.assertIsNone(field.add_ship(1, 10, 10, "v"))

    def test_in_rigth_up_corner(self):
        self.assertIsNone(field.add_ship(1, 10, 1, "v"))

    def test_in_left_up_corner(self):
        self.assertIsNone(field.add_ship(1, 1, 1, "v"))

    def test_in_left_down_corner(self):
        self.assertIsNone(field.add_ship(1, 1, 10, "v"))
