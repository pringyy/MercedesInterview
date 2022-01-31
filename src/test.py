import unittest
from main import function1, function2, function3, function4, averageValue

class TestFunctions(unittest.TestCase):

    def test_function1(self):
        self.assertEqual(function1([1,2]), [2.5, 4.5], "Should be [2.5, 4.5]")

    def test_function2(self):
        self.assertEqual(function2([1,2], [3,4]), 5, "Should be 5")
    
    def test_function3(self):
        self.assertEqual(function3([1,2,4,10]), [1, 0.5, 0.25, 0.1], "Should be [1, 0.5, 0.25, 0.1]")

    def test_function3_2(self):
        self.assertEqual(function3([0,2,4,10]), [0, 0.5, 0.25, 0.1], "Should be [0, 0.5, 0.25, 0.1]")

    def test_averageValue(self):
        self.assertEqual(averageValue([1,2,4,10]), 4.25, "Should be 4.25")
  
if __name__ == '__main__':
    unittest.main()