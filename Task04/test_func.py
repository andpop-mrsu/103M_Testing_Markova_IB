import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TriangleFunctionTests(unittest.TestCase):
    def test_all_equal(self):
        self.assertEqual(get_triangle_type(10, 10, 10), "equilateral")

    def test_two_equal(self):
        self.assertEqual(get_triangle_type(10, 10, 7), "isosceles")

    def test_different_sides(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_invalid_data(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 0, 0)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 5, 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 5, 5)

if __name__ == "__main__":
    unittest.main()