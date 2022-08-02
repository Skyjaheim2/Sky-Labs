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

    def test_regularLimits(self):
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
            {
                'expression': 'lim_{x→3}(3t^{2}+2t+1)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[c\\right]=c', 'info': '\\displaystyle \\lim_{x\\to3}\\left(3t^{2}+2t+1\\right)=3t^{2}+2t+1'}], 'finalResult': '3t^{2}+2t+1'},
            },
            {
                'expression': 'lim_{x→3}(3t^{2}+2t+x^{2}+3x+1)+5t^{2}+t+3',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to3}\\left(3t^{2}+2t+x^{2}+3x+1\\right)=3t^{2}+2t+19', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=3', 'info': '\\displaystyle 3t^{2}+2t+x^{2}+3x+1=3t^{2}+2t+3^{2}+3\\cdot3+1'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 3\\cdot3=9'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 3t^{2}+2t+3^{2}+9+1=3t^{2}+3^{2}+2t+9+1'},
                        {'type': 'e-step', 'heading': '\\displaystyle 3^{2}=9', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '3^{2}=9'}]},
                        {'type': 'e-step', 'heading': '\\displaystyle 2t+9+1=2t+10', 'e-steps': [
                            {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2t+9+1=2t+10'}]},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 9+3t^{2}+2t+10'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 9+3t^{2}+2t+10=3t^{2}+9+2t+10'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 9+2t+10=2t+9+10'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 2t+9+10=2t+19'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 3t^{2}+2t+19+5t^{2}+t+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle 3t^{2}+2t+19+5t^{2}+t+3=3t^{2}+5t^{2}+2t+19+t+3'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Exponentials}', 'info': '\\displaystyle 3t^{2}+5t^{2}=8t^{2}'},
                    {'type': 'e-step', 'heading': '\\displaystyle 2t+19+t+3=3t+22', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Group Like Terms}', 'info': '\\displaystyle 2t+19+t+3=2t+t+19+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle 2t+t+19+3=3t+19+3'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 3t+19+3=3t+22'}]}], 'finalResult': '8t^{2}+3t+22'},
            },
            {
                'expression': 'lim_{x→3}(x^{2}+2x+1)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Plug in the value}\\ x=3', 'info': '\\displaystyle x^{2}+2x+1=3^{2}+2\\cdot3+1'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Multiply And Divide (left to right)}', 'info': '\\displaystyle 2\\cdot3=6'},
                    {'type': 'e-step', 'heading': '\\displaystyle 3^{2}=9', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Compute Exponent}', 'info': '\\displaystyle 3^{2}=9'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle 6+1=7', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 6+1=7'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle 9+7'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle 9+7=16'}], 'finalResult': '16'},
            }

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


    def test_limitsAtInfinity(self):

        expressionsAndExpectedVal = [
            {
                'expression': "lim_{x→infty}(x^{2}+2x+1)",
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is even}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(x^{2}+2x+1\\right)=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(-x^{4}-3x^{3}+2x+1)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=-\\infty,a<0, n\\ \\text{is even}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(-x^{4}-3x^{3}+2x+1\\right)=-\\infty'}], 'finalResult': '-\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(x^{3}+5x^{2}+2x+3)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is odd}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(x^{3}+5x^{2}+2x+3\\right)=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(-3x^{3}+5x^{2}+2x+3)',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=-\\infty,a<0, n\\ \\text{is odd}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(-3x^{3}+5x^{2}+2x+3\\right)=-\\infty'}], 'finalResult': '-\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(10x^{6}+5x^{3}+2x^{2}+x+1)+10+12+1-5',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is even}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(10x^{6}+5x^{3}+2x^{2}+x+1\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+10+12+1--5'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Numbers Left to Right}', 'info': '\\displaystyle \\infty+10+12+1+5=\\infty+28'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}\\ \\infty+c=\\infty', 'info': '\\displaystyle \\infty+28=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(3x^{2})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is even}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(3x^{2}\\right)=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(sqrt{10x^{3}+5x^{2}+x+1})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[\\sqrt{f(x)}\\right]=\\sqrt{\\lim_{x\\to a}\\left( f(x) \\right)}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{10x^{3}+5x^{2}+x+1}\\right)=\\sqrt{\\lim_{x\\to\\infty}\\left(10x^{3}+5x^{2}+x+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is odd}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(10x^{3}+5x^{2}+x+1\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{10x^{3}+5x^{2}+x+1}\\right)=\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\sqrt{\\infty}=\\infty', 'info': '\\displaystyle \\sqrt{\\infty}=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(15x^{3}+sqrt{10x^{3}+5x^{2}+x+1})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[f(x)\\pm g(x)\\right]=\\lim_{x\\to a}f(x)\\pm \\lim_{x\\to a}g(x)', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(15x^{3}+\\sqrt{10x^{3}+5x^{2}+x+1}\\right)=\\lim_{x\\to\\infty}\\left(15x^{3}\\right)+\\lim_{x\\to\\infty}\\left(\\sqrt{10x^{3}+5x^{2}+x+1}\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is odd}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(15x^{3}\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[\\sqrt{f(x)}\\right]=\\sqrt{\\lim_{x\\to a}\\left( f(x) \\right)}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{10x^{3}+5x^{2}+x+1}\\right)=\\sqrt{\\lim_{x\\to\\infty}\\left(10x^{3}+5x^{2}+x+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is odd}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(10x^{3}+5x^{2}+x+1\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{10x^{3}+5x^{2}+x+1}\\right)=\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle \\infty+\\sqrt{\\infty}=\\sqrt{\\infty}+\\infty'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\sqrt{\\infty}=\\infty', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\sqrt{\\infty}=\\infty', 'info': '\\displaystyle \\sqrt{\\infty}=\\infty'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle \\infty+\\infty=2\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}\\ c\\cdot\\infty=\\infty', 'info': '\\displaystyle 2\\infty=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(sqrt{x^{2}+sqrt{10x^{3}+5x^{2}+x+1}})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[\\sqrt{f(x)}\\right]=\\sqrt{\\lim_{x\\to a}\\left( f(x) \\right)}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{x^{2}+\\sqrt{10x^{3}+5x^{2}+x+1}}\\right)=\\sqrt{\\lim_{x\\to\\infty}\\left(x^{2}+\\sqrt{10x^{3}+5x^{2}+x+1}\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[f(x)\\pm g(x)\\right]=\\lim_{x\\to a}f(x)\\pm \\lim_{x\\to a}g(x)', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(x^{2}+\\sqrt{10x^{3}+5x^{2}+x+1}\\right)=\\lim_{x\\to\\infty}\\left(x^{2}\\right)+\\lim_{x\\to\\infty}\\left(\\sqrt{10x^{3}+5x^{2}+x+1}\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is even}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(x^{2}\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[\\sqrt{f(x)}\\right]=\\sqrt{\\lim_{x\\to a}\\left( f(x) \\right)}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{10x^{3}+5x^{2}+x+1}\\right)=\\sqrt{\\lim_{x\\to\\infty}\\left(10x^{3}+5x^{2}+x+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is odd}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(10x^{3}+5x^{2}+x+1\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{10x^{3}+5x^{2}+x+1}\\right)=\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle \\infty+\\sqrt{\\infty}=\\sqrt{\\infty}+\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\sqrt{\\infty}=\\infty', 'info': '\\displaystyle \\sqrt{\\infty}=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle \\infty+\\infty=2\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}\\ c\\cdot\\infty=\\infty', 'info': '\\displaystyle 2\\infty=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{x^{2}+\\sqrt{10x^{3}+5x^{2}+x+1}}\\right)=\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\sqrt{\\infty}=\\infty', 'info': '\\displaystyle \\sqrt{\\infty}=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(e^{3x^{2}+2x+3})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[f(x)\\right]^b=\\left[ \\lim_{x\\to a}\\left( f(x) \\right) \\right]^b', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(e^{3x^{2}+2x+3}\\right)=e^{\\lim_{x\\to\\infty}\\left(3x^{2}+2x+3\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is even}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(3x^{2}+2x+3\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(e^{3x^{2}+2x+3}\\right)=e^{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\infty^c=\\infty', 'info': '\\displaystyle e^{\\infty}=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(e^{3x+sqrt{3x^{3}+sqrt{10x^{6}+20x^{4}+5x+1}}})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[f(x)\\right]^b=\\left[ \\lim_{x\\to a}\\left( f(x) \\right) \\right]^b', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(e^{3x+\\sqrt{3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}}}\\right)=e^{\\lim_{x\\to\\infty}\\left(3x+\\sqrt{3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}}\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[f(x)\\pm g(x)\\right]=\\lim_{x\\to a}f(x)\\pm \\lim_{x\\to a}g(x)', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(3x+\\sqrt{3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}}\\right)=\\lim_{x\\to\\infty}\\left(3x\\right)+\\lim_{x\\to\\infty}\\left(\\sqrt{3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}}\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is odd}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(3x\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[\\sqrt{f(x)}\\right]=\\sqrt{\\lim_{x\\to a}\\left( f(x) \\right)}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}}\\right)=\\sqrt{\\lim_{x\\to\\infty}\\left(3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[f(x)\\pm g(x)\\right]=\\lim_{x\\to a}f(x)\\pm \\lim_{x\\to a}g(x)', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}\\right)=\\lim_{x\\to\\infty}\\left(3x^{3}\\right)+\\lim_{x\\to\\infty}\\left(\\sqrt{10x^{6}+20x^{4}+5x+1}\\right)'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is odd}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(3x^{3}\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[\\sqrt{f(x)}\\right]=\\sqrt{\\lim_{x\\to a}\\left( f(x) \\right)}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{10x^{6}+20x^{4}+5x+1}\\right)=\\sqrt{\\lim_{x\\to\\infty}\\left(10x^{6}+20x^{4}+5x+1\\right)}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is even}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(10x^{6}+20x^{4}+5x+1\\right)=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{10x^{6}+20x^{4}+5x+1}\\right)=\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle \\infty+\\sqrt{\\infty}=\\sqrt{\\infty}+\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\sqrt{\\infty}=\\infty', 'info': '\\displaystyle \\sqrt{\\infty}=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle \\infty+\\infty=2\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}\\ c\\cdot\\infty=\\infty', 'info': '\\displaystyle 2\\infty=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}}\\right)=\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+\\sqrt{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Group Terms}', 'info': '\\displaystyle \\displaystyle \\infty+\\sqrt{\\infty}=\\sqrt{\\infty}+\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\sqrt{\\infty}=\\infty', 'info': '\\displaystyle \\sqrt{\\infty}=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\infty+\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Add Like Terms Left to Right}', 'info': '\\displaystyle \\infty+\\infty=2\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}\\ c\\cdot\\infty=\\infty', 'info': '\\displaystyle 2\\infty=\\infty'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(e^{3x+\\sqrt{3x^{3}+\\sqrt{10x^{6}+20x^{4}+5x+1}}}\\right)=e^{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\infty^c=\\infty', 'info': '\\displaystyle e^{\\infty}=\\infty'}], 'finalResult': '\\infty'},
            },
            {
                'expression': 'lim_{x→infty}(frac{3t^{2}+5t+2}{sqrt{x^{2}+2x+1}})',
                'keyword': None,
                'expected_val': {'steps': [
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[\\cfrac{f(x)}{g(x)}\\right]=\\cfrac{\\lim_{x\\to a}f(x)}{\\lim_{x\\to a}g(x)}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\frac{3t^{2}+5t+2}{\\sqrt{x^{2}+2x+1}}\\right)=\\frac{\\lim_{x\\to\\infty}\\left(3t^{2}+5t+2\\right)}{\\lim_{x\\to\\infty}\\left(\\sqrt{x^{2}+2x+1}\\right)}'},
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to\\infty}\\left(3t^{2}+5t+2\\right)=3t^{2}+5t+2', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[c\\right]=c', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(3t^{2}+5t+2\\right)=3t^{2}+5t+2'}]},
                    {'type': 'e-step', 'heading': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{x^{2}+2x+1}\\right)=\\infty', 'e-steps': [
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Limit Law:}\\lim_{x\\to a}\\left[\\sqrt{f(x)}\\right]=\\sqrt{\\lim_{x\\to a}\\left( f(x) \\right)}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{x^{2}+2x+1}\\right)=\\sqrt{\\lim_{x\\to\\infty}\\left(x^{2}+2x+1\\right)}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinite Limit Property:}\\lim_{x\\to\\pm\\infty}\\left( ax^{n}+\\dots+bx+c \\right)=\\infty,a>0, n\\ \\text{is even}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(x^{2}+2x+1\\right)=\\infty'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\sqrt{x^{2}+2x+1}\\right)=\\sqrt{\\infty}'},
                        {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\sqrt{\\infty}=\\infty', 'info': '\\displaystyle \\sqrt{\\infty}=\\infty'}]},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Combine Results}', 'info': '\\displaystyle \\lim_{x\\to\\infty}\\left(\\frac{3t^{2}+5t+2}{\\sqrt{x^{2}+2x+1}}\\right)=\\frac{3t^{2}+5t+2}{\\infty}'},
                    {'type': 'main-step', 'description': '\\displaystyle \\text{Apply Infinity Property}:\\ \\cfrac{c}{\\infty}=0', 'info': '\\displaystyle \\frac{3t^{2}+5t+2}{\\infty}=0'}], 'finalResult': '0'},
            }
        ]

        for item in expressionsAndExpectedVal:
            # try:
            expression = Expression(item['expression'])
            # print(expression)
            expectedVal = item['expected_val']
            keyword = item['keyword']
            returnedVal = evaluateCalculusExpression(expression, keyword=keyword)
            self.assertEqual(expectedVal, returnedVal,
                             f"Failed: {expression}\nLatex: {latexify(expression)}\nKeyword: {keyword}")

            # except Exception as error:
            #     print(f"Error: {error}\nOn: {item['expression']}\nLatex: {latexify(item['expression'])}\nKeyword: {item['keyword']}\n")


if __name__ == '__main__':
    unittest.main()
