import unittest
import Intersect_Function


class MyTestCase(unittest.TestCase):
    # here i'm checking my intersect_distance function output
    def test_myTestCase(self):
        line_1 = {(2, -1), (2, 1)}
        angle = 45
        right_output = ({(2, -1), (2, 1)}, 2.83) # the correct output
        result = Intersect_Function.intersect_distance(angle, line_1) # the function output
        self.assertEqual(result, right_output ) # checking equality


if __name__ == '__main__':
    unittest.main()
