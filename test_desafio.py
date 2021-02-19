import unittest
from unittest import result
import desafio

class TestDesafio(unittest.TestCase):

    def test_problema_1(self):
        result = desafio.time_converter("6:47:00PM")
        self.assertEqual(result, "18:47:00")

        result = desafio.time_converter("12:47:00PM")
        self.assertEqual(result, "12:47:00")

        result = desafio.time_converter("12:47:00AM")
        self.assertEqual(result, "00:47:00")

        result = desafio.time_converter("12:47:00PM")
        self.assertEqual(result, "12:47:00")

        result = desafio.time_converter("3:1:6PM")
        self.assertEqual(result, "15:01:06")


    def test_problema_2(self):
        result = desafio.diagonals_diff([[1,2,3],
                                         [4,5,6],
                                         [9,8,9]])
        self.assertEqual(result, 2)

        result = desafio.diagonals_diff([[1,2,-3],
                                         [4,-5,6],
                                         [-9,8,9]])
        self.assertEqual(result, 22)


    def test_problema_3(self):
        result = desafio.div_sum([1, 3 , 2, 6, 1, 2], 3)
        self.assertEqual(result, 5)

        result = desafio.div_sum([1, 3 , 2, 6, 1, 2], 77)
        self.assertEqual(result, 0)

        result = desafio.div_sum([0, 1, 3 , 2, 6, 1, 2], 3)
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()