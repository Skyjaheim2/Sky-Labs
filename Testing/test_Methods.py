import sys
sys.path.append(r"C:\Users\jahei\OneDrive\Documents\Flask-Projects\Flask\Personal-Projects\Computer Algebra") # Add path where project is located to allow for import of application
import os
import unittest
from Methods import *


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


    # TEST isSingleExpression
    def test_isSingleExpression(self):
        expressionsAndResults = [
            {
                'expression': '1262',
                'result': True,
            },
            {
                'expression': '-17264',
                'result': True,
            },
            {
                'expression': '128+92',
                'result': False,
            },
            {
                'expression': '-2742-8242',
                'result': False,
            },
            {
                'expression': '476*12',
                'result': False,
            },

        ]

        for item in expressionsAndResults:
            self.assertEqual(isSingleExpression(item['expression']), item['result'], f"Expression: {item['expression']}")

    # TEST getOperationToPerform
    def test_getOperationToPerform(self):
        expressionAndResults = [
            {
                'expression': '146+481',
                'result': 'arithmetic-add-single',
            },
            {
                'expression': '-148+482',
                'result': 'add-subtract-only',
            },
            {
                'expression': '2894-287+834+984-2974',
                'result': 'add-subtract-only',
            },
            {
                'expression': '183*822',
                'result': 'arithmetic-multiply-single',
            },
            {
                'expression': '-282*824',
                'result': 'arithmetic-multiply-single',
            },
            {
                'expression': '-925*-3298',
                'result': 'arithmetic-multiply-single',
            },
            {
                'expression': '274*732*826*636*816',
                'result': 'multiply-only',
            },
            {
                'expression': '-498*-842*-9842*824',
                'result': 'multiply-only',
            },
            {
                'expression': '284+724-2848*12+734-12*14',
                'result': 'general-arithmetic',
            },
            {
                'expression': '1+27*712*12-5',
                'result': 'general-arithmetic',
            },
            {
                'expression': '123',
                'result': 'no-operation',
            },
        ]

        for item in expressionAndResults:
            Expression = ArithmeticExpression(item['expression'])
            self.assertEqual(Expression.getOperationToPerform(), item['result'], f"Expression: {item['expression']}")

    # TEST evaluateArithmetic
    def test_evaluateArithmetic(self):
        expressionsAndResults = [
            # ADDITION AND SUBTRACTION
            {
                'expression': '1+1',
                'result': '2',
                'steps': {1: {'step': 'Add the first and second term: 1+1 = 2', 'simplification': '2'}},
            },
            {
                'expression': '1+2+3+4+5+6',
                'result': '21',
                'steps': {1: {'step': 'Add and subtract [left to right]: 1+2+3+4+5+6 = 21', 'simplification': '21'}},
            },
            {
                'expression': '1+2+5+8-872+92-3',
                'result': '-767',
                'steps': {1: {'step': 'Add and subtract [left to right]: 1+2+5+8-872+92-3 = -767', 'simplification': '-767'}},
            },
            {
                'expression': '2+-+-+-3',
                'result': '-1',
                'steps': {1: {'step': 'Apply rule: a+-b = a-b', 'simplification': '2---3'},
                          2: {'step': 'Apply rule: a--b = a+b', 'simplification': '2+-3'},
                          3: {'step': 'Apply rule: a+-b = a-b', 'simplification': '2-3'},
                          4: {'step': 'Subtract the first and second term: 2-3 = -1', 'simplification': '-1'}},
            },
            # MULTIPLICATION
            {
                'expression': '1*2*3*4*5',
                'result': '120',
                'steps': {1: {'step': 'Multiply [left to right]: 1*2*3*4*5 = 120', 'simplification': '120'}},
            },
            {
                'expression': '-2*-5*-3',
                'result': '-30',
                'steps': {1: {'step': 'Multiply [left to right]: -2*-5*-3 = -30', 'simplification': '-30'}},
            },
            # EXPONENTS
            {
                'expression': '2^2',
                'result': '4',
                'steps': {1: {'step': 'Calculate exponent: 2^2 = 4', 'simplification': '4'}},
            },
            {
                'expression': '5^-3',
                'result': '0.008',
                'steps': {1: {'step': 'Calculate exponent: 5^-3 = 0.008', 'simplification': '0.008'}},
            },
            {
                'expression': '(-3)^2',
                'result': '9',
                'steps': {1: {'step': 'Calculate exponent: (-3)^2 = 9', 'simplification': '9'}},
            },
            {
                'expression': '-3^2',
                'result': '-9',
                'steps': {1: {'step': 'Calculate exponent: -3^2 = -9', 'simplification': '-9'}},
            },
            {
                'expression': '3.141592653589793^2',
                'result': '9.8696',
                'steps': {1: {'step': 'Calculate exponent: 3.141592653589793^2 = 9.8696', 'simplification': '9.8696'}},
            },
            {
                'expression': '2^{1+2+3}',
                'result': '64',
                'steps': {1: {'step': 'Add and subtract [left to right]: 1+2+3 = 6', 'simplification': '2^{6}'},
                          2: {'step': 'Calculate exponent: 2^{6} = 64', 'simplification': '64'}},
            },
            {
                'expression': '3^{2+3*5}',
                'result': '129140163',
                'steps': {1: {'step': 'Apply PEMDAS: 2+3*5 = 2+(3*5)', 'simplification': '3^{2+(3*5)}'},
                          2: {'step': 'Multiply the first and second term: (3*5) = (15)', 'simplification': '3^{2+(15)}'},
                          3: {'step': 'Add the first and second term: 2+15 = 17', 'simplification': '3^{17}'},
                          4: {'step': 'Calculate exponent: 3^{17} = 129140163', 'simplification': '129140163'}},
            },
            {
                'expression': '3^{(2*3.141592653589793+2.718281828459045)}',
                'result': '19714.81294',
                'steps': {1: {'step': 'Apply PEMDAS: (2*3.141592653589793+2.718281828459045) = ((2*3.141592653589793)+2.718281828459045)', 'simplification': '3^{((2*3.141592653589793)+2.718281828459045)}'},
                          2: {'step': 'Multiply the first and second term: (2*3.141592653589793) = (6.28319)', 'simplification': '3^{((6.28319)+2.718281828459045)}'},
                          3: {'step': 'Add the first and second term: (6.28319+2.718281828459045) = (9.00147)', 'simplification': '3^{(9.00147)}'},
                          4: {'step': 'Calculate exponent: 3^{9.00147} = 19714.81294', 'simplification': '19714.81294'}},
            },
            {
                'expression': '2^{((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30)}',
                'result': '1.22875...e+406',
                'steps': {1: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '2^{((1+(2+2)*3)+5)+(3*2+5)*(121)}'},
                          2: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '2^{((1+(2+2)*3)+5)+((3*2)+5)*121}'},
                          3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '2^{((1+(2+2)*3)+5)+((6)+5)*121}'},
                          4: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '2^{((1+(2+2)*3)+5)+(11)*121}'},
                          5: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '2^{((1+(4)*3)+5)+11*121}'},
                          6: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '2^{((1+(4*3))+5)+11*121}'},
                          7: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '2^{((1+(12))+5)+11*121}'},
                          8: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '2^{((13)+5)+11*121}'},
                          9: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '2^{(18)+11*121}'},
                          10: {'step': 'Apply PEMDAS: 18+11*121 = 18+(11*121)', 'simplification': '2^{18+(11*121)}'},
                          11: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '2^{18+(1331)}'},
                          12: {'step': 'Add the first and second term: 18+1331 = 1349', 'simplification': '2^{1349}'},
                          13: {'step': 'Calculate exponent: 2^{1349} = 1.22875...e+406', 'simplification': '1.22875...e+406'}},
            },
            {
                'expression': '1^{((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30)}',
                'result': '1',
                'steps': {1: {'step': 'Apply rule exponent: 1^a = 1', 'simplification': '1'}},
            },
            {
                'expression': '(1+2+3)^2',
                'result': '36',
                'steps': {1: {'step': 'Add and subtract [left to right]: (1+2+3) = (6)', 'simplification': '(6)^2'},
                          2: {'step': 'Calculate exponent: 6^2 = 36', 'simplification': '36'}},
            },
            {
                'expression': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^3',
                'result': '2454911549',
                'steps': {1: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(121))^3'},
                          2: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '(((1+(2+2)*3)+5)+((3*2)+5)*121)^3'},
                          3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '(((1+(2+2)*3)+5)+((6)+5)*121)^3'},
                          4: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '(((1+(2+2)*3)+5)+(11)*121)^3'},
                          5: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '(((1+(4)*3)+5)+11*121)^3'},
                          6: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '(((1+(4*3))+5)+11*121)^3'},
                          7: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '(((1+(12))+5)+11*121)^3'},
                          8: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '(((13)+5)+11*121)^3'},
                          9: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '((18)+11*121)^3'},
                          10: {'step': 'Apply PEMDAS: (18+11*121) = (18+(11*121))', 'simplification': '(18+(11*121))^3'},
                          11: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '(18+(1331))^3'},
                          12: {'step': 'Add the first and second term: (18+1331) = (1349)', 'simplification': '(1349)^3'},
                          13: {'step': 'Calculate exponent: 1349^3 = 2454911549', 'simplification': '2454911549'}},
            },
            {
                'expression': '(1+2+3)^{2+4+5}',
                'result': '362797056',
                'steps': {1: {'step': 'Add and subtract [left to right]: 2+4+5 = 11', 'simplification': '(1+2+3)^{11}'},
                          2: {'step': 'Add and subtract [left to right]: (1+2+3) = (6)', 'simplification': '(6)^{11}'},
                          3: {'step': 'Calculate exponent: 6^{11} = 362797056', 'simplification': '362797056'}},
            },
            {
                'expression': '(1+2*3)^{2+4*5}',
                'result': '3909821048582988049',
                'steps': {1: {'step': 'Apply PEMDAS: 2+4*5 = 2+(4*5)', 'simplification': '(1+2*3)^{2+(4*5)}'},
                          2: {'step': 'Multiply the first and second term: (4*5) = (20)', 'simplification': '(1+2*3)^{2+(20)}'},
                          3: {'step': 'Add the first and second term: 2+20 = 22', 'simplification': '(1+2*3)^{22}'},
                          4: {'step': 'Apply PEMDAS: (1+2*3) = (1+(2*3))', 'simplification': '(1+(2*3))^{22}'},
                          5: {'step': 'Multiply the first and second term: (2*3) = (6)', 'simplification': '(1+(6))^{22}'},
                          6: {'step': 'Add the first and second term: (1+6) = (7)', 'simplification': '(7)^{22}'},
                          7: {'step': 'Calculate exponent: 7^{22} = 3909821048582988049', 'simplification': '3909821048582988049'}},
            },
            {
                'expression': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))}',
                'result': '2.43288...e+4222',
                'steps': {1: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(121))^{(((1+(2+2)*3)+5)+(3*2+5)*(121))}'},
                          2: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '(((1+(2+2)*3)+5)+((3*2)+5)*121)^{(((1+(2+2)*3)+5)+((3*2)+5)*121)}'},
                          3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '(((1+(2+2)*3)+5)+((6)+5)*121)^{(((1+(2+2)*3)+5)+((6)+5)*121)}'},
                          4: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '(((1+(2+2)*3)+5)+(11)*121)^{(((1+(2+2)*3)+5)+(11)*121)}'},
                          5: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '(((1+(4)*3)+5)+11*121)^{(((1+(4)*3)+5)+11*121)}'},
                          6: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '(((1+(4*3))+5)+11*121)^{(((1+(4*3))+5)+11*121)}'},
                          7: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '(((1+(12))+5)+11*121)^{(((1+(12))+5)+11*121)}'},
                          8: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '(((13)+5)+11*121)^{(((13)+5)+11*121)}'},
                          9: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '((18)+11*121)^{((18)+11*121)}'},
                          10: {'step': 'Apply PEMDAS: (18+11*121) = (18+(11*121))', 'simplification': '(18+(11*121))^{(18+(11*121))}'},
                          11: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '(18+(1331))^{(18+(1331))}'},
                          12: {'step': 'Add the first and second term: (18+1331) = (1349)', 'simplification': '(1349)^{(1349)}'},
                          13: {'step': 'Calculate exponent: 1349^{1349} = 2.43288...e+4222', 'simplification': '2.43288...e+4222'}},
            },
            {
                'expression': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+(3*4+2)*(1+33+35+39+12))}',
                'result': '5.13416...e+5361',
                'steps': {1: {'step': 'Add and subtract [left to right]: (1+33+35+39+12) = (120)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+(3*4+2)*(120))}'},
                          2: {'step': 'Apply PEMDAS: (3*4+2) = ((3*4)+2)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+((3*4)+2)*120)}'},
                          3: {'step': 'Multiply the first and second term: (3*4) = (12)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+((12)+2)*120)}'},
                          4: {'step': 'Add the first and second term: (12+2) = (14)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(2+3)*5)+5)+(14)*120)}'},
                          5: {'step': 'Add the first and second term: (2+3) = (5)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(5)*5)+5)+14*120)}'},
                          6: {'step': 'Apply PEMDAS: (3+5*5) = (3+(5*5))', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(5*5))+5)+14*120)}'},
                          7: {'step': 'Multiply the first and second term: (5*5) = (25)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((3+(25))+5)+14*120)}'},
                          8: {'step': 'Add the first and second term: (3+25) = (28)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(((28)+5)+14*120)}'},
                          9: {'step': 'Add the first and second term: (28+5) = (33)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{((33)+14*120)}'},
                          10: {'step': 'Apply PEMDAS: (33+14*120) = (33+(14*120))', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(33+(14*120))}'},
                          11: {'step': 'Multiply the first and second term: (14*120) = (1680)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(33+(1680))}'},
                          12: {'step': 'Add the first and second term: (33+1680) = (1713)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30))^{(1713)}'},
                          13: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '(((1+(2+2)*3)+5)+(3*2+5)*(121))^{1713}'},
                          14: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '(((1+(2+2)*3)+5)+((3*2)+5)*121)^{1713}'},
                          15: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '(((1+(2+2)*3)+5)+((6)+5)*121)^{1713}'},
                          16: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '(((1+(2+2)*3)+5)+(11)*121)^{1713}'},
                          17: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '(((1+(4)*3)+5)+11*121)^{1713}'},
                          18: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '(((1+(4*3))+5)+11*121)^{1713}'},
                          19: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '(((1+(12))+5)+11*121)^{1713}'},
                          20: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '(((13)+5)+11*121)^{1713}'},
                          21: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '((18)+11*121)^{1713}'},
                          22: {'step': 'Apply PEMDAS: (18+11*121) = (18+(11*121))', 'simplification': '(18+(11*121))^{1713}'},
                          23: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '(18+(1331))^{1713}'},
                          24: {'step': 'Add the first and second term: (18+1331) = (1349)', 'simplification': '(1349)^{1713}'},
                          25: {'step': 'Calculate exponent: 1349^{1713} = 5.13416...e+5361', 'simplification': '5.13416...e+5361'}},
            },
            {
              'expression': '2^3+5',
              'result': '13',
              'steps': {1: {'step': 'Apply PEMDAS: 2^3+5 = (2^3)+5', 'simplification': '(2^3)+5'},
                        2: {'step': 'Calculate exponent: (2^3) = (8)', 'simplification': '(8)+5'},
                        3: {'step': 'Add the first and second term: 8+5 = 13', 'simplification': '13'}},
            },
            {
                'expression': '2^3+1+2+3+4',
                'result': '18',
                'steps': {1: {'step': 'Apply PEMDAS: 2^3+1+2+3+4 = (2^3)+1+2+3+4', 'simplification': '(2^3)+1+2+3+4'},
                          2: {'step': 'Calculate exponent: (2^3) = (8)', 'simplification': '(8)+1+2+3+4'},
                          3: {'step': 'Add and subtract [left to right]: 8+1+2+3+4 = 18', 'simplification': '18'}},
            },
            {
                'expression': '2^3+1+2*13*4+23',
                'result': '136',
                'steps': {1: {'step': 'Apply PEMDAS: 2^3+1+2*13*4+23 = (2^3)+1+2*13*4+23', 'simplification': '(2^3)+1+2*13*4+23'},
                          2: {'step': 'Calculate exponent: (2^3) = (8)', 'simplification': '(8)+1+2*13*4+23'},
                          3: {'step': 'Apply PEMDAS: 8+1+2*13*4+23 = 8+1+(2*13*4)+23', 'simplification': '8+1+(2*13*4)+23'},
                          4: {'step': 'Multiply [left to right]: (2*13*4) = (104)', 'simplification': '8+1+(104)+23'},
                          5: {'step': 'Add and subtract [left to right]: 8+1+104+23 = 136', 'simplification': '136'}},
            },
            {
                'expression': '1+2*13*4+23+2^3',
                'result': '136',
                'steps': {1: {'step': 'Apply PEMDAS: 1+2*13*4+23+2^3 = 1+2*13*4+23+(2^3)', 'simplification': '1+2*13*4+23+(2^3)'},
                          2: {'step': 'Calculate exponent: (2^3) = (8)', 'simplification': '1+2*13*4+23+(8)'},
                          3: {'step': 'Apply PEMDAS: 1+2*13*4+23+8 = 1+(2*13*4)+23+8', 'simplification': '1+(2*13*4)+23+8'},
                          4: {'step': 'Multiply [left to right]: (2*13*4) = (104)', 'simplification': '1+(104)+23+8'},
                          5: {'step': 'Add and subtract [left to right]: 1+104+23+8 = 136', 'simplification': '136'}},
            },
            {
                'expression': '3^{1+2+3}+13',
                'result': '742',
                'steps': {1: {'step': 'Apply PEMDAS: 3^{1+2+3}+13 = (3^{1+2+3})+13', 'simplification': '(3^{1+2+3})+13'},
                          2: {'step': 'Add and subtract [left to right]: (1+2+3) = (6)', 'simplification': '(3^{6})+13'},
                          3: {'step': 'Calculate exponent: (3^{6}) = (729)', 'simplification': '(729)+13'},
                          4: {'step': 'Add the first and second term: 729+13 = 742', 'simplification': '742'}},
            },
            {
                'expression': '3^{1+2*3*2+11}+3+5+6*3*12',
                'result': '282429536705',
                'steps': {1: {'step': 'Apply PEMDAS: 3^{1+2*3*2+11}+3+5+6*3*12 = (3^{1+2*3*2+11})+3+5+6*3*12', 'simplification': '(3^{1+2*3*2+11})+3+5+6*3*12'},
                          2: {'step': 'Apply PEMDAS: (1+2*3*2+11) = (1+(2*3*2)+11)', 'simplification': '(3^{1+(2*3*2)+11})+3+5+6*3*12'},
                          3: {'step': 'Multiply [left to right]: (2*3*2) = (12)', 'simplification': '(3^{1+(12)+11})+3+5+6*3*12'},
                          4: {'step': 'Add and subtract [left to right]: (1+12+11) = (24)', 'simplification': '(3^{24})+3+5+6*3*12'},
                          5: {'step': 'Calculate exponent: (3^{24}) = (282429536481)', 'simplification': '(282429536481)+3+5+6*3*12'},
                          6: {'step': 'Apply PEMDAS: 282429536481+3+5+6*3*12 = 282429536481+3+5+(6*3*12)', 'simplification': '282429536481+3+5+(6*3*12)'},
                          7: {'step': 'Multiply [left to right]: (6*3*12) = (216)', 'simplification': '282429536481+3+5+(216)'},
                          8: {'step': 'Add and subtract [left to right]: 282429536481+3+5+216 = 282429536705', 'simplification': '282429536705'}},
            },
            {
                'expression': '(1+2*3*4+10)^{4+2*1*1}+(5*4+3+2+1)',
                'result': '1838265651',
                'steps': {1: {'step': 'Apply PEMDAS: (5*4+3+2+1) = ((5*4)+3+2+1)', 'simplification': '(1+2*3*4+10)^{4+2*1*1}+((5*4)+3+2+1)'},
                          2: {'step': 'Multiply the first and second term: (5*4) = (20)', 'simplification': '(1+2*3*4+10)^{4+2*1*1}+((20)+3+2+1)'},
                          3: {'step': 'Add and subtract [left to right]: (20+3+2+1) = (26)', 'simplification': '(1+2*3*4+10)^{4+2*1*1}+(26)'},
                          4: {'step': 'Apply PEMDAS: (1+2*3*4+10) = (1+(2*3*4)+10)', 'simplification': '(1+(2*3*4)+10)^{4+2*1*1}+26'},
                          5: {'step': 'Multiply [left to right]: (2*3*4) = (24)', 'simplification': '(1+(24)+10)^{4+2*1*1}+26'},
                          6: {'step': 'Add and subtract [left to right]: (1+24+10) = (35)', 'simplification': '(35)^{4+2*1*1}+26'},
                          7: {'step': 'Apply PEMDAS: 35^{4+2*1*1}+26 = (35^{4+2*1*1})+26', 'simplification': '(35^{4+2*1*1})+26'},
                          8: {'step': 'Apply PEMDAS: (4+2*1*1) = (4+(2*1*1))', 'simplification': '(35^{4+(2*1*1)})+26'},
                          9: {'step': 'Multiply [left to right]: (2*1*1) = (2)', 'simplification': '(35^{4+(2)})+26'},
                          10: {'step': 'Add the first and second term: (4+2) = (6)', 'simplification': '(35^{6})+26'},
                          11: {'step': 'Calculate exponent: (35^{6}) = (1838265625)', 'simplification': '(1838265625)+26'},
                          12: {'step': 'Add the first and second term: 1838265625+26 = 1838265651', 'simplification': '1838265651'}},
            },
            {
                'expression': '(1+2)^{2+1}+(2+3)^{3+2}-(4+5)^{5+4}+(5+6)^{6+5}',
                'result': '284924253274',
                'steps': {1: {'step': 'Add the first and second term: (5+6) = (11)', 'simplification': '(1+2)^{2+1}+(2+3)^{3+2}-(4+5)^{5+4}+(11)^{6+5}'},
                          2: {'step': 'Add the first and second term: (4+5) = (9)', 'simplification': '(1+2)^{2+1}+(2+3)^{3+2}-(9)^{5+4}+11^{6+5}'},
                          3: {'step': 'Add the first and second term: (2+3) = (5)', 'simplification': '(1+2)^{2+1}+(5)^{3+2}-9^{5+4}+11^{6+5}'},
                          4: {'step': 'Add the first and second term: (1+2) = (3)', 'simplification': '(3)^{2+1}+5^{3+2}-9^{5+4}+11^{6+5}'},
                          5: {'step': 'Apply PEMDAS: 3^{2+1}+5^{3+2}-9^{5+4}+11^{6+5} = (3^{2+1})+5^{3+2}-9^{5+4}+11^{6+5}', 'simplification': '(3^{2+1})+5^{3+2}-9^{5+4}+11^{6+5}'},
                          6: {'step': 'Add the first and second term: (2+1) = (3)', 'simplification': '(3^{3})+5^{3+2}-9^{5+4}+11^{6+5}'},
                          7: {'step': 'Calculate exponent: (3^{3}) = (27)', 'simplification': '(27)+5^{3+2}-9^{5+4}+11^{6+5}'},
                          8: {'step': 'Apply PEMDAS: 27+5^{3+2}-9^{5+4}+11^{6+5} = 27+(5^{3+2})-9^{5+4}+11^{6+5}', 'simplification': '27+(5^{3+2})-9^{5+4}+11^{6+5}'},
                          9: {'step': 'Add the first and second term: (3+2) = (5)', 'simplification': '27+(5^{5})-9^{5+4}+11^{6+5}'},
                          10: {'step': 'Calculate exponent: (5^{5}) = (3125)', 'simplification': '27+(3125)-9^{5+4}+11^{6+5}'},
                          11: {'step': 'Apply PEMDAS: 27+3125-9^{5+4}+11^{6+5} = 27+3125-(9^{5+4})+11^{6+5}', 'simplification': '27+3125-(9^{5+4})+11^{6+5}'},
                          12: {'step': 'Add the first and second term: (5+4) = (9)', 'simplification': '27+3125-(9^{9})+11^{6+5}'},
                          13: {'step': 'Calculate exponent: (9^{9}) = (387420489)', 'simplification': '27+3125-(387420489)+11^{6+5}'},
                          14: {'step': 'Apply PEMDAS: 27+3125-387420489+11^{6+5} = 27+3125-387420489+(11^{6+5})', 'simplification': '27+3125-387420489+(11^{6+5})'},
                          15: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '27+3125-387420489+(11^{11})'},
                          16: {'step': 'Calculate exponent: (11^{11}) = (285311670611)', 'simplification': '27+3125-387420489+(285311670611)'},
                          17: {'step': 'Add and subtract [left to right]: 27+3125-387420489+285311670611 = 284924253274', 'simplification': '284924253274'}},
            },
            {
                'expression': '101000+1000*(9.8*2+0.5*(25^2-5^2))',
                'result': '420600',
                'steps': {1: {'step': 'Apply PEMDAS: (25^2-5^2) = ((25^2)-5^2)', 'simplification': '101000+1000*(9.8*2+0.5*((25^2)-5^2))'},
                          2: {'step': 'Calculate exponent: (25^2) = (625)', 'simplification': '101000+1000*(9.8*2+0.5*((625)-5^2))'},
                          3: {'step': 'Apply PEMDAS: (625-5^2) = (625-(5^2))', 'simplification': '101000+1000*(9.8*2+0.5*(625-(5^2)))'},
                          4: {'step': 'Calculate exponent: (5^2) = (25)', 'simplification': '101000+1000*(9.8*2+0.5*(625-(25)))'},
                          5: {'step': 'Subtract the first and second term: (625-25) = (600)', 'simplification': '101000+1000*(9.8*2+0.5*(600))'},
                          6: {'step': 'Apply PEMDAS: (9.8*2+0.5*600) = ((9.8*2)+(0.5*600))', 'simplification': '101000+1000*((9.8*2)+(0.5*600))'},
                          7: {'step': 'Multiply the first and second term: (0.5*600) = (300)', 'simplification': '101000+1000*((9.8*2)+(300))'},
                          8: {'step': 'Multiply the first and second term: (9.8*2) = (19.6)', 'simplification': '101000+1000*((19.6)+300)'},
                          9: {'step': 'Add the first and second term: (19.6+300) = (319.6)', 'simplification': '101000+1000*(319.6)'},
                          10: {'step': 'Apply PEMDAS: 101000+1000*319.6 = 101000+(1000*319.6)', 'simplification': '101000+(1000*319.6)'},
                          11: {'step': 'Multiply the first and second term: (1000*319.6) = (319600)', 'simplification': '101000+(319600)'},
                          12: {'step': 'Add the first and second term: 101000+319600 = 420600', 'simplification': '420600'}},
            },
            {
                'expression': '2^{2+1}*2^{3+2}*2^{4+3}*2^{1+4*3}',
                'result': '268435456',
                'steps': {1: {'step': 'Apply rule exponent: a^b * a^c = a^{b+c}', 'simplification': '2^{(2+1)+(3+2)+(4+3)+(1+4*3)}'},
                          2: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '2^{(2+1)+(3+2)+(4+3)+(1+(4*3))}'},
                          3: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '2^{(2+1)+(3+2)+(4+3)+(1+(12))}'},
                          4: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '2^{(2+1)+(3+2)+(4+3)+(13)}'},
                          5: {'step': 'Add the first and second term: (4+3) = (7)', 'simplification': '2^{(2+1)+(3+2)+(7)+13}'},
                          6: {'step': 'Add the first and second term: (3+2) = (5)', 'simplification': '2^{(2+1)+(5)+7+13}'},
                          7: {'step': 'Add the first and second term: (2+1) = (3)', 'simplification': '2^{(3)+5+7+13}'},
                          8: {'step': 'Add and subtract [left to right]: 3+5+7+13 = 28', 'simplification': '2^{28}'},
                          9: {'step': 'Calculate exponent: 2^{28} = 268435456', 'simplification': '268435456'}},
            },

            # PEMDAS
            {
                'expression': '1+2+3*5',
                'result': '18',
                'steps': {1: {'step': 'Apply PEMDAS: 1+2+3*5 = 1+2+(3*5)', 'simplification': '1+2+(3*5)'},
                          2: {'step': 'Multiply the first and second term: (3*5) = (15)', 'simplification': '1+2+(15)'},
                          3: {'step': 'Add and subtract [left to right]: 1+2+15 = 18', 'simplification': '18'}},
            },
            {
                'expression': '23-125*11+18',
                'result': '-1334',
                'steps': {1: {'step': 'Apply PEMDAS: 23-125*11+18 = 23-(125*11)+18', 'simplification': '23-(125*11)+18'},
                          2: {'step': 'Multiply the first and second term: (125*11) = (1375)', 'simplification': '23-(1375)+18'},
                          3: {'step': 'Add and subtract [left to right]: 23-1375+18 = -1334', 'simplification': '-1334'}}
            },
            {
                'expression': '1+2+3+4*5+6+7+9*10',
                'result': '129',
                'steps': {1: {'step': 'Apply PEMDAS: 1+2+3+4*5+6+7+9*10 = 1+2+3+(4*5)+6+7+(9*10)', 'simplification': '1+2+3+(4*5)+6+7+(9*10)'},
                          2: {'step': 'Multiply the first and second term: (9*10) = (90)', 'simplification': '1+2+3+(4*5)+6+7+(90)'},
                          3: {'step': 'Multiply the first and second term: (4*5) = (20)', 'simplification': '1+2+3+(20)+6+7+90'},
                          4: {'step': 'Add and subtract [left to right]: 1+2+3+20+6+7+90 = 129', 'simplification': '129'}},
            },
            {
                'expression': '1+2+3+4*5*6*7+8+9',
                'result': '863',
                'steps': {1: {'step': 'Apply PEMDAS: 1+2+3+4*5*6*7+8+9 = 1+2+3+(4*5*6*7)+8+9', 'simplification': '1+2+3+(4*5*6*7)+8+9'},
                          2: {'step': 'Multiply [left to right]: (4*5*6*7) = (840)', 'simplification': '1+2+3+(840)+8+9'},
                          3: {'step': 'Add and subtract [left to right]: 1+2+3+840+8+9 = 863', 'simplification': '863'}},
            },
            {
                'expression': '1+2*-3*-4*5+9',
                'result': '130',
                'steps': {1: {'step': 'Apply PEMDAS: 1+2*-3*-4*5+9 = 1+(2*-3*-4*5)+9', 'simplification': '1+(2*-3*-4*5)+9'},
                          2: {'step': 'Multiply [left to right]: (2*-3*-4*5) = (120)', 'simplification': '1+(120)+9'},
                          3: {'step': 'Add and subtract [left to right]: 1+120+9 = 130', 'simplification': '130'}},
            },

            {
                'expression': '((1+(2+2)*3)+5)+(3*2+5)*(1+30+30+30+30)',
                'result': '1349',
                'steps': {1: {'step': 'Add and subtract [left to right]: (1+30+30+30+30) = (121)', 'simplification': '((1+(2+2)*3)+5)+(3*2+5)*(121)'},
                          2: {'step': 'Apply PEMDAS: (3*2+5) = ((3*2)+5)', 'simplification': '((1+(2+2)*3)+5)+((3*2)+5)*121'},
                          3: {'step': 'Multiply the first and second term: (3*2) = (6)', 'simplification': '((1+(2+2)*3)+5)+((6)+5)*121'},
                          4: {'step': 'Add the first and second term: (6+5) = (11)', 'simplification': '((1+(2+2)*3)+5)+(11)*121'},
                          5: {'step': 'Add the first and second term: (2+2) = (4)', 'simplification': '((1+(4)*3)+5)+11*121'},
                          6: {'step': 'Apply PEMDAS: (1+4*3) = (1+(4*3))', 'simplification': '((1+(4*3))+5)+11*121'},
                          7: {'step': 'Multiply the first and second term: (4*3) = (12)', 'simplification': '((1+(12))+5)+11*121'},
                          8: {'step': 'Add the first and second term: (1+12) = (13)', 'simplification': '((13)+5)+11*121'},
                          9: {'step': 'Add the first and second term: (13+5) = (18)', 'simplification': '(18)+11*121'},
                          10: {'step': 'Apply PEMDAS: 18+11*121 = 18+(11*121)', 'simplification': '18+(11*121)'},
                          11: {'step': 'Multiply the first and second term: (11*121) = (1331)', 'simplification': '18+(1331)'},
                          12: {'step': 'Add the first and second term: 18+1331 = 1349', 'simplification': '1349'}},
            },
            # COMPLICATED
            {
                'expression': '((((((28+298)*34)+22)*2821)*18)+7)+((((((27+213)*242)+1763)*3)*4)+3)',
                'result': '564658594',
                'steps': {1: {'step': 'Add the first and second term: (27+213) = (240)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+((((((240)*242)+1763)*3)*4)+3)'},
                          2: {'step': 'Multiply the first and second term: (240*242) = (58080)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+(((((58080)+1763)*3)*4)+3)'},
                          3: {'step': 'Add the first and second term: (58080+1763) = (59843)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+((((59843)*3)*4)+3)'},
                          4: {'step': 'Multiply the first and second term: (59843*3) = (179529)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+(((179529)*4)+3)'},
                          5: {'step': 'Multiply the first and second term: (179529*4) = (718116)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+((718116)+3)'},
                          6: {'step': 'Add the first and second term: (718116+3) = (718119)', 'simplification': '((((((28+298)*34)+22)*2821)*18)+7)+(718119)'},
                          7: {'step': 'Add the first and second term: (28+298) = (326)', 'simplification': '((((((326)*34)+22)*2821)*18)+7)+718119'},
                          8: {'step': 'Multiply the first and second term: (326*34) = (11084)', 'simplification': '(((((11084)+22)*2821)*18)+7)+718119'},
                          9: {'step': 'Add the first and second term: (11084+22) = (11106)', 'simplification': '((((11106)*2821)*18)+7)+718119'},
                          10: {'step': 'Multiply the first and second term: (11106*2821) = (31330026)', 'simplification': '(((31330026)*18)+7)+718119'},
                          11: {'step': 'Multiply the first and second term: (31330026*18) = (563940468)', 'simplification': '((563940468)+7)+718119'},
                          12: {'step': 'Add the first and second term: (563940468+7) = (563940475)', 'simplification': '(563940475)+718119'},
                          13: {'step': 'Add the first and second term: 563940475+718119 = 564658594', 'simplification': '564658594'}},
            },
            # SPECIAL NUMBERS
            {
                'expression': '4*3.141592653589793*(1+72+827-36)',
                'result': '10857.34368',
                'steps': {1: {'step': 'Add and subtract [left to right]: (1+72+827-36) = (864)', 'simplification': '4*3.141592653589793*(864)'},
                          2: {'step': 'Multiply [left to right]: 4*3.141592653589793*864 = 10857.34368', 'simplification': '10857.34368'}},
            },
            {
                'expression': '9*2.718281828459045*(283+82-4)',
                'result': '8831.69894',
                'steps': {1: {'step': 'Add and subtract [left to right]: (283+82-4) = (361)', 'simplification': '9*2.718281828459045*(361)'},
                          2: {'step': 'Multiply [left to right]: 9*2.718281828459045*361 = 8831.69894', 'simplification': '8831.69894'}},
            },

        ]

        for item in expressionsAndResults:
            Simplification = evaluateArithmetic(item['expression'])
            Steps = Simplification[0]
            Result = Simplification[1]

            self.assertEqual(Steps, item['steps'], f"Expression: {item['expression']}")
            self.assertEqual(Result, item['result'], f"Expression: {item['expression']}")

    # TEST performOperation
    def test_performOperation(self):
        expressionAndResults = [
            {
                'expression': '1+2+3+4+5+6',
                'result': '21',
                'operation': 'arithmetic-add-single',
            },
            {
                'expression': '1+26+274+8723+26',
                'result': '9050',
                'operation': 'arithmetic-add-single',
            },
            {
                'expression': '-44-245-27-47-482',
                'result': '-845',
                'operation': 'add-subtract-only',
            },
            {
                'expression': '264+2842+132-427+183-78',
                'result': '2916',
                'operation': 'add-subtract-only',
            },
            {
                'expression': '21*62*51*12',
                'result': '796824',
                'operation': 'multiply-only',
            },
            {
                'expression': '21*62*51*12*11',
                'result': '8765064',
                'operation': 'multiply-only',
            },
            {
                'expression': '12*-5*21*32*-12*3*-3',
                'result': '-4354560',
                'operation': 'multiply-only',
            },
            {
                'expression': '12*-5*21*32*-12*3*-3*-2',
                'result': '8709120',
                'operation': 'multiply-only',
            },
        ]

        for item in expressionAndResults:
            self.assertEqual(performOperation(item['expression'], item['operation']), item['result'], f"Expression: {item['expression']}")

    # TEST applyPEMDAS
    def test_applyPEMDAS(self):
        expressionAndResults = [
            {
                'expression': '1+2+3',
                'result': '1+2+3',
            },
            {
                'expression': '1+2*3',
                'result': '1+(2*3)',
            },
            {
                'expression': '1-2*3',
                'result': '1-(2*3)',
            },
            {
                'expression': '1+2*3*4*5',
                'result': '1+(2*3*4*5)',
            },
            {
                'expression': '1+274*24*24*5',
                'result': '1+(274*24*24*5)',
            },
            {
                'expression': '1+24*43*24*5*6+234',
                'result': '1+(24*43*24*5*6)+234',
            },
            {
                'expression': '1+2*-5*-23*4*54+96',
                'result': '1+(2*-5*-23*4*54)+96',
            },
            {
                'expression': '12+3*2+67+9*13+12-5*7',
                'result': '12+(3*2)+67+(9*13)+12-(5*7)',
            },

        ]

        for item in expressionAndResults:
            Expression = ArithmeticExpression(item['expression'])
            self.assertEqual(str(Expression.applyPEMDAS()), item['result'], f"Expression: {item['expression']}")

    # TEST getIndexOfInnerMostParen
    def test_getIndexOfInnerMostParen(self):
        expressionAndResults = [
            {
                'expression': '23*(3+2+(3*2))',
                'result': 8,
            },
            {
                'expression': '((((((28+298)*34)+22)*2821)*18)+7)',
                'result': 5,
            },
            {
                'expression': '23*(5*(5+3+(3*(3+62+75*(23+89)))))',
                'result': 23,
            },
        ]

        for item in expressionAndResults:
            Expression = ArithmeticExpression(item['expression'])
            self.assertEqual(Expression.getIndexOfInnerMostParen(), item['result'], f"Expression: {item['expression']}")

    # TEST wrapStepInParen
    def test_wrapStepInParen(self):
        stepsAndResults = [
            {
                'step': 'Add and subtract [left to right]: (3*53*342) = (54378)',
                'result': 'Add and subtract [left to right]: (3*53*342) = (54378)',
            },
            {
                'step': 'Add and subtract [left to right]: 3*53*342 = 54378',
                'result': 'Add and subtract [left to right]: (3*53*342) = (54378)',
            },
            {
                'step': 'Apply log rule [ln(a*b) = ln(a) + ln(b)]: ln(e*a^t) = ln(e) + ln(a^t)',
                'result': 'Apply log rule [ln(a*b) = ln(a) + ln(b)]: (ln(e*a^t)) = (ln(e) + ln(a^t))',
            },
        ]

        for item in stepsAndResults:
            self.assertEqual(item['result'], wrapStepInParen(item['step']), f"Step: {item['step']}")

    # TEST splitExpression
    def test_splitExpression(self):
        expressionAndResults = [
            {
                'expression': '132*425+12-48',
                'index': 7,
                'operator': '+',
                'operation': 'arithmetic-add-single',
                'binarySplit': True,
                'result': ('425', '12'),
            },
            {
                'expression': '132+425*12-48',
                'index': 7,
                'operator': '*',
                'operation': 'multiply-only',
                'binarySplit': False,
                'result': ('132+425', '12-48'),
            },
            {
                'expression': '56-123*57-28',
                'index': 6,
                'operator': '*',
                'operation': 'multiply-only',
                'binarySplit': True,
                'result': ('-123', '57'),
            },
            {
                'expression': '56-123*57-28',
                'index': 6,
                'operator': '*',
                'operation': 'multiply-only',
                'binarySplit': False,
                'result': ('56-123', '57-28'),
            },
            {
                'expression': '12+127*-57-28',
                'index': 6,
                'operator': '*',
                'operation': 'multiply-only',
                'binarySplit': True,
                'result': ('127', '-57'),
            },
            {
                'expression': '12+127*-57-28',
                'index': 6,
                'operator': '*',
                'operation': 'multiply-only',
                'binarySplit': False,
                'result': ('12+127', '-57-28'),
            },
        ]

        for item in expressionAndResults:
            Result = splitExpression(item['expression'], item['index'], item['operator'], item['binarySplit'], item['operation'])
            self.assertEqual(item['result'], Result, f"Expression: {item['expression']}")

    # TEST castToFloatOrInt
    def test_castToFloatOrInt(self):
        expressionAndResults = [
            {
                'expression': 2.0,
                'castToString': True,
                'result': '2',
            },
            {
                'expression': 2.0,
                'castToString': False,
                'result': 2,
            },
            {
                'expression': 0.25,
                'castToString': True,
                'result': '0.25',
            },
            {
                'expression': 0.25,
                'castToString': False,
                'result': 0.25,
            },
        ]

        for item in expressionAndResults:
            self.assertEqual(item['result'], castToFloatOrInt(item['expression'], item['castToString']))

def test():
    Simplification = evaluateArithmetic('23-125*11+18')

    result = Simplification[1]
    print(result)





# test()



if __name__ == '__main__':
    unittest.main()