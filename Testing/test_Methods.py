import sys
sys.path.append(r"C:\Users\jahei\OneDrive\Documents\Flask-Projects\Flask\Personal-Projects\Computer Algebra") # Add path where project is located to allow for import of application
import os
import unittest
from Methods import *
# from test import *


# python -m unittest test_Methods.py

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
                'expression': '1+pi+5\sin(ab+c)-2\sin(ab+c)+3pi+3',
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
                'expression': 'sqrt{(5x+3x+1)^{2}}',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply radical rule:}\\ \\sqrt[n]{a^n}=a', 'info': '\\displaystyle \\sqrt{\\left(5x+3x+1\\right)^{2}}=\\left(5x+3x+1\\right)'},
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
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{5x+3x+2x}{3x-2x}=\\frac{10x}{x}'},
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
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{8x+2x}{2x+3x}=\\frac{10x}{5x}'},
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
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}}{5x+3x+2x}=\\frac{27x^{2}+5x}{10x}'}], 'finalResult': '\\frac{27x^{2}+5x}{10x}'},
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
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{10x^{2}+12x^{2}+5x+7x^{2}-2x^{2}}{5x+3x+2x}=\\frac{27x^{2}+5x}{10x}'},
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
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{5x+3x+e^{7x+3x+2}+5}{e^{2\\sqrt{x}+3\\sqrt{3x-2x}}+\\sqrt{25x-12x+2}}=\\frac{e^{10x+2}+8x+5}{e^{5\\sqrt{x}}+\\sqrt{13x+2}}'}], 'finalResult': '\\frac{e^{10x+2}+8x+5}{e^{5\\sqrt{x}}+\\sqrt{13x+2}}'}
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
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{5x^{2}+2x^{2}+1+3}{1+\\sqrt{10x+3x+y}}=\\frac{7x^{2}+4}{\\sqrt{13x+y}+1}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\frac{15x+21x}{e^{3x+2x}+\\sqrt{7x-2x}}=\\frac{36x}{e^{5x}+\\sqrt{5x}}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 15x+21x=36x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{15x+21x}{e^{3x+2x}+\\sqrt{7x-2x}}=\\frac{36x}{e^{3x+2x}+\\sqrt{7x-2x}}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 3x+2x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle e^{3x+2x}=e^{5x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 7x-2x=5x'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{7x-2x}=\\sqrt{5x}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{15x+21x}{e^{3x+2x}+\\sqrt{7x-2x}}=\\frac{36x}{e^{5x}+\\sqrt{5x}}'}]},
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
                'expression': '21x*3x^{2}* x^{4}*5x^{10}',
                'keyword': 'simplify',
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 21x\\cdot3x^{2}\\cdot x^{4}\\cdot5x^{10}=315x^{1+2+4+10}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 315x^{1+2+4+10}=315x^{17}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 1+2+4+10=17'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Exponent}', 'info': '\\displaystyle 315x^{1+2+4+10}=315x^{17}'}]}], 'finalResult': '315x^{17}'},
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
                'expression': 'frac{1}{2}',
                'keyword': None,
                'expected_val': {'steps': [], 'finalResult': '\\frac{1}{2}'},
            },
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
            # try:
            expression = Expression(item['expression'])
            expectedVal = item['expected_val']
            keyword = item['keyword']
            returnedVal = simplifyExpression(expression, keyword=keyword)
            self.assertEqual(expectedVal, returnedVal, f"Failed: {expression}\nLatex: {latexify(expression)}\nKeyword: {keyword}")
            # except Exception as error:
            #     print(f"Error: {error}\nOn: {item['expression']}\nLatex: {latexify(item['expression'])}\n")


def test():
    pass





# test()



if __name__ == '__main__':
    unittest.main()