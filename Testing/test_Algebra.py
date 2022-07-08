import unittest
import sys
""" ADD PATH WHERE PROJECT IS LOCATED TO ALLOW FOR IMPORT OF APPLICATION """
sys.path.append(r"C:\Users\jahei\OneDrive\Documents\Flask-Projects\Flask\Personal-Projects\Computer Algebra")
from Algebra import get_start_of_var, get_var, get_coefficient, addNumbers, simplifyExpression, latexify, Expression



# RUN: python -m unittest test_Algebra.py

class TestCalc(unittest.TestCase):
    # maxDiff = None

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
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+3+4=10'}], 'finalResult': '10'},
            },
            {
                'expression': '1+a+a+b',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+a+a+b=a+a+b+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle a+a+b+1=2a+b+1'}], 'finalResult': '2a+b+1'},
            },
            {
                'expression': '1+2+3+a+a+c',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2+3+a+a+c=a+a+c+1+2+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle a+a+c+1+2+3=2a+c+1+2+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2a+c+1+2+3=2a+c+6'}], 'finalResult': '2a+c+6'},
            },
            {
                'expression': '15x+13x+x-2+15',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 15x+13x+x-2+15=29x-2+15'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 29x-2+15=29x+13'}], 'finalResult': '29x+13'}
            },
            {
                'expression': 'a+a+5b-2b+c-c',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle a+a+5b-2b+c-c=2a+3b+0'}], 'finalResult': '2a+3b'},
            },
            {
                'expression': '5x+3+5+x',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 5x+3+5+x=5x+x+3+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+x+3+5=6x+3+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 6x+3+5=6x+8'}], 'finalResult': '6x+8'},
            },
            {
                'expression': '1+pi+5sin(ab+c)-2sin(ab+c)+3pi+3',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+\\pi+5\\sin\\left(ab+c\\right)-2\\sin\\left(ab+c\\right)+3\\pi+3=\\pi+3\\pi+5\\sin\\left(ab+c\\right)-2\\sin\\left(ab+c\\right)+1+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle \\pi+3\\pi+5\\sin\\left(ab+c\\right)-2\\sin\\left(ab+c\\right)+1+3=4\\pi+3\\sin\\left(ab+c\\right)+1+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4\\pi+3\\sin\\left(ab+c\\right)+1+3=4\\pi+3\\sin\\left(ab+c\\right)+4'}], 'finalResult': '4\\pi+3\\sin\\left(ab+c\\right)+4'}
            },
            {
                'expression': 'sqrt{1+2+x+15x-3}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2+x+15x-3=x+15x+1+2-3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle x+15x+1+2-3=16x+1+2-3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 16x+1+2-3=16x+0'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{1+2+x+15x-3}=\\sqrt{16x}'}], 'finalResult': '\\sqrt{16x}'},
            },
            {
                'expression': 'sqrt{15x-2x}+2+3',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{15x-2x}=\\sqrt{13x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 15x-2x=13x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{15x-2x}=\\sqrt{13x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 2+3=5', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'}]}], 'finalResult': '\\sqrt{13x}+5'},
            },
            {
                'expression': '1+x+sqrt{1+25x-15x+3x+13}+3x-5',
                'keyword': None,
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
                'keyword': None,
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
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\sqrt{36}=6'}], 'finalResult': '6'},
            },
            {
                'expression': 'sqrt{72}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Factor Radical}', 'info': '\\displaystyle \\sqrt{72}=\\sqrt{36}\\cdot\\sqrt{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{36}\\cdot\\sqrt{2}=6\\sqrt{2}'}], 'finalResult': '6\\sqrt{2}'},
            },
            {
                'expression': '2sqrt{3+1}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+1=4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 2\\sqrt{3+1}=2\\sqrt{4}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle 2\\sqrt{4}=2\\cdot2'}], 'finalResult': '2\\cdot2'},

            },
            {
                'expression': '(a+b)sqrt{4}+(2x+y)sqrt{36}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(a+b\\right)\\sqrt{4}=2\\left(a+b\\right)', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\left(a+b\\right)\\sqrt{4}=2\\left(a+b\\right)'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(2x+y\\right)\\sqrt{36}=6\\left(2x+y\\right)', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\left(2x+y\\right)\\sqrt{36}=6\\left(2x+y\\right)'}]}], 'finalResult': '2\\left(a+b\\right)+6\\left(2x+y\\right)'},

            },
            {
                'expression': 'sqrt[3]{94+2}+sqrt[5]{2x+3x+1}',
                'keyword': None,
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
                'keyword': None,
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
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+3x+2x=3x+2x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x+1=5x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt[n]{1+3x+2x}=\\sqrt[n]{5x+1}'}], 'finalResult': '\\sqrt[n]{5x+1}'},
            },
            {
                'expression': '2^3',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 2^3=8'}], 'finalResult': '8'},
            },
            {
                'expression': '(1+2+2x+3x+3)^2',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2+2x+3x+3=2x+3x+1+2+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+3x+1+2+3=5x+1+2+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5x+1+2+3=5x+6'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(1+2+2x+3x+3\\right)^2=\\left(5x+6\\right)^{2}'}], 'finalResult': '\\left(5x+6\\right)^{2}'},
            },
            {
                'expression': 'e^{1+5x+3x+4}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+5x+3x+4=5x+3x+1+4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+1+4=8x+1+4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 8x+1+4=8x+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{1+5x+3x+4}=e^{8x+5}'}], 'finalResult': 'e^{8x+5}'},
            },
            {
                'expression': '(2x+x+1)^{1+2+3x-x}',
                'keyword': None,
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
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x+1=5x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(3x+2x+1\\right)^{1+2+3}=\\left(5x+1\\right)^{1+2+3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+3=6'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(5x+1\\right)^{1+2+3}=\\left(5x+1\\right)^{6}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{\\left(3x+2x+1\\right)^{1+2+3}}=\\sqrt{\\left(5x+1\\right)^{6}}'}], 'finalResult': '\\sqrt{\\left(5x+1\\right)^{6}}'},
            },
            {
                'expression': '(5x+2x+1)^{3+2-5}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+2x+1=7x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(5x+2x+1\\right)^{3+2-5}=\\left(7x+1\\right)^{3+2-5}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+2-5=0'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(7x+1\\right)^{3+2-5}=\\left(7x+1\\right)^{0}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply exponent rule:}\\ a^0=1', 'info': '\\displaystyle \\left(7x+1\\right)^{0}=1'}], 'finalResult': '1'},
            },
            {
                'expression': '3(2x+x)^{3-1}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+x=3x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle 3\\left(2x+x\\right)^{3-1}=3\\left(3x\\right)^{3-1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3-1=2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3\\left(3x\\right)^{3-1}=3\\left(3x\\right)^{2}'}], 'finalResult': '3\\left(3x\\right)^{2}'},
            },
            {
                'expression': '(5x+2x-7x)^{1+2x}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+2x-7x=0'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(5x+2x-7x\\right)^{1+2x}=0^{1+2x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2x=2x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 0^{1+2x}=0^{2x+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply exponent rule:}\\ 0^a=0', 'info': '\\displaystyle 0^{2x+1}=0'}], 'finalResult': '0'},
            },
            {
                'expression': '1+2+sqrt{74+6}+2^{1+2}+(3+2)^2',
                'keyword': None,
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
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2\\sqrt{x}+3\\sqrt{x}=5\\sqrt{x}'}], 'finalResult': '5\\sqrt{x}'},
            },
            {
                'expression': '1+2+3sqrt{5x+3x+2x}+5sqrt{8x+2x}',
                'keyword': None,
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
                'expression': '(1+2)^{sqrt{x+sqrt{8}}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(1+2\\right)^{\\sqrt{x+\\sqrt{8}}}=3^{\\sqrt{x+\\sqrt{8}}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle x+\\sqrt{8}=\\sqrt{8}+x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Factor Radical}', 'info': '\\displaystyle \\sqrt{8}=\\sqrt{4}\\cdot\\sqrt{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{4}\\cdot\\sqrt{2}=2\\sqrt{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{x+\\sqrt{8}}=\\sqrt{2\\sqrt{2}+x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3^{\\sqrt{x+\\sqrt{8}}}=3^{\\sqrt{2\\sqrt{2}+x}}'}], 'finalResult': '3^{\\sqrt{2\\sqrt{2}+x}}'},
            },
            {
                'expression': '2^{2^{2^2}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 2^2=4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2^{2^2}=2^{4}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponential}', 'info': '\\displaystyle 2^{4}=16'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2^{2^{2^2}}=2^{16}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponential}', 'info': '\\displaystyle 2^{16}=65536'}], 'finalResult': '65536'},
            },
            {
                'expression': '2^{2^{2^{2^{2^2}}}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 2^2=4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2^{2^2}=2^{4}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponential}', 'info': '\\displaystyle 2^{4}=16'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2^{2^{2^2}}=2^{16}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponential}', 'info': '\\displaystyle 2^{16}=65536'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2^{2^{2^{2^2}}}=2^{65536}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2^{2^{2^{2^{2^2}}}}=2^{2^{65536}}'}], 'finalResult': '2^{2^{65536}}'}
            },
            {
                'expression': '(1+1)^x+2^{3x-2x}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(1+1\\right)^x=2^{x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(1+1\\right)^x=2^{x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 2^{3x-2x}=2^{x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x-2x=x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2^{3x-2x}=2^{x}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle \\left(1+1\\right)^x+2^{3x-2x}=2^{x}+2^{x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 2^{x}+2^{x}=2\\cdot2^{x}'}], 'finalResult': '2\\cdot2^{x}'},
            },
            {
                'expression': '4x+2x+(1+1)^{x}+(3-1)^{x}+(5-2)^{5x-4x}+2^{x}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 4x+2x+\\left(1+1\\right)^{x}+\\left(3-1\\right)^{x}+\\left(5-2\\right)^{5x-4x}+2^{x}=\\left(1+1\\right)^{x}+\\left(3-1\\right)^{x}+\\left(5-2\\right)^{5x-4x}+2^{x}+4x+2x'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(1+1\\right)^{x}=2^{x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(1+1\\right)^{x}=2^{x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(3-1\\right)^{x}=2^{x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3-1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(3-1\\right)^{x}=2^{x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(5-2\\right)^{5x-4x}=3^{x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5-2=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(5-2\\right)^{5x-4x}=3^{5x-4x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x-4x=x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3^{5x-4x}=3^{x}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle \\left(1+1\\right)^{x}+\\left(3-1\\right)^{x}+\\left(5-2\\right)^{5x-4x}+2^{x}=2^{x}+2^{x}+3^{x}+2^{x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 2^{x}+2^{x}+3^{x}+2^{x}=2^{x}+2^{x}+2^{x}+3^{x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 2^{x}+2^{x}+2^{x}+3^{x}=3\\cdot2^{x}+3^{x}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 4x+2x=6x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 4x+2x=6x'}]}], 'finalResult': '3\\cdot2^{x}+3^{x}+6x'}
            },
            {
                'expression': '2^{x}+2^{3}+1+2+3',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle 2^{3}=8', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '2^{3}=8'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+2+3=6', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+3=6'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 8+2^{x}+6'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 8+2^{x}+6=2^{x}+8+6'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 8+6=14'}], 'finalResult': '2^{x}+14'},

            },
            {
                'expression': '2^{x}+3^{x}+4^{x}',
                'keyword': None,
                'expected_val': {'steps': [], 'finalResult': '2^{x}+3^{x}+4^{x}'},
            },
            {
                'expression': '3*2^{x}',
                'keyword': None,
                'expected_val': {'steps': [], 'finalResult': '3\\cdot2^{x}'},
            },
            {
                'expression': '123^{2}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 123^{2}=15129'}], 'finalResult': '15129'},
            },
            {
                'expression': 'sqrt{(5x+3x+1)^{2}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply radical rule:}\\ \\sqrt[n]{a^n}=a', 'info': '\\displaystyle \\sqrt{\\left(5x+3x+1\\right)^{2}}=\\left(5x+3x+1\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(5x+3x+1\\right)=5x+3x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+1=8x+1'}], 'finalResult': '8x+1'},
            },
            {
                'expression': '(sqrt{5x+3x+1})^{5-3}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(\\sqrt{5x+3x+1}\\right)^{5-3}=\\left(\\sqrt{8x+1}\\right)^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+1=8x+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{5x+3x+1}=\\sqrt{8x+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(\\sqrt{5x+3x+1}\\right)^{5-3}=\\left(\\sqrt{8x+1}\\right)^{5-3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5-3=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(\\sqrt{8x+1}\\right)^{5-3}=\\left(\\sqrt{8x+1}\\right)^{2}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\left(\\sqrt{8x+1}\\right)^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply exponential rule:}\\ (\\sqrt[n]{a})^n=a', 'info': '\\displaystyle \\left(\\sqrt{8x+1}\\right)^{2}=8x+1'}], 'finalResult': '8x+1'}
            },
            {
                'expression': '(sqrt{5x+3x+1})^{3}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+1=8x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{5x+3x+1}=\\sqrt{8x+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(\\sqrt{5x+3x+1}\\right)^{3}=\\left(\\sqrt{8x+1}\\right)^{3}'}], 'finalResult': '\\left(\\sqrt{8x+1}\\right)^{3}'}
            },
            {
                'expression': 'frac{5x+3x+2x}{3x-2x}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+2x=10x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{5x+3x+2x}{3x-2x}=\\frac{10x}{3x-2x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x-2x=x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{10x}{3x-2x}=\\frac{10x}{x}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{10x}{x}=10', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Cancel like terms}', 'info': '\\displaystyle \\frac{10x}{x}=10'}]}], 'finalResult': '10'},
            },
            {
                'expression': 'frac{8x+2x}{2x+3x}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{8x+2x}{2x+3x}=\\frac{10}{5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 8x+2x=10x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{8x+2x}{2x+3x}=\\frac{10x}{2x+3x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+3x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{10x}{2x+3x}=\\frac{10x}{5x}'},
                        {'type': 'e-step', 'heading': '\\displaystyle \\frac{10x}{5x}=\\frac{10}{5}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Cancel like terms}', 'info': '\\displaystyle \\frac{10x}{5x}=\\frac{10}{5}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{10}{5}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Divide The Numbers}', 'info': '\\displaystyle \\frac{10}{5}=2'}], 'finalResult': '2'},
            },
            {
                'expression': 'frac{10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}}{5x+3x+2x}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}=10x^{2}+12x^{2}+7x^{2}-2x^{2}+5x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 10x^{2}+12x^{2}+7x^{2}-2x^{2}=27x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}}{5x+3x+2x}=\\frac{27x^{2}+5x}{5x+3x+2x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+2x=10x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{27x^{2}+5x}{5x+3x+2x}=\\frac{27x^{2}+5x}{10x}'}], 'finalResult': '\\frac{27x^{2}+5x}{10x}'},
            },
            {
                'expression': 'frac{10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}}{5x+3x+2x}',
                'keyword': 'expand',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}}{5x+3x+2x}=\\frac{27x}{10}+\\frac{5}{10}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}=10x^{2}+12x^{2}+7x^{2}-2x^{2}+5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 10x^{2}+12x^{2}+7x^{2}-2x^{2}=27x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}}{5x+3x+2x}=\\frac{27x^{2}+5x}{5x+3x+2x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+2x=10x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{27x^{2}+5x}{5x+3x+2x}=\\frac{27x^{2}+5x}{10x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a \\pm b}{c}=\\frac{a}{c}\\pm\\frac{b}{c}', 'info': '\\displaystyle \\frac{27x^{2}+5x}{10x}=\\frac{27x^{2}}{10x}+\\frac{5x}{10x}'},
                        {'type': 'e-step', 'heading': '\\displaystyle \\frac{27x^{2}}{10x}+\\frac{5x}{10x}=\\frac{27x}{10}+\\frac{5}{10}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Cancel like terms}', 'info': '\\displaystyle \\frac{27x^{2}}{10x}=\\frac{27x}{10}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Cancel like terms}', 'info': '\\displaystyle \\frac{5x}{10x}=\\frac{5}{10}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{27x}{10}+\\frac{5}{10}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Reduce Fraction}', 'info': '\\displaystyle \\frac{5}{10}=\\frac{1}{2}'}], 'finalResult': '\\frac{27x}{10}+\\frac{1}{2}'},
            },
            {
                'expression': 'frac{5x+3x+e^{7x+3x+2}+5}{e^{2sqrt{x}+3sqrt{3x-2x}}+sqrt{25x-12x+2}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 5x+3x+e^{7x+3x+2}+5=e^{7x+3x+2}+5x+3x+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 7x+3x+2=10x+2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{7x+3x+2}=e^{10x+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+3x+5=8x+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{5x+3x+e^{7x+3x+2}+5}{e^{2\\sqrt{x}+3\\sqrt{3x-2x}}+\\sqrt{25x-12x+2}}=\\frac{e^{10x+2}+8x+5}{e^{2\\sqrt{x}+3\\sqrt{3x-2x}}+\\sqrt{25x-12x+2}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x-2x=x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 3\\sqrt{3x-2x}=3\\sqrt{x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 2\\sqrt{x}+3\\sqrt{x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2\\sqrt{x}+3\\sqrt{x}=5\\sqrt{x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{2\\sqrt{x}+3\\sqrt{3x-2x}}=e^{5\\sqrt{x}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 25x-12x+2=13x+2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{25x-12x+2}=\\sqrt{13x+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{e^{10x+2}+8x+5}{e^{2\\sqrt{x}+3\\sqrt{3x-2x}}+\\sqrt{25x-12x+2}}=\\frac{e^{10x+2}+8x+5}{e^{5\\sqrt{x}}+\\sqrt{13x+2}}'}], 'finalResult': '\\frac{e^{10x+2}+8x+5}{e^{5\\sqrt{x}}+\\sqrt{13x+2}}'}
            },
            {
                'expression': 'frac{1+1+1+1}{2}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1+1+1=4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{1+1+1+1}{2}=\\frac{4}{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Divide The Numbers}', 'info': '\\displaystyle \\frac{4}{2}=2'}], 'finalResult': '2'}
            },
            {
                'expression': 'frac{26}{50}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Reduce Fraction}', 'info': '\\displaystyle \\frac{26}{50}=\\frac{13}{25}'}], 'finalResult': '\\frac{13}{25}'},
            },
            {
                'expression': 'frac{1}{2}+frac{2}{5}+frac{1}{7}+frac{3}{9}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{3}{9}=\\frac{1}{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Reduce Fraction}', 'info': '\\displaystyle \\frac{3}{9}=\\frac{1}{3}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }210', 'info': '\\displaystyle \\frac{1}{2}+\\frac{2}{5}+\\frac{1}{7}+\\frac{1}{3}=\\frac{105}{210}+\\frac{84}{210}+\\frac{30}{210}+\\frac{70}{210}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{105}{210}+\\frac{84}{210}+\\frac{30}{210}+\\frac{70}{210}=\\frac{105+84+30+70}{210}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{105+84+30+70}{210}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 105+84+30+70=289'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{105+84+30+70}{210}=\\frac{289}{210}'}], 'finalResult': '\\frac{289}{210}'},
            },
            {
                'expression': 'frac{5+2+7}{a}+frac{10-12}{b}+frac{11}{c}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{5+2+7}{a}=\\frac{14}{a}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5+2+7=14'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{5+2+7}{a}=\\frac{14}{a}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{10-12}{b}=\\frac{-2}{b}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 10-12=-2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{10-12}{b}=\\frac{-2}{b}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }abc', 'info': '\\displaystyle \\frac{14}{a}+\\frac{-2}{b}+\\frac{11}{c}=\\frac{14bc}{abc}+\\frac{-2ac}{abc}+\\frac{11ab}{abc}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{14bc}{abc}+\\frac{-2ac}{abc}+\\frac{11ab}{abc}=\\frac{14bc+-2ac+11ab}{abc}'}], 'finalResult': '\\frac{14bc-2ac+11ab}{abc}'},
            },
            {
                'expression': 'frac{1}{a+b}+frac{2}{c+d}+frac{10}{u+v}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)', 'info': '\\displaystyle \\frac{1}{a+b}+\\frac{2}{c+d}+\\frac{10}{u+v}=\\frac{\\left(c+d\\right)\\left(u+v\\right)}{\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)}+\\frac{2\\left(a+b\\right)\\left(u+v\\right)}{\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)}+\\frac{10\\left(a+b\\right)\\left(c+d\\right)}{\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{\\left(c+d\\right)\\left(u+v\\right)}{\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)}+\\frac{2\\left(a+b\\right)\\left(u+v\\right)}{\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)}+\\frac{10\\left(a+b\\right)\\left(c+d\\right)}{\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)}=\\frac{\\left(c+d\\right)\\left(u+v\\right)+2\\left(a+b\\right)\\left(u+v\\right)+10\\left(a+b\\right)\\left(c+d\\right)}{\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)}'}], 'finalResult': '\\frac{\\left(c+d\\right)\\left(u+v\\right)+2\\left(a+b\\right)\\left(u+v\\right)+10\\left(a+b\\right)\\left(c+d\\right)}{\\left(a+b\\right)\\left(c+d\\right)\\left(u+v\\right)}'},
            },
            {
                'expression': 'frac{7x^{2}-3x^{2}}{x+y}-frac{10x^{2}+5x^{2}}{u+v}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{7x^{2}-3x^{2}}{x+y}=\\frac{4x^{2}}{x+y}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 7x^{2}-3x^{2}=4x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{7x^{2}-3x^{2}}{x+y}=\\frac{4x^{2}}{x+y}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{10x^{2}+5x^{2}}{u+v}=\\frac{15x^{2}}{u+v}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 10x^{2}+5x^{2}=15x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{10x^{2}+5x^{2}}{u+v}=\\frac{15x^{2}}{u+v}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\left(x+y\\right)\\left(u+v\\right)', 'info': '\\displaystyle \\frac{4x^{2}}{x+y}-\\frac{15x^{2}}{u+v}=\\frac{4x^{2}\\left(u+v\\right)}{\\left(x+y\\right)\\left(u+v\\right)}-\\frac{15x^{2}\\left(x+y\\right)}{\\left(x+y\\right)\\left(u+v\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{4x^{2}\\left(u+v\\right)}{\\left(x+y\\right)\\left(u+v\\right)}-\\frac{15x^{2}\\left(x+y\\right)}{\\left(x+y\\right)\\left(u+v\\right)}=\\frac{4x^{2}\\left(u+v\\right)-15x^{2}\\left(x+y\\right)}{\\left(x+y\\right)\\left(u+v\\right)}'}], 'finalResult': '\\frac{4x^{2}\\left(u+v\\right)-15x^{2}\\left(x+y\\right)}{\\left(x+y\\right)\\left(u+v\\right)}'},
            },
            {
                'expression': 'frac{10y}{x}+frac{3x}{x+1}+frac{2}{x+y+z}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }x\\left(x+1\\right)\\left(x+y+z\\right)', 'info': '\\displaystyle \\frac{10y}{x}+\\frac{3x}{x+1}+\\frac{2}{x+y+z}=\\frac{10y\\left(x+1\\right)\\left(x+y+z\\right)}{x\\left(x+1\\right)\\left(x+y+z\\right)}+\\frac{3xx\\left(x+y+z\\right)}{x\\left(x+1\\right)\\left(x+y+z\\right)}+\\frac{2x\\left(x+1\\right)}{x\\left(x+1\\right)\\left(x+y+z\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{10y\\left(x+1\\right)\\left(x+y+z\\right)}{x\\left(x+1\\right)\\left(x+y+z\\right)}+\\frac{3xx\\left(x+y+z\\right)}{x\\left(x+1\\right)\\left(x+y+z\\right)}+\\frac{2x\\left(x+1\\right)}{x\\left(x+1\\right)\\left(x+y+z\\right)}=\\frac{10y\\left(x+1\\right)\\left(x+y+z\\right)+3xx\\left(x+y+z\\right)+2x\\left(x+1\\right)}{x\\left(x+1\\right)\\left(x+y+z\\right)}'}], 'finalResult': '\\frac{10y\\left(x+1\\right)\\left(x+y+z\\right)+3xx\\left(x+y+z\\right)+2x\\left(x+1\\right)}{x\\left(x+1\\right)\\left(x+y+z\\right)}'},
            },
            {
                'expression': 'frac{5x^{2}+2x^{2}+1+3}{1+sqrt{10x+3x+y}}+frac{15x+21x}{e^{3x+2x}+sqrt{7x-2x}}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{5x^{2}+2x^{2}+1+3}{1+\\sqrt{10x+3x+y}}=\\frac{7x^{2}+4}{\\sqrt{13x+y}+1}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 5x^{2}+2x^{2}=7x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+3=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{5x^{2}+2x^{2}+1+3}{1+\\sqrt{10x+3x+y}}=\\frac{7x^{2}+4}{1+\\sqrt{10x+3x+y}}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 1+\\sqrt{10x+3x+y}=\\sqrt{10x+3x+y}+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 10x+3x+y=13x+y'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{10x+3x+y}=\\sqrt{13x+y}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{7x^{2}+4}{1+\\sqrt{10x+3x+y}}=\\frac{7x^{2}+4}{\\sqrt{13x+y}+1}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{15x+21x}{e^{3x+2x}+\\sqrt{7x-2x}}=\\frac{36x}{e^{5x}+\\sqrt{5x}}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 15x+21x=36x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{15x+21x}{e^{3x+2x}+\\sqrt{7x-2x}}=\\frac{36x}{e^{3x+2x}+\\sqrt{7x-2x}}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{3x+2x}=e^{5x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 7x-2x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{7x-2x}=\\sqrt{5x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{36x}{e^{3x+2x}+\\sqrt{7x-2x}}=\\frac{36x}{e^{5x}+\\sqrt{5x}}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\left(\\sqrt{13x+y}+1\\right)\\left(e^{5x}+\\sqrt{5x}\\right)', 'info': '\\displaystyle \\frac{7x^{2}+4}{\\sqrt{13x+y}+1}+\\frac{36x}{e^{5x}+\\sqrt{5x}}=\\frac{\\left(7x^{2}+4\\right)\\left(e^{5x}+\\sqrt{5x}\\right)}{\\left(\\sqrt{13x+y}+1\\right)\\left(e^{5x}+\\sqrt{5x}\\right)}+\\frac{36x\\left(\\sqrt{13x+y}+1\\right)}{\\left(\\sqrt{13x+y}+1\\right)\\left(e^{5x}+\\sqrt{5x}\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{\\left(7x^{2}+4\\right)\\left(e^{5x}+\\sqrt{5x}\\right)}{\\left(\\sqrt{13x+y}+1\\right)\\left(e^{5x}+\\sqrt{5x}\\right)}+\\frac{36x\\left(\\sqrt{13x+y}+1\\right)}{\\left(\\sqrt{13x+y}+1\\right)\\left(e^{5x}+\\sqrt{5x}\\right)}=\\frac{\\left(7x^{2}+4\\right)\\left(e^{5x}+\\sqrt{5x}\\right)+36x\\left(\\sqrt{13x+y}+1\\right)}{\\left(\\sqrt{13x+y}+1\\right)\\left(e^{5x}+\\sqrt{5x}\\right)}'}], 'finalResult': '\\frac{\\left(7x^{2}+4\\right)\\left(e^{5x}+\\sqrt{5x}\\right)+36x\\left(\\sqrt{13x+y}+1\\right)}{\\left(\\sqrt{13x+y}+1\\right)\\left(e^{5x}+\\sqrt{5x}\\right)}'},
            },
            {
                'expression': 'frac{x}{y}+frac{u}{v}+2',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }yv', 'info': '\\displaystyle \\frac{x}{y}+\\frac{u}{v}+2=\\frac{xv}{yv}+\\frac{uy}{yv}+\\frac{2yv}{yv}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{xv}{yv}+\\frac{uy}{yv}+\\frac{2yv}{yv}=\\frac{xv+uy+2yv}{yv}'}], 'finalResult': '\\frac{xv+uy+2yv}{yv}'},
            },
            {
                'expression': 'frac{x}{y}+frac{u}{v}+s',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle s=\\frac{s}{1}', 'e-steps': []},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }yv', 'info': '\\displaystyle \\frac{x}{y}+\\frac{u}{v}+\\frac{s}{1}=\\frac{xv}{yv}+\\frac{uy}{yv}+\\frac{syv}{yv}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{xv}{yv}+\\frac{uy}{yv}+\\frac{syv}{yv}=\\frac{xv+uy+syv}{yv}'}], 'finalResult': '\\frac{xv+uy+syv}{yv}'},
            },
            {
                'expression': 'frac{10}{2}+frac{s}{t}',
                'keyword': 'combine',
                'expected_val': {'steps': [{'type': 'e-step', 'heading': '\\displaystyle \\frac{10}{2}=5', 'e-steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Divide The Numbers}', 'info': '\\displaystyle \\frac{10}{2}=5'}]},
                                           {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }t', 'info': '\\displaystyle 5+\\frac{s}{t}=\\frac{5t}{t}+\\frac{s}{t}'},
                                           {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{5t}{t}+\\frac{s}{t}=\\frac{5t+s}{t}'}], 'finalResult': '\\frac{5t+s}{t}'},
            },
            {
                'expression': 'frac{10x^{2}}{x}+frac{s}{t}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{10x^{2}}{x}=\\frac{10x}{1}', 'e-steps': [
                        {'type': 'e-step', 'heading': '\\displaystyle \\frac{10x^{2}}{x}=\\frac{10x}{1}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Cancel like terms}', 'info': '\\displaystyle \\frac{10x^{2}}{x}=\\frac{10x}{1}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }t', 'info': '\\displaystyle \\frac{10x}{1}+\\frac{s}{t}=\\frac{10xt}{t}+\\frac{s}{t}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{10xt}{t}+\\frac{s}{t}=\\frac{10xt+s}{t}'}], 'finalResult': '\\frac{10xt+s}{t}'},
            },
            {
                'expression': 'e^{2x+x}+frac{s}{t+1}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle e^{2x+x}=\\frac{e^{3x}}{1}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+x=3x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{2x+x}=e^{3x}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\left(t+1\\right)', 'info': '\\displaystyle \\frac{e^{3x}}{1}+\\frac{s}{t+1}=\\frac{e^{3x}\\left(t+1\\right)}{\\left(t+1\\right)}+\\frac{s}{\\left(t+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{e^{3x}\\left(t+1\\right)}{\\left(t+1\\right)}+\\frac{s}{\\left(t+1\\right)}=\\frac{e^{3x}\\left(t+1\\right)+s}{\\left(t+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{e^{3x}\\left(t+1\\right)+s}{\\left(t+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(t+1\\right)=t+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{e^{3x}\\left(t+1\\right)+s}{\\left(t+1\\right)}=\\frac{e^{3x}\\left(t+1\\right)+s}{t+1}'}], 'finalResult': '\\frac{e^{3x}\\left(t+1\\right)+s}{t+1}'},
            },
            {
                'expression': 'frac{x}{2}+frac{3x}{7}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }14', 'info': '\\displaystyle \\frac{x}{2}+\\frac{3x}{7}=\\frac{7\\cdot x}{14}+\\frac{2\\cdot3x}{14}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{7\\cdot x}{14}+\\frac{2\\cdot3x}{14}=\\frac{7\\cdot x+2\\cdot3x}{14}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{7\\cdot x+2\\cdot3x}{14}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 7\\cdot x=7x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot3x=6x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 7x+6x=13x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{7\\cdot x+2\\cdot3x}{14}=\\frac{13x}{14}'}], 'finalResult': '\\frac{13x}{14}'},
            },
            {
                'expression': 'frac{1}{sqrt{n}}-frac{1}{sqrt{n+1}}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\sqrt{n}\\sqrt{n+1}', 'info': '\\displaystyle \\frac{1}{\\sqrt{n}}-\\frac{1}{\\sqrt{n+1}}=\\frac{\\sqrt{n+1}}{\\sqrt{n}\\sqrt{n+1}}-\\frac{\\sqrt{n}}{\\sqrt{n}\\sqrt{n+1}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{\\sqrt{n+1}}{\\sqrt{n}\\sqrt{n+1}}-\\frac{\\sqrt{n}}{\\sqrt{n}\\sqrt{n+1}}=\\frac{\\sqrt{n+1}-\\sqrt{n}}{\\sqrt{n}\\sqrt{n+1}}'}], 'finalResult': '\\frac{\\sqrt{n+1}-\\sqrt{n}}{\\sqrt{n}\\sqrt{n+1}}'},
            },
            {
                'expression': 'frac{n}{sqrt{n}}-frac{5n+1}{sqrt{n^{3}+5n^{2}+1}}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\sqrt{n^{3}+5n^{2}+1}\\sqrt{n}', 'info': '\\displaystyle \\frac{n}{\\sqrt{n}}-\\frac{5n+1}{\\sqrt{n^{3}+5n^{2}+1}}=\\frac{n\\sqrt{n^{3}+5n^{2}+1}}{\\sqrt{n^{3}+5n^{2}+1}\\sqrt{n}}-\\frac{\\left(5n+1\\right)\\sqrt{n}}{\\sqrt{n^{3}+5n^{2}+1}\\sqrt{n}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{n\\sqrt{n^{3}+5n^{2}+1}}{\\sqrt{n^{3}+5n^{2}+1}\\sqrt{n}}-\\frac{\\left(5n+1\\right)\\sqrt{n}}{\\sqrt{n^{3}+5n^{2}+1}\\sqrt{n}}=\\frac{-\\left(5n+1\\right)\\sqrt{n}+n\\sqrt{n^{3}+5n^{2}+1}}{\\sqrt{n^{3}+5n^{2}+1}\\sqrt{n}}'}], 'finalResult': '\\frac{-\\left(5n+1\\right)\\sqrt{n}+n\\sqrt{n^{3}+5n^{2}+1}}{\\sqrt{n^{3}+5n^{2}+1}\\sqrt{n}}'},
            },
            {
                'expression': 'frac{1}{x}+frac{2}{x^{2}}+frac{3}{x^{3}}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }x^{3}', 'info': '\\displaystyle \\frac{1}{x}+\\frac{2}{x^{2}}+\\frac{3}{x^{3}}=\\frac{x^{2}}{x^{3}}+\\frac{2x}{x^{3}}+\\frac{3}{x^{3}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{x^{2}}{x^{3}}+\\frac{2x}{x^{3}}+\\frac{3}{x^{3}}=\\frac{x^{2}+2x+3}{x^{3}}'}], 'finalResult': '\\frac{x^{2}+2x+3}{x^{3}}'},
            },
            {
                'expression': 'frac{1}{x+1}+frac{2}{(x+1)^{2}}+frac{3}{(x+1)^{3}}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\left(x+1\\right)^{3}', 'info': '\\displaystyle \\frac{1}{x+1}+\\frac{2}{\\left(x+1\\right)^{2}}+\\frac{3}{\\left(x+1\\right)^{3}}=\\frac{\\left(x+1\\right)^{2}}{\\left(x+1\\right)^{3}}+\\frac{2\\left(x+1\\right)}{\\left(x+1\\right)^{3}}+\\frac{3}{\\left(x+1\\right)^{3}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{\\left(x+1\\right)^{2}}{\\left(x+1\\right)^{3}}+\\frac{2\\left(x+1\\right)}{\\left(x+1\\right)^{3}}+\\frac{3}{\\left(x+1\\right)^{3}}=\\frac{\\left(x+1\\right)^{2}+2\\left(x+1\\right)+3}{\\left(x+1\\right)^{3}}'}], 'finalResult': '\\frac{\\left(x+1\\right)^{2}+2\\left(x+1\\right)+3}{\\left(x+1\\right)^{3}}'},
            },
            {
                'expression': 'frac{1}{x+1}+frac{2}{(x+1)^{2}}+frac{3}{(x+1)^{n}}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\left(x+1\\right)^{2}', 'info': '\\displaystyle \\frac{1}{x+1}+\\frac{2}{\\left(x+1\\right)^{2}}+\\frac{3}{\\left(x+1\\right)^{n}}=\\frac{x+1}{\\left(x+1\\right)^{2}}+\\frac{2}{\\left(x+1\\right)^{2}}+\\frac{3\\left(x+1\\right)^{-n+2}}{\\left(x+1\\right)^{2}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{x+1}{\\left(x+1\\right)^{2}}+\\frac{2}{\\left(x+1\\right)^{2}}+\\frac{3\\left(x+1\\right)^{-n+2}}{\\left(x+1\\right)^{2}}=\\frac{3\\left(x+1\\right)^{-n+2}+x+1+2}{\\left(x+1\\right)^{2}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{3\\left(x+1\\right)^{-n+2}+x+1+2}{\\left(x+1\\right)^{2}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle x+1+2=x+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3\\left(x+1\\right)^{-n+2}+x+1+2}{\\left(x+1\\right)^{2}}=\\frac{3\\left(x+1\\right)^{-n+2}+x+3}{\\left(x+1\\right)^{2}}'}], 'finalResult': '\\frac{3\\left(x+1\\right)^{-n+2}+x+3}{\\left(x+1\\right)^{2}}'},
            },
            {
                'expression': 'frac{1}{n}-frac{1}{n+1}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }n\\left(n+1\\right)', 'info': '\\displaystyle \\frac{1}{n}-\\frac{1}{n+1}=\\frac{n+1}{n\\left(n+1\\right)}-\\frac{n}{n\\left(n+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{n+1}{n\\left(n+1\\right)}-\\frac{n}{n\\left(n+1\\right)}=\\frac{n-n+1}{n\\left(n+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{n-n+1}{n\\left(n+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle n-n+1=0+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 0+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 0+1=1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{n-n+1}{n\\left(n+1\\right)}=\\frac{1}{n\\left(n+1\\right)}'}], 'finalResult': '\\frac{1}{n\\left(n+1\\right)}'},
            },
            {
                'expression': 'frac{y}{3}+frac{1}{x}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }3x', 'info': '\\displaystyle \\frac{y}{3}+\\frac{1}{x}=\\frac{yx}{3x}+\\frac{3}{3x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{yx}{3x}+\\frac{3}{3x}=\\frac{yx+3}{3x}'}], 'finalResult': '\\frac{yx+3}{3x}'},
            },
            {
                'expression': '2*3*5*7',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot3\\cdot5\\cdot7=210'}], 'finalResult': '210'}
            },
            {
                'expression': '2*3*5*7+5*2*4+2*9',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot3\\cdot5\\cdot7=210'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot2\\cdot4=40'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot9=18'},
                    {'type': 'e-step', 'heading': '\\displaystyle 210+40+18=268', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 210+40+18=268'}]}], 'finalResult': '268'},
            },
            {
                'expression': '2.363*23.532',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2.363\\cdot23.532=55.606116'}], 'finalResult': '55.606116'},
            },
            {
                'expression': '34.237*0.2345',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 34.237\\cdot0.2345=8.0285765'}], 'finalResult': '8.0285765'},
            },
            {
                'expression': '1*160x^{2}uv^{3}',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot160x^{2}uv^{3}=160x^{2}uv^{3}'}], 'finalResult': '160x^{2}uv^{3}'},
            },
            {
                'expression': '21x*3x^{2}* x^{4}*5x^{10}',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 21x\\cdot3x^{2}\\cdot x^{4}\\cdot5x^{10}=315x^{1+2+4+10}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+4+10=17'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 315x^{1+2+4+10}=315x^{17}'}], 'finalResult': '315x^{17}'},
            },
            {
                'expression': '21x*3x^{2}*x^{4}*5x^{10}+10y^{2}*2y*5x^{3}*5x^{a}+3y^{b}*2y^{3b}*x^{2a}',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 21x\\cdot3x^{2}\\cdot x^{4}\\cdot5x^{10}=315x^{1+2+4+10}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 10y^{2}\\cdot2y\\cdot5x^{3}\\cdot5x^{a}=500y^{2+1}x^{3+a}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3y^{b}\\cdot2y^{3b}\\cdot x^{2a}=6y^{b+3b}x^{2a}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 500y^{2+1}=500y^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 500y^{2+1}=500y^{3}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle x^{3+a}=x^{a+3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 3+a=a+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{3+a}=x^{a+3}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 6y^{b+3b}=6y^{4b}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle b+3b=4b'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 6y^{b+3b}=6y^{4b}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 315x^{1+2+4+10}=315x^{17}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+4+10=17'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 315x^{1+2+4+10}=315x^{17}'}]}], 'finalResult': '315x^{17}+500y^{3}x^{a+3}+6y^{4b}x^{2a}'},
            },
            {
                'expression': '2*3*4*x+5*3*2*y*y',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot3\\cdot4\\cdot x=24x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot3\\cdot2\\cdot y\\cdot y=30y^{1+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 24x+30y^{1+1}=30y^{1+1}+24x'},
                    {'type': 'e-step', 'heading': '\\displaystyle 30y^{1+1}=30y^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 30y^{1+1}=30y^{2}'}]}], 'finalResult': '30y^{2}+24x'},
            },
            {
                'expression': 'frac{5x*x*x+1+2+3}{1+x}+frac{5x*y*x+3y+2y+1+2}{1+y}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{5x\\cdot x\\cdot x+1+2+3}{1+x}=\\frac{5x^{3}+6}{x+1}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot x\\cdot x=5x^{1+1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 5x^{1+1+1}=5x^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+3=6'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{5x\\cdot x\\cdot x+1+2+3}{1+x}=\\frac{5x^{3}+6}{1+x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+x=x+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{5x^{3}+6}{1+x}=\\frac{5x^{3}+6}{x+1}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{5x\\cdot y\\cdot x+3y+2y+1+2}{1+y}=\\frac{5x^{2}y+5y+3}{y+1}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot y\\cdot x=5x^{1+1}y'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 5x^{1+1}=5x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x^{2}y+3y+2y+1+2=5x^{2}y+5y+1+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5x^{2}y+5y+1+2=5x^{2}y+5y+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{5x\\cdot y\\cdot x+3y+2y+1+2}{1+y}=\\frac{5x^{2}y+5y+3}{1+y}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+y=y+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{5x^{2}y+5y+3}{1+y}=\\frac{5x^{2}y+5y+3}{y+1}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\left(x+1\\right)\\left(y+1\\right)', 'info': '\\displaystyle \\frac{5x^{3}+6}{x+1}+\\frac{5x^{2}y+5y+3}{y+1}=\\frac{\\left(5x^{3}+6\\right)\\left(y+1\\right)}{\\left(x+1\\right)\\left(y+1\\right)}+\\frac{\\left(5x^{2}y+5y+3\\right)\\left(x+1\\right)}{\\left(x+1\\right)\\left(y+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{\\left(5x^{3}+6\\right)\\left(y+1\\right)}{\\left(x+1\\right)\\left(y+1\\right)}+\\frac{\\left(5x^{2}y+5y+3\\right)\\left(x+1\\right)}{\\left(x+1\\right)\\left(y+1\\right)}=\\frac{\\left(5x^{3}+6\\right)\\left(y+1\\right)+\\left(5x^{2}y+5y+3\\right)\\left(x+1\\right)}{\\left(x+1\\right)\\left(y+1\\right)}'}], 'finalResult': '\\frac{\\left(5x^{3}+6\\right)\\left(y+1\\right)+\\left(5x^{2}y+5y+3\\right)\\left(x+1\\right)}{\\left(x+1\\right)\\left(y+1\\right)}'}
            },
            {
                'expression': 'frac{1}{2}',
                'keyword': None,
                'expected_val': {'steps': [], 'finalResult': '\\frac{1}{2}'},
            },
            {
                'expression': '1+2+(5+2+(25-3)-7+(23+8))+(3+2+(82+(52+5-11)))',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(23+8\\right)=31', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 23+8=31'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5+2+\\left(25-3\\right)-7+\\left(23+8\\right)\\right)=\\left(5+2+\\left(25-3\\right)-7+31\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(52+5-11\\right)=46', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 52+5-11=46'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(3+2+\\left(82+\\left(52+5-11\\right)\\right)\\right)=\\left(3+2+\\left(82+46\\right)\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(25-3\\right)=22', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 25-3=22'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5+2+\\left(25-3\\right)-7+31\\right)=\\left(5+2+22-7+31\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(82+46\\right)=128', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 82+46=128'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(3+2+\\left(82+46\\right)\\right)=\\left(3+2+128\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(5+2+22-7+31\\right)=53', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5+2+22-7+31=53'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5+2+22-7+31\\right)=53'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(3+2+128\\right)=133', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+2+128=133'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(3+2+128\\right)=133'},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+2+53+133=189', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+53+133=189'}]}], 'finalResult': '189'},
            },

            {
                'expression': '1+2+(5+(11*12+12*5))+7+9',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(11\\cdot12+12\\cdot5\\right)=192', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 11\\cdot12=132'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 12\\cdot5=60'},
                        {'type': 'e-step', 'heading': '\\displaystyle 132+60=192', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 132+60=192'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5+\\left(11\\cdot12+12\\cdot5\\right)\\right)=\\left(5+192\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(5+192\\right)=197', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5+192=197'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5+192\\right)=197'},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+2+197+7+9=216', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+197+7+9=216'}]}], 'finalResult': '216'},
            },
            {
                'expression': '1+3+(5x+(e^{2x}+3e^{2x}+(25x-15x+4x)+3+2)+sqrt{25x^{2}+(15x^{2}+25x+(15x+3+2))+1+3})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(15x+3+2\\right)=15x+5', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 15x+3+2=15x+5'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5x+\\left(e^{2x}+3e^{2x}+\\left(25x-15x+4x\\right)+3+2\\right)+\\sqrt{25x^{2}+\\left(15x^{2}+25x+\\left(15x+3+2\\right)\\right)+1+3}\\right)=\\left(5x+\\left(e^{2x}+3e^{2x}+\\left(25x-15x+4x\\right)+3+2\\right)+\\sqrt{25x^{2}+\\left(15x^{2}+25x+15x+5\\right)+1+3}\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(15x^{2}+25x+15x+5\\right)=15x^{2}+40x+5', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 25x+15x+5=40x+5'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5x+\\left(e^{2x}+3e^{2x}+\\left(25x-15x+4x\\right)+3+2\\right)+\\sqrt{25x^{2}+\\left(15x^{2}+25x+15x+5\\right)+1+3}\\right)=\\left(5x+\\left(e^{2x}+3e^{2x}+\\left(25x-15x+4x\\right)+3+2\\right)+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(25x-15x+4x\\right)=14x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 25x-15x+4x=14x'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5x+\\left(e^{2x}+3e^{2x}+\\left(25x-15x+4x\\right)+3+2\\right)+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}\\right)=\\left(5x+\\left(e^{2x}+3e^{2x}+14x+3+2\\right)+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(e^{2x}+3e^{2x}+14x+3+2\\right)=4e^{2x}+14x+5', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle e^{2x}+3e^{2x}=4e^{2x}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 14x+3+2=14x+5', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 14x+3+2=14x+5'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5x+\\left(e^{2x}+3e^{2x}+14x+3+2\\right)+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}\\right)=\\left(5x+4e^{2x}+14x+5+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(5x+4e^{2x}+14x+5+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}\\right)=4e^{2x}+\\sqrt{40x^{2}+40x+9}+19x+5', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 5x+4e^{2x}+14x+5+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}=4e^{2x}+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}+5x+14x+5'},
                        {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{25x^{2}+15x^{2}+40x+5+1+3}=\\sqrt{40x^{2}+40x+9}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 25x^{2}+15x^{2}=40x^{2}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 40x+5+1+3=40x+9'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{25x^{2}+15x^{2}+40x+5+1+3}=\\sqrt{40x^{2}+40x+9}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 5x+14x+5=19x+5', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+14x+5=19x+5'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(5x+4e^{2x}+14x+5+\\sqrt{25x^{2}+15x^{2}+40x+5+1+3}\\right)=4e^{2x}+\\sqrt{40x^{2}+40x+9}+19x+5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 1+3+4e^{2x}+\\sqrt{40x^{2}+40x+9}+19x+5=4e^{2x}+\\sqrt{40x^{2}+40x+9}+1+3+19x+5'},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+3+19x+5=19x+9', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+3+19x+5=19x+1+3+5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 19x+1+3+5=19x+9'}]}], 'finalResult': '4e^{2x}+\\sqrt{40x^{2}+40x+9}+19x+9'},
            },
            {
                'expression': 'frac{3x+(2x+x+1)}{sqrt{e^{2x}+5e^{2x}}+(3x+(e^{4x+(3x+2x)}))}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+x+1=3x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(2x+x+1\\right)=3x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+3x+1=6x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3x+\\left(2x+x+1\\right)}{\\sqrt{e^{2x}+5e^{2x}}+\\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)}=\\frac{6x+1}{\\sqrt{e^{2x}+5e^{2x}}+\\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle e^{2x}+5e^{2x}=6e^{2x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{e^{2x}+5e^{2x}}=\\sqrt{6e^{2x}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x=5x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)=\\left(3x+\\left(e^{4x+5x}\\right)\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(3x+\\left(e^{4x+5x}\\right)\\right)=3x+\\left(e^{4x+5x}\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 4x+5x=9x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{4x+5x}=e^{9x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(e^{4x+5x}\\right)=e^{9x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 3x+e^{9x}=e^{9x}+3x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\sqrt{6e^{2x}}+e^{9x}+3x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle \\sqrt{6e^{2x}}+e^{9x}+3x=e^{9x}+\\sqrt{6e^{2x}}+3x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{6x+1}{\\sqrt{e^{2x}+5e^{2x}}+\\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)}=\\frac{6x+1}{e^{9x}+\\sqrt{6e^{2x}}+3x}'}], 'finalResult': '\\frac{6x+1}{e^{9x}+\\sqrt{6e^{2x}}+3x}'},
            },

            {
                'expression': 'frac{3x+(2x+x+1)}{sqrt{e^{2x}+5e^{2x}}+(3x+(e^{4x+(3x+2x)}))}+frac{25x^{2}+(36x^{2}-12x^{2})+3+3}{(15sqrt{x}-4sqrt{x}+(9sqrt{x}+3sqrt{5x-4x})+3)+1}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{3x+\\left(2x+x+1\\right)}{\\sqrt{e^{2x}+5e^{2x}}+\\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)}=\\frac{6x+1}{e^{9x}+\\sqrt{6e^{2x}}+3x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+x+1=3x+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(2x+x+1\\right)=3x+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+3x+1=6x+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3x+\\left(2x+x+1\\right)}{\\sqrt{e^{2x}+5e^{2x}}+\\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)}=\\frac{6x+1}{\\sqrt{e^{2x}+5e^{2x}}+\\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle e^{2x}+5e^{2x}=6e^{2x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{e^{2x}+5e^{2x}}=\\sqrt{6e^{2x}}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)=\\left(3x+\\left(e^{4x+5x}\\right)\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(3x+\\left(e^{4x+5x}\\right)\\right)=3x+\\left(e^{4x+5x}\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 4x+5x=9x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{4x+5x}=e^{9x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(e^{4x+5x}\\right)=e^{9x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 3x+e^{9x}=e^{9x}+3x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\sqrt{6e^{2x}}+e^{9x}+3x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle \\sqrt{6e^{2x}}+e^{9x}+3x=e^{9x}+\\sqrt{6e^{2x}}+3x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{6x+1}{\\sqrt{e^{2x}+5e^{2x}}+\\left(3x+\\left(e^{4x+\\left(3x+2x\\right)}\\right)\\right)}=\\frac{6x+1}{e^{9x}+\\sqrt{6e^{2x}}+3x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{25x^{2}+\\left(36x^{2}-12x^{2}\\right)+3+3}{\\left(15\\sqrt{x}-4\\sqrt{x}+\\left(9\\sqrt{x}+3\\sqrt{5x-4x}\\right)+3\\right)+1}=\\frac{49x^{2}+6}{23\\sqrt{x}+4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 36x^{2}-12x^{2}=24x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(36x^{2}-12x^{2}\\right)=24x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+3=6'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 25x^{2}+24x^{2}+6'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 25x^{2}+24x^{2}=49x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{25x^{2}+\\left(36x^{2}-12x^{2}\\right)+3+3}{\\left(15\\sqrt{x}-4\\sqrt{x}+\\left(9\\sqrt{x}+3\\sqrt{5x-4x}\\right)+3\\right)+1}=\\frac{49x^{2}+6}{\\left(15\\sqrt{x}-4\\sqrt{x}+\\left(9\\sqrt{x}+3\\sqrt{5x-4x}\\right)+3\\right)+1}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3\\sqrt{5x-4x}=3\\sqrt{x}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x-4x=x'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 3\\sqrt{5x-4x}=3\\sqrt{x}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 9\\sqrt{x}+3\\sqrt{x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 9\\sqrt{x}+3\\sqrt{x}=12\\sqrt{x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(15\\sqrt{x}-4\\sqrt{x}+\\left(9\\sqrt{x}+3\\sqrt{5x-4x}\\right)+3\\right)=\\left(15\\sqrt{x}-4\\sqrt{x}+12\\sqrt{x}+3\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 15\\sqrt{x}-4\\sqrt{x}+12\\sqrt{x}+3=23\\sqrt{x}+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\left(15\\sqrt{x}-4\\sqrt{x}+12\\sqrt{x}+3\\right)=23\\sqrt{x}+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+1=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{49x^{2}+6}{\\left(15\\sqrt{x}-4\\sqrt{x}+\\left(9\\sqrt{x}+3\\sqrt{5x-4x}\\right)+3\\right)+1}=\\frac{49x^{2}+6}{23\\sqrt{x}+4}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)\\left(23\\sqrt{x}+4\\right)', 'info': '\\displaystyle \\frac{6x+1}{e^{9x}+\\sqrt{6e^{2x}}+3x}+\\frac{49x^{2}+6}{23\\sqrt{x}+4}=\\frac{\\left(6x+1\\right)\\left(23\\sqrt{x}+4\\right)}{\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)\\left(23\\sqrt{x}+4\\right)}+\\frac{\\left(49x^{2}+6\\right)\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)}{\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)\\left(23\\sqrt{x}+4\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{\\left(6x+1\\right)\\left(23\\sqrt{x}+4\\right)}{\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)\\left(23\\sqrt{x}+4\\right)}+\\frac{\\left(49x^{2}+6\\right)\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)}{\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)\\left(23\\sqrt{x}+4\\right)}=\\frac{\\left(6x+1\\right)\\left(23\\sqrt{x}+4\\right)+\\left(49x^{2}+6\\right)\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)}{\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)\\left(23\\sqrt{x}+4\\right)}'}], 'finalResult': '\\frac{\\left(6x+1\\right)\\left(23\\sqrt{x}+4\\right)+\\left(49x^{2}+6\\right)\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)}{\\left(e^{9x}+\\sqrt{6e^{2x}}+3x\\right)\\left(23\\sqrt{x}+4\\right)}'},
            },

            {
                'expression': 'frac{12+24+57}{23-56}+frac{23+15}{16}',
                'keyword': 'combine',
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{12+24+57}{23-56}=\\frac{31}{-11}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 12+24+57=93'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{12+24+57}{23-56}=\\frac{93}{23-56}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 23-56=-33'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{93}{23-56}=\\frac{93}{-33}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Reduce Fraction}', 'info': '\\displaystyle \\frac{93}{-33}=\\frac{31}{-11}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{23+15}{16}=\\frac{19}{8}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 23+15=38'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{23+15}{16}=\\frac{38}{16}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Reduce Fraction}', 'info': '\\displaystyle \\frac{38}{16}=\\frac{19}{8}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }88', 'info': '\\displaystyle \\frac{31}{-11}+\\frac{19}{8}=\\frac{-248}{88}+\\frac{209}{88}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{-248}{88}+\\frac{209}{88}=\\frac{-248+209}{88}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{-248+209}{88}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle -248+209=-39'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{-248+209}{88}=\\frac{-39}{88}'}], 'finalResult': '\\frac{-39}{88}'}
            },
            {
                'expression': '5*(4x^{2}+3x+9)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5\\cdot\\left(4x^{2}+3x+9\\right)=5\\cdot4x^{2}+5\\cdot3x+5\\cdot9'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot4x^{2}=20x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot3x=15x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot9=45'}], 'finalResult': '20x^{2}+15x+45'},
            },
            {
                'expression': '12*(9x^{3}+3x^{2}-5x-9)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 12\\cdot\\left(9x^{3}+3x^{2}-5x-9\\right)=12\\cdot9x^{3}+12\\cdot3x^{2}-12\\cdot5x-12\\cdot9'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 12\\cdot9x^{3}=108x^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 12\\cdot3x^{2}=36x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 12\\cdot5x=60x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 12\\cdot9=108'}], 'finalResult': '108x^{3}+36x^{2}-60x-108'},
            },
            {
                'expression': 'x*(10x^{3}+5x^{2}-3x-13)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle x\\cdot\\left(10x^{3}+5x^{2}-3x-13\\right)=x\\cdot10x^{3}+x\\cdot5x^{2}-x\\cdot3x-x\\cdot13'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot10x^{3}=10x^{1+3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot5x^{2}=5x^{1+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot3x=3x^{1+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot13=13x'},
                    {'type': 'e-step', 'heading': '\\displaystyle 10x^{1+3}=10x^{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+3=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 10x^{1+3}=10x^{4}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 5x^{1+2}=5x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 5x^{1+2}=5x^{3}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle -3x^{1+1}=-3x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle -3x^{1+1}=-3x^{2}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 10x^{1+3}+5x^{1+2}-3x^{1+1}=10x^{4}+5x^{3}-3x^{2}'}], 'finalResult': '10x^{4}+5x^{3}-3x^{2}-13x'},
            },
            {
                'expression': '240x^{2}*(a+b)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 240x^{2}\\cdot\\left(a+b\\right)=240x^{2}\\cdot a+240x^{2}\\cdot b'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 240x^{2}\\cdot a=240x^{2}a'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 240x^{2}\\cdot b=240x^{2}b'}], 'finalResult': '240x^{2}a+240x^{2}b'},
            },
            {
                'expression': '4x^{2}*(10x^{n}+5x^{2}+3x+13)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 4x^{2}\\cdot\\left(10x^{n}+5x^{2}+3x+13\\right)=4x^{2}\\cdot10x^{n}+4x^{2}\\cdot5x^{2}+4x^{2}\\cdot3x+4x^{2}\\cdot13'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4x^{2}\\cdot10x^{n}=40x^{2+n}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4x^{2}\\cdot5x^{2}=20x^{2+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4x^{2}\\cdot3x=12x^{2+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4x^{2}\\cdot13=52x^{2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 40x^{2+n}=40x^{n+2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 2+n=n+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 40x^{2+n}=40x^{n+2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 20x^{2+2}=20x^{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 20x^{2+2}=20x^{4}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 12x^{2+1}=12x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 12x^{2+1}=12x^{3}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 40x^{2+n}+20x^{2+2}+12x^{2+1}+52x^{2}=40x^{n+2}+20x^{4}+12x^{3}+52x^{2}'}], 'finalResult': '40x^{n+2}+20x^{4}+12x^{3}+52x^{2}'},
            },
            {
                'expression': '5x^{n}*(12x^{a}+3x^{2}+9x+4)+9x^{1+2}*(x^{2}+3x+10)+2+5x^{n}+10x^{3}+11',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle 5x^{n}\\cdot\\left(12x^{a}+3x^{2}+9x+4\\right)=60x^{n+a}+15x^{n+2}+45x^{n+1}+20x^{n}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x^{n}\\cdot\\left(12x^{a}+3x^{2}+9x+4\\right)=5x^{n}\\cdot12x^{a}+5x^{n}\\cdot3x^{2}+5x^{n}\\cdot9x+5x^{n}\\cdot4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{n}\\cdot12x^{a}=60x^{n+a}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{n}\\cdot3x^{2}=15x^{n+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{n}\\cdot9x=45x^{n+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{n}\\cdot4=20x^{n}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 9x^{1+2}\\cdot\\left(x^{2}+3x+10\\right)=9x^{5}+27x^{4}+90x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 9x^{1+2}\\cdot\\left(x^{2}+3x+10\\right)=9x^{1+2}\\cdot x^{2}+9x^{1+2}\\cdot3x+9x^{1+2}\\cdot10'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 9x^{1+2}\\cdot x^{2}=9x^{1+2+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 9x^{1+2}\\cdot3x=27x^{1+2+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 9x^{1+2}\\cdot10=90x^{1+2}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 9x^{1+2+2}=9x^{5}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+2=5'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 9x^{1+2+2}=9x^{5}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 27x^{1+2+1}=27x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+1=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 27x^{1+2+1}=27x^{4}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 90x^{1+2}=90x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 90x^{1+2}=90x^{3}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 9x^{1+2+2}+27x^{1+2+1}+90x^{1+2}=9x^{5}+27x^{4}+90x^{3}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 60x^{n+a}+15x^{n+2}+45x^{n+1}+20x^{n}+9x^{5}+27x^{4}+90x^{3}+2+5x^{n}+10x^{3}+11=60x^{n+a}+15x^{n+2}+45x^{n+1}+20x^{n}+9x^{5}+27x^{4}+90x^{3}+5x^{n}+10x^{3}+2+11'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 60x^{n+a}+15x^{n+2}+45x^{n+1}+20x^{n}+9x^{5}+27x^{4}+90x^{3}+5x^{n}+10x^{3}=60x^{n+a}+15x^{n+2}+45x^{n+1}+20x^{n}+5x^{n}+9x^{5}+27x^{4}+90x^{3}+10x^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 60x^{n+a}+15x^{n+2}+45x^{n+1}+20x^{n}+5x^{n}+9x^{5}+27x^{4}+90x^{3}+10x^{3}=60x^{n+a}+15x^{n+2}+45x^{n+1}+25x^{n}+9x^{5}+27x^{4}+100x^{3}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 2+11=13', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+11=13'}]}], 'finalResult': '60x^{n+a}+15x^{n+2}+45x^{n+1}+25x^{n}+9x^{5}+27x^{4}+100x^{3}+13'},
            },
            {
                'expression': '5x^{2}*(3x^{3}+2x^{2}+(9x^{4}+3x^{2}+11))+x*(3x+1)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle 5x^{2}\\cdot\\left(3x^{3}+2x^{2}+\\left(9x^{4}+3x^{2}+11\\right)\\right)=15x^{5}+25x^{4}+45x^{6}+55x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x^{2}\\cdot\\left(3x^{3}+2x^{2}+\\left(9x^{4}+3x^{2}+11\\right)\\right)=5x^{2}\\cdot3x^{3}+5x^{2}\\cdot2x^{2}+5x^{2}\\cdot\\left(9x^{4}+3x^{2}+11\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot3x^{3}=15x^{2+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot2x^{2}=10x^{2+2}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 5x^{2}\\cdot\\left(9x^{4}+3x^{2}+11\\right)=45x^{6}+15x^{4}+55x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x^{2}\\cdot\\left(9x^{4}+3x^{2}+11\\right)=5x^{2}\\cdot9x^{4}+5x^{2}\\cdot3x^{2}+5x^{2}\\cdot11'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot9x^{4}=45x^{2+4}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot3x^{2}=15x^{2+2}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot11=55x^{2}'},
                            {'type': 'e-step', 'heading': '\\displaystyle 45x^{2+4}=45x^{6}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+4=6'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 45x^{2+4}=45x^{6}'}]},
                            {'type': 'e-step', 'heading': '\\displaystyle 15x^{2+2}=15x^{4}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{2+2}=15x^{4}'}]},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 45x^{2+4}+15x^{2+2}+55x^{2}=45x^{6}+15x^{4}+55x^{2}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 15x^{2+3}=15x^{5}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{2+3}=15x^{5}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 10x^{2+2}=10x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 10x^{2+2}=10x^{4}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 15x^{2+3}+10x^{2+2}+45x^{6}+15x^{4}+55x^{2}=15x^{5}+10x^{4}+45x^{6}+15x^{4}+55x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 15x^{5}+10x^{4}+45x^{6}+15x^{4}+55x^{2}=15x^{5}+10x^{4}+15x^{4}+45x^{6}+55x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 15x^{5}+10x^{4}+15x^{4}+45x^{6}+55x^{2}=15x^{5}+25x^{4}+45x^{6}+55x^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle x\\cdot\\left(3x+1\\right)=3x^{2}+x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle x\\cdot\\left(3x+1\\right)=x\\cdot3x+x\\cdot1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot3x=3x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot1=x'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3x^{1+1}=3x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3x^{1+1}=3x^{2}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 15x^{5}+25x^{4}+45x^{6}+55x^{2}+3x^{2}=15x^{5}+25x^{4}+45x^{6}+58x^{2}'}], 'finalResult': '15x^{5}+25x^{4}+45x^{6}+58x^{2}+x'},
            },
            {
                'expression': '5x^{2}*(3x^{3}+2x^{2}+(9x^{4}+3x^{2}+11))+5x*(3x^{p}+9x^{2}+(3x^{2}+2x+5))',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle 5x^{2}\\cdot\\left(3x^{3}+2x^{2}+\\left(9x^{4}+3x^{2}+11\\right)\\right)=15x^{5}+25x^{4}+45x^{6}+55x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x^{2}\\cdot\\left(3x^{3}+2x^{2}+\\left(9x^{4}+3x^{2}+11\\right)\\right)=5x^{2}\\cdot3x^{3}+5x^{2}\\cdot2x^{2}+5x^{2}\\cdot\\left(9x^{4}+3x^{2}+11\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot3x^{3}=15x^{2+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot2x^{2}=10x^{2+2}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 5x^{2}\\cdot\\left(9x^{4}+3x^{2}+11\\right)=45x^{6}+15x^{4}+55x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x^{2}\\cdot\\left(9x^{4}+3x^{2}+11\\right)=5x^{2}\\cdot9x^{4}+5x^{2}\\cdot3x^{2}+5x^{2}\\cdot11'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot9x^{4}=45x^{2+4}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot3x^{2}=15x^{2+2}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2}\\cdot11=55x^{2}'},
                            {'type': 'e-step', 'heading': '\\displaystyle 45x^{2+4}=45x^{6}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+4=6'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 45x^{2+4}=45x^{6}'}]},
                            {'type': 'e-step', 'heading': '\\displaystyle 15x^{2+2}=15x^{4}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{2+2}=15x^{4}'}]},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 45x^{2+4}+15x^{2+2}+55x^{2}=45x^{6}+15x^{4}+55x^{2}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 15x^{2+3}=15x^{5}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{2+3}=15x^{5}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 10x^{2+2}=10x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 10x^{2+2}=10x^{4}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 15x^{2+3}+10x^{2+2}+45x^{6}+15x^{4}+55x^{2}=15x^{5}+10x^{4}+45x^{6}+15x^{4}+55x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 15x^{5}+10x^{4}+45x^{6}+15x^{4}+55x^{2}=15x^{5}+10x^{4}+15x^{4}+45x^{6}+55x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 15x^{5}+10x^{4}+15x^{4}+45x^{6}+55x^{2}=15x^{5}+25x^{4}+45x^{6}+55x^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 5x\\cdot\\left(3x^{p}+9x^{2}+\\left(3x^{2}+2x+5\\right)\\right)=15x^{p+1}+60x^{3}+10x^{2}+25x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x\\cdot\\left(3x^{p}+9x^{2}+\\left(3x^{2}+2x+5\\right)\\right)=5x\\cdot3x^{p}+5x\\cdot9x^{2}+5x\\cdot\\left(3x^{2}+2x+5\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot3x^{p}=15x^{1+p}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot9x^{2}=45x^{1+2}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 5x\\cdot\\left(3x^{2}+2x+5\\right)=15x^{3}+10x^{2}+25x', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x\\cdot\\left(3x^{2}+2x+5\\right)=5x\\cdot3x^{2}+5x\\cdot2x+5x\\cdot5'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot3x^{2}=15x^{1+2}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot2x=10x^{1+1}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot5=25x'},
                            {'type': 'e-step', 'heading': '\\displaystyle 15x^{1+2}=15x^{3}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{1+2}=15x^{3}'}]},
                            {'type': 'e-step', 'heading': '\\displaystyle 10x^{1+1}=10x^{2}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 10x^{1+1}=10x^{2}'}]},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 15x^{1+2}+10x^{1+1}=15x^{3}+10x^{2}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 15x^{1+p}=15x^{p+1}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+p=p+1'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{1+p}=15x^{p+1}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 45x^{1+2}=45x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 45x^{1+2}=45x^{3}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 15x^{1+p}+45x^{1+2}+15x^{3}+10x^{2}=15x^{p+1}+45x^{3}+15x^{3}+10x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 15x^{p+1}+45x^{3}+15x^{3}+10x^{2}=15x^{p+1}+60x^{3}+10x^{2}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 15x^{5}+25x^{4}+45x^{6}+55x^{2}+15x^{p+1}+60x^{3}+10x^{2}=15x^{5}+25x^{4}+45x^{6}+55x^{2}+10x^{2}+15x^{p+1}+60x^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 15x^{5}+25x^{4}+45x^{6}+55x^{2}+10x^{2}+15x^{p+1}+60x^{3}=15x^{5}+25x^{4}+45x^{6}+65x^{2}+15x^{p+1}+60x^{3}'}], 'finalResult': '15x^{5}+25x^{4}+45x^{6}+65x^{2}+15x^{p+1}+60x^{3}+25x'},
            },
            {
                'expression': '3x^{2}*(5x^{4}+2x^{3}+(x^{2}+3x+(9x^{3}+5x^{2}+3x+(7x^{2}+x+9))))',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 3x^{2}\\cdot\\left(5x^{4}+2x^{3}+\\left(x^{2}+3x+\\left(9x^{3}+5x^{2}+3x+\\left(7x^{2}+x+9\\right)\\right)\\right)\\right)=3x^{2}\\cdot5x^{4}+3x^{2}\\cdot2x^{3}+3x^{2}\\cdot\\left(x^{2}+3x+\\left(9x^{3}+5x^{2}+3x+\\left(7x^{2}+x+9\\right)\\right)\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot5x^{4}=15x^{2+4}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot2x^{3}=6x^{2+3}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 3x^{2}\\cdot\\left(x^{2}+3x+\\left(9x^{3}+5x^{2}+3x+\\left(7x^{2}+x+9\\right)\\right)\\right)=39x^{4}+21x^{3}+27x^{5}+27x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 3x^{2}\\cdot\\left(x^{2}+3x+\\left(9x^{3}+5x^{2}+3x+\\left(7x^{2}+x+9\\right)\\right)\\right)=3x^{2}\\cdot x^{2}+3x^{2}\\cdot3x+3x^{2}\\cdot\\left(9x^{3}+5x^{2}+3x+\\left(7x^{2}+x+9\\right)\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot x^{2}=3x^{2+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot3x=9x^{2+1}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3x^{2}\\cdot\\left(9x^{3}+5x^{2}+3x+\\left(7x^{2}+x+9\\right)\\right)=27x^{5}+36x^{4}+12x^{3}+27x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 3x^{2}\\cdot\\left(9x^{3}+5x^{2}+3x+\\left(7x^{2}+x+9\\right)\\right)=3x^{2}\\cdot9x^{3}+3x^{2}\\cdot5x^{2}+3x^{2}\\cdot3x+3x^{2}\\cdot\\left(7x^{2}+x+9\\right)'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot9x^{3}=27x^{2+3}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot5x^{2}=15x^{2+2}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot3x=9x^{2+1}'},
                            {'type': 'e-step', 'heading': '\\displaystyle 3x^{2}\\cdot\\left(7x^{2}+x+9\\right)=21x^{4}+3x^{3}+27x^{2}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 3x^{2}\\cdot\\left(7x^{2}+x+9\\right)=3x^{2}\\cdot7x^{2}+3x^{2}\\cdot x+3x^{2}\\cdot9'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot7x^{2}=21x^{2+2}'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot x=3x^{2+1}'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot9=27x^{2}'},
                                {'type': 'e-step', 'heading': '\\displaystyle 21x^{2+2}=21x^{4}', 'e-steps': [
                                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 21x^{2+2}=21x^{4}'}]},
                                {'type': 'e-step', 'heading': '\\displaystyle 3x^{2+1}=3x^{3}', 'e-steps': [
                                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3x^{2+1}=3x^{3}'}]},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 21x^{2+2}+3x^{2+1}+27x^{2}=21x^{4}+3x^{3}+27x^{2}'}]},
                            {'type': 'e-step', 'heading': '\\displaystyle 27x^{2+3}=27x^{5}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 27x^{2+3}=27x^{5}'}]},
                            {'type': 'e-step', 'heading': '\\displaystyle 15x^{2+2}=15x^{4}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{2+2}=15x^{4}'}]},
                            {'type': 'e-step', 'heading': '\\displaystyle 9x^{2+1}=9x^{3}', 'e-steps': [
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                                {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 9x^{2+1}=9x^{3}'}]},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 27x^{2+3}+15x^{2+2}+9x^{2+1}+21x^{4}+3x^{3}+27x^{2}=27x^{5}+15x^{4}+9x^{3}+21x^{4}+3x^{3}+27x^{2}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 27x^{5}+15x^{4}+9x^{3}+21x^{4}+3x^{3}+27x^{2}=27x^{5}+15x^{4}+21x^{4}+9x^{3}+3x^{3}+27x^{2}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 27x^{5}+15x^{4}+21x^{4}+9x^{3}+3x^{3}+27x^{2}=27x^{5}+36x^{4}+12x^{3}+27x^{2}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 3x^{2+2}=3x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3x^{2+2}=3x^{4}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 9x^{2+1}=9x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 9x^{2+1}=9x^{3}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 3x^{2+2}+9x^{2+1}+27x^{5}+36x^{4}+12x^{3}+27x^{2}=3x^{4}+9x^{3}+27x^{5}+36x^{4}+12x^{3}+27x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 3x^{4}+9x^{3}+27x^{5}+36x^{4}+12x^{3}+27x^{2}=3x^{4}+36x^{4}+9x^{3}+12x^{3}+27x^{5}+27x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 3x^{4}+36x^{4}+9x^{3}+12x^{3}+27x^{5}+27x^{2}=39x^{4}+21x^{3}+27x^{5}+27x^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 15x^{2+4}=15x^{6}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+4=6'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{2+4}=15x^{6}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 6x^{2+3}=6x^{5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 6x^{2+3}=6x^{5}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 15x^{2+4}+6x^{2+3}+39x^{4}+21x^{3}+27x^{5}+27x^{2}=15x^{6}+6x^{5}+39x^{4}+21x^{3}+27x^{5}+27x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 15x^{6}+6x^{5}+39x^{4}+21x^{3}+27x^{5}+27x^{2}=15x^{6}+6x^{5}+27x^{5}+39x^{4}+21x^{3}+27x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 15x^{6}+6x^{5}+27x^{5}+39x^{4}+21x^{3}+27x^{2}=15x^{6}+33x^{5}+39x^{4}+21x^{3}+27x^{2}'}], 'finalResult': '15x^{6}+33x^{5}+39x^{4}+21x^{3}+27x^{2}'},
            },
            {
                'expression': '5*x*(x^{2}+3x+2)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 5\\cdot x=5x'},
                    {'type': 'e-step', 'heading': '\\displaystyle 5x\\cdot\\left(x^{2}+3x+2\\right)=5x^{3}+15x^{2}+10x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x\\cdot\\left(x^{2}+3x+2\\right)=5x\\cdot x^{2}+5x\\cdot3x+5x\\cdot2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot x^{2}=5x^{1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot3x=15x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot2=10x'},
                        {'type': 'e-step', 'heading': '\\displaystyle 5x^{1+2}=5x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 5x^{1+2}=5x^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 15x^{1+1}=15x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{1+1}=15x^{2}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 5x^{1+2}+15x^{1+1}=5x^{3}+15x^{2}'}]}], 'finalResult': '5x^{3}+15x^{2}+10x'},
            },

            {
                'expression': 'x^{2}*(4x^{3}+2x^{2}+5x*(13x^{3}+3x^{2}+2x+1))',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle x^{2}\\cdot\\left(4x^{3}+2x^{2}+5x\\cdot\\left(13x^{3}+3x^{2}+2x+1\\right)\\right)=x^{2}\\cdot4x^{3}+x^{2}\\cdot2x^{2}+x^{2}\\cdot5x\\cdot\\left(13x^{3}+3x^{2}+2x+1\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x^{2}\\cdot4x^{3}=4x^{2+3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x^{2}\\cdot2x^{2}=2x^{2+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle x^{2}\\cdot5x=5x^{2+1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 5x^{2+1}\\cdot\\left(13x^{3}+3x^{2}+2x+1\\right)=65x^{6}+15x^{5}+10x^{4}+5x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x^{2+1}\\cdot\\left(13x^{3}+3x^{2}+2x+1\\right)=5x^{2+1}\\cdot13x^{3}+5x^{2+1}\\cdot3x^{2}+5x^{2+1}\\cdot2x+5x^{2+1}\\cdot1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2+1}\\cdot13x^{3}=65x^{2+1+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2+1}\\cdot3x^{2}=15x^{2+1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2+1}\\cdot2x=10x^{2+1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x^{2+1}\\cdot1=5x^{2+1}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 65x^{2+1+3}=65x^{6}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1+3=6'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 65x^{2+1+3}=65x^{6}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 15x^{2+1+2}=15x^{5}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1+2=5'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 15x^{2+1+2}=15x^{5}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 10x^{2+1+1}=10x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1+1=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 10x^{2+1+1}=10x^{4}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 5x^{2+1}=5x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 5x^{2+1}=5x^{3}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 65x^{2+1+3}+15x^{2+1+2}+10x^{2+1+1}+5x^{2+1}=65x^{6}+15x^{5}+10x^{4}+5x^{3}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 4x^{2+3}=4x^{5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 4x^{2+3}=4x^{5}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 2x^{2+2}=2x^{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2x^{2+2}=2x^{4}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 4x^{2+3}+2x^{2+2}+65x^{6}+15x^{5}+10x^{4}+5x^{3}=4x^{5}+2x^{4}+65x^{6}+15x^{5}+10x^{4}+5x^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 4x^{5}+2x^{4}+65x^{6}+15x^{5}+10x^{4}+5x^{3}=4x^{5}+15x^{5}+2x^{4}+10x^{4}+65x^{6}+5x^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 4x^{5}+15x^{5}+2x^{4}+10x^{4}+65x^{6}+5x^{3}=19x^{5}+12x^{4}+65x^{6}+5x^{3}'}], 'finalResult': '19x^{5}+12x^{4}+65x^{6}+5x^{3}'},
            },

            {
                'expression': '-1*(x^{2}+3x+5)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle -1\\cdot\\left(x^{2}+3x+5\\right)=-x^{2}-3x-5'}], 'finalResult': '-x^{2}-3x-5'},
            },
            {
                'expression': '-1*(-x^{2}+3x-5)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle -1\\cdot\\left(-x^{2}+3x-5\\right)=x^{2}-3x+5'}], 'finalResult': 'x^{2}-3x+5'},
            },
            {
                'expression': 'frac{ln(3x+2x+5+3)+x+3x}{x^{2}+3x^{2}+2+3}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x+5+3=5x+5+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5x+5+3=5x+8'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\ln\\left(3x+2x+5+3\\right)=\\ln\\left(5x+8\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle \\ln\\left(5x+8\\right)+x+3x=\\ln\\left(5x+8\\right)+4x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{\\ln\\left(3x+2x+5+3\\right)+x+3x}{x^{2}+3x^{2}+2+3}=\\frac{\\ln\\left(5x+8\\right)+4x}{x^{2}+3x^{2}+2+3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{2}+3x^{2}=4x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{\\ln\\left(5x+8\\right)+4x}{x^{2}+3x^{2}+2+3}=\\frac{\\ln\\left(5x+8\\right)+4x}{4x^{2}+5}'}], 'finalResult': '\\frac{\\ln\\left(5x+8\\right)+4x}{4x^{2}+5}'},
            },
            {
                'expression': 'cos(5x^{2}+sqrt{9x^{2}+x^{2}+2+3}+3x^{2})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle 5x^{2}+\\sqrt{9x^{2}+x^{2}+2+3}+3x^{2}=8x^{2}+\\sqrt{10x^{2}+5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 5x^{2}+\\sqrt{9x^{2}+x^{2}+2+3}+3x^{2}=5x^{2}+3x^{2}+\\sqrt{9x^{2}+x^{2}+2+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 5x^{2}+3x^{2}=8x^{2}'},
                        {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{9x^{2}+x^{2}+2+3}=\\sqrt{10x^{2}+5}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 9x^{2}+x^{2}=10x^{2}'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{9x^{2}+x^{2}+2+3}=\\sqrt{10x^{2}+5}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\cos\\left(5x^{2}+\\sqrt{9x^{2}+x^{2}+2+3}+3x^{2}\\right)=\\cos\\left(8x^{2}+\\sqrt{10x^{2}+5}\\right)'}], 'finalResult': '\\cos\\left(8x^{2}+\\sqrt{10x^{2}+5}\\right)'},
            },
            {
                'expression': '(sqrt{5x+2x+1}+2)^{2}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+2x+1=7x+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{5x+2x+1}=\\sqrt{7x+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(\\sqrt{5x+2x+1}+2\\right)^{2}=\\left(\\sqrt{7x+1}+2\\right)^{2}'}], 'finalResult': '\\left(\\sqrt{7x+1}+2\\right)^{2}'},
            },
            {
                'expression': 'frac{x^{2}+(5x-2x-x-x)^{2}+(1+sqrt{3x^{2}+9x^{2}+3+2})^{1+1}}{x^{2}+sqrt{(x^{2}+3x^{2}+1)^{2}}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x-2x-x-x=x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(5x-2x-x-x\\right)^{2}=x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 1+\\sqrt{3x^{2}+9x^{2}+3+2}=\\sqrt{3x^{2}+9x^{2}+3+2}+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 3x^{2}+9x^{2}=12x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+2=5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{3x^{2}+9x^{2}+3+2}=\\sqrt{12x^{2}+5}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(1+\\sqrt{3x^{2}+9x^{2}+3+2}\\right)^{1+1}=\\left(\\sqrt{12x^{2}+5}+1\\right)^{1+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(\\sqrt{12x^{2}+5}+1\\right)^{1+1}=\\left(\\sqrt{12x^{2}+5}+1\\right)^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle x^{2}+\\left(5x-2x-x-x\\right)^{2}+\\left(1+\\sqrt{3x^{2}+9x^{2}+3+2}\\right)^{1+1}=x^{2}+x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{2}+x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{2}=2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{x^{2}+\\left(5x-2x-x-x\\right)^{2}+\\left(1+\\sqrt{3x^{2}+9x^{2}+3+2}\\right)^{1+1}}{x^{2}+\\sqrt{\\left(x^{2}+3x^{2}+1\\right)^{2}}}=\\frac{2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{2}}{x^{2}+\\sqrt{\\left(x^{2}+3x^{2}+1\\right)^{2}}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply radical rule:}\\ \\sqrt[n]{a^n}=a', 'info': '\\displaystyle \\sqrt{\\left(x^{2}+3x^{2}+1\\right)^{2}}=\\left(x^{2}+3x^{2}+1\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(x^{2}+3x^{2}+1\\right)=x^{2}+3x^{2}+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{2}+3x^{2}=4x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x^{2}+4x^{2}+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{2}+4x^{2}=5x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{2}}{x^{2}+\\sqrt{\\left(x^{2}+3x^{2}+1\\right)^{2}}}=\\frac{2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{2}}{5x^{2}+1}'}], 'finalResult': '\\frac{2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{2}}{5x^{2}+1}'},
            },

            {
                'expression': 'frac{x^{2}+(5x-2x-x-x)^{2}+(1+sqrt{3x^{2}+9x^{2}+3+2})^{sqrt{5x+2x+e^{x^{2}+3x^{2}+1}}}}{(t^{4}+3t^{3}+5*(1+t^{2}+(3t^{2}+t^{2}+2)))^{2}+sqrt{(x^{2}+3x^{2}+1)^{2}}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x-2x-x-x=x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(5x-2x-x-x\\right)^{2}=x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 1+\\sqrt{3x^{2}+9x^{2}+3+2}=\\sqrt{3x^{2}+9x^{2}+3+2}+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 3x^{2}+9x^{2}=12x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+2=5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{3x^{2}+9x^{2}+3+2}=\\sqrt{12x^{2}+5}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(1+\\sqrt{3x^{2}+9x^{2}+3+2}\\right)^{\\sqrt{5x+2x+e^{x^{2}+3x^{2}+1}}}=\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{5x+2x+e^{x^{2}+3x^{2}+1}}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 5x+2x+e^{x^{2}+3x^{2}+1}=e^{x^{2}+3x^{2}+1}+5x+2x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{2}+3x^{2}=4x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{x^{2}+3x^{2}+1}=e^{4x^{2}+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+2x=7x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{5x+2x+e^{x^{2}+3x^{2}+1}}=\\sqrt{e^{4x^{2}+1}+7x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{5x+2x+e^{x^{2}+3x^{2}+1}}}=\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{e^{4x^{2}+1}+7x}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle x^{2}+\\left(5x-2x-x-x\\right)^{2}+\\left(1+\\sqrt{3x^{2}+9x^{2}+3+2}\\right)^{\\sqrt{5x+2x+e^{x^{2}+3x^{2}+1}}}=x^{2}+x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{e^{4x^{2}+1}+7x}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{2}+x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{e^{4x^{2}+1}+7x}}=2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{e^{4x^{2}+1}+7x}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{x^{2}+\\left(5x-2x-x-x\\right)^{2}+\\left(1+\\sqrt{3x^{2}+9x^{2}+3+2}\\right)^{\\sqrt{5x+2x+e^{x^{2}+3x^{2}+1}}}}{\\left(t^{4}+3t^{3}+5\\cdot\\left(1+t^{2}+\\left(3t^{2}+t^{2}+2\\right)\\right)\\right)^{2}+\\sqrt{\\left(x^{2}+3x^{2}+1\\right)^{2}}}=\\frac{2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{e^{4x^{2}+1}+7x}}}{\\left(t^{4}+3t^{3}+5\\cdot\\left(1+t^{2}+\\left(3t^{2}+t^{2}+2\\right)\\right)\\right)^{2}+\\sqrt{\\left(x^{2}+3x^{2}+1\\right)^{2}}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5\\cdot\\left(1+t^{2}+\\left(3t^{2}+t^{2}+2\\right)\\right)=5\\cdot1+5\\cdot t^{2}+5\\cdot\\left(3t^{2}+t^{2}+2\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot1=5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot t^{2}=5t^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5\\cdot\\left(3t^{2}+t^{2}+2\\right)=5\\cdot3t^{2}+5\\cdot t^{2}+5\\cdot2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot3t^{2}=15t^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot t^{2}=5t^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot2=10'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 15t^{2}+5t^{2}=20t^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 5+5t^{2}+20t^{2}+10=5t^{2}+20t^{2}+5+10'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 5t^{2}+20t^{2}=25t^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5+10=15'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(t^{4}+3t^{3}+5\\cdot\\left(1+t^{2}+\\left(3t^{2}+t^{2}+2\\right)\\right)\\right)^{2}=\\left(t^{4}+3t^{3}+25t^{2}+15\\right)^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply radical rule:}\\ \\sqrt[n]{a^n}=a', 'info': '\\displaystyle \\sqrt{\\left(x^{2}+3x^{2}+1\\right)^{2}}=\\left(x^{2}+3x^{2}+1\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(x^{2}+3x^{2}+1\\right)=x^{2}+3x^{2}+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{2}+3x^{2}=4x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{e^{4x^{2}+1}+7x}}}{\\left(t^{4}+3t^{3}+5\\cdot\\left(1+t^{2}+\\left(3t^{2}+t^{2}+2\\right)\\right)\\right)^{2}+\\sqrt{\\left(x^{2}+3x^{2}+1\\right)^{2}}}=\\frac{2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{e^{4x^{2}+1}+7x}}}{\\left(t^{4}+3t^{3}+25t^{2}+15\\right)^{2}+4x^{2}+1}'}], 'finalResult': '\\frac{2x^{2}+\\left(\\sqrt{12x^{2}+5}+1\\right)^{\\sqrt{e^{4x^{2}+1}+7x}}}{\\left(t^{4}+3t^{3}+25t^{2}+15\\right)^{2}+4x^{2}+1}'},
            },

            {
                'expression': '5*(t^{2}+sqrt{3t^{2}+t^{2}+1})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5\\cdot\\left(t^{2}+\\sqrt{3t^{2}+t^{2}+1}\\right)=5\\cdot t^{2}+5\\cdot\\sqrt{3t^{2}+t^{2}+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot t^{2}=5t^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot\\sqrt{3t^{2}+t^{2}+1}=5\\sqrt{3t^{2}+t^{2}+1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 5\\sqrt{3t^{2}+t^{2}+1}=5\\sqrt{4t^{2}+1}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 3t^{2}+t^{2}=4t^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 5\\sqrt{3t^{2}+t^{2}+1}=5\\sqrt{4t^{2}+1}'}]}], 'finalResult': '5t^{2}+5\\sqrt{4t^{2}+1}'},
            },
            {
                'expression': '(frac{3x^{2}+x^{2}+3+4}{3x+x+1+2})^{1+1}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 3x^{2}+x^{2}=4x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+4=7'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3x^{2}+x^{2}+3+4}{3x+x+1+2}=\\frac{4x^{2}+7}{3x+x+1+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+x+1+2=4x+1+2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4x+1+2=4x+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{4x^{2}+7}{3x+x+1+2}=\\frac{4x^{2}+7}{4x+3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(\\frac{3x^{2}+x^{2}+3+4}{3x+x+1+2}\\right)^{1+1}=\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{1+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(\\frac{4x^{2}+7}{4x+3}\\right)^{1+1}=\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{2}'}], 'finalResult': '\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{2}'},
            },
            {
                'expression': 'sqrt{(frac{3x^{2}+x^{2}+3+4}{3x+x+1+2})^{1+1}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{\\left(\\frac{3x^{2}+x^{2}+3+4}{3x+x+1+2}\\right)^{1+1}}=\\sqrt{\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{2}}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 3x^{2}+x^{2}=4x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+4=7'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3x^{2}+x^{2}+3+4}{3x+x+1+2}=\\frac{4x^{2}+7}{3x+x+1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+x+1+2=4x+1+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4x+1+2=4x+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{4x^{2}+7}{3x+x+1+2}=\\frac{4x^{2}+7}{4x+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(\\frac{3x^{2}+x^{2}+3+4}{3x+x+1+2}\\right)^{1+1}=\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(\\frac{4x^{2}+7}{4x+3}\\right)^{1+1}=\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{\\left(\\frac{3x^{2}+x^{2}+3+4}{3x+x+1+2}\\right)^{1+1}}=\\sqrt{\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{2}}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\sqrt{\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{2}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply radical rule:}\\ \\sqrt[n]{a^n}=a', 'info': '\\displaystyle \\sqrt{\\left(\\frac{4x^{2}+7}{4x+3}\\right)^{2}}=\\left(\\frac{4x^{2}+7}{4x+3}\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(\\frac{4x^{2}+7}{4x+3}\\right)=\\frac{4x^{2}+7}{4x+3}'}], 'finalResult': '\\frac{4x^{2}+7}{4x+3}'},
            },
            {
                'expression': 'sqrt{(frac{3x^{2}+x^{2}+3+4}{5x+x+1+2})^{1+1}}+sqrt[3]{(frac{15x+3x+2+1}{2x^{2}+3x^{2}+3+5})^{5-2}}+sqrt{(frac{4x+2x+1}{9x-x+5x+2+3})^{2+3}}+sqrt{frac{3x+x+1}{5x-x+3}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{\\left(\\frac{3x^{2}+x^{2}+3+4}{5x+x+1+2}\\right)^{1+1}}=\\sqrt{\\left(\\frac{4x^{2}+7}{6x+3}\\right)^{2}}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 3x^{2}+x^{2}=4x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+4=7'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3x^{2}+x^{2}+3+4}{5x+x+1+2}=\\frac{4x^{2}+7}{5x+x+1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x+x+1+2=6x+1+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 6x+1+2=6x+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{4x^{2}+7}{5x+x+1+2}=\\frac{4x^{2}+7}{6x+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(\\frac{3x^{2}+x^{2}+3+4}{5x+x+1+2}\\right)^{1+1}=\\left(\\frac{4x^{2}+7}{6x+3}\\right)^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(\\frac{4x^{2}+7}{6x+3}\\right)^{1+1}=\\left(\\frac{4x^{2}+7}{6x+3}\\right)^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{\\left(\\frac{3x^{2}+x^{2}+3+4}{5x+x+1+2}\\right)^{1+1}}=\\sqrt{\\left(\\frac{4x^{2}+7}{6x+3}\\right)^{2}}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt[3]{\\left(\\frac{15x+3x+2+1}{2x^{2}+3x^{2}+3+5}\\right)^{5-2}}=\\sqrt[3]{\\left(\\frac{18x+3}{5x^{2}+8}\\right)^{3}}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 15x+3x+2+1=18x+2+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 18x+2+1=18x+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{15x+3x+2+1}{2x^{2}+3x^{2}+3+5}=\\frac{18x+3}{2x^{2}+3x^{2}+3+5}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 2x^{2}+3x^{2}=5x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+5=8'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{18x+3}{2x^{2}+3x^{2}+3+5}=\\frac{18x+3}{5x^{2}+8}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(\\frac{15x+3x+2+1}{2x^{2}+3x^{2}+3+5}\\right)^{5-2}=\\left(\\frac{18x+3}{5x^{2}+8}\\right)^{5-2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5-2=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(\\frac{18x+3}{5x^{2}+8}\\right)^{5-2}=\\left(\\frac{18x+3}{5x^{2}+8}\\right)^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt[3]{\\left(\\frac{15x+3x+2+1}{2x^{2}+3x^{2}+3+5}\\right)^{5-2}}=\\sqrt[3]{\\left(\\frac{18x+3}{5x^{2}+8}\\right)^{3}}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{\\left(\\frac{4x+2x+1}{9x-x+5x+2+3}\\right)^{2+3}}=\\sqrt{\\left(\\frac{6x+1}{13x+5}\\right)^{5}}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 4x+2x+1=6x+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{4x+2x+1}{9x-x+5x+2+3}=\\frac{6x+1}{9x-x+5x+2+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 9x-x+5x+2+3=13x+2+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 13x+2+3=13x+5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{6x+1}{9x-x+5x+2+3}=\\frac{6x+1}{13x+5}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Base}', 'info': '\\displaystyle \\left(\\frac{4x+2x+1}{9x-x+5x+2+3}\\right)^{2+3}=\\left(\\frac{6x+1}{13x+5}\\right)^{2+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle \\left(\\frac{6x+1}{13x+5}\\right)^{2+3}=\\left(\\frac{6x+1}{13x+5}\\right)^{5}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{\\left(\\frac{4x+2x+1}{9x-x+5x+2+3}\\right)^{2+3}}=\\sqrt{\\left(\\frac{6x+1}{13x+5}\\right)^{5}}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{\\frac{3x+x+1}{5x-x+3}}=\\sqrt{\\frac{4x+1}{4x+3}}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+x+1=4x+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3x+x+1}{5x-x+3}=\\frac{4x+1}{5x-x+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 5x-x+3=4x+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{4x+1}{5x-x+3}=\\frac{4x+1}{4x+3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{\\frac{3x+x+1}{5x-x+3}}=\\sqrt{\\frac{4x+1}{4x+3}}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\sqrt{\\left(\\frac{4x^{2}+7}{6x+3}\\right)^{2}}+\\sqrt[3]{\\left(\\frac{18x+3}{5x^{2}+8}\\right)^{3}}+\\sqrt{\\left(\\frac{6x+1}{13x+5}\\right)^{5}}+\\sqrt{\\frac{4x+1}{4x+3}}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply radical rule:}\\ \\sqrt[n]{a^n}=a', 'info': '\\displaystyle \\sqrt{\\left(\\frac{4x^{2}+7}{6x+3}\\right)^{2}}=\\left(\\frac{4x^{2}+7}{6x+3}\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(\\frac{4x^{2}+7}{6x+3}\\right)=\\frac{4x^{2}+7}{6x+3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply radical rule:}\\ \\sqrt[n]{a^n}=a', 'info': '\\displaystyle \\sqrt[3]{\\left(\\frac{18x+3}{5x^{2}+8}\\right)^{3}}=\\left(\\frac{18x+3}{5x^{2}+8}\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Remove Redundant Parentheses}', 'info': '\\displaystyle \\left(\\frac{18x+3}{5x^{2}+8}\\right)=\\frac{18x+3}{5x^{2}+8}'}], 'finalResult': '\\frac{4x^{2}+7}{6x+3}+\\frac{18x+3}{5x^{2}+8}+\\sqrt{\\left(\\frac{6x+1}{13x+5}\\right)^{5}}+\\sqrt{\\frac{4x+1}{4x+3}}'},
            },
            {
                'expression': 'sin(frac{pi}{3})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\sin\\left(\\frac{\\pi}{3}\\right)=\\frac{\\sqrt{3}}{2}'}], 'finalResult': '\\frac{\\sqrt{3}}{2}'},
            },
            {
                'expression': '1+2+cos(frac{pi}{3})+3+4+sin(frac{pi}{3})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\cos\\left(\\frac{\\pi}{3}\\right)=\\frac{1}{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\sin\\left(\\frac{\\pi}{3}\\right)=\\frac{\\sqrt{3}}{2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 1+2+\\frac{1}{2}+3+4+\\frac{\\sqrt{3}}{2}=\\frac{1}{2}+\\frac{\\sqrt{3}}{2}+10', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 1+2+\\frac{1}{2}+3+4+\\frac{\\sqrt{3}}{2}=\\frac{1}{2}+\\frac{\\sqrt{3}}{2}+1+2+3+4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle \\frac{1}{2}+\\frac{\\sqrt{3}}{2}+1+2+3+4=\\frac{1}{2}+\\frac{\\sqrt{3}}{2}+10'}]}], 'finalResult': '\\frac{1}{2}+\\frac{\\sqrt{3}}{2}+10'},
            },
            {
                'expression': '5+3+sin(2pi)+sin(frac{3pi}{2})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\sin\\left(2\\pi\\right)=0'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\sin\\left(\\frac{3\\pi}{2}\\right)=-1'},
                    {'type': 'e-step', 'heading': '\\displaystyle 5+3+0-1=7', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5+3+0-1=7'}]}], 'finalResult': '7'},
            },
            {
                'expression': '2+3+sin(2pi)+cos(2pi)+sin(frac{pi}{4})+csc(frac{pi}{4})+tan(frac{pi}{3})+ln(e)+5+9',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\sin\\left(2\\pi\\right)=0'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\cos\\left(2\\pi\\right)=1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\sin\\left(\\frac{\\pi}{4}\\right)=\\frac{\\sqrt{2}}{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\csc\\left(\\frac{\\pi}{4}\\right)=\\sqrt{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\tan\\left(\\frac{\\pi}{3}\\right)=\\sqrt{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Evaluate Function}', 'info': '\\displaystyle \\ln\\left(e\\right)=1'},
                    {'type': 'e-step', 'heading': '\\displaystyle 2+3+0+1+\\frac{\\sqrt{2}}{2}+\\sqrt{2}+\\sqrt{3}+1+5+9=\\frac{\\sqrt{2}}{2}+\\sqrt{2}+\\sqrt{3}+21', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 2+3+0+1+\\frac{\\sqrt{2}}{2}+\\sqrt{2}+\\sqrt{3}+1+5+9=\\frac{\\sqrt{2}}{2}+\\sqrt{2}+\\sqrt{3}+2+3+0+1+1+5+9'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle \\frac{\\sqrt{2}}{2}+\\sqrt{2}+\\sqrt{3}+2+3+0+1+1+5+9=\\frac{\\sqrt{2}}{2}+\\sqrt{2}+\\sqrt{3}+21'}]}], 'finalResult': '\\frac{\\sqrt{2}}{2}+\\sqrt{2}+\\sqrt{3}+21'},
            },
            {
                'expression': '3*7*5*frac{sqrt{2}}{2}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle 3\\cdot7\\cdot5\\cdot\\frac{\\sqrt{2}}{2}=\\frac{3\\cdot7\\cdot5\\cdot\\sqrt{2}}{1\\cdot1\\cdot1\\cdot2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{3\\cdot7\\cdot5\\cdot\\sqrt{2}}{1\\cdot1\\cdot1\\cdot2}=\\frac{105\\sqrt{2}}{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot7\\cdot5\\cdot\\sqrt{2}=105\\sqrt{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3\\cdot7\\cdot5\\cdot\\sqrt{2}}{1\\cdot1\\cdot1\\cdot2}=\\frac{105\\sqrt{2}}{1\\cdot1\\cdot1\\cdot2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot1\\cdot1\\cdot2=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{105\\sqrt{2}}{1\\cdot1\\cdot1\\cdot2}=\\frac{105\\sqrt{2}}{2}'}]}], 'finalResult': '\\frac{105\\sqrt{2}}{2}'},
            },
            {
                'expression': '5*frac{3}{2}*frac{4}{5}*frac{3}{6}*3*2+3*frac{4}{2}*frac{1}{2}*2*4',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle 5\\cdot\\frac{3}{2}\\cdot\\frac{4}{5}\\cdot\\frac{3}{6}\\cdot3\\cdot2=\\frac{5\\cdot3\\cdot4\\cdot3\\cdot3\\cdot2}{1\\cdot2\\cdot5\\cdot6\\cdot1\\cdot1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle 3\\cdot\\frac{4}{2}\\cdot\\frac{1}{2}\\cdot2\\cdot4=\\frac{3\\cdot4\\cdot1\\cdot2\\cdot4}{1\\cdot2\\cdot2\\cdot1\\cdot1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{5\\cdot3\\cdot4\\cdot3\\cdot3\\cdot2}{1\\cdot2\\cdot5\\cdot6\\cdot1\\cdot1}=18', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot3\\cdot4\\cdot3\\cdot3\\cdot2=1080'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{5\\cdot3\\cdot4\\cdot3\\cdot3\\cdot2}{1\\cdot2\\cdot5\\cdot6\\cdot1\\cdot1}=\\frac{1080}{1\\cdot2\\cdot5\\cdot6\\cdot1\\cdot1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot2\\cdot5\\cdot6\\cdot1\\cdot1=60'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{1080}{1\\cdot2\\cdot5\\cdot6\\cdot1\\cdot1}=\\frac{1080}{60}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Divide The Numbers}', 'info': '\\displaystyle \\frac{1080}{60}=18'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{3\\cdot4\\cdot1\\cdot2\\cdot4}{1\\cdot2\\cdot2\\cdot1\\cdot1}=24', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot4\\cdot1\\cdot2\\cdot4=96'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3\\cdot4\\cdot1\\cdot2\\cdot4}{1\\cdot2\\cdot2\\cdot1\\cdot1}=\\frac{96}{1\\cdot2\\cdot2\\cdot1\\cdot1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot2\\cdot2\\cdot1\\cdot1=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{96}{1\\cdot2\\cdot2\\cdot1\\cdot1}=\\frac{96}{4}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Divide The Numbers}', 'info': '\\displaystyle \\frac{96}{4}=24'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 18+24'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 18+24=42'}], 'finalResult': '42'},
            },
            {
                'expression': '5*x*frac{3}{y}*3*x^{2}*frac{4}{3y}*frac{1}{7}*4+3*frac{4}{2}*frac{1}{2}*2*4',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle 5\\cdot x\\cdot\\frac{3}{y}\\cdot3\\cdot x^{2}\\cdot\\frac{4}{3y}\\cdot\\frac{1}{7}\\cdot4=\\frac{5\\cdot x\\cdot3\\cdot3\\cdot x^{2}\\cdot4\\cdot1\\cdot4}{1\\cdot1\\cdot y\\cdot1\\cdot1\\cdot3y\\cdot7\\cdot1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle 3\\cdot\\frac{4}{2}\\cdot\\frac{1}{2}\\cdot2\\cdot4=\\frac{3\\cdot4\\cdot1\\cdot2\\cdot4}{1\\cdot2\\cdot2\\cdot1\\cdot1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{5\\cdot x\\cdot3\\cdot3\\cdot x^{2}\\cdot4\\cdot1\\cdot4}{1\\cdot1\\cdot y\\cdot1\\cdot1\\cdot3y\\cdot7\\cdot1}=\\frac{720x^{3}}{21y^{2}}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot x\\cdot3\\cdot3\\cdot x^{2}\\cdot4\\cdot1\\cdot4=720x^{1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 720x^{1+2}=720x^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{5\\cdot x\\cdot3\\cdot3\\cdot x^{2}\\cdot4\\cdot1\\cdot4}{1\\cdot1\\cdot y\\cdot1\\cdot1\\cdot3y\\cdot7\\cdot1}=\\frac{720x^{3}}{1\\cdot1\\cdot y\\cdot1\\cdot1\\cdot3y\\cdot7\\cdot1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot1\\cdot y\\cdot1\\cdot1\\cdot3y\\cdot7\\cdot1=21y^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 21y^{1+1}=21y^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{720x^{3}}{1\\cdot1\\cdot y\\cdot1\\cdot1\\cdot3y\\cdot7\\cdot1}=\\frac{720x^{3}}{21y^{2}}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{3\\cdot4\\cdot1\\cdot2\\cdot4}{1\\cdot2\\cdot2\\cdot1\\cdot1}=24', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot4\\cdot1\\cdot2\\cdot4=96'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{3\\cdot4\\cdot1\\cdot2\\cdot4}{1\\cdot2\\cdot2\\cdot1\\cdot1}=\\frac{96}{1\\cdot2\\cdot2\\cdot1\\cdot1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot2\\cdot2\\cdot1\\cdot1=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{96}{1\\cdot2\\cdot2\\cdot1\\cdot1}=\\frac{96}{4}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Divide The Numbers}', 'info': '\\displaystyle \\frac{96}{4}=24'}]}], 'finalResult': '\\frac{720x^{3}}{21y^{2}}+24'},
            },
            {
                'expression': '4*x^{2}*3*x*(x+3)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 4\\cdot x^{2}\\cdot3\\cdot x=12x^{2+1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 12x^{2+1}\\cdot\\left(x+3\\right)=12x^{4}+36x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 12x^{2+1}\\cdot\\left(x+3\\right)=12x^{2+1}\\cdot x+12x^{2+1}\\cdot3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 12x^{2+1}\\cdot x=12x^{2+1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 12x^{2+1}\\cdot3=36x^{2+1}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 12x^{2+1+1}=12x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1+1=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 12x^{2+1+1}=12x^{4}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 36x^{2+1}=36x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 36x^{2+1}=36x^{3}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 12x^{2+1+1}+36x^{2+1}=12x^{4}+36x^{3}'}]}], 'finalResult': '12x^{4}+36x^{3}'},
            },
            {
                'expression': '3x^{2}*-x*2* t',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot-x\\cdot2\\cdot t=-6x^{2+1}t'},
                    {'type': 'e-step', 'heading': '\\displaystyle 6x^{2+1}=6x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 6x^{2+1}=6x^{3}'}]}], 'finalResult': '-6x^{3}t'},
            },
            {
                'expression': '4*3*x*(x+3)*5*4',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 4\\cdot3\\cdot x\\cdot5\\cdot4=240x'},
                    {'type': 'e-step', 'heading': '\\displaystyle 240x\\cdot\\left(x+3\\right)=240x^{2}+720x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 240x\\cdot\\left(x+3\\right)=240x\\cdot x+240x\\cdot3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 240x\\cdot x=240x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 240x\\cdot3=720x'},
                        {'type': 'e-step', 'heading': '\\displaystyle 240x^{1+1}=240x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 240x^{1+1}=240x^{2}'}]}]}], 'finalResult': '240x^{2}+720x'},
            },
            {
                'expression': '(25x^{2}+6x+3)*5x*4',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 5x\\cdot4=20x'},
                    {'type': 'e-step', 'heading': '\\displaystyle 20x\\cdot\\left(25x^{2}+6x+3\\right)=500x^{3}+120x^{2}+60x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 20x\\cdot\\left(25x^{2}+6x+3\\right)=20x\\cdot25x^{2}+20x\\cdot6x+20x\\cdot3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 20x\\cdot25x^{2}=500x^{1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 20x\\cdot6x=120x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 20x\\cdot3=60x'},
                        {'type': 'e-step', 'heading': '\\displaystyle 500x^{1+2}=500x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 500x^{1+2}=500x^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 120x^{1+1}=120x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 120x^{1+1}=120x^{2}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 500x^{1+2}+120x^{1+1}=500x^{3}+120x^{2}'}]}], 'finalResult': '500x^{3}+120x^{2}+60x'},
            },
            {
                'expression': '2x*3x^{2}*(10x^{2}+2x+1)*5x*4*3',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 2x\\cdot3x^{2}\\cdot5x\\cdot4\\cdot3=360x^{1+2+1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 360x^{1+2+1}\\cdot\\left(10x^{2}+2x+1\\right)=3600x^{6}+720x^{5}+360x^{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 360x^{1+2+1}\\cdot\\left(10x^{2}+2x+1\\right)=360x^{1+2+1}\\cdot10x^{2}+360x^{1+2+1}\\cdot2x+360x^{1+2+1}\\cdot1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 360x^{1+2+1}\\cdot10x^{2}=3600x^{1+2+1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 360x^{1+2+1}\\cdot2x=720x^{1+2+1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 360x^{1+2+1}\\cdot1=360x^{1+2+1}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3600x^{1+2+1+2}=3600x^{6}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+1+2=6'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3600x^{1+2+1+2}=3600x^{6}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 720x^{1+2+1+1}=720x^{5}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+1+1=5'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 720x^{1+2+1+1}=720x^{5}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 360x^{1+2+1}=360x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+1=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 360x^{1+2+1}=360x^{4}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 3600x^{1+2+1+2}+720x^{1+2+1+1}+360x^{1+2+1}=3600x^{6}+720x^{5}+360x^{4}'}]}], 'finalResult': '3600x^{6}+720x^{5}+360x^{4}'},
            },
            {
                'expression': '4*x*frac{x+3}{5}*3*frac{4}{y+1}*3',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle 4\\cdot x\\cdot\\frac{x+3}{5}\\cdot3\\cdot\\frac{4}{y+1}\\cdot3=\\frac{4\\cdot x\\cdot\\left(x+3\\right)\\cdot3\\cdot4\\cdot3}{1\\cdot1\\cdot5\\cdot1\\cdot\\left(y+1\\right)\\cdot1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{4\\cdot x\\cdot\\left(x+3\\right)\\cdot3\\cdot4\\cdot3}{1\\cdot1\\cdot5\\cdot1\\cdot\\left(y+1\\right)\\cdot1}=\\frac{144x^{2}+432x}{5y+5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 4\\cdot x\\cdot3\\cdot4\\cdot3=144x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 144x\\cdot\\left(x+3\\right)=144x\\cdot x+144x\\cdot3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 144x\\cdot x=144x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 144x\\cdot3=432x'},
                        {'type': 'e-step', 'heading': '\\displaystyle 144x^{1+1}=144x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 144x^{1+1}=144x^{2}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{4\\cdot x\\cdot\\left(x+3\\right)\\cdot3\\cdot4\\cdot3}{1\\cdot1\\cdot5\\cdot1\\cdot\\left(y+1\\right)\\cdot1}=\\frac{144x^{2}+432x}{1\\cdot1\\cdot5\\cdot1\\cdot\\left(y+1\\right)\\cdot1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 1\\cdot1\\cdot5\\cdot1\\cdot1=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5\\cdot\\left(y+1\\right)=5\\cdot y+5\\cdot1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot y=5y'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot1=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{144x^{2}+432x}{1\\cdot1\\cdot5\\cdot1\\cdot\\left(y+1\\right)\\cdot1}=\\frac{144x^{2}+432x}{5y+5}'}]}], 'finalResult': '\\frac{144x^{2}+432x}{5y+5}'},
            },
            {
                'expression': '20uv^{2}x*5x^{2}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 20uv^{2}x\\cdot5x^{2}=100x^{2+1}uv^{2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 100x^{2+1}=100x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 100x^{2+1}=100x^{3}'}]}], 'finalResult': '100x^{3}uv^{2}'},
            },
            {
                'expression': '4u*5*v^{2}*x*(5x^{2}+3x^{2}+2x+1)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 4u\\cdot5\\cdot v^{2}\\cdot x=20uv^{2}x'},
                    {'type': 'e-step', 'heading': '\\displaystyle 20uv^{2}x\\cdot\\left(5x^{2}+3x^{2}+2x+1\\right)=160x^{3}uv^{2}+40x^{2}uv^{2}+20uv^{2}x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 20uv^{2}x\\cdot\\left(5x^{2}+3x^{2}+2x+1\\right)=20uv^{2}x\\cdot5x^{2}+20uv^{2}x\\cdot3x^{2}+20uv^{2}x\\cdot2x+20uv^{2}x\\cdot1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 20uv^{2}x\\cdot5x^{2}=100x^{2+1}uv^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 20uv^{2}x\\cdot3x^{2}=60x^{2+1}uv^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 20uv^{2}x\\cdot2x=40x^{1+1}uv^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 20uv^{2}x\\cdot1=20uv^{2}x'},
                        {'type': 'e-step', 'heading': '\\displaystyle 100x^{2+1}=100x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 100x^{2+1}=100x^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 60x^{2+1}=60x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 60x^{2+1}=60x^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 40x^{1+1}=40x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 40x^{1+1}=40x^{2}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 100x^{3}uv^{2}+60x^{3}uv^{2}+40x^{2}uv^{2}+20uv^{2}x=160x^{3}uv^{2}+40x^{2}uv^{2}+20uv^{2}x', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 100x^{3}uv^{2}+60x^{3}uv^{2}+40x^{2}uv^{2}+20uv^{2}x=160x^{3}uv^{2}+40x^{2}uv^{2}+20uv^{2}x'}]}]}], 'finalResult': '160x^{3}uv^{2}+40x^{2}uv^{2}+20uv^{2}x'},
            },
            {
                'expression': '4u*frac{5}{x}* v^{2}* x*frac{u+v}{u^{2}-v^{2}}*frac{2}{x+y}*frac{5x^{2}+3x^{2}+2x+1}{x^{2}+y^{2}}*5x^{2}*3u^{2}*frac{v}{12x^{2}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle 4u\\cdot\\frac{5}{x}\\cdot v^{2}\\cdot x\\cdot\\frac{u+v}{u^{2}-v^{2}}\\cdot\\frac{2}{x+y}\\cdot\\frac{5x^{2}+3x^{2}+2x+1}{x^{2}+y^{2}}\\cdot5x^{2}\\cdot3u^{2}\\cdot\\frac{v}{12x^{2}}=\\frac{4u\\cdot5\\cdot v^{2}\\cdot x\\cdot\\left(u+v\\right)\\cdot2\\cdot\\left(5x^{2}+3x^{2}+2x+1\\right)\\cdot5x^{2}\\cdot3u^{2}\\cdot v}{1\\cdot x\\cdot1\\cdot1\\cdot\\left(u^{2}-v^{2}\\right)\\cdot\\left(x+y\\right)\\cdot\\left(x^{2}+y^{2}\\right)\\cdot1\\cdot1\\cdot12x^{2}}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{4u\\cdot5\\cdot v^{2}\\cdot x\\cdot\\left(u+v\\right)\\cdot2\\cdot\\left(5x^{2}+3x^{2}+2x+1\\right)\\cdot5x^{2}\\cdot3u^{2}\\cdot v}{1\\cdot x\\cdot1\\cdot1\\cdot\\left(u^{2}-v^{2}\\right)\\cdot\\left(x+y\\right)\\cdot\\left(x^{2}+y^{2}\\right)\\cdot1\\cdot1\\cdot12x^{2}}=\\frac{600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(8x^{2}+2x+1\\right)}{12x^{3}\\left(u^{2}-v^{2}\\right)\\left(x+y\\right)\\left(x^{2}+y^{2}\\right)}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 4u\\cdot5\\cdot v^{2}\\cdot x\\cdot2\\cdot5x^{2}\\cdot3u^{2}\\cdot v=600u^{1+2}v^{2+1}x^{1+2}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 600u^{1+2}=600u^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 600u^{1+2}=600u^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle v^{2+1}=v^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle v^{2+1}=v^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle x^{1+2}=x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+2}=x^{3}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Result}', 'info': '\\displaystyle 4u\\cdot5\\cdot v^{2}\\cdot x\\cdot\\left(u+v\\right)\\cdot2\\cdot\\left(5x^{2}+3x^{2}+2x+1\\right)\\cdot5x^{2}\\cdot3u^{2}\\cdot v=600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(5x^{2}+3x^{2}+2x+1\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 5x^{2}+3x^{2}=8x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(5x^{2}+3x^{2}+2x+1\\right)=600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(8x^{2}+2x+1\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{4u\\cdot5\\cdot v^{2}\\cdot x\\cdot\\left(u+v\\right)\\cdot2\\cdot\\left(5x^{2}+3x^{2}+2x+1\\right)\\cdot5x^{2}\\cdot3u^{2}\\cdot v}{1\\cdot x\\cdot1\\cdot1\\cdot\\left(u^{2}-v^{2}\\right)\\cdot\\left(x+y\\right)\\cdot\\left(x^{2}+y^{2}\\right)\\cdot1\\cdot1\\cdot12x^{2}}=\\frac{600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(8x^{2}+2x+1\\right)}{1\\cdot x\\cdot1\\cdot1\\cdot\\left(u^{2}-v^{2}\\right)\\cdot\\left(x+y\\right)\\cdot\\left(x^{2}+y^{2}\\right)\\cdot1\\cdot1\\cdot12x^{2}}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 1\\cdot x\\cdot1\\cdot1\\cdot1\\cdot1\\cdot12x^{2}=12x^{1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 12x^{1+2}=12x^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Result}', 'info': '\\displaystyle 1\\cdot x\\cdot1\\cdot1\\cdot\\left(u^{2}-v^{2}\\right)\\cdot\\left(x+y\\right)\\cdot\\left(x^{2}+y^{2}\\right)\\cdot1\\cdot1\\cdot12x^{2}=12x^{3}\\left(u^{2}-v^{2}\\right)\\left(x+y\\right)\\left(x^{2}+y^{2}\\right)'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(8x^{2}+2x+1\\right)}{1\\cdot x\\cdot1\\cdot1\\cdot\\left(u^{2}-v^{2}\\right)\\cdot\\left(x+y\\right)\\cdot\\left(x^{2}+y^{2}\\right)\\cdot1\\cdot1\\cdot12x^{2}}=\\frac{600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(8x^{2}+2x+1\\right)}{12x^{3}\\left(u^{2}-v^{2}\\right)\\left(x+y\\right)\\left(x^{2}+y^{2}\\right)}'}]}], 'finalResult': '\\frac{600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(8x^{2}+2x+1\\right)}{12x^{3}\\left(u^{2}-v^{2}\\right)\\left(x+y\\right)\\left(x^{2}+y^{2}\\right)}'},
            },
            {
                'expression': '5x*3u*3*2*x^{2}*u^{2}*(3x^{2}+2x+3)*(x+2)*2u*u^{2}*x^{3}*(x+1)*u',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 5x\\cdot3u\\cdot3\\cdot2\\cdot x^{2}\\cdot u^{2}\\cdot2u\\cdot u^{2}\\cdot x^{3}\\cdot u=180x^{1+2+3}u^{1+2+1+2+1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 180x^{1+2+3}u^{1+2+1+2+1}=180x^{6}u^{7}', 'e-steps': [
                        {'type': 'e-step', 'heading': '\\displaystyle 180x^{1+2+3}=180x^{6}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+3=6'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 180x^{1+2+3}=180x^{6}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle u^{1+2+1+2+1}=u^{7}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+1+2+1=7'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle u^{1+2+1+2+1}=u^{7}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Result}', 'info': '\\displaystyle 5x\\cdot3u\\cdot3\\cdot2\\cdot x^{2}\\cdot u^{2}\\cdot\\left(3x^{2}+2x+3\\right)\\cdot\\left(x+2\\right)\\cdot2u\\cdot u^{2}\\cdot x^{3}\\cdot\\left(x+1\\right)\\cdot u=180x^{6}u^{7}\\left(3x^{2}+2x+3\\right)\\left(x+2\\right)\\left(x+1\\right)'}], 'finalResult': '180x^{6}u^{7}\\left(3x^{2}+2x+3\\right)\\left(x+2\\right)\\left(x+1\\right)'},
            },
            {
                'expression': '4u*5* v^{2}* x*(u+v)*2*(5x^{2}+3x^{2}+2x+1)*5x^{2}*3u^{2}* v',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 4u\\cdot5\\cdot v^{2}\\cdot x\\cdot2\\cdot5x^{2}\\cdot3u^{2}\\cdot v=600u^{1+2}v^{2+1}x^{1+2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 600u^{1+2}v^{2+1}x^{1+2}=600u^{3}v^{3}x^{3}', 'e-steps': [
                        {'type': 'e-step', 'heading': '\\displaystyle 600u^{1+2}=600u^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 600u^{1+2}=600u^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle v^{2+1}=v^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle v^{2+1}=v^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle x^{1+2}=x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+2}=x^{3}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Result}', 'info': '\\displaystyle 4u\\cdot5\\cdot v^{2}\\cdot x\\cdot\\left(u+v\\right)\\cdot2\\cdot\\left(5x^{2}+3x^{2}+2x+1\\right)\\cdot5x^{2}\\cdot3u^{2}\\cdot v=600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(5x^{2}+3x^{2}+2x+1\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle 5x^{2}+3x^{2}+2x+1=8x^{2}+2x+1', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 5x^{2}+3x^{2}=8x^{2}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(5x^{2}+3x^{2}+2x+1\\right)=600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(8x^{2}+2x+1\\right)'}], 'finalResult': '600u^{3}v^{3}x^{3}\\left(u+v\\right)\\left(8x^{2}+2x+1\\right)'},
            },
            {
                'expression': '2*frac{x+y}{a+b}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle 2\\cdot\\frac{x+y}{a+b}=\\frac{2\\cdot\\left(x+y\\right)}{1\\cdot\\left(a+b\\right)}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{2\\cdot\\left(x+y\\right)}{1\\cdot\\left(a+b\\right)}=\\frac{2x+2y}{a+b}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 2\\cdot\\left(x+y\\right)=2\\cdot x+2\\cdot y'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot x=2x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot y=2y'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{2\\cdot\\left(x+y\\right)}{1\\cdot\\left(a+b\\right)}=\\frac{2x+2y}{1\\cdot\\left(a+b\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 1\\cdot\\left(a+b\\right)=1\\cdot a+1\\cdot b'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot a=1a'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot b=1b'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 1a+1b=a+b'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{2x+2y}{1\\cdot\\left(a+b\\right)}=\\frac{2x+2y}{a+b}'}]}], 'finalResult': '\\frac{2x+2y}{a+b}'},
            },
            {
                'expression': 'frac{1}{2}*frac{x+y}{a+b}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle \\frac{1}{2}\\cdot\\frac{x+y}{a+b}=\\frac{1\\cdot\\left(x+y\\right)}{2\\cdot\\left(a+b\\right)}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{1\\cdot\\left(x+y\\right)}{2\\cdot\\left(a+b\\right)}=\\frac{x+y}{2a+2b}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 1\\cdot\\left(x+y\\right)=1\\cdot x+1\\cdot y'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot x=1x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 1\\cdot y=1y'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 1x+1y=x+y'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{1\\cdot\\left(x+y\\right)}{2\\cdot\\left(a+b\\right)}=\\frac{x+y}{2\\cdot\\left(a+b\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 2\\cdot\\left(a+b\\right)=2\\cdot a+2\\cdot b'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot a=2a'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot b=2b'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{x+y}{2\\cdot\\left(a+b\\right)}=\\frac{x+y}{2a+2b}'}]}], 'finalResult': '\\frac{x+y}{2a+2b}'},
            },
            {
                'expression': '2x*3x*5u^{2}*u*sqrt{5x^{2}+3x^{2}+2+3}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2x\\cdot3x\\cdot5u^{2}\\cdot u\\cdot\\sqrt{5x^{2}+3x^{2}+2+3}=30x^{1+1}u^{2+1}\\sqrt{5x^{2}+3x^{2}+2+3}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 30x^{1+1}=30x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 30x^{1+1}=30x^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle u^{2+1}=u^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle u^{2+1}=u^{3}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{5x^{2}+3x^{2}+2+3}=\\sqrt{8x^{2}+5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 5x^{2}+3x^{2}=8x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{5x^{2}+3x^{2}+2+3}=\\sqrt{8x^{2}+5}'}]}], 'finalResult': '30x^{2}u^{3}\\sqrt{8x^{2}+5}'},
            },
            {
                'expression': '2x*3x*5u^{2}*u*sqrt{5x^{2}+3x^{2}+2+3}*3t*t',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2x\\cdot3x\\cdot5u^{2}\\cdot u\\cdot\\sqrt{5x^{2}+3x^{2}+2+3}\\cdot3t\\cdot t=90x^{1+1}u^{2+1}t^{1+1}\\sqrt{5x^{2}+3x^{2}+2+3}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 90x^{1+1}=90x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 90x^{1+1}=90x^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle u^{2+1}=u^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle u^{2+1}=u^{3}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle t^{1+1}=t^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle t^{1+1}=t^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{5x^{2}+3x^{2}+2+3}=\\sqrt{8x^{2}+5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 5x^{2}+3x^{2}=8x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{5x^{2}+3x^{2}+2+3}=\\sqrt{8x^{2}+5}'}]}], 'finalResult': '90x^{2}u^{3}t^{2}\\sqrt{8x^{2}+5}'},
            },
            {
                'expression': '(x+2)*(x+3)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+2\\right)\\left(x+3\\right)=x\\cdot x+x\\cdot3+2\\cdot x+2\\cdot3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot3=3x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot x=2x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot3=6'},
                    {'type': 'e-step', 'heading': '\\displaystyle x^{1+1}=x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 3x+2x+6=5x+6', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x+6=5x+6'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot3+2\\cdot x+2\\cdot3=x^{2}+5x+6'}], 'finalResult': 'x^{2}+5x+6'},
            },
            {
                'expression': '(x+y)*(u+v)*(s+t)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(x+y\\right)\\left(u+v\\right)=xu+xv+yu+yv', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+y\\right)\\left(u+v\\right)=x\\cdot u+x\\cdot v+y\\cdot u+y\\cdot v'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot u=xu'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot v=xv'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle y\\cdot u=yu'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle y\\cdot v=yv'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot u+x\\cdot v+y\\cdot u+y\\cdot v=xu+xv+yu+yv'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(xu+xv+yu+yv\\right)\\left(s+t\\right)=sxu+txu+sxv+txv+syu+tyu+syv+tyv', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle \\left(xu+xv+yu+yv\\right)\\left(s+t\\right)=xu\\cdot s+xu\\cdot t+xv\\cdot s+xv\\cdot t+yu\\cdot s+yu\\cdot t+yv\\cdot s+yv\\cdot t'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle xu\\cdot s=sxu'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle xu\\cdot t=txu'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle xv\\cdot s=sxv'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle xv\\cdot t=txv'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle yu\\cdot s=syu'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle yu\\cdot t=tyu'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle yv\\cdot s=syv'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle yv\\cdot t=tyv'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle xu\\cdot s+xu\\cdot t+xv\\cdot s+xv\\cdot t+yu\\cdot s+yu\\cdot t+yv\\cdot s+yv\\cdot t=sxu+txu+sxv+txv+syu+tyu+syv+tyv'}]}], 'finalResult': 'sxu+txu+sxv+txv+syu+tyu+syv+tyv'},
            },
            {
                'expression': '(2x-2)*(-x-3)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(2x-2\\right)\\left(-x-3\\right)=2x\\cdot-x+2x\\cdot-3+-2\\cdot-x+-2\\cdot-3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2x\\cdot-x=-2x^{1+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2x\\cdot-3=-6x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot-x=-2x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot-3=-6'},
                    {'type': 'e-step', 'heading': '\\displaystyle -2x^{1+1}=-2x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle -2x^{1+1}=-2x^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle -6x+2x+6=-4x+6', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle -6x+2x+6=-4x+6'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 2x\\cdot-x+2x\\cdot-3+-2\\cdot-x+-2\\cdot-3=-2x^{2}-4x+6'}], 'finalResult': '-2x^{2}-4x+6'},
            },
            {
                'expression': '(3x^{2}+2xy+4)*(9x^{3}+2x^{2}+y+1)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle \\left(3x^{2}+2xy+4\\right)\\left(9x^{3}+2x^{2}+y+1\\right)=3x^{2}\\cdot9x^{3}+3x^{2}\\cdot2x^{2}+3x^{2}\\cdot y+3x^{2}\\cdot1+2xy\\cdot9x^{3}+2xy\\cdot2x^{2}+2xy\\cdot y+2xy\\cdot1+4\\cdot9x^{3}+4\\cdot2x^{2}+4\\cdot y+4\\cdot1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot9x^{3}=27x^{2+3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot2x^{2}=6x^{2+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot y=3x^{2}y'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot1=3x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2xy\\cdot9x^{3}=18x^{3+1}y'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2xy\\cdot2x^{2}=4x^{2+1}y'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2xy\\cdot y=2y^{1+1}x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2xy\\cdot1=2xy'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4\\cdot9x^{3}=36x^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4\\cdot2x^{2}=8x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4\\cdot y=4y'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4\\cdot1=4'},
                    {'type': 'e-step', 'heading': '\\displaystyle 18x^{3+1}=18x^{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+1=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 18x^{3+1}=18x^{4}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 4x^{2+1}=4x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 4x^{2+1}=4x^{3}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 2y^{1+1}=2y^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2y^{1+1}=2y^{2}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 27x^{2+3}+6x^{2+2}+3x^{2}y+3x^{2}+18x^{4}y+4x^{3}y+2y^{2}x+2xy+36x^{3}+8x^{2}+4y+4=27x^{2+3}+6x^{2+2}+3x^{2}+36x^{3}+8x^{2}+3x^{2}y+18x^{4}y+4x^{3}y+2y^{2}x+2xy+4y+4'},
                    {'type': 'e-step', 'heading': '\\displaystyle 27x^{2+3}=27x^{5}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 27x^{2+3}=27x^{5}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 6x^{2+2}=6x^{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 6x^{2+2}=6x^{4}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 27x^{2+3}+6x^{2+2}+3x^{2}+36x^{3}+8x^{2}=27x^{5}+6x^{4}+3x^{2}+36x^{3}+8x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 27x^{5}+6x^{4}+3x^{2}+36x^{3}+8x^{2}=27x^{5}+6x^{4}+3x^{2}+8x^{2}+36x^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 27x^{5}+6x^{4}+3x^{2}+8x^{2}+36x^{3}=27x^{5}+6x^{4}+11x^{2}+36x^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 3x^{2}\\cdot9x^{3}+3x^{2}\\cdot2x^{2}+3x^{2}\\cdot y+3x^{2}\\cdot1+2xy\\cdot9x^{3}+2xy\\cdot2x^{2}+2xy\\cdot y+2xy\\cdot1+4\\cdot9x^{3}+4\\cdot2x^{2}+4\\cdot y+4\\cdot1=27x^{5}+6x^{4}+11x^{2}+36x^{3}+3x^{2}y+18x^{4}y+4x^{3}y+2y^{2}x+2xy+4y+4'}], 'finalResult': '27x^{5}+6x^{4}+11x^{2}+36x^{3}+3x^{2}y+18x^{4}y+4x^{3}y+2y^{2}x+2xy+4y+4'},
            },
            {
                'expression': '(2y-y^{2})*(2-2y)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(2y-y^{2}\\right)\\left(2-2y\\right)=2y\\cdot2+2y\\cdot-2y+-y^{2}\\cdot2+-y^{2}\\cdot-2y'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2y\\cdot2=4y'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2y\\cdot-2y=-4y^{1+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle y^{2}\\cdot2=2y^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle y^{2}\\cdot-2y=-2y^{2+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 4y-4y^{1+1}-2y^{2}+2y^{2+1}=-4y^{1+1}-2y^{2}+2y^{2+1}+4y'},
                    {'type': 'e-step', 'heading': '\\displaystyle -4y^{1+1}=-4y^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle -4y^{1+1}=-4y^{2}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 2y^{2+1}=2y^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2y^{2+1}=2y^{3}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle -4y^{1+1}-2y^{2}+2y^{2+1}=-4y^{2}-2y^{2}+2y^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle -4y^{2}-2y^{2}+2y^{3}=-6y^{2}+2y^{3}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 2y\\cdot2+2y\\cdot-2y+-y^{2}\\cdot2+-y^{2}\\cdot-2y=-6y^{2}+2y^{3}+4y'}], 'finalResult': '-6y^{2}+2y^{3}+4y'},
            },
            {
                'expression': '2x^{2}*x*t*(2x^{2}+3x^{2}+x+2)*(x^{2}+1)*3t^{2}',
                'keyword': 'expand',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 2x^{2}\\cdot x\\cdot t\\cdot3t^{2}=6x^{2+1}t^{1+2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 6x^{2+1}t^{1+2}=6x^{3}t^{3}', 'e-steps': [
                        {'type': 'e-step', 'heading': '\\displaystyle 6x^{2+1}=6x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 6x^{2+1}=6x^{3}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle t^{1+2}=t^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle t^{1+2}=t^{3}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Result}', 'info': '\\displaystyle 2x^{2}\\cdot x\\cdot t\\cdot\\left(2x^{2}+3x^{2}+x+2\\right)\\cdot\\left(x^{2}+1\\right)\\cdot3t^{2}=6x^{3}t^{3}\\left(2x^{2}+3x^{2}+x+2\\right)\\left(x^{2}+1\\right)'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\left(2x^{2}+3x^{2}+x+2\\right)\\left(x^{2}+1\\right)=5x^{4}+7x^{2}+x^{3}+x+2', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle \\left(2x^{2}+3x^{2}+x+2\\right)\\left(x^{2}+1\\right)=2x^{2}\\cdot x^{2}+2x^{2}\\cdot1+3x^{2}\\cdot x^{2}+3x^{2}\\cdot1+x\\cdot x^{2}+x\\cdot1+2\\cdot x^{2}+2\\cdot1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2x^{2}\\cdot x^{2}=2x^{2+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2x^{2}\\cdot1=2x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot x^{2}=3x^{2+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x^{2}\\cdot1=3x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x^{2}=x^{1+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot1=x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot x^{2}=2x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 2x^{2+2}+2x^{2}+3x^{2+2}+3x^{2}+x^{1+2}+x+2x^{2}+2=2x^{2+2}+2x^{2}+3x^{2+2}+3x^{2}+x^{1+2}+2x^{2}+x+2'},
                        {'type': 'e-step', 'heading': '\\displaystyle 2x^{2+2}=2x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2x^{2+2}=2x^{4}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 3x^{2+2}=3x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3x^{2+2}=3x^{4}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle x^{1+2}=x^{3}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+2}=x^{3}'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle 2x^{2+2}+2x^{2}+3x^{2+2}+3x^{2}+x^{1+2}+2x^{2}=2x^{4}+2x^{2}+3x^{4}+3x^{2}+x^{3}+2x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Exponentials}', 'info': '\\displaystyle 2x^{4}+2x^{2}+3x^{4}+3x^{2}+x^{3}+2x^{2}=2x^{4}+3x^{4}+2x^{2}+3x^{2}+2x^{2}+x^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 2x^{4}+3x^{4}+2x^{2}+3x^{2}+2x^{2}+x^{3}=5x^{4}+7x^{2}+x^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 2x^{2}\\cdot x^{2}+2x^{2}\\cdot1+3x^{2}\\cdot x^{2}+3x^{2}\\cdot1+x\\cdot x^{2}+x\\cdot1+2\\cdot x^{2}+2\\cdot1=5x^{4}+7x^{2}+x^{3}+x+2'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 6x^{3}t^{3}\\cdot\\left(5x^{4}+7x^{2}+x^{3}+x+2\\right)=30x^{7}t^{3}+42x^{5}t^{3}+6x^{6}t^{3}+6x^{4}t^{3}+12x^{3}t^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 6x^{3}t^{3}\\cdot\\left(5x^{4}+7x^{2}+x^{3}+x+2\\right)=6x^{3}t^{3}\\cdot5x^{4}+6x^{3}t^{3}\\cdot7x^{2}+6x^{3}t^{3}\\cdot x^{3}+6x^{3}t^{3}\\cdot x+6x^{3}t^{3}\\cdot2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 6x^{3}t^{3}\\cdot5x^{4}=30x^{4+3}t^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 6x^{3}t^{3}\\cdot7x^{2}=42x^{2+3}t^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 6x^{3}t^{3}\\cdot x^{3}=6x^{3+3}t^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 6x^{3}t^{3}\\cdot x=6x^{1+3}t^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 6x^{3}t^{3}\\cdot2=12x^{3}t^{3}'},
                        {'type': 'e-step', 'heading': '\\displaystyle 30x^{4+3}=30x^{7}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4+3=7'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 30x^{4+3}=30x^{7}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 42x^{2+3}=42x^{5}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+3=5'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 42x^{2+3}=42x^{5}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 6x^{3+3}=6x^{6}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3+3=6'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 6x^{3+3}=6x^{6}'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 6x^{1+3}=6x^{4}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+3=4'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 6x^{1+3}=6x^{4}'}]}]}], 'finalResult': '30x^{7}t^{3}+42x^{5}t^{3}+6x^{6}t^{3}+6x^{4}t^{3}+12x^{3}t^{3}'},
            },
            {
                'expression': '(x+2)*(x^{2}+2x+5*(x+2))',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle \\left(x+2\\right)\\left(x^{2}+2x+5\\cdot\\left(x+2\\right)\\right)=x\\cdot x^{2}+x\\cdot2x+x\\cdot5\\cdot\\left(x+2\\right)+2\\cdot x^{2}+2\\cdot2x+2\\cdot5\\cdot\\left(x+2\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x^{2}=x^{1+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot2x=2x^{1+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle x\\cdot5=5x'},
                    {'type': 'e-step', 'heading': '\\displaystyle 5x\\cdot\\left(x+2\\right)=5x^{2}+10x', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 5x\\cdot\\left(x+2\\right)=5x\\cdot x+5x\\cdot2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot x=5x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5x\\cdot2=10x'},
                        {'type': 'e-step', 'heading': '\\displaystyle 5x^{1+1}=5x^{2}', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 5x^{1+1}=5x^{2}'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot x^{2}=2x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot2x=4x'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply Terms (left to right)}', 'info': '\\displaystyle 2\\cdot5=10'},
                    {'type': 'e-step', 'heading': '\\displaystyle 10\\cdot\\left(x+2\\right)=10x+20', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle 10\\cdot\\left(x+2\\right)=10\\cdot x+10\\cdot2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 10\\cdot x=10x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 10\\cdot2=20'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle x^{1+2}+2x^{1+1}+5x^{2}+10x+2x^{2}+4x+10x+20=x^{1+2}+2x^{1+1}+5x^{2}+2x^{2}+10x+4x+10x+20'},
                    {'type': 'e-step', 'heading': '\\displaystyle x^{1+2}=x^{3}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+2}=x^{3}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 2x^{1+1}=2x^{2}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2x^{1+1}=2x^{2}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle x^{1+2}+2x^{1+1}+5x^{2}+2x^{2}=x^{3}+2x^{2}+5x^{2}+2x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{3}+2x^{2}+5x^{2}+2x^{2}=x^{3}+9x^{2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 10x+4x+10x+20=24x+20', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 10x+4x+10x+20=24x+20'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x^{2}+x\\cdot2x+x\\cdot5\\cdot\\left(x+2\\right)+2\\cdot x^{2}+2\\cdot2x+2\\cdot5\\cdot\\left(x+2\\right)=x^{3}+9x^{2}+24x+20'}], 'finalResult': 'x^{3}+9x^{2}+24x+20'},
            },
            {
                'expression': 'x^{2}*x*t*x*e^{2x+3x}*t^{2}*sqrt{10x-2x}*t',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x^{2}\\cdot x\\cdot t\\cdot x\\cdot e^{2x+3x}\\cdot t^{2}\\cdot\\sqrt{10x-2x}\\cdot t=x^{2+1+1}t^{1+2+1}e^{2x+3x}\\sqrt{10x-2x}'},
                    {'type': 'e-step', 'heading': '\\displaystyle x^{2+1+1}=x^{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1+1=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{2+1+1}=x^{4}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle t^{1+2+1}=t^{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+1=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle t^{1+2+1}=t^{4}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle e^{2x+3x}=e^{5x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+3x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{2x+3x}=e^{5x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{10x-2x}=\\sqrt{8x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 10x-2x=8x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{10x-2x}=\\sqrt{8x}'}]}], 'finalResult': 'x^{4}t^{4}e^{5x}\\sqrt{8x}'},
            },
            {
                'expression': '(e^{2x+x}+sqrt{4x^{2}+2x^{2}+1})*(x^{2}+2)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(e^{2x+x}+\\sqrt{4x^{2}+2x^{2}+1}\\right)\\left(x^{2}+2\\right)=e^{2x+x}\\cdot x^{2}+e^{2x+x}\\cdot2+\\sqrt{4x^{2}+2x^{2}+1}\\cdot x^{2}+\\sqrt{4x^{2}+2x^{2}+1}\\cdot2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle e^{2x+x}\\cdot x^{2}=e^{2x+x}x^{2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle e^{2x+x}\\cdot2=2e^{2x+x}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle \\sqrt{4x^{2}+2x^{2}+1}\\cdot x^{2}=x^{2}\\sqrt{4x^{2}+2x^{2}+1}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle \\sqrt{4x^{2}+2x^{2}+1}\\cdot2=2\\sqrt{4x^{2}+2x^{2}+1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle e^{2x+x}=e^{3x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+x=3x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{2x+x}=e^{3x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{4x^{2}+2x^{2}+1}=\\sqrt{6x^{2}+1}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 4x^{2}+2x^{2}=6x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{4x^{2}+2x^{2}+1}=\\sqrt{6x^{2}+1}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle e^{3x}x^{2}+2e^{2x+x}+x^{2}\\sqrt{6x^{2}+1}+2\\sqrt{4x^{2}+2x^{2}+1}=2e^{2x+x}+2\\sqrt{4x^{2}+2x^{2}+1}+e^{3x}x^{2}+x^{2}\\sqrt{6x^{2}+1}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 2e^{2x+x}=2e^{3x}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+x=3x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2e^{2x+x}=2e^{3x}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 2\\sqrt{4x^{2}+2x^{2}+1}=2\\sqrt{6x^{2}+1}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 4x^{2}+2x^{2}=6x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle 2\\sqrt{4x^{2}+2x^{2}+1}=2\\sqrt{6x^{2}+1}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle e^{2x+x}\\cdot x^{2}+e^{2x+x}\\cdot2+\\sqrt{4x^{2}+2x^{2}+1}\\cdot x^{2}+\\sqrt{4x^{2}+2x^{2}+1}\\cdot2=2e^{3x}+2\\sqrt{6x^{2}+1}+e^{3x}x^{2}+x^{2}\\sqrt{6x^{2}+1}'}], 'finalResult': '2e^{3x}+2\\sqrt{6x^{2}+1}+e^{3x}x^{2}+x^{2}\\sqrt{6x^{2}+1}'},
            },
            {
                'expression': '(frac{x+2}{x+3}+frac{x+4}{x+5})*(frac{x+6}{x+7}+frac{x+8}{x+9})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(\\frac{x+2}{x+3}+\\frac{x+4}{x+5}\\right)\\left(\\frac{x+6}{x+7}+\\frac{x+8}{x+9}\\right)=\\frac{x+2}{x+3}\\cdot\\frac{x+6}{x+7}+\\frac{x+2}{x+3}\\cdot\\frac{x+8}{x+9}+\\frac{x+4}{x+5}\\cdot\\frac{x+6}{x+7}+\\frac{x+4}{x+5}\\cdot\\frac{x+8}{x+9}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle \\frac{x+2}{x+3}\\cdot\\frac{x+6}{x+7}=\\frac{\\left(x+2\\right)\\cdot\\left(x+6\\right)}{\\left(x+3\\right)\\cdot\\left(x+7\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle \\frac{x+2}{x+3}\\cdot\\frac{x+8}{x+9}=\\frac{\\left(x+2\\right)\\cdot\\left(x+8\\right)}{\\left(x+3\\right)\\cdot\\left(x+9\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle \\frac{x+4}{x+5}\\cdot\\frac{x+6}{x+7}=\\frac{\\left(x+4\\right)\\cdot\\left(x+6\\right)}{\\left(x+5\\right)\\cdot\\left(x+7\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle \\frac{x+4}{x+5}\\cdot\\frac{x+8}{x+9}=\\frac{\\left(x+4\\right)\\cdot\\left(x+8\\right)}{\\left(x+5\\right)\\cdot\\left(x+9\\right)}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{\\left(x+2\\right)\\cdot\\left(x+6\\right)}{\\left(x+3\\right)\\cdot\\left(x+7\\right)}=\\frac{x^{2}+8x+12}{x^{2}+10x+21}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+2\\right)\\left(x+6\\right)=x\\cdot x+x\\cdot6+2\\cdot x+2\\cdot6'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot6=6x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot x=2x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot6=12'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 6x+2x+12=8x+12'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot6+2\\cdot x+2\\cdot6=x^{2}+8x+12'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{\\left(x+2\\right)\\cdot\\left(x+6\\right)}{\\left(x+3\\right)\\cdot\\left(x+7\\right)}=\\frac{x^{2}+8x+12}{\\left(x+3\\right)\\cdot\\left(x+7\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+3\\right)\\left(x+7\\right)=x\\cdot x+x\\cdot7+3\\cdot x+3\\cdot7'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot7=7x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot x=3x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot7=21'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 7x+3x+21=10x+21'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot7+3\\cdot x+3\\cdot7=x^{2}+10x+21'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{x^{2}+8x+12}{\\left(x+3\\right)\\cdot\\left(x+7\\right)}=\\frac{x^{2}+8x+12}{x^{2}+10x+21}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{\\left(x+2\\right)\\cdot\\left(x+8\\right)}{\\left(x+3\\right)\\cdot\\left(x+9\\right)}=\\frac{x^{2}+10x+16}{x^{2}+12x+27}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+2\\right)\\left(x+8\\right)=x\\cdot x+x\\cdot8+2\\cdot x+2\\cdot8'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot8=8x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot x=2x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot8=16'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 8x+2x+16=10x+16'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot8+2\\cdot x+2\\cdot8=x^{2}+10x+16'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{\\left(x+2\\right)\\cdot\\left(x+8\\right)}{\\left(x+3\\right)\\cdot\\left(x+9\\right)}=\\frac{x^{2}+10x+16}{\\left(x+3\\right)\\cdot\\left(x+9\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+3\\right)\\left(x+9\\right)=x\\cdot x+x\\cdot9+3\\cdot x+3\\cdot9'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot9=9x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot x=3x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot9=27'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 9x+3x+27=12x+27'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot9+3\\cdot x+3\\cdot9=x^{2}+12x+27'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{x^{2}+10x+16}{\\left(x+3\\right)\\cdot\\left(x+9\\right)}=\\frac{x^{2}+10x+16}{x^{2}+12x+27}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{\\left(x+4\\right)\\cdot\\left(x+6\\right)}{\\left(x+5\\right)\\cdot\\left(x+7\\right)}=\\frac{x^{2}+10x+24}{x^{2}+12x+35}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+4\\right)\\left(x+6\\right)=x\\cdot x+x\\cdot6+4\\cdot x+4\\cdot6'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot6=6x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4\\cdot x=4x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4\\cdot6=24'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 6x+4x+24=10x+24'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot6+4\\cdot x+4\\cdot6=x^{2}+10x+24'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{\\left(x+4\\right)\\cdot\\left(x+6\\right)}{\\left(x+5\\right)\\cdot\\left(x+7\\right)}=\\frac{x^{2}+10x+24}{\\left(x+5\\right)\\cdot\\left(x+7\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+5\\right)\\left(x+7\\right)=x\\cdot x+x\\cdot7+5\\cdot x+5\\cdot7'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot7=7x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot7=35'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 7x+5x+35=12x+35'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot7+5\\cdot x+5\\cdot7=x^{2}+12x+35'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{x^{2}+10x+24}{\\left(x+5\\right)\\cdot\\left(x+7\\right)}=\\frac{x^{2}+10x+24}{x^{2}+12x+35}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{\\left(x+4\\right)\\cdot\\left(x+8\\right)}{\\left(x+5\\right)\\cdot\\left(x+9\\right)}=\\frac{x^{2}+12x+32}{x^{2}+14x+45}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+4\\right)\\left(x+8\\right)=x\\cdot x+x\\cdot8+4\\cdot x+4\\cdot8'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot8=8x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4\\cdot x=4x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 4\\cdot8=32'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 8x+4x+32=12x+32'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot8+4\\cdot x+4\\cdot8=x^{2}+12x+32'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{\\left(x+4\\right)\\cdot\\left(x+8\\right)}{\\left(x+5\\right)\\cdot\\left(x+9\\right)}=\\frac{x^{2}+12x+32}{\\left(x+5\\right)\\cdot\\left(x+9\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply FOIL Method}: \\\\ (a+b)(c+d)=ac+ad+bc+bd', 'info': '\\displaystyle \\left(x+5\\right)\\left(x+9\\right)=x\\cdot x+x\\cdot9+5\\cdot x+5\\cdot9'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot x=x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x\\cdot9=9x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot9=45'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{1+1}=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 9x+5x+45=14x+45'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x\\cdot x+x\\cdot9+5\\cdot x+5\\cdot9=x^{2}+14x+45'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{x^{2}+12x+32}{\\left(x+5\\right)\\cdot\\left(x+9\\right)}=\\frac{x^{2}+12x+32}{x^{2}+14x+45}'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{x+2}{x+3}\\cdot\\frac{x+6}{x+7}+\\frac{x+2}{x+3}\\cdot\\frac{x+8}{x+9}+\\frac{x+4}{x+5}\\cdot\\frac{x+6}{x+7}+\\frac{x+4}{x+5}\\cdot\\frac{x+8}{x+9}=\\frac{x^{2}+8x+12}{x^{2}+10x+21}+\\frac{x^{2}+10x+16}{x^{2}+12x+27}+\\frac{x^{2}+10x+24}{x^{2}+12x+35}+\\frac{x^{2}+12x+32}{x^{2}+14x+45}'}], 'finalResult': '\\frac{x^{2}+8x+12}{x^{2}+10x+21}+\\frac{x^{2}+10x+16}{x^{2}+12x+27}+\\frac{x^{2}+10x+24}{x^{2}+12x+35}+\\frac{x^{2}+12x+32}{x^{2}+14x+45}'},
            },
            {
                'expression': 'frac{x^{2}+2x+2}{x^{2}+3x+5}*frac{x+1}{x+2}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Convert Numbers To Fractions and Multiply Left To Right}', 'info': '\\displaystyle \\frac{x^{2}+2x+2}{x^{2}+3x+5}\\cdot\\frac{x+1}{x+2}=\\frac{\\left(x^{2}+2x+2\\right)\\cdot\\left(x+1\\right)}{\\left(x^{2}+3x+5\\right)\\cdot\\left(x+2\\right)}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{\\left(x^{2}+2x+2\\right)\\cdot\\left(x+1\\right)}{\\left(x^{2}+3x+5\\right)\\cdot\\left(x+2\\right)}=\\frac{x^{3}+3x^{2}+4x+2}{x^{3}+5x^{2}+11x+10}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle \\left(x^{2}+2x+2\\right)\\left(x+1\\right)=x^{2}\\cdot x+x^{2}\\cdot1+2x\\cdot x+2x\\cdot1+2\\cdot x+2\\cdot1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x^{2}\\cdot x=x^{2+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x^{2}\\cdot1=x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2x\\cdot x=2x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2x\\cdot1=2x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot x=2x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{2+1}=x^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 2x^{1+1}=2x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle x^{2+1}+x^{2}+2x^{1+1}=x^{3}+x^{2}+2x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{3}+x^{2}+2x^{2}=x^{3}+3x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2x+2x+2=4x+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x^{2}\\cdot x+x^{2}\\cdot1+2x\\cdot x+2x\\cdot1+2\\cdot x+2\\cdot1=x^{3}+3x^{2}+4x+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{\\left(x^{2}+2x+2\\right)\\cdot\\left(x+1\\right)}{\\left(x^{2}+3x+5\\right)\\cdot\\left(x+2\\right)}=\\frac{x^{3}+3x^{2}+4x+2}{\\left(x^{2}+3x+5\\right)\\cdot\\left(x+2\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Distribute Parentheses}', 'info': '\\displaystyle \\left(x^{2}+3x+5\\right)\\left(x+2\\right)=x^{2}\\cdot x+x^{2}\\cdot2+3x\\cdot x+3x\\cdot2+5\\cdot x+5\\cdot2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x^{2}\\cdot x=x^{2+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle x^{2}\\cdot2=2x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x\\cdot x=3x^{1+1}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3x\\cdot2=6x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 5\\cdot2=10'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+1=3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle x^{2+1}=x^{3}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+1=2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 3x^{1+1}=3x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Exponentials}', 'info': '\\displaystyle x^{2+1}+2x^{2}+3x^{1+1}=x^{3}+2x^{2}+3x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle x^{3}+2x^{2}+3x^{2}=x^{3}+5x^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 6x+5x+10=11x+10'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle x^{2}\\cdot x+x^{2}\\cdot2+3x\\cdot x+3x\\cdot2+5\\cdot x+5\\cdot2=x^{3}+5x^{2}+11x+10'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{x^{3}+3x^{2}+4x+2}{\\left(x^{2}+3x+5\\right)\\cdot\\left(x+2\\right)}=\\frac{x^{3}+3x^{2}+4x+2}{x^{3}+5x^{2}+11x+10}'}]}], 'finalResult': '\\frac{x^{3}+3x^{2}+4x+2}{x^{3}+5x^{2}+11x+10}'},
            },
            # {
            #     'expression': '',
            #     'keyword': None,
            #     'expected_val': {},
            # },
            # {
            #     'expression': '',
            #     'keyword': None,
            #     'expected_val': {},
            # },
            # {
            #     'expression': '',
            #     'keyword': None,
            #     'expected_val': {},
            # },
            # {
            #     'expression': '',
            #     'keyword': None,
            #     'expected_val': {},
            # },
            {
                'expression': '1',
                'keyword': None,
                'expected_val': {'steps': [], 'finalResult': '1'},
            },
            {
                'expression': 'a',
                'keyword': None,
                'expected_val': {'steps': [], 'finalResult': 'a'}
            }

        ]

        for item in expressionsAndExpectedVal:
            if item['expression'] == '2+3+sin(2pi)+cos(2pi)+sin(frac{pi}{4})+csc(frac{pi}{4})+tan(frac{pi}{3})+ln(e)+5+9':
                print(f"Expected val: {simplifyExpression(Expression(item['expression']), item['keyword'])}")
            # try:
            expression = Expression(item['expression'])
            # print(expression)
            expectedVal = item['expected_val']
            keyword = item['keyword']
            returnedVal = simplifyExpression(expression, keyword=keyword)
            self.assertEqual(expectedVal, returnedVal,
                             f"Failed: {expression}\nLatex: {latexify(expression)}\nKeyword: {keyword}")

            # except Exception as error:
            #     print(f"Error: {error}\nOn: {item['expression']}\nLatex: {latexify(item['expression'])}\nKeyword: {item['keyword']}\n")


def test():
    pass


# test()


if __name__ == '__main__':
    unittest.main()