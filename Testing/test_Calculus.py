import unittest
import sys

""" ADD PATH WHERE PROJECT IS LOCATED TO ALLOW FOR IMPORT OF APPLICATION """
sys.path.append(r"C:\Users\jahei\OneDrive\Documents\Flask-Projects\Flask\Personal-Projects\Computer Algebra")
from Methods import latexify
from Algebra import Expression
from Calculus import evaluateCalculusExpression


# RUN: python -m unittest test_Algebra.py


class MyTestCase(unittest.TestCase):
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

    def test_Limits(self):
        expressionsAndExpectedVal = [
            {
                'expression': 'lim_{x→2}(frac{x^{2}+23x+1}{x+2})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=2', 'info': '\\displaystyle \\frac{x^{2}+23x+1}{x+2}=\\frac{2^{2}+23\\cdot2+1}{2+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 23\\cdot2=46'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 2^{2}=4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 46+1=47'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 4+47'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4+47=51'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{2^{2}+23\\cdot2+1}{2+2}=\\frac{51}{2+2}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{51}{2+2}=\\frac{51}{4}'}], 'finalResult': '\\frac{51}{4}'},
            },
            {
                'expression': 'lim_{x→2}(frac{x^{2}+23x+1}{x+2})+lim_{x→3}(x^{3}+3x+2)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to2}\\left(\\frac{x^{2}+23x+1}{x+2}\\right)=\\frac{51}{4}', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=2', 'info': '\\displaystyle \\frac{x^{2}+23x+1}{x+2}=\\frac{2^{2}+23\\cdot2+1}{2+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 23\\cdot2=46'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 2^{2}=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 46+1=47'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 4+47'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4+47=51'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{2^{2}+23\\cdot2+1}{2+2}=\\frac{51}{2+2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2+2=4'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Denominator}', 'info': '\\displaystyle \\frac{51}{2+2}=\\frac{51}{4}'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to3}\\left(x^{3}+3x+2\\right)=38', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=3', 'info': '\\displaystyle x^{3}+3x+2=3^{3}+3\\cdot3+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot3=9'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3^{3}=27', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 3^{3}=27'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 9+2=11', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 9+2=11'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 27+11'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 27+11=38'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{51}{4}+38'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Adjust fractions based on their LCM of }4', 'info': '\\displaystyle \\frac{51}{4}+38=\\frac{51}{4}+\\frac{152}{4}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply The Fraction Rule:}\\ \\frac{a}{c}\\pm\\frac{b}{c}=\\frac{a \\pm b}{c}', 'info': '\\displaystyle \\frac{51}{4}+\\frac{152}{4}=\\frac{51+152}{4}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\frac{51+152}{4}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 51+152=203'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify Numerator}', 'info': '\\displaystyle \\frac{51+152}{4}=\\frac{203}{4}'}], 'finalResult': '\\frac{203}{4}'},
            },
            {
                'expression': 'lim_{x→3}(x^{3}+3x+2)+sqrt{23+2}+3*2',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to3}\\left(x^{3}+3x+2\\right)=38', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=3', 'info': '\\displaystyle x^{3}+3x+2=3^{3}+3\\cdot3+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot3=9'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3^{3}=27', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 3^{3}=27'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 9+2=11', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 9+2=11'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 27+11'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 27+11=38'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 38+\\sqrt{23+2}+3\\cdot2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot2=6'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 38+\\sqrt{23+2}+6=\\sqrt{23+2}+38+6'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{23+2}=5', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 23+2=25'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Simplify}', 'info': '\\displaystyle \\sqrt{23+2}=\\sqrt{25}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Radical}', 'info': '\\displaystyle \\sqrt{25}=5'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 38+6=44', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 38+6=44'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 5+44'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 5+44=49'}], 'finalResult': '49'},
            },
            {
                'expression': 'lim_{x→3}(x^{2}t+3xt^{2}+t+2x)+2t^{2}+3t+2',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to3}\\left(x^{2}t+3xt^{2}+t+2x\\right)=9t^{2}+10t+6', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=3', 'info': '\\displaystyle x^{2}t+3xt^{2}+t+2x=3^{2}t+3\\cdot3t^{2}+t+2\\cdot3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot3t^{2}=9t^{2}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot3=6'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3^{2}=9', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 3^{2}=9'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 9t+9t^{2}+t+6=9t^{2}+9t+t+6'},
                        {'type': 'e-step', 'heading': '\\displaystyle 9t+t+6=10t+6', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 9t+t+6=10t+6'}]}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 9t^{2}+10t+6+2t^{2}+3t+2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 9t^{2}+10t+6+2t^{2}+3t+2=9t^{2}+2t^{2}+10t+6+3t+2'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 9t^{2}+2t^{2}=11t^{2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 10t+6+3t+2=13t+8', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 10t+6+3t+2=10t+3t+6+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 10t+3t+6+2=13t+6+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 13t+6+2=13t+8'}]}], 'finalResult': '11t^{2}+13t+8'},
            },
            {
                'expression': 'lim_{x→2}(x^{2}+2)+4+lim_{x→3}(x^{3}+3)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to2}\\left(x^{2}+2\\right)=6', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=2', 'info': '\\displaystyle x^{2}+2=2^{2}+2'},
                        {'type': 'e-step', 'heading': '\\displaystyle 2^{2}=4', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 2^{2}=4'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 4+2'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 4+2=6'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to3}\\left(x^{3}+3\\right)=30', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=3', 'info': '\\displaystyle x^{3}+3=3^{3}+3'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3^{3}=27', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 3^{3}=27'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 27+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 27+3=30'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 6+4+30'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 6+4+30=40'}], 'finalResult': '40'},
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

        ]

        for item in expressionsAndExpectedVal:
            # try:
            expression = Expression(item['expression'])
            # print(expression)
            expectedVal = item['expected_val']
            keyword = item['keyword']
            returnedVal = evaluateCalculusExpression(expression, keyword=keyword)
            self.assertEqual(expectedVal, returnedVal, f"Failed: {expression}\nLatex: {latexify(expression)}\nKeyword: {keyword}")

            # except Exception as error:
            #     print(f"Error: {error}\nOn: {item['expression']}\nLatex: {latexify(item['expression'])}\nKeyword: {item['keyword']}\n")


if __name__ == '__main__':
    unittest.main()
