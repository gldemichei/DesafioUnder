import unittest
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

if __name__ == '__main__':
    unittest.main()