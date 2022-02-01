import unittest
from main import function1, function2, function3, function4, floatArrayToString


class TestFunctions(unittest.TestCase):

    def test_function1_listOfFloats_ShouldGiveDesiredOutput(self):
        self.assertEqual(function1([1,2], 2, 1), [3, 5], "Should be [2.5, 4.5]")

    def test_function1_listOfFloatsContainsAString_ShouldThrowError(self):
        self.assertRaises(TypeError, function1(["hello",2.21312312312,0.21312312312,100.1232131221], 2, 1))

    def test_function2(self):
        d1, d2 = function2([1,2], [3,4])
        self.assertEqual(d1, [4,6])
        self.assertEqual(d2, 5)
    
    def test_function3(self):
        self.assertEqual(function3([1,2,4,10]), [1, 0.5, 0.25, 0.1], "Should be [1, 0.5, 0.25, 0.1]")

    def test_function3_2(self):
        self.assertEqual(function3([0,2,4,10]), [0, 0.5, 0.25, 0.1], "Should be [0, 0.5, 0.25, 0.1]")

    def test_floatArrayToString(self):
        self.assertEqual(floatArrayToString([1.23123124,2.21312312312,0.21312312312,100.1232131221]), "1.23123124, 2.21312312312, 0.21312312312, 100.1232131221", "Should be 1.23123124, 2.21312312312, 0.21312312312, 100.1232131221")
    
    
    print("Unit tests complete.")

if __name__ == '__main__':
    print("Performing unit tests...")
    unittest.main()