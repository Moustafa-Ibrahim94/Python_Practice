import unittest
import Intersect_Function


class MyTestCase(unittest.TestCase):
    def test_myTestCase(self):
        line_1 = {(2, -1), (2, 1)}
        angle = 45
        result = Intersect_Function.intersect_distance(angle, line_1)
        self.assertEqual(result, ({(2, -1), (2, 1)}, 2.83))


if __name__ == '__main__':
    unittest.main()