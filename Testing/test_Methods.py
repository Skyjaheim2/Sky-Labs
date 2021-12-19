import sys
sys.path.append(r"C:\Users\jahei\OneDrive\Documents\Flask-Projects\Flask\Personal-Projects\Computer Algebra") # Add path where project is located to allow for import of application
import os
import unittest
from Methods import *
# from test import *


# python -m unittest test_Methods.py

class TestCalc(unittest.TestCase):
    # THIS RUNS 'ONCE' BEFORE ALL THE TESTS
    @classmethod
    def setUpClass(cls):
        pass

    # THIS RUNS 'ONCE' AFTER ALL THE TESTS END
    @classmethod
    def tearDownClass(cls):
        pass

    # THIS WILL RUN BEFORE EVERY TEST
    def setUp(self) -> None:
        pass


    # # TEST isSingleExpression
    # def test_isSingleExpression(self):
    #     expressionsAndResults = [
    #         {
    #             'expression': '1262',
    #             'result': True,
    #         },
    #         {
    #             'expression': '-17264',
    #             'result': True,
    #         },
    #         {
    #             'expression': '128+92',
    #             'result': False,
    #         },
    #         {
    #             'expression': '-2742-8242',
    #             'result': False,
    #         },
    #         {
    #             'expression': '476*12',
    #             'result': False,
    #         },
    #
    #     ]
    #
    #     for item in expressionsAndResults:
    #         self.assertEqual(isSingleExpression(item['expression']), item['result'], f"Expression: {item['expression']}")
    #
    # # TEST getOperationToPerform
    # def test_getOperationToPerform(self):
    #     expressionAndResults = [
    #         {
    #             'expression': '146+481',
    #             'result': 'arithmetic-add-single',
    #         },
    #         {
    #             'expression': '-148+482',
    #             'result': 'add-subtract-only',
    #         },
    #         {
    #             'expression': '2894-287+834+984-2974',
    #             'result': 'add-subtract-only',
    #         },
    #         {
    #             'expression': '183*822',
    #             'result': 'arithmetic-multiply-single',
    #         },
    #         {
    #             'expression': '-282*824',
    #             'result': 'arithmetic-multiply-single',
    #         },
    #         {
    #             'expression': '-925*-3298',
    #             'result': 'arithmetic-multiply-single',
    #         },
    #         {
    #             'expression': '274*732*826*636*816',
    #             'result': 'multiply-only',
    #         },
    #         {
    #             'expression': '-498*-842*-9842*824',
    #             'result': 'multiply-only',
    #         },
    #         {
    #             'expression': '284+724-2848*12+734-12*14',
    #             'result': 'general-arithmetic',
    #         },
    #         {
    #             'expression': '1+27*712*12-5',
    #             'result': 'general-arithmetic',
    #         },
    #         {
    #             'expression': '123',
    #             'result': 'no-operation',
    #         },
    #         {
    #             'expression': 'sqrt{2}',
    #             'result': 'radical',
    #         },
    #         {
    #             'expression': 'sqrt{5*3+2}',
    #             'result': 'radical',
    #         },
    #         {
    #             'expression': '1+sqrt{2}',
    #             'result': 'general-arithmetic',
    #         },
    #         {
    #             'expression': '5*2+sqrt{1+2+3}',
    #             'result': 'general-arithmetic',
    #         },
    #         {
    #             'expression': 'sqrt{(5+3*2)^2}',
    #             'result': 'radical',
    #         }
    #
    #     ]
    #
    #     for item in expressionAndResults:
    #         Expression = ArithmeticExpression(item['expression'])
    #         self.assertEqual(Expression.getOperationToPerform(), item['result'], f"Expression: {item['expression']}")
    #
    # # TEST evaluateArithmetic
    # def test_evaluateArithmetic(self):
    #     expressionsAndResults = [
    #         # ADDITION AND SUBTRACTION
    #         {
    #             'expression': '1+1',
    #             'result': '2',
    #             'steps': {1: {'step': 'Add the first and second term: 1+1 = 2', 'simplification': '2'}},
    #         },
    #         {
    #             'expression': '1+2+3+4+5+6',
    #             'result': '21',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: 1+2+3+4+5+6 = 21', 'simplification': '21'}},
    #         },
    #         {
    #             'expression': '1+2+5+8-872+92-3',
    #             'result': '-767',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: 1+2+5+8-872+92-3 = -767', 'simplification': '-767'}},
    #         },
    #         {
    #             'expression': '2+-+-+-3',
    #             'result': '-1',
    #             'steps': {1: {'step': 'Apply rule: a+-b = a-b', 'simplification': '2---3'},
    #                       2: {'step': 'Apply rule: a--b = a+b', 'simplification': '2+-3'},
    #                       3: {'step': 'Apply rule: a+-b = a-b', 'simplification': '2-3'},
    #                       4: {'step': 'Subtract the first and second term: 2-3 = -1', 'simplification': '-1'}},
    #         },
    #         # MULTIPLICATION
    #         {
    #             'expression': '1*2*3*4*5',
    #             'result': '120',
    #             'steps': {1: {'step': 'Multiply [left to right]: 1*2*3*4*5 = 120', 'simplification': '120'}},
    #         },
    #         {
    #             'expression': '-2*-5*-3',
    #             'result': '-30',
    #             'steps': {1: {'step': 'Multiply [left to right]: -2*-5*-3 = -30', 'simplification': '-30'}},
    #         },
    #         # EXPONENTS
    #         {
    #             'expression': '2^2',
    #             'result': '4',
    #             'steps': {1: {'step': 'Calculate exponent: 2^2 = 4', 'simplification': '4'}},
    #         },
    #         {
    #             'expression': '5^-3',
    #             'result': '0.008',
    #             'steps': {1: {'step': 'Calculate exponent: 5^-3 = 0.008', 'simplification': '0.008'}},
    #         },
    #         {
    #             'expression': '(-3)^2',
    #             'result': '9',
    #             'steps': {1: {'step': 'Calculate exponent: (-3)^2 = 9', 'simplification': '9'}},
    #         },
    #         {
    #             'expression': '-3^2',
    #             'result': '-9',
    #             'steps': {1: {'step': 'Calculate exponent: -3^2 = -9', 'simplification': '-9'}},
    #         },
    #         {
    #             'expression': '3.141592653589793^2',
    #             'result': '9.8696',
    #             'steps': {1: {'step': 'Calculate exponent: 3.141592653589793^2 = 9.8696', 'simplification': '9.8696'}},
    #         },
    #         {
    #             'expression': '2^{1+2+3}',
    #             'result': '64',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: 1+2+3 = 6', 'simplification': '2^{6}'},
    #                       2: {'step': 'Calculate exponent: 2^{6} = 64', 'simplification': '64'}},
    #         },
    #         {
    #             'expression': '3^{2+3*5}',
    #             'result': '129140163',
    #             'steps': {1: {'step': 'Apply PEMDAS: 2+3*5 = 2+(3*5)', 'simplification': '3^{2+(3*5)}'},
    #                       2: {'step': 'Multiply the first and second term: (3*5) = (15)', 'simplification': '3^{2+(15)}'},
    #                       3: {'step': 'Add the first and second term: 2+15 = 17', 'simplification': '3^{17}'},
    #                       4: {'step': 'Calculate exponent: 3^{17} = 129140163', 'simplification': '129140163'}},
    #         },
    #         {
    #             'expression': '3^{(2*3.141592653589793+2.718281828459045)}',
    #             'result': '19714.81294',
    #             'steps': {1: {'step': 'Apply PEMDAS: (2*3.141592653589793+2.718281828459045) = ((2*3.141592653589793)+2.718281828459045)', 'simplification': '3^{((2*3.141592653589793)+2.718281828459045)}'},
    #                       2: {'step': 'Multiply the first and second term: (2*3.141592653589793) = (6.28319)', 'simplification': '3^{((6.28319)+2.718281828459045)}'},
    #                       3: {'step': 'Add the first and second term: (6.28319+2.718281828459045) = (9.00147)', 'simplification': '3^{(9.00147)}'},
    #                       4: {'step': 'Calculate exponent: 3^{9.00147} = 19714.81294', 'simplification': '19714.81294'}},
    #         },
    #         {
    #             'expression': '2^{((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30)}',
    #             'result': '1.22875...e+406',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '2^{((1+(2+2)*3)+5)+(3*2+5)*(121)}'},
    #                       2: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '2^{((1+(2+2)*3)+5)+((3*2)+5)*121}'},
    #                       3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '2^{((1+(2+2)*3)+5)+((6)+5)*121}'},
    #                       4: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '2^{((1+(2+2)*3)+5)+(11)*121}'},
    #                       5: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '2^{((1+(4)*3)+5)+11*121}'},
    #                       6: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '2^{((1+(4*3))+5)+11*121}'},
    #                       7: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '2^{((1+(12))+5)+11*121}'},
    #                       8: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '2^{((13)+5)+11*121}'},
    #                       9: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '2^{(18)+11*121}'},
    #                       10: {'step': 'Apply PEMDAS: 18+11*121 = 18+(11*121)', 'simplification': '2^{18+(11*121)}'},
    #                       11: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '2^{18+(1331)}'},
    #                       12: {'step': 'Add the first and second term: 18+1331 = 1349', 'simplification': '2^{1349}'},
    #                       13: {'step': 'Calculate exponent: 2^{1349} = 1.22875...e+406', 'simplification': '1.22875...e+406'}},
    #         },
    #         {
    #             'expression': '1^{((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30)}',
    #             'result': '1',
    #             'steps': {1: {'step': 'Apply rule exponent: 1^a = 1', 'simplification': '1'}},
    #         },
    #         {
    #             'expression': '(1+2+3)^2',
    #             'result': '36',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: (1+2+3) = (6)', 'simplification': '(6)^2'},
    #                       2: {'step': 'Calculate exponent: 6^2 = 36', 'simplification': '36'}},
    #         },
    #         {
    #             'expression': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^3',
    #             'result': '2454911549',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(121))^3'},
    #                       2: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '(((1+(2+2)*3)+5)+((3*2)+5)*121)^3'},
    #                       3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '(((1+(2+2)*3)+5)+((6)+5)*121)^3'},
    #                       4: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '(((1+(2+2)*3)+5)+(11)*121)^3'},
    #                       5: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '(((1+(4)*3)+5)+11*121)^3'},
    #                       6: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '(((1+(4*3))+5)+11*121)^3'},
    #                       7: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '(((1+(12))+5)+11*121)^3'},
    #                       8: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '(((13)+5)+11*121)^3'},
    #                       9: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '((18)+11*121)^3'},
    #                       10: {'step': 'Apply PEMDAS: (18+11*121) = (18+(11*121))', 'simplification': '(18+(11*121))^3'},
    #                       11: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '(18+(1331))^3'},
    #                       12: {'step': 'Add the first and second term: (18+1331) = (1349)', 'simplification': '(1349)^3'},
    #                       13: {'step': 'Calculate exponent: 1349^3 = 2454911549', 'simplification': '2454911549'}},
    #         },
    #         {
    #             'expression': '(1+2+3)^{2+4+5}',
    #             'result': '362797056',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: 2+4+5 = 11', 'simplification': '(1+2+3)^{11}'},
    #                       2: {'step': 'Add and subtract [left to right]: (1+2+3) = (6)', 'simplification': '(6)^{11}'},
    #                       3: {'step': 'Calculate exponent: 6^{11} = 362797056', 'simplification': '362797056'}},
    #         },
    #         {
    #             'expression': '(1+2*3)^{2+4*5}',
    #             'result': '3909821048582988049',
    #             'steps': {1: {'step': 'Apply PEMDAS: 2+4*5 = 2+(4*5)', 'simplification': '(1+2*3)^{2+(4*5)}'},
    #                       2: {'step': 'Multiply the first and second term: (4*5) = (20)', 'simplification': '(1+2*3)^{2+(20)}'},
    #                       3: {'step': 'Add the first and second term: 2+20 = 22', 'simplification': '(1+2*3)^{22}'},
    #                       4: {'step': 'Apply PEMDAS: (1+2*3) = (1+(2*3))', 'simplification': '(1+(2*3))^{22}'},
    #                       5: {'step': 'Multiply the first and second term: (2*3) = (6)', 'simplification': '(1+(6))^{22}'},
    #                       6: {'step': 'Add the first and second term: (1+6) = (7)', 'simplification': '(7)^{22}'},
    #                       7: {'step': 'Calculate exponent: 7^{22} = 3909821048582988049', 'simplification': '3909821048582988049'}},
    #         },
    #         {
    #             'expression': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))}',
    #             'result': '2.43288...e+4222',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(121))^{(((1+(2+2)*3)+5)+(3*2+5)*(121))}'},
    #                       2: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '(((1+(2+2)*3)+5)+((3*2)+5)*121)^{(((1+(2+2)*3)+5)+((3*2)+5)*121)}'},
    #                       3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '(((1+(2+2)*3)+5)+((6)+5)*121)^{(((1+(2+2)*3)+5)+((6)+5)*121)}'},
    #                       4: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '(((1+(2+2)*3)+5)+(11)*121)^{(((1+(2+2)*3)+5)+(11)*121)}'},
    #                       5: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '(((1+(4)*3)+5)+11*121)^{(((1+(4)*3)+5)+11*121)}'},
    #                       6: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '(((1+(4*3))+5)+11*121)^{(((1+(4*3))+5)+11*121)}'},
    #                       7: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '(((1+(12))+5)+11*121)^{(((1+(12))+5)+11*121)}'},
    #                       8: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '(((13)+5)+11*121)^{(((13)+5)+11*121)}'},
    #                       9: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '((18)+11*121)^{((18)+11*121)}'},
    #                       10: {'step': 'Apply PEMDAS: (18+11*121) = (18+(11*121))', 'simplification': '(18+(11*121))^{(18+(11*121))}'},
    #                       11: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '(18+(1331))^{(18+(1331))}'},
    #                       12: {'step': 'Add the first and second term: (18+1331) = (1349)', 'simplification': '(1349)^{(1349)}'},
    #                       13: {'step': 'Calculate exponent: 1349^{1349} = 2.43288...e+4222', 'simplification': '2.43288...e+4222'}},
    #         },
    #         {
    #             'expression': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+(3*4+2)*(1+33+35+39+12))}',
    #             'result': '5.13416...e+5361',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: (1+33+35+39+12) = (120)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+(3*4+2)*(120))}'},
    #                       2: {'step': 'Apply PEMDAS: (3*4+2) = ((3*4)+2)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+((3*4)+2)*120)}'},
    #                       3: {'step': 'Multiply the first and second term: (3*4) = (12)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+((12)+2)*120)}'},
    #                       4: {'step': 'Add the first and second term: (12+2) = (14)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+(14)*120)}'},
    #                       5: {'step': 'Add the first and second term: (2+3) = (5)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(5)*5)+5)+14*120)}'},
    #                       6: {'step': 'Apply PEMDAS: (3+5*5) = (3+(5*5))', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(5*5))+5)+14*120)}'},
    #                       7: {'step': 'Multiply the first and second term: (5*5) = (25)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(25))+5)+14*120)}'},
    #                       8: {'step': 'Add the first and second term: (3+25) = (28)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((28)+5)+14*120)}'},
    #                       9: {'step': 'Add the first and second term: (28+5) = (33)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{((33)+14*120)}'},
    #                       10: {'step': 'Apply PEMDAS: (33+14*120) = (33+(14*120))', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(33+(14*120))}'},
    #                       11: {'step': 'Multiply the first and second term: (14*120) = (1680)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(33+(1680))}'},
    #                       12: {'step': 'Add the first and second term: (33+1680) = (1713)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(1713)}'},
    #                       13: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(121))^{1713}'},
    #                       14: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '(((1+(2+2)*3)+5)+((3*2)+5)*121)^{1713}'},
    #                       15: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '(((1+(2+2)*3)+5)+((6)+5)*121)^{1713}'},
    #                       16: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '(((1+(2+2)*3)+5)+(11)*121)^{1713}'},
    #                       17: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '(((1+(4)*3)+5)+11*121)^{1713}'},
    #                       18: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '(((1+(4*3))+5)+11*121)^{1713}'},
    #                       19: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '(((1+(12))+5)+11*121)^{1713}'},
    #                       20: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '(((13)+5)+11*121)^{1713}'},
    #                       21: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '((18)+11*121)^{1713}'},
    #                       22: {'step': 'Apply PEMDAS: (18+11*121) = (18+(11*121))', 'simplification': '(18+(11*121))^{1713}'},
    #                       23: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '(18+(1331))^{1713}'},
    #                       24: {'step': 'Add the first and second term: (18+1331) = (1349)', 'simplification': '(1349)^{1713}'},
    #                       25: {'step': 'Calculate exponent: 1349^{1713} = 5.13416...e+5361', 'simplification': '5.13416...e+5361'}},
    #         },
    #         {
    #           'expression': '2^3+5',
    #           'result': '13',
    #           'steps': {1: {'step': 'Apply PEMDAS: 2^3+5 = (2^3)+5', 'simplification': '(2^3)+5'},
    #                     2: {'step': 'Calculate exponent: (2^3) = (8)', 'simplification': '(8)+5'},
    #                     3: {'step': 'Add the first and second term: 8+5 = 13', 'simplification': '13'}},
    #         },
    #         {
    #             'expression': '2^3+1+2+3+4',
    #             'result': '18',
    #             'steps': {1: {'step': 'Apply PEMDAS: 2^3+1+2+3+4 = (2^3)+1+2+3+4', 'simplification': '(2^3)+1+2+3+4'},
    #                       2: {'step': 'Calculate exponent: (2^3) = (8)', 'simplification': '(8)+1+2+3+4'},
    #                       3: {'step': 'Add and subtract [left to right]: 8+1+2+3+4 = 18', 'simplification': '18'}},
    #         },
    #         {
    #             'expression': '2^3+1+2*13*4+23',
    #             'result': '136',
    #             'steps': {1: {'step': 'Apply PEMDAS: 2^3+1+2*13*4+23 = (2^3)+1+2*13*4+23', 'simplification': '(2^3)+1+2*13*4+23'},
    #                       2: {'step': 'Calculate exponent: (2^3) = (8)', 'simplification': '(8)+1+2*13*4+23'},
    #                       3: {'step': 'Apply PEMDAS: 8+1+2*13*4+23 = 8+1+(2*13*4)+23', 'simplification': '8+1+(2*13*4)+23'},
    #                       4: {'step': 'Multiply [left to right]: (2*13*4) = (104)', 'simplification': '8+1+(104)+23'},
    #                       5: {'step': 'Add and subtract [left to right]: 8+1+104+23 = 136', 'simplification': '136'}},
    #         },
    #         {
    #             'expression': '1+2*13*4+23+2^3',
    #             'result': '136',
    #             'steps': {1: {'step': 'Apply PEMDAS: 1+2*13*4+23+2^3 = 1+2*13*4+23+(2^3)', 'simplification': '1+2*13*4+23+(2^3)'},
    #                       2: {'step': 'Calculate exponent: (2^3) = (8)', 'simplification': '1+2*13*4+23+(8)'},
    #                       3: {'step': 'Apply PEMDAS: 1+2*13*4+23+8 = 1+(2*13*4)+23+8', 'simplification': '1+(2*13*4)+23+8'},
    #                       4: {'step': 'Multiply [left to right]: (2*13*4) = (104)', 'simplification': '1+(104)+23+8'},
    #                       5: {'step': 'Add and subtract [left to right]: 1+104+23+8 = 136', 'simplification': '136'}},
    #         },
    #         {
    #             'expression': '3^{1+2+3}+13',
    #             'result': '742',
    #             'steps': {1: {'step': 'Apply PEMDAS: 3^{1+2+3}+13 = (3^{1+2+3})+13', 'simplification': '(3^{1+2+3})+13'},
    #                       2: {'step': 'Add and subtract [left to right]: (1+2+3) = (6)', 'simplification': '(3^{6})+13'},
    #                       3: {'step': 'Calculate exponent: (3^{6}) = (729)', 'simplification': '(729)+13'},
    #                       4: {'step': 'Add the first and second term: 729+13 = 742', 'simplification': '742'}},
    #         },
    #         {
    #             'expression': '3^{1+2*3*2+11}+3+5+6*3*12',
    #             'result': '282429536705',
    #             'steps': {1: {'step': 'Apply PEMDAS: 3^{1+2*3*2+11}+3+5+6*3*12 = (3^{1+2*3*2+11})+3+5+6*3*12', 'simplification': '(3^{1+2*3*2+11})+3+5+6*3*12'},
    #                       2: {'step': 'Apply PEMDAS: (1+2*3*2+11) = (1+(2*3*2)+11)', 'simplification': '(3^{1+(2*3*2)+11})+3+5+6*3*12'},
    #                       3: {'step': 'Multiply [left to right]: (2*3*2) = (12)', 'simplification': '(3^{1+(12)+11})+3+5+6*3*12'},
    #                       4: {'step': 'Add and subtract [left to right]: (1+12+11) = (24)', 'simplification': '(3^{24})+3+5+6*3*12'},
    #                       5: {'step': 'Calculate exponent: (3^{24}) = (282429536481)', 'simplification': '(282429536481)+3+5+6*3*12'},
    #                       6: {'step': 'Apply PEMDAS: 282429536481+3+5+6*3*12 = 282429536481+3+5+(6*3*12)', 'simplification': '282429536481+3+5+(6*3*12)'},
    #                       7: {'step': 'Multiply [left to right]: (6*3*12) = (216)', 'simplification': '282429536481+3+5+(216)'},
    #                       8: {'step': 'Add and subtract [left to right]: 282429536481+3+5+216 = 282429536705', 'simplification': '282429536705'}},
    #         },
    #         {
    #             'expression': '(1+2*3*4+10)^{4+2*1*1}+(5*4+3+2+1)',
    #             'result': '1838265651',
    #             'steps': {1: {'step': 'Apply PEMDAS: (5*4+3+2+1) = ((5*4)+3+2+1)', 'simplification': '(1+2*3*4+10)^{4+2*1*1}+((5*4)+3+2+1)'},
    #                       2: {'step': 'Multiply the first and second term: (5*4) = (20)', 'simplification': '(1+2*3*4+10)^{4+2*1*1}+((20)+3+2+1)'},
    #                       3: {'step': 'Add and subtract [left to right]: (20+3+2+1) = (26)', 'simplification': '(1+2*3*4+10)^{4+2*1*1}+(26)'},
    #                       4: {'step': 'Apply PEMDAS: (1+2*3*4+10) = (1+(2*3*4)+10)', 'simplification': '(1+(2*3*4)+10)^{4+2*1*1}+26'},
    #                       5: {'step': 'Multiply [left to right]: (2*3*4) = (24)', 'simplification': '(1+(24)+10)^{4+2*1*1}+26'},
    #                       6: {'step': 'Add and subtract [left to right]: (1+24+10) = (35)', 'simplification': '(35)^{4+2*1*1}+26'},
    #                       7: {'step': 'Apply PEMDAS: 35^{4+2*1*1}+26 = (35^{4+2*1*1})+26', 'simplification': '(35^{4+2*1*1})+26'},
    #                       8: {'step': 'Apply PEMDAS: (4+2*1*1) = (4+(2*1*1))', 'simplification': '(35^{4+(2*1*1)})+26'},
    #                       9: {'step': 'Multiply [left to right]: (2*1*1) = (2)', 'simplification': '(35^{4+(2)})+26'},
    #                       10: {'step': 'Add the first and second term: (4+2) = (6)', 'simplification': '(35^{6})+26'},
    #                       11: {'step': 'Calculate exponent: (35^{6}) = (1838265625)', 'simplification': '(1838265625)+26'},
    #                       12: {'step': 'Add the first and second term: 1838265625+26 = 1838265651', 'simplification': '1838265651'}},
    #         },
    #         {
    #             'expression': '(1+2)^{2+1}+(2+3)^{3+2}-(4+5)^{5+4}+(5+6)^{6+5}',
    #             'result': '284924253274',
    #             'steps': {1: {'step': 'Add the first and second term: (5+6) = (11)', 'simplification': '(1+2)^{2+1}+(2+3)^{3+2}-(4+5)^{5+4}+(11)^{6+5}'},
    #                       2: {'step': 'Add the first and second term: (4+5) = (9)', 'simplification': '(1+2)^{2+1}+(2+3)^{3+2}-(9)^{5+4}+11^{6+5}'},
    #                       3: {'step': 'Add the first and second term: (2+3) = (5)', 'simplification': '(1+2)^{2+1}+(5)^{3+2}-9^{5+4}+11^{6+5}'},
    #                       4: {'step': 'Add the first and second term: (1+2) = (3)', 'simplification': '(3)^{2+1}+5^{3+2}-9^{5+4}+11^{6+5}'},
    #                       5: {'step': 'Apply PEMDAS: 3^{2+1}+5^{3+2}-9^{5+4}+11^{6+5} = (3^{2+1})+5^{3+2}-9^{5+4}+11^{6+5}', 'simplification': '(3^{2+1})+5^{3+2}-9^{5+4}+11^{6+5}'},
    #                       6: {'step': 'Add the first and second term: (2+1) = (3)', 'simplification': '(3^{3})+5^{3+2}-9^{5+4}+11^{6+5}'},
    #                       7: {'step': 'Calculate exponent: (3^{3}) = (27)', 'simplification': '(27)+5^{3+2}-9^{5+4}+11^{6+5}'},
    #                       8: {'step': 'Apply PEMDAS: 27+5^{3+2}-9^{5+4}+11^{6+5} = 27+(5^{3+2})-9^{5+4}+11^{6+5}', 'simplification': '27+(5^{3+2})-9^{5+4}+11^{6+5}'},
    #                       9: {'step': 'Add the first and second term: (3+2) = (5)', 'simplification': '27+(5^{5})-9^{5+4}+11^{6+5}'},
    #                       10: {'step': 'Calculate exponent: (5^{5}) = (3125)', 'simplification': '27+(3125)-9^{5+4}+11^{6+5}'},
    #                       11: {'step': 'Apply PEMDAS: 27+3125-9^{5+4}+11^{6+5} = 27+3125-(9^{5+4})+11^{6+5}', 'simplification': '27+3125-(9^{5+4})+11^{6+5}'},
    #                       12: {'step': 'Add the first and second term: (5+4) = (9)', 'simplification': '27+3125-(9^{9})+11^{6+5}'},
    #                       13: {'step': 'Calculate exponent: (9^{9}) = (387420489)', 'simplification': '27+3125-(387420489)+11^{6+5}'},
    #                       14: {'step': 'Apply PEMDAS: 27+3125-387420489+11^{6+5} = 27+3125-387420489+(11^{6+5})', 'simplification': '27+3125-387420489+(11^{6+5})'},
    #                       15: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '27+3125-387420489+(11^{11})'},
    #                       16: {'step': 'Calculate exponent: (11^{11}) = (285311670611)', 'simplification': '27+3125-387420489+(285311670611)'},
    #                       17: {'step': 'Add and subtract [left to right]: 27+3125-387420489+285311670611 = 284924253274', 'simplification': '284924253274'}},
    #         },
    #         {
    #             'expression': '101000+1000*(9.8*2+0.5*(25^2-5^2))',
    #             'result': '420600',
    #             'steps': {1: {'step': 'Apply PEMDAS: (25^2-5^2) = ((25^2)-5^2)', 'simplification': '101000+1000*(9.8*2+0.5*((25^2)-5^2))'},
    #                       2: {'step': 'Calculate exponent: (25^2) = (625)', 'simplification': '101000+1000*(9.8*2+0.5*((625)-5^2))'},
    #                       3: {'step': 'Apply PEMDAS: (625-5^2) = (625-(5^2))', 'simplification': '101000+1000*(9.8*2+0.5*(625-(5^2)))'},
    #                       4: {'step': 'Calculate exponent: (5^2) = (25)', 'simplification': '101000+1000*(9.8*2+0.5*(625-(25)))'},
    #                       5: {'step': 'Subtract the first and second term: (625-25) = (600)', 'simplification': '101000+1000*(9.8*2+0.5*(600))'},
    #                       6: {'step': 'Apply PEMDAS: (9.8*2+0.5*600) = ((9.8*2)+(0.5*600))', 'simplification': '101000+1000*((9.8*2)+(0.5*600))'},
    #                       7: {'step': 'Multiply the first and second term: (0.5*600) = (300)', 'simplification': '101000+1000*((9.8*2)+(300))'},
    #                       8: {'step': 'Multiply the first and second term: (9.8*2) = (19.6)', 'simplification': '101000+1000*((19.6)+300)'},
    #                       9: {'step': 'Add the first and second term: (19.6+300) = (319.6)', 'simplification': '101000+1000*(319.6)'},
    #                       10: {'step': 'Apply PEMDAS: 101000+1000*319.6 = 101000+(1000*319.6)', 'simplification': '101000+(1000*319.6)'},
    #                       11: {'step': 'Multiply the first and second term: (1000*319.6) = (319600)', 'simplification': '101000+(319600)'},
    #                       12: {'step': 'Add the first and second term: 101000+319600 = 420600', 'simplification': '420600'}},
    #         },
    #         {
    #             'expression': '2^{2+1}*2^{3+2}*2^{4+3}*2^{1+4*3}',
    #             'result': '268435456',
    #             'steps': {1: {'step': 'Apply rule exponent: a^b * a^c = a^{b+c}', 'simplification': '2^{(2+1)+(3+2)+(4+3)+(1+4*3)}'},
    #                       2: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '2^{(2+1)+(3+2)+(4+3)+(1+(4*3))}'},
    #                       3: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '2^{(2+1)+(3+2)+(4+3)+(1+(12))}'},
    #                       4: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '2^{(2+1)+(3+2)+(4+3)+(13)}'},
    #                       5: {'step': 'Add the first and second term: (4+3) = (7)', 'simplification': '2^{(2+1)+(3+2)+(7)+13}'},
    #                       6: {'step': 'Add the first and second term: (3+2) = (5)', 'simplification': '2^{(2+1)+(5)+7+13}'},
    #                       7: {'step': 'Add the first and second term: (2+1) = (3)', 'simplification': '2^{(3)+5+7+13}'},
    #                       8: {'step': 'Add and subtract [left to right]: 3+5+7+13 = 28', 'simplification': '2^{28}'},
    #                       9: {'step': 'Calculate exponent: 2^{28} = 268435456', 'simplification': '268435456'}},
    #         },
    #         # RADICALS
    #         {
    #             'expression': 'sqrt{2}',
    #             'result': '1.41421',
    #             'steps': {1: {'step': 'Simplify Radical: sqrt{2} = 1.41421', 'simplification': '1.41421'}},
    #         },
    #         {
    #             'expression': '1+sqrt{2}',
    #             'result': '2.41421',
    #             'steps': {1: {'step': 'Apply PEMDAS: 1+sqrt{2} = 1+(sqrt{2})', 'simplification': '1+(sqrt{2})'},
    #                       2: {'step': 'Simplify Radical: (sqrt{2}) = (1.41421)', 'simplification': '1+(1.41421)'},
    #                       3: {'step': 'Add the first and second term: 1+1.41421 = 2.41421', 'simplification': '2.41421'}},
    #         },
    #         {
    #             'expression': 'sqrt{3}+5',
    #             'result': '6.73205',
    #             'steps': {1: {'step': 'Apply PEMDAS: sqrt{3}+5 = (sqrt{3})+5', 'simplification': '(sqrt{3})+5'},
    #                       2: {'step': 'Simplify Radical: (sqrt{3}) = (1.73205)', 'simplification': '(1.73205)+5'},
    #                       3: {'step': 'Add the first and second term: 1.73205+5 = 6.73205', 'simplification': '6.73205'}},
    #         },
    #         {
    #             'expression': '5+3*2+sqrt{7+5*21}',
    #             'result': '21.58301',
    #             'steps': {1: {'step': 'Apply PEMDAS: 5+3*2+sqrt{7+5*21} = 5+3*2+(sqrt{7+5*21})', 'simplification': '5+3*2+(sqrt{7+5*21})'},
    #                       2: {'step': 'Apply PEMDAS: (7+5*21) = (7+(5*21))', 'simplification': '5+3*2+(sqrt{7+(5*21)})'},
    #                       3: {'step': 'Multiply the first and second term: (5*21) = (105)', 'simplification': '5+3*2+(sqrt{7+(105)})'},
    #                       4: {'step': 'Add the first and second term: (7+105) = (112)', 'simplification': '5+3*2+(sqrt{112})'},
    #                       5: {'step': 'Simplify Radical: (sqrt{112}) = (10.58301)', 'simplification': '5+3*2+(10.58301)'},
    #                       6: {'step': 'Apply PEMDAS: 5+3*2+10.58301 = 5+(3*2)+10.58301', 'simplification': '5+(3*2)+10.58301'},
    #                       7: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '5+(6)+10.58301'},
    #                       8: {'step': 'Add and subtract [left to right]: 5+6+10.58301 = 21.58301', 'simplification': '21.58301'}},
    #         },
    #         {
    #             'expression': '5+3*2+sqrt{7+5*21}+(8+4*2)',
    #             'result': '37.58301',
    #             'steps': {1: {'step': 'Apply PEMDAS: (8+4*2) = (8+(4*2))', 'simplification': '5+3*2+sqrt{7+5*21}+(8+(4*2))'},
    #                       2: {'step': 'Multiply the first and second term: (4*2) = (8)', 'simplification': '5+3*2+sqrt{7+5*21}+(8+(8))'},
    #                       3: {'step': 'Add the first and second term: (8+8) = (16)', 'simplification': '5+3*2+sqrt{7+5*21}+(16)'},
    #                       4: {'step': 'Apply PEMDAS: 5+3*2+sqrt{7+5*21}+16 = 5+3*2+(sqrt{7+5*21})+16', 'simplification': '5+3*2+(sqrt{7+5*21})+16'},
    #                       5: {'step': 'Apply PEMDAS: (7+5*21) = (7+(5*21))', 'simplification': '5+3*2+(sqrt{7+(5*21)})+16'},
    #                       6: {'step': 'Multiply the first and second term: (5*21) = (105)', 'simplification': '5+3*2+(sqrt{7+(105)})+16'},
    #                       7: {'step': 'Add the first and second term: (7+105) = (112)', 'simplification': '5+3*2+(sqrt{112})+16'},
    #                       8: {'step': 'Simplify Radical: (sqrt{112}) = (10.58301)', 'simplification': '5+3*2+(10.58301)+16'},
    #                       9: {'step': 'Apply PEMDAS: 5+3*2+10.58301+16 = 5+(3*2)+10.58301+16', 'simplification': '5+(3*2)+10.58301+16'},
    #                       10: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '5+(6)+10.58301+16'},
    #                       11: {'step': 'Add and subtract [left to right]: 5+6+10.58301+16 = 37.58301', 'simplification': '37.58301'}},
    #         },
    #         {
    #             'expression': 'sqrt{2^{3.141592653589793}}',
    #             'result': '2.97069',
    #             'steps': {1: {'step': 'Calculate exponent: 2^{3.141592653589793} = 8.82498', 'simplification': 'sqrt{8.82498}'},
    #                       2: {'step': 'Simplify Radical: sqrt{8.82498} = 2.97069', 'simplification': '2.97069'}},
    #         },
    #         {
    #             'expression': 'sqrt{(5+3*2)^2}',
    #             'result': '11',
    #             'steps': {1: {'step': 'Apply PEMDAS: (5+3*2) = (5+(3*2))', 'simplification': 'sqrt{(5+(3*2))^2}'},
    #                       2: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': 'sqrt{(5+(6))^2}'},
    #                       3: {'step': 'Add the first and second term: (5+6) = (11)', 'simplification': 'sqrt{(11)^2}'},
    #                       4: {'step': 'Calculate exponent: 11^2 = 121', 'simplification': 'sqrt{121}'},
    #                       5: {'step': 'Simplify Radical: sqrt{121} = 11', 'simplification': '11'}},
    #         },
    #         {
    #             'expression': 'sqrt{(5+3*2)^{1+2+3}}',
    #             'result': '1331',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: 1+2+3 = 6', 'simplification': 'sqrt{(5+3*2)^{6}}'},
    #                       2: {'step': 'Apply PEMDAS: (5+3*2) = (5+(3*2))', 'simplification': 'sqrt{(5+(3*2))^{6}}'},
    #                       3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': 'sqrt{(5+(6))^{6}}'},
    #                       4: {'step': 'Add the first and second term: (5+6) = (11)', 'simplification': 'sqrt{(11)^{6}}'},
    #                       5: {'step': 'Calculate exponent: 11^{6} = 1771561', 'simplification': 'sqrt{1771561}'},
    #                       6: {'step': 'Simplify Radical: sqrt{1771561} = 1331', 'simplification': '1331'}},
    #         },
    #         # PEMDAS
    #         {
    #             'expression': '1+2+3*5',
    #             'result': '18',
    #             'steps': {1: {'step': 'Apply PEMDAS: 1+2+3*5 = 1+2+(3*5)', 'simplification': '1+2+(3*5)'},
    #                       2: {'step': 'Multiply the first and second term: (3*5) = (15)', 'simplification': '1+2+(15)'},
    #                       3: {'step': 'Add and subtract [left to right]: 1+2+15 = 18', 'simplification': '18'}},
    #         },
    #         {
    #             'expression': '23-125*11+18',
    #             'result': '-1334',
    #             'steps': {1: {'step': 'Apply PEMDAS: 23-125*11+18 = 23-(125*11)+18', 'simplification': '23-(125*11)+18'},
    #                       2: {'step': 'Multiply the first and second term: (125*11) = (1375)', 'simplification': '23-(1375)+18'},
    #                       3: {'step': 'Add and subtract [left to right]: 23-1375+18 = -1334', 'simplification': '-1334'}}
    #         },
    #         {
    #             'expression': '1+2+3+4*5+6+7+9*10',
    #             'result': '129',
    #             'steps': {1: {'step': 'Apply PEMDAS: 1+2+3+4*5+6+7+9*10 = 1+2+3+(4*5)+6+7+(9*10)', 'simplification': '1+2+3+(4*5)+6+7+(9*10)'},
    #                       2: {'step': 'Multiply the first and second term: (9*10) = (90)', 'simplification': '1+2+3+(4*5)+6+7+(90)'},
    #                       3: {'step': 'Multiply the first and second term: (4*5) = (20)', 'simplification': '1+2+3+(20)+6+7+90'},
    #                       4: {'step': 'Add and subtract [left to right]: 1+2+3+20+6+7+90 = 129', 'simplification': '129'}},
    #         },
    #         {
    #             'expression': '1+2+3+4*5*6*7+8+9',
    #             'result': '863',
    #             'steps': {1: {'step': 'Apply PEMDAS: 1+2+3+4*5*6*7+8+9 = 1+2+3+(4*5*6*7)+8+9', 'simplification': '1+2+3+(4*5*6*7)+8+9'},
    #                       2: {'step': 'Multiply [left to right]: (4*5*6*7) = (840)', 'simplification': '1+2+3+(840)+8+9'},
    #                       3: {'step': 'Add and subtract [left to right]: 1+2+3+840+8+9 = 863', 'simplification': '863'}},
    #         },
    #         {
    #             'expression': '1+2*-3*-4*5+9',
    #             'result': '130',
    #             'steps': {1: {'step': 'Apply PEMDAS: 1+2*-3*-4*5+9 = 1+(2*-3*-4*5)+9', 'simplification': '1+(2*-3*-4*5)+9'},
    #                       2: {'step': 'Multiply [left to right]: (2*-3*-4*5) = (120)', 'simplification': '1+(120)+9'},
    #                       3: {'step': 'Add and subtract [left to right]: 1+120+9 = 130', 'simplification': '130'}},
    #         },
    #
    #         {
    #             'expression': '((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30)',
    #             'result': '1349',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '((1+(2+2)*3)+5)+(3*2+5)*(121)'},
    #                       2: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '((1+(2+2)*3)+5)+((3*2)+5)*121'},
    #                       3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '((1+(2+2)*3)+5)+((6)+5)*121'},
    #                       4: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '((1+(2+2)*3)+5)+(11)*121'},
    #                       5: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '((1+(4)*3)+5)+11*121'},
    #                       6: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '((1+(4*3))+5)+11*121'},
    #                       7: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '((1+(12))+5)+11*121'},
    #                       8: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '((13)+5)+11*121'},
    #                       9: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '(18)+11*121'},
    #                       10: {'step': 'Apply PEMDAS: 18+11*121 = 18+(11*121)', 'simplification': '18+(11*121)'},
    #                       11: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '18+(1331)'},
    #                       12: {'step': 'Add the first and second term: 18+1331 = 1349', 'simplification': '1349'}},
    #         },
    #         # COMPLICATED
    #         {
    #             'expression': '((((((28+298)*34)+22)*2821)*18)+7)+((((((27+213)*242)+1763)*3)*4)+3)',
    #             'result': '564658594',
    #             'steps': {1: {'step': 'Add the first and second term: (27+213) = (240)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+((((((240)*242)+1763)*3)*4)+3)'},
    #                       2: {'step': 'Multiply the first and second term: (240*242) = (58080)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+(((((58080)+1763)*3)*4)+3)'},
    #                       3: {'step': 'Add the first and second term: (58080+1763) = (59843)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+((((59843)*3)*4)+3)'},
    #                       4: {'step': 'Multiply the first and second term: (59843*3) = (179529)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+(((179529)*4)+3)'},
    #                       5: {'step': 'Multiply the first and second term: (179529*4) = (718116)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+((718116)+3)'},
    #                       6: {'step': 'Add the first and second term: (718116+3) = (718119)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+(718119)'},
    #                       7: {'step': 'Add the first and second term: (28+298) = (326)', 'simplification': '((((((326)*34)+22)*2821)*18)+7)+718119'},
    #                       8: {'step': 'Multiply the first and second term: (326*34) = (11084)', 'simplification': '(((((11084)+22)*2821)*18)+7)+718119'},
    #                       9: {'step': 'Add the first and second term: (11084+22) = (11106)', 'simplification': '((((11106)*2821)*18)+7)+718119'},
    #                       10: {'step': 'Multiply the first and second term: (11106*2821) = (31330026)', 'simplification': '(((31330026)*18)+7)+718119'},
    #                       11: {'step': 'Multiply the first and second term: (31330026*18) = (563940468)', 'simplification': '((563940468)+7)+718119'},
    #                       12: {'step': 'Add the first and second term: (563940468+7) = (563940475)', 'simplification': '(563940475)+718119'},
    #                       13: {'step': 'Add the first and second term: 563940475+718119 = 564658594', 'simplification': '564658594'}},
    #         },
    #         # SPECIAL NUMBERS
    #         {
    #             'expression': '4*3.141592653589793*(1+72+827-36)',
    #             'result': '10857.34368',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: (1+72+827-36) = (864)', 'simplification': '4*3.141592653589793*(864)'},
    #                       2: {'step': 'Multiply [left to right]: 4*3.141592653589793*864 = 10857.34368', 'simplification': '10857.34368'}},
    #         },
    #         {
    #             'expression': '9*2.718281828459045*(283+82-4)',
    #             'result': '8831.69894',
    #             'steps': {1: {'step': 'Add and subtract [left to right]: (283+82-4) = (361)', 'simplification': '9*2.718281828459045*(361)'},
    #                       2: {'step': 'Multiply [left to right]: 9*2.718281828459045*361 = 8831.69894', 'simplification': '8831.69894'}},
    #         },
    #
    #     ]
    #
    #     for item in expressionsAndResults:
    #         Simplification = evaluateArithmetic(item['expression'])
    #         Steps = Simplification[0]
    #         Result = Simplification[1]
    #
    #         self.assertEqual(Steps, item['steps'], f"Expression: {item['expression']}")
    #         self.assertEqual(Result, item['result'], f"Expression: {item['expression']}")
    #
    # # TEST performOperation
    # def test_performOperation(self):
    #     expressionAndResults = [
    #         {
    #             'expression': '1+2+3+4+5+6',
    #             'result': '21',
    #             'operation': 'arithmetic-add-single',
    #         },
    #         {
    #             'expression': '1+26+274+8723+26',
    #             'result': '9050',
    #             'operation': 'arithmetic-add-single',
    #         },
    #         {
    #             'expression': '-44-245-27-47-482',
    #             'result': '-845',
    #             'operation': 'add-subtract-only',
    #         },
    #         {
    #             'expression': '264+2842+132-427+183-78',
    #             'result': '2916',
    #             'operation': 'add-subtract-only',
    #         },
    #         {
    #             'expression': '21*62*51*12',
    #             'result': '796824',
    #             'operation': 'multiply-only',
    #         },
    #         {
    #             'expression': '21*62*51*12*11',
    #             'result': '8765064',
    #             'operation': 'multiply-only',
    #         },
    #         {
    #             'expression': '12*-5*21*32*-12*3*-3',
    #             'result': '-4354560',
    #             'operation': 'multiply-only',
    #         },
    #         {
    #             'expression': '12*-5*21*32*-12*3*-3*-2',
    #             'result': '8709120',
    #             'operation': 'multiply-only',
    #         },
    #     ]
    #
    #     for item in expressionAndResults:
    #         self.assertEqual(performOperation(item['expression'], item['operation']), item['result'], f"Expression: {item['expression']}")
    #
    # # TEST applyPEMDAS
    # def test_applyPEMDAS(self):
    #     expressionAndResults = [
    #         {
    #             'expression': '1+2+3',
    #             'result': '1+2+3',
    #         },
    #         {
    #             'expression': '1+2*3',
    #             'result': '1+(2*3)',
    #         },
    #         {
    #             'expression': '1-2*3',
    #             'result': '1-(2*3)',
    #         },
    #         {
    #             'expression': '1+2*3*4*5',
    #             'result': '1+(2*3*4*5)',
    #         },
    #         {
    #             'expression': '1+274*24*24*5',
    #             'result': '1+(274*24*24*5)',
    #         },
    #         {
    #             'expression': '1+24*43*24*5*6+234',
    #             'result': '1+(24*43*24*5*6)+234',
    #         },
    #         {
    #             'expression': '1+2*-5*-23*4*54+96',
    #             'result': '1+(2*-5*-23*4*54)+96',
    #         },
    #         {
    #             'expression': '12+3*2+67+9*13+12-5*7',
    #             'result': '12+(3*2)+67+(9*13)+12-(5*7)',
    #         },
    #
    #     ]
    #
    #     for item in expressionAndResults:
    #         Expression = ArithmeticExpression(item['expression'])
    #         self.assertEqual(str(Expression.applyPEMDAS()), item['result'], f"Expression: {item['expression']}")
    #
    # # TEST getIndexOfInnerMostParen
    # def test_getIndexOfInnerMostParen(self):
    #     expressionAndResults = [
    #         {
    #             'expression': '23*(3+2+(3*2))',
    #             'result': 8,
    #         },
    #         {
    #             'expression': '((((((28+298)*34)+22)*2821)*18)+7)',
    #             'result': 5,
    #         },
    #         {
    #             'expression': '23*(5*(5+3+(3*(3+62+75*(23+89)))))',
    #             'result': 23,
    #         },
    #     ]
    #
    #     for item in expressionAndResults:
    #         Expression = ArithmeticExpression(item['expression'])
    #         self.assertEqual(Expression.getIndexOfInnerMostParen(), item['result'], f"Expression: {item['expression']}")
    #
    # # TEST wrapStepInParen
    # def test_wrapStepInParen(self):
    #     stepsAndResults = [
    #         {
    #             'step': 'Add and subtract [left to right]: (3*53*342) = (54378)',
    #             'result': 'Add and subtract [left to right]: (3*53*342) = (54378)',
    #         },
    #         {
    #             'step': 'Add and subtract [left to right]: 3*53*342 = 54378',
    #             'result': 'Add and subtract [left to right]: (3*53*342) = (54378)',
    #         },
    #         {
    #             'step': 'Apply log rule [ln(a*b) = ln(a) + ln(b)]: ln(e*a^t) = ln(e) + ln(a^t)',
    #             'result': 'Apply log rule [ln(a*b) = ln(a) + ln(b)]: (ln(e*a^t)) = (ln(e) + ln(a^t))',
    #         },
    #     ]
    #
    #     for item in stepsAndResults:
    #         self.assertEqual(item['result'], wrapStepInParen(item['step']), f"Step: {item['step']}")
    #
    # # TEST splitExpression
    # def test_splitExpression(self):
    #     expressionAndResults = [
    #         {
    #             'expression': '132*425+12-48',
    #             'index': 7,
    #             'operator': '+',
    #             'operation': 'arithmetic-add-single',
    #             'binarySplit': True,
    #             'result': ('425', '12'),
    #         },
    #         {
    #             'expression': '132+425*12-48',
    #             'index': 7,
    #             'operator': '*',
    #             'operation': 'multiply-only',
    #             'binarySplit': False,
    #             'result': ('132+425', '12-48'),
    #         },
    #         {
    #             'expression': '56-123*57-28',
    #             'index': 6,
    #             'operator': '*',
    #             'operation': 'multiply-only',
    #             'binarySplit': True,
    #             'result': ('-123', '57'),
    #         },
    #         {
    #             'expression': '56-123*57-28',
    #             'index': 6,
    #             'operator': '*',
    #             'operation': 'multiply-only',
    #             'binarySplit': False,
    #             'result': ('56-123', '57-28'),
    #         },
    #         {
    #             'expression': '12+127*-57-28',
    #             'index': 6,
    #             'operator': '*',
    #             'operation': 'multiply-only',
    #             'binarySplit': True,
    #             'result': ('127', '-57'),
    #         },
    #         {
    #             'expression': '12+127*-57-28',
    #             'index': 6,
    #             'operator': '*',
    #             'operation': 'multiply-only',
    #             'binarySplit': False,
    #             'result': ('12+127', '-57-28'),
    #         },
    #     ]
    #
    #     for item in expressionAndResults:
    #         Result = splitExpression(item['expression'], item['index'], item['operator'], item['binarySplit'], item['operation'])
    #         self.assertEqual(item['result'], Result, f"Expression: {item['expression']}")
    #
    # # TEST castToFloatOrInt
    # def test_castToFloatOrInt(self):
    #     expressionAndResults = [
    #         {
    #             'expression': 2.0,
    #             'castToString': True,
    #             'result': '2',
    #         },
    #         {
    #             'expression': 2.0,
    #             'castToString': False,
    #             'result': 2,
    #         },
    #         {
    #             'expression': 0.25,
    #             'castToString': True,
    #             'result': '0.25',
    #         },
    #         {
    #             'expression': 0.25,
    #             'castToString': False,
    #             'result': 0.25,
    #         },
    #     ]
    #
    #     for item in expressionAndResults:
    #         self.assertEqual(item['result'], castToFloatOrInt(item['expression'], item['castToString']))

    """ NEW FUNCTIONS """
    def test_get_start_of_var(self):
        expressionAndExpectedVal = [
            {
                'expression': '+25x',
                'expected_val': 3,
            },
            {
                'expression': '15y',
                'expected_val': 2,
            },
            {
                'expression': '+125xyz',
                'expected_val': 4,
            },
        ]
        for item in expressionAndExpectedVal:
            expression = item['expression']
            expectedVal = item['expected_val']
            returnedVal = get_start_of_var(expression)
            self.assertEqual(expectedVal, returnedVal, f"Failed: {expression}")

    def test_get_var(self):
        expressionAndExpectedVal = [
            {
                'term': '+25x',
                'start_of_var': 3,
                'expected_val': 'x',
            },
            {
                'term': '15y',
                'start_of_var': 2,
                'expected_val': 'y',
            },
            {
                'term': '+125xyz',
                'start_of_var': 4,
                'expected_val': 'xyz',
            },
            {
                'term': '-15sin(ab+c)',
                'start_of_var': 3,
                'expected_val': 'sin(ab+c)',
            },
        ]
        for item in expressionAndExpectedVal:
            term = item['term']
            start_of_var = item['start_of_var']
            expectedVal = item['expected_val']
            returnedVal = get_var(term, start_of_var)
            self.assertEqual(expectedVal, returnedVal, f"Failed: {term}")

    def test_get_coefficient(self):
        expressionAndExpectedVal = [
            {
                'term': '+25x',
                'start_of_var': 3,
                'expected_val': '+25',
            },
            {
                'term': '15y',
                'start_of_var': 2,
                'expected_val': '15',
            },
            {
                'term': '+125xyz',
                'start_of_var': 4,
                'expected_val': '+125',
            },
            {
                'term': '-15sin(ab+c)',
                'start_of_var': 3,
                'expected_val': '-15',
            },
        ]
        for item in expressionAndExpectedVal:
            term = item['term']
            start_of_var = item['start_of_var']
            expectedVal = item['expected_val']
            returnedVal = get_coefficient(term, start_of_var)
            self.assertEqual(expectedVal, returnedVal, f"Failed: {term}")

    def test_addNumbers(self):
        numbersAndExpectedVal = [
            {
                'numbers': ['+1', '+2', '3', '-4', '+72', '-17'],
                'expectedVal': 57,
            },
            {
                'numbers': ['0.25', '+92.24', '-23.0', '23.2345'],
                'expectedVal': 92.72449999999999
            }
        ]
        for item in numbersAndExpectedVal:
            numbers = item['numbers']
            expectedVal = item['expectedVal']
            returnedVal = addNumbers(numbers)
            self.assertEqual(expectedVal, returnedVal, f"Failed: {numbers}")

    def test_simplifyExpression(self):
        expressionsAndExpectedVal = [
            {
                'expression': '1+2+3+4',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+3+4=10'}], 'finalResult': '10'},
            },
            {
                'expression': '1+a+a+b',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+a+a+b=a+a+b+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle a+a+b+1=2a+b+1'}], 'finalResult': '2a+b+1'},
            },
            {
                'expression': '1+2+3+a+a+c',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2+3+a+a+c=a+a+c+1+2+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle a+a+c+1+2+3=2a+c+1+2+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2a+c+1+2+3=2a+c+6'}], 'finalResult': '2a+c+6'},
            },
            {
                'expression': '15x+13x+x-2+15',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 15x+13x+x-2+15=29x-2+15'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 29x-2+15=29x+13'}], 'finalResult': '29x+13'}
            },
            {
                'expression': 'a+a+5b-2b+c-c',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle a+a+5b-2b+c-c=2a+3b+0'}], 'finalResult': '2a+3b'},
            },
            {
                'expression': '5x+3+5+x',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 5x+3+5+x=5x+x+3+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+x+3+5=6x+3+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 6x+3+5=6x+8'}], 'finalResult': '6x+8'},
            },
            {
                'expression': '1+pi+5\sin(ab+c)-2\sin(ab+c)+3pi+3',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+\\pi+5\\sin\\left(ab+c\\right)-2\\sin\\left(ab+c\\right)+3\\pi+3=\\pi+3\\pi+5\\sin\\left(ab+c\\right)-2\\sin\\left(ab+c\\right)+1+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle \\pi+3\\pi+5\\sin\\left(ab+c\\right)-2\\sin\\left(ab+c\\right)+1+3=4\\pi+3\\sin\\left(ab+c\\right)+1+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4\\pi+3\\sin\\left(ab+c\\right)+1+3=4\\pi+3\\sin\\left(ab+c\\right)+4'}], 'finalResult': '4\\pi+3\\sin\\left(ab+c\\right)+4'}
            },
            {
                'expression': 'sqrt{1+2+x+15x-3}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2+x+15x-3=x+15x+1+2-3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle x+15x+1+2-3=16x+1+2-3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 16x+1+2-3=16x+0'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{1+2+x+15x-3}=\\sqrt{16x}'}], 'finalResult': '\\sqrt{16x}'},
            },
            {
                'expression': 'sqrt{15x-2x}+2+3',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{15x-2x}=\\sqrt{13x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 15x-2x=13x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{15x-2x}=\\sqrt{13x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 2+3=5', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'}]}], 'finalResult': '\\sqrt{13x}+5'},
            },
            {
                'expression': '1+x+sqrt{1+25x-15x+3x+13}+3x-5',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 1+x+\\sqrt{1+25x-15x+3x+13}+3x-5=\\sqrt{1+25x-15x+3x+13}+1+x+3x-5'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{1+25x-15x+3x+13}=\\sqrt{13x+14}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+25x-15x+3x+13=25x-15x+3x+1+13'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 25x-15x+3x+1+13=13x+1+13'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 13x+1+13=13x+14'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{1+25x-15x+3x+13}=\\sqrt{13x+14}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+x+3x-5=4x-4', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+x+3x-5=x+3x+1-5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle x+3x+1-5=4x+1-5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4x+1-5=4x+-4'}]}], 'finalResult': '\\sqrt{13x+14}+4x-4'}
            },
            {
                'expression': '1+2+sqrt{25x+15x+sqrt{12x-6x+3}-13+5}+3',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 1+2+\\sqrt{25x+15x+\\sqrt{12x-6x+3}-13+5}+3=\\sqrt{25x+15x+\\sqrt{12x-6x+3}-13+5}+1+2+3'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{25x+15x+\\sqrt{12x-6x+3}-13+5}=\\sqrt{\\sqrt{6x+3}+40x-8}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 25x+15x+\\sqrt{12x-6x+3}-13+5=\\sqrt{12x-6x+3}+25x+15x-13+5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 12x-6x+3=6x+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{12x-6x+3}=\\sqrt{6x+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 25x+15x-13+5=40x-13+5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 40x-13+5=40x-8'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{25x+15x+\\sqrt{12x-6x+3}-13+5}=\\sqrt{\\sqrt{6x+3}+40x-8}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+2+3=6', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+3=6'}]}], 'finalResult': '\\sqrt{\\sqrt{6x+3}+40x-8}+6'},
            },
            {
                'expression': 'sqrt{36}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\sqrt{36}=6'}], 'finalResult': '6'},

            },
            {
                'expression': 'sqrt{72}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Factor Radical}', 'info': '\\displaystyle \\sqrt{72}=\\sqrt{36}\\cdot\\sqrt{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{36}\\cdot\\sqrt{2}=6\\sqrt{2}'}], 'finalResult': '6\\sqrt{2}'},

            },
            {
                'expression': '2sqrt{3+1}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+1=4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 2\\sqrt{3+1}=2\\sqrt{4}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle 2\\sqrt{4}=2\\cdot2'}], 'finalResult': '2\\cdot2'},

            },
            {
                'expression': '(a+b)sqrt{4}+(2x+y)sqrt{36}',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(a+b\\right)\\sqrt{4}=2\\left(a+b\\right)', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\left(a+b\\right)\\sqrt{4}=2\\left(a+b\\right)'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(2x+y\\right)\\sqrt{36}=6\\left(2x+y\\right)', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\left(2x+y\\right)\\sqrt{36}=6\\left(2x+y\\right)'}]}], 'finalResult': '2\\left(a+b\\right)+6\\left(2x+y\\right)'},

            },
            {
                'expression': 'sqrt[3]{94+2}+sqrt[5]{2x+3x+1}',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt[3]{94+2}=2\\sqrt[3]{12}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 94+2=96'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt[3]{94+2}=\\sqrt[3]{96}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Factor Radical}', 'info': '\\displaystyle \\sqrt[3]{96}=\\sqrt[3]{8}\\cdot\\sqrt[3]{12}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt[3]{8}\\cdot\\sqrt[3]{12}=2\\sqrt[3]{12}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt[5]{2x+3x+1}=\\sqrt[5]{5x+1}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+3x+1=5x+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt[5]{2x+3x+1}=\\sqrt[5]{5x+1}'}]}], 'finalResult': '2\\sqrt[3]{12}+\\sqrt[5]{5x+1}'}
            },
            {
                'expression': 'a+b+3a+1+sqrt{36}+sqrt{25}+sqrt{25-23}+3',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle a+b+3a+1+\\sqrt{36}+\\sqrt{25}+\\sqrt{25-23}+3=\\sqrt{36}+\\sqrt{25}+\\sqrt{25-23}+a+b+3a+1+3'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{36}=6', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\sqrt{36}=6'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{25}=5', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\sqrt{25}=5'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{25-23}=\\sqrt{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 25-23=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{25-23}=\\sqrt{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle a+b+3a+1+3=4a+b+4', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle a+b+3a+1+3=a+3a+b+1+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle a+3a+b+1+3=4a+b+1+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4a+b+1+3=4a+b+4'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 6+5+\\sqrt{2}+4a+b+4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 6+5+\\sqrt{2}+4a+b+4=\\sqrt{2}+6+5+4a+b+4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle \\sqrt{2}+6+5+4a+b+4=\\sqrt{2}+4a+b+6+5+4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle \\sqrt{2}+4a+b+6+5+4=\\sqrt{2}+4a+b+15'}], 'finalResult': '\\sqrt{2}+4a+b+15'},

            },
            {
                'expression': 'sqrt[n]{1+3x+2x}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+3x+2x=3x+2x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x+1=5x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt[n]{1+3x+2x}=\\sqrt[n]{5x+1}'}], 'finalResult': '\\sqrt[n]{5x+1}'},
            },
            {
                'expression': '2^3',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 2^3=8'}], 'finalResult': '8'},
            },
            {
                'expression': '(1+2+2x+3x+3)^2',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2+2x+3x+3=2x+3x+1+2+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+3x+1+2+3=5x+1+2+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5x+1+2+3=5x+6'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(1+2+2x+3x+3\\right)^2=\\left(5x+6\\right)^{2}'}], 'finalResult': '\\left(5x+6\\right)^{2}'},
            },
            {
                'expression': 'e^{1+5x+3x+4}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+5x+3x+4=5x+3x+1+4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+1+4=8x+1+4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 8x+1+4=8x+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{1+5x+3x+4}=e^{8x+5}'}], 'finalResult': 'e^{8x+5}'},
            },
            {
                'expression': '(2x+x+1)^{1+2+3x-x}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+x+1=3x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(2x+x+1\\right)^{1+2+3x-x}=\\left(3x+1\\right)^{1+2+3x-x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2+3x-x=3x-x+1+2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x-x+1+2=2x+1+2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2x+1+2=2x+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(3x+1\\right)^{1+2+3x-x}=\\left(3x+1\\right)^{2x+3}'}], 'finalResult': '\\left(3x+1\\right)^{2x+3}'},
            },
            {
                'expression': 'sqrt{(3x+2x+1)^{1+2+3}}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x+1=5x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(3x+2x+1\\right)^{1+2+3}=\\left(5x+1\\right)^{1+2+3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+3=6'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(5x+1\\right)^{1+2+3}=\\left(5x+1\\right)^{6}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{\\left(3x+2x+1\\right)^{1+2+3}}=\\sqrt{\\left(5x+1\\right)^{6}}'}], 'finalResult': '\\sqrt{\\left(5x+1\\right)^{6}}'},
            },
            {
                'expression': '(5x+2x+1)^{3+2-5}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+2x+1=7x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(5x+2x+1\\right)^{3+2-5}=\\left(7x+1\\right)^{3+2-5}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+2-5=0'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(7x+1\\right)^{3+2-5}=\\left(7x+1\\right)^{0}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply exponent rule:}\\ a^0=1', 'info': '\\displaystyle \\left(7x+1\\right)^{0}=1'}], 'finalResult': '1'},
            },
            {
                'expression': '(5x+2x-7x)^{1+2x}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+2x-7x=0'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(5x+2x-7x\\right)^{1+2x}=0^{1+2x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2x=2x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 0^{1+2x}=0^{2x+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply exponent rule:}\\ 0^a=0', 'info': '\\displaystyle 0^{2x+1}=0'}], 'finalResult': '0'},
            },
            {
                'expression': '1+2+sqrt{74+6}+2^{1+2}+(3+2)^2',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 1+2+\\sqrt{74+6}+2^{1+2}+\\left(3+2\\right)^2=2^{1+2}+\\left(3+2\\right)^2+\\sqrt{74+6}+1+2'},
                    {'type': 'e-step', 'heading': '\\displaystyle 2^{1+2}=8', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2^{1+2}=2^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponential}', 'info': '\\displaystyle 2^{3}=8'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(3+2\\right)^2=25', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+2=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(3+2\\right)^2=5^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponential}', 'info': '\\displaystyle 5^{2}=25'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{74+6}=4\\sqrt{5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 74+6=80'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{74+6}=\\sqrt{80}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Factor Radical}', 'info': '\\displaystyle \\sqrt{80}=\\sqrt{16}\\cdot\\sqrt{5}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{16}\\cdot\\sqrt{5}=4\\sqrt{5}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+2=3', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 8+25+4\\sqrt{5}+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 8+25+4\\sqrt{5}+3=4\\sqrt{5}+8+25+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4\\sqrt{5}+8+25+3=4\\sqrt{5}+36'}], 'finalResult': '4\\sqrt{5}+36'},
            },
            {
                'expression': '2sqrt{x}+3sqrt{x}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2\\sqrt{x}+3\\sqrt{x}=5\\sqrt{x}'}], 'finalResult': '5\\sqrt{x}'},
            },
            {
                'expression': '1+2+3sqrt{5x+3x+2x}+5sqrt{8x+2x}',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 1+2+3\\sqrt{5x+3x+2x}+5\\sqrt{8x+2x}=3\\sqrt{5x+3x+2x}+5\\sqrt{8x+2x}+1+2'},
                    {'type': 'e-step', 'heading': '\\displaystyle 3\\sqrt{5x+3x+2x}=3\\sqrt{10x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+2x=10x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 3\\sqrt{5x+3x+2x}=3\\sqrt{10x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 5\\sqrt{8x+2x}=5\\sqrt{10x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 8x+2x=10x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 5\\sqrt{8x+2x}=5\\sqrt{10x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+2=3', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 3\\sqrt{10x}+5\\sqrt{10x}+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3\\sqrt{10x}+5\\sqrt{10x}+3=8\\sqrt{10x}+3'}], 'finalResult': '8\\sqrt{10x}+3'},
            },
            {
                'expression': '1',
                'expected_val': {'steps': [], 'finalResult': '1'},
            },
            {
                'expression': 'a',
                'expected_val': {'steps': [], 'finalResult': 'a'}
            }

        ]

        for item in expressionsAndExpectedVal:
            expression = Expression(item['expression'])
            expectedVal = item['expected_val']
            returnedVal = simplifyExpression(expression)
            self.assertEqual(expectedVal, returnedVal, f"Failed: {expression} Latex: {latexify(expression)}")


def test():
    pass





# test()



if __name__ == '__main__':
    unittest.main()