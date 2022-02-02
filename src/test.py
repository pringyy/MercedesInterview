import unittest
from main import function1, function2, function3, function4, floatArrayToString
from decimal import *
import sys



class TestFunctions(unittest.TestCase):

    #Tests for function1() in main.py:
    def test_function1_allArgumentsAreValidInputs_shouldReturnExpectedValues(self):
        self.assertEqual(function1([Decimal('0.5'), Decimal('1.2'), Decimal('2.5')], Decimal('2'), Decimal('1')), [Decimal('2'), Decimal('3.4'), Decimal('6')], "[Decimal('2'), Decimal('3.4'), Decimal('6')]")
        self.assertEqual(function1([Decimal('0.814723686393179'), Decimal('0.905791937075619'), Decimal('0.126986816293506')], Decimal('2'), Decimal('0.5')), [Decimal('2.1294473727863580'), Decimal('2.3115838741512380'), Decimal('0.7539736325870120')], "Should be [Decimal('2.1294473727863580'), Decimal('2.3115838741512380'), Decimal('0.7539736325870120')]")
        self.assertEqual(function1([Decimal('5'), Decimal('3'), Decimal('1'), Decimal('10')], Decimal('5'), Decimal('2')), [Decimal('27'), Decimal('17'), Decimal('7'), Decimal('52')], "Should be [Decimal('27'), Decimal('17'), Decimal('7'), Decimal('52')]")
        self.assertEqual(function1([Decimal('0.5'), Decimal('1.2'), Decimal('2.5')], Decimal('2'), Decimal('1')), [Decimal('2'), Decimal('3.4'), Decimal('6')], "[Decimal('2'), Decimal('3.4'), Decimal('6')]")
    
    def test_function1_firstArgumentIsNotListType_shouldThrowError(self):
        self.assertRaises(TypeError, function1("Decimal('0.5'), Decimal('1.2'), Decimal('2.5')", Decimal('2'), Decimal('1')))
        self.assertRaises(TypeError, function1(5, Decimal('2'), Decimal('1')))
        self.assertRaises(TypeError, function1(True, Decimal('2'), Decimal('1')))
        self.assertRaises(TypeError, function1(1.21321312, Decimal('2'), Decimal('1')))

    def test_function1_secondArgumentIsNotDecimalType_shouldThrowError(self):
        self.assertRaises(TypeError, function1([Decimal('0.524234234'), Decimal('1.223423423'), Decimal('2.523423423')], 2.512321321, Decimal('1')))
        self.assertRaises(TypeError, function1([Decimal('0.12312412421'), Decimal('11.212312312'), Decimal('2.51312')], "Hello", Decimal('1')))
        self.assertRaises(TypeError, function1([Decimal('0.523432'), Decimal('1.23434'), Decimal('2.5')], True, Decimal('1')))
        self.assertRaises(TypeError, function1([Decimal('0.5'), Decimal('1.2'), Decimal('2.5')], 54, Decimal('1')))

    def test_function1_thirdArgumentIsNotDecimalType_shouldThrowError(self):
        self.assertRaises(TypeError, function1([Decimal('0.5'), Decimal('1.2'), Decimal('2.5')], Decimal('1'), 2.512321321))
        self.assertRaises(TypeError, function1([Decimal('0.5'), Decimal('1.2'), Decimal('2.5')], Decimal('1'), "Hello"))
        self.assertRaises(TypeError, function1([Decimal('0.5'), Decimal('1.2'), Decimal('2.5')], Decimal('1'), True))
        self.assertRaises(TypeError, function1([Decimal('0.5'), Decimal('1.2'), Decimal('2.5')], Decimal('1'), 54))


    #Tests for function2() in main.py:
    def test_function2_allArgumentsAreValidInputs_shouldReturnExpectedValues(self):
        output1, output2 = function2([Decimal('1'),Decimal('2')], [Decimal('3'),Decimal('4')])
        self.assertEqual(output1, [Decimal('4'),Decimal('6')])
        self.assertEqual(output2, Decimal('5'))
        output1, output2 = function2([Decimal('1.382932'),Decimal('2.12321312'),Decimal('0.12321312'),Decimal('0.1')], [Decimal('3.12312'),Decimal('4.21312'),Decimal('6.312'),Decimal('0.56')])
        self.assertEqual(output1, [Decimal('4.506052'),Decimal('6.33633312'), Decimal('6.43521312'),Decimal('0.66')])
        self.assertEqual(output2, Decimal('4.48439956'))
    
    def test_function2_firstArgumentIsNotListType_shouldThrowError(self):
        self.assertRaises(TypeError, function2(None, [1, 2, 3, 4, 5]))
        self.assertRaises(TypeError, function2("Hello",[Decimal('1'),Decimal('2')]))
        self.assertRaises(TypeError, function2(123456, [Decimal('1.382932'),Decimal('2.12321312'),Decimal('0.12321312'),Decimal('0.1')]))
        self.assertRaises(TypeError, function2(Decimal('5.2123213'), [Decimal('4'),Decimal('6')]))
    
    def test_function2_secondArgumentIsNotListType_shouldThrowError(self):
        self.assertRaises(TypeError, function2([1, 2, 3, 4, 5], None))
        self.assertRaises(TypeError, function2([Decimal('1'),Decimal('2')], "Hello"))
        self.assertRaises(TypeError, function2([Decimal('1.382932'),Decimal('2.12321312'),Decimal('0.12321312'),Decimal('0.1')], 123456))
        self.assertRaises(TypeError, function2([Decimal('4'),Decimal('6')], Decimal('5.2123213')))
    
    #Tests for function3() in main.py:
    def test_function3_allArgumentsAreValidInputs_shouldReturnExpectedValues(self):
        self.assertEqual(function3([0,2,4,10]), [0, 0.5, 0.25, 0.1], "Should be [0, 0.5, 0.25, 0.1]")
       
    def test_function3_onlyArgumentIsNotListType_shouldThrowError(self):
        self.assertRaises(TypeError, function3("hello"))
        self.assertRaises(TypeError, function3({'a':'b', 'c':'d'}))
        self.assertRaises(TypeError, function3(Decimal('1.212131213213')))
        self.assertRaises(TypeError, function3(1021312312321))

    def test_function3_inputListContainsNumberZero_shouldHandleDivisionByZeroError(self):
        self.assertEqual(function3([Decimal('0'),Decimal('0.25'),Decimal('1.25'),Decimal('10.0')]), [Decimal('0'), Decimal('4'), Decimal('0.8'), Decimal('0.1')], "Should be [Decimal(0), Decimal(4), Decimal(0.8), Decimal(0.1)]")
        self.assertEqual(function3([10, 0, 25, 20]), [0.1, 0, 0.04, 0.05], "Should be [0.1, 0, 0.04, 0.05]") 

     #Tests for function4() in main.py:
    def test_function4_allArgumentsAreValidInputs_shouldReturnExpectedValues(self):
        self.assertEqual(function4([Decimal('1'),Decimal('0.25'),Decimal('1.25'),Decimal('10.0')], Decimal('2.4')), [Decimal('3.4'), Decimal('2.65'), Decimal('3.65'), Decimal('12.4')], "Should be [Decimal('2.4'), Decimal('2.65'), Decimal('3.65'), Decimal('12.4')")
    
    def test_function4_firstArgumentsIsNotListType_shouldReturnExpectedValues(self):
        self.assertRaises(TypeError, function4(("hello"), Decimal('1.22324224')))
        self.assertRaises(TypeError, function4({'a':'b', 'c':'d'}, Decimal('2.12312312')))
        self.assertRaises(TypeError, function4(Decimal('1.212131213213'), Decimal('0.1231241241')))
        self.assertRaises(TypeError, function4(1021312312321, Decimal('0.1231241241')))

    
    #Tests for floatArrayToString() in main.py:
    def test_floatArrayToString(self):
        self.assertEqual(floatArrayToString([Decimal(1.23123124), Decimal(2.21312312312), Decimal(0.21312312312), Decimal(100.1232131221)]), "1.23123124, 2.21312312312, 0.21312312312, 100.1232131221", "Should be 1.23123124, 2.21312312312, 0.21312312312, 100.1232131221")
    
    
    print("Unit tests complete.")




if __name__ == '__main__':
    print("Performing unit tests...")
    unittest.main()

