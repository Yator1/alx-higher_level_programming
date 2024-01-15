"""
This module contains tests for the module models.square.py
it contain one class test_Square
"""

from models.rectangle import Rectangle
from models.square import Square
import unittest


class test_Square(unittest.TestCase):
    """ Test all possible cases of class Square"""
    def test_inheritance(self):
        """ Test inheritance from class Rectangle"""
        s1 = Square(5)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertIsInstance(s1, Rectangle)

    def test_attributes(self):
        """Test for attribute assignment"""
        s1 = Square(3)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

        s2 = Square(5, 3, 7, 8)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 7)
        self.assertEqual(s2.id, 8)

    def test_area(self):
        """Test area of square"""
        s1 = Square(9)
        self.assertEqual(s1.area(), 81)

        s2 = Square(4)
        self.assertEqual(s2.area(), 16)

    def test_str(self):
        """Test the string represantaion"""
        s1 = Square(5, 2, 3, 9)
        self.assertEqual(str(s1), "[Square] (9) 2/3 - 5")

    def test_update(self):
        """Test the update method"""
        s1 = Square(9, 6, 4)
        s1.update(13)
        s1.update(y=12)
        self.assertEqual(s1.id, 13)
        self.assertEqual(s1.size, 9)
        self.assertEqual(s1.width, 9)
        self.assertEqual(s1.height, 9)
        self.assertEqual(s1.x, 6)
        self.assertEqual(s1.y, 12)

        s1.update(17, 12, 3, 6)
        self.assertEqual(s1.id, 17)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.width, 12)
        self.assertEqual(s1.height, 12)
    
    def test_setter(self):
        """Test the setter and getter"""
        s1 = Square(9, 12)
        with self.assertRaises(TypeError):
            s1.size = "1sc"
        with self.assertRaises(ValueError):
            s1.size = -2
        self.assertEqual(s1.size, 9)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s1 = Square(9, 3, 5, 7)
        expected_dict = {
            'id': 7,
            'size': 9,
            'x': 3,
            'y': 5
            }
        self.assertEqual(s1.to_dictionary(), expected_dict)
       

if __name__ == '__main__':
    unittest.main()
