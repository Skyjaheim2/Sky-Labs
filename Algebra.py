import math
import re
from math import floor, pi, e, sqrt
from exceptions import *

from Methods import (latexify, parseLatex, getSpecialFunctions, createMainStep, createExpandableStep,
                     createGroupedTermsDict, createEStepHeadingFromGroup, parenIsBalanced, joinList,
                     indexOf, getIndexOfLastOccurrence, list_diff, numOccurrences, splitAtIndex, reverseList)


maxInt = 1000000000000000

class Expression:
    def __init__(self, expression):
        self.expression = expression
        self.__Terms = []

    def getNumOpenParen(self):
        counter = 0
        for i in range(len(self.expression)):
            if self.expression[i] == '(':
                counter += 1
        return counter

    def getIndexOfInnerMostParen(self):
        paren = '('
        if paren not in self.expression:
            raise ValueError(f"{paren} not in expression")

        numOpenParen = self.getNumOpenParen()
        parenCounter = 0
        for i in range(len(self.expression)):
            if self.expression[i] == paren:
                parenCounter += 1
            if parenCounter == numOpenParen:
                return i

    def getTerms(self):
        if self.__Terms != []:
            return self.__Terms
        isCompleteTerm = True
        numOpenCurlyParen, numClosedCurlyParen, numOpenSquareParen, numClosedSquareParen, numOpenParen, numClosedParen = 0, 0, 0, 0, 0, 0
        currentTerm = ''
        i = 0
        while i < len(self.expression):
            # CHECK FOR PARENTHESES
            if self.expression[i] == '{':
                numOpenCurlyParen += 1
                isCompleteTerm = False
            elif self.expression[i] == '(':
                numOpenParen += 1
                isCompleteTerm = False
            elif self.expression[i] == '[':
                numOpenSquareParen += 1
                isCompleteTerm = False
            elif self.expression[i] == '}':
                numClosedCurlyParen += 1
            elif self.expression[i] == ')':
                numClosedParen += 1
            elif self.expression[i] == ']':
                numClosedSquareParen += 1
            # CHECK FOR COMPLETED TERM
            if not isCompleteTerm:
                if (numOpenCurlyParen == numClosedCurlyParen) and (numOpenParen == numClosedParen) and (
                        numOpenSquareParen == numClosedSquareParen):
                    isCompleteTerm = True
                    numOpenCurlyParen, numClosedCurlyParen, numOpenSquareParen, numClosedSquareParen, numOpenParen, numClosedParen = 0, 0, 0, 0, 0, 0
            if (self.expression[i] == '+' or self.expression[i] == '-') and isCompleteTerm and self.expression[
                i - 1] != '*':
                if currentTerm != '':
                    self.addTerm(currentTerm)
                    currentTerm = ''

            currentTerm += self.expression[i]
            # ADD LAST TERM
            if i == len(self.expression) - 1:
                self.addTerm(currentTerm)
            i += 1

        return self.castTerms(self.__Terms)

    def addTerm(self, termToAdd):
        self.__Terms.append(termToAdd)

    def getGroupedTerms(self):
        Terms = self.getTerms()
        groupedTerms = {
            'Exponential': [],
            'Radicals': [],
            'Fractions': [],
            'Constants': [],
        }
        for term in Terms:
            if type(term) == Constant:
                groupedTerms['Constants'].append(term)
            elif type(term) == Exponential:
                groupedTerms['Exponential'].append(term)
            elif type(term) == Radical:
                groupedTerms['Radicals'].append(term)
            elif type(term) == Fraction:
                groupedTerms['Fractions'].append(term)

        return groupedTerms

    def getGroupedExpressions(self):
        GTerms = self.getGroupedTerms()
        addOpenParen = False

        groupedExpressionStr = ''
        groupedExpressionStrWithoutParen = ''
        groupedExpressionList = []
        for i, group in enumerate(GTerms):
            removedSign = False
            if GTerms[group] != []:
                if len(GTerms[group]) != 1:
                    groupedExpressionStr += '('
                    addOpenParen = True
                for term in GTerms[group]:
                    term = str(term)

                    if term[0] == '+' and (str(GTerms[group][0]) == term) and (not removedSign):
                        term = term[1:]
                        removedSign = True
                    groupedExpressionStrWithoutParen += term
                    groupedExpressionStr += term

                if i != len(GTerms) - 1:
                    if addOpenParen:
                        groupedExpressionStr += ')+'
                        groupedExpressionStrWithoutParen += '+'
                        addOpenParen = False
                    else:
                        groupedExpressionStr += '+'
                        groupedExpressionStrWithoutParen += '+'
                else:
                    if addOpenParen:
                        groupedExpressionStr += ')'
                        addOpenParen = False

        # FORMATTING
        groupedExpressionStr = groupedExpressionStr.replace('+-', '-').replace('++', '+').replace('--', '+')
        groupedExpressionStrWithoutParen = groupedExpressionStrWithoutParen.replace('+-', '-').replace('++',
                                                                                                       '+').replace(
            '--', '+')
        if groupedExpressionStr[-1] == '+':
            groupedExpressionStr = groupedExpressionStr[:-1]
        if groupedExpressionStrWithoutParen[-1] == '+':
            groupedExpressionStrWithoutParen = groupedExpressionStrWithoutParen[:-1]

        # POPULATE groupedExpressionArray
        expressionToAdd = ''
        for i in range(len(groupedExpressionStr)):
            expressionToAdd += groupedExpressionStr[i]
            if i == len(groupedExpressionStr) - 1:
                groupedExpressionList.append(expressionToAdd)
            if (groupedExpressionStr[i] == '+' or groupedExpressionStr[i] == '-') and parenIsBalanced(expressionToAdd,
                                                                                                      'both'):
                groupedExpressionList.append(expressionToAdd[:-1])
                expressionToAdd = ''

        return {
            'str': groupedExpressionStr,
            'strWithoutParen': groupedExpressionStrWithoutParen,
            'list': groupedExpressionList,
        }

    def isSimplified(self):
        expression = Expression(self.expression)
        simplificationAttempt = simplifyExpression(expression)['steps']
        return len(simplificationAttempt) == 0

    def isSingleExpression(self):
        return len(self.getTerms()) == 1

    @staticmethod
    def castTerms(Terms):
        for i in range(len(Terms)):
            # if '*' in Terms[i]:
            #     Terms[i] = Constant(Terms[i])
            # else:
            radical_pattern = re.compile(r".*[)0-9]sqrt")
            radical_matches = radical_pattern.findall(Terms[i])
            if len(radical_matches) > 0:
                if not parenIsBalanced(radical_matches[0], 'both'):
                    radical_matches = []

            fraction_pattern = re.compile(r".*[)0-9]frac")
            fraction_matches = fraction_pattern.findall(Terms[i])

            # fraction_pattern = re.compile(r"frac{.+}{.+}$")
            # fraction_matches = fraction_pattern.findall(Terms[i])

            exponential_pattern = re.compile(r"^[0-9a-zA-Z()^{}+-]+\^{*.+")
            exponential_matches = exponential_pattern.findall(Terms[i])

            leftExponentialProductPattern = re.compile(r'[a-zA-Z]\w\^{')
            leftExponentialProductMatches = leftExponentialProductPattern.findall(Terms[i])

            rightExponentialProductPattern = re.compile(r'}[\w]')
            rightExponentialProductMatches = rightExponentialProductPattern.findall(Terms[i])

            if Terms[i][0:3] == 'lim':
                Terms[i] = Constant(Terms[i])
            elif len(leftExponentialProductMatches) > 0 or len(rightExponentialProductMatches) > 0:
                # if len(matches) > 0:
                Terms[i] = Constant(Terms[i])
            elif ('frac' in Terms[i][0:5] or fraction_matches != []) and Terms[i][0:5][0] != '(':
                if '*' in Terms[i]:
                    allProducts = Terms[i].split('*')
                    allParenBalanced = True
                    for term in allProducts:
                        if not parenIsBalanced(term, 'both'):
                            allParenBalanced = False
                    if allParenBalanced:
                        # CASE: frac{x+1}{y+1}*frac{u+1}{v+1} -> Constant
                        # print('yes')
                        Terms[i] = Constant(Terms[i])
                    else:
                        Terms[i] = Fraction(Terms[i])
                else:
                    Terms[i] = Fraction(Terms[i])
            elif ('sqrt' in Terms[i][0:5] and parenIsBalanced(Terms[i][0:5])) or radical_matches != []:
                Terms[i] = Radical(Terms[i])
            elif '^' in Terms[i] or exponential_matches != []:
                try:
                    exp = Exponential(Terms[i])
                    if parenIsBalanced(exp.base) and parenIsBalanced(exp.exponent) and Constant(
                            exp.coefficient).is_digit:
                        Terms[i] = Exponential(Terms[i])
                    else:
                        Terms[i] = Constant(Terms[i])
                except TypeError:
                    Terms[i] = Constant(Terms[i])

                # base = Terms[i].split('^')[0]
                # if base[0] == '+': base = base[1:]
                # if base[0] == '-': base = base[1:]
                # exponent = Terms[i].split('^')[1]
                # if exponent[-1] == ')':
                #     Terms[i] = Constant(Terms[i])
                # elif parenIsBalanced(base) and parenIsBalanced(exponent):
                #     Terms[i] = Exponential(Terms[i])
                #
                # else:
                #     Terms[i] = Constant(Terms[i])
            else:
                Terms[i] = Constant(Terms[i])
        return Terms

    def replace(self, subStringToBeReplace: str, replacement: str):
        return self.expression.replace(subStringToBeReplace, replacement)

    def split(self, char):
        return self.expression.split(char)

    def __str__(self):
        return self.expression

    def __repr__(self):
        return self.expression

    def __len__(self):
        return len(self.getTerms())

    def __contains__(self, item):
        """ 'in' OPERATOR """
        return item in self.expression

    def __getitem__(self, index):
        """ [] OPERATOR """
        if isinstance(index, slice):
            return Expression(self.expression[index])
        return self.expression[index]

class Exponential:
    def __init__(self, expression, cast_as_non_exponential=False, cast_entire_term_as_exp=False, CETAEIOCF=False):
        # CETAEIOCF: is short for cast_entire_term_as_exp_if_original_cast_failed
        self.expression = expression
        self.exponential = self.expression
        sign = self.exponential[0]
        if self.exponential[0] == '+' or self.exponential[0] == '-': self.exponential = self.exponential[1:]

        if sign != '+' and sign != '-': sign = ''
        if sign == '+': sign = ''

        expression = str(self.exponential)

        if expression[0] == '(' and expression[-1] == ')':
            pass
            # tmp_expression = expression[1:-1]
            # if parenIsBalanced(tmp_expression):
            #     if len(Expression(tmp_expression)) > 1:
            #         self.coefficient = '1'
            #         self.base = expression
            #         self.exponent = '1'
            #         return
            #     else:
            #         expression = tmp_expression

        if cast_entire_term_as_exp:
            self.base = expression
            self.coefficient = '1'
            self.exponent = '1'
            return

        if '^' not in expression or cast_as_non_exponential:
            if Constant(expression).is_digit:
                self.base = expression
                self.coefficient = '1'
                self.exponent = '1'
                return
            else:
                self.coefficient = ''
                for char in expression:
                    if Constant(char).is_digit:
                        self.coefficient += char
                    if char == '(' or char == '{':
                        break

                self.base = expression[len(self.coefficient):]
                self.exponent = '1'
                if self.coefficient == '': self.coefficient = '1'
                return

        else:
            if '{' in expression:
                self.base = None
                self.exponent = None
                for i in range(len(expression)):
                    if expression[i] == '^':
                        left = expression[:i]
                        right = expression[i + 1:]
                        if parenIsBalanced(left, 'both') and parenIsBalanced(right, 'both'):
                            self.base = left
                            self.exponent = right[1:-1]
                if self.base == None or self.exponent == None:
                    if CETAEIOCF:
                        newExp = Exponential(self.expression, cast_as_non_exponential=True)
                        self.coefficient, self.base, self.exponent = newExp.coefficient, newExp.base, newExp.exponent
                        return
                    else:
                        raise TypeError(f'{expression} cannot be casted as an exponential')

                # base_pattern = re.compile(r".+\^{")
                # base_matches = base_pattern.findall(expression)
                # self.base = base_matches[0][:-2]
                #
                # if '^' in self.base and not parenIsBalanced(self.base, 'both'):  # NESTED EXPONENTS
                #     self.base = Exponential(self.base).base
                #
                # exponent_pattern = re.compile(r"(\^{.+}$|[0-9a-zA-Z]$)")
                # exponent_matches = exponent_pattern.findall(expression)
                # if '{' in exponent_matches[0] and '}' in exponent_matches[0]:
                #     self.exponent = exponent_matches[0][2:-1]
                # else:
                #     self.exponent = exponent_matches[0]
                #
                # if not parenIsBalanced(self.base, 'both') or not parenIsBalanced(self.exponent, 'both'):
                #     newExp = Exponential(self.expression, cast_as_non_exponential=True)
                #     self.coefficient, self.base, self.exponent = newExp.coefficient, newExp.base, newExp.exponent
                #     return

            else:
                i_lc = getIndexOfLastOccurrence(expression, '^')
                exponentData = splitAtIndex(expression, i_lc)
                self.base = exponentData[0]
                self.exponent = exponentData[1]

        if self.base != None:
            if self.base[0] == '+' or self.base[0] == '-': self.base = self.base[1:]

            coefficient = ''
            if len(self.base) > 1:
                for i, char in enumerate(self.base):
                    char = Constant(char)
                    if char == '(' and self.base[-1] == ')':
                        break
                    if self.exponential[i + 1] != '^':
                        coefficient += str(char)

            if coefficient == '':
                self.coefficient = '1'
                if sign == '-': self.coefficient = '-1'
            else:
                self.coefficient = coefficient
                if self.coefficient[-1] == '*': self.coefficient = self.coefficient[:-1]
                if len(self.base) == len(coefficient) + 1:
                    # if Constant(expression[len(coefficient)]).is_digit and '*' in expression: self.base = expression[len(coefficient)]
                    if not Constant(expression[len(coefficient)]).is_digit or '*' in expression: self.base = expression[
                        len(coefficient)]
                else:
                    if self.base[len(coefficient)] == '(' and self.base[-1] == ')':
                        self.base = expression[len(coefficient): len(coefficient) + 1]
                        i = 1
                        while not parenIsBalanced(self.base, 'both') or self.base == '':
                            self.base = expression[len(coefficient): len(self.coefficient) + i]
                            i += 1
                self.coefficient = f"{sign}{self.coefficient}"

    def computeExponential(self):
        base = Constant(self.base)
        exponent = Constant(self.exponent)
        if (base.is_digit or Constant(str(base)[1:-1]).is_digit) and exponent.is_digit:
            solution = Constant(str(eval(f'{self.base}**{self.exponent}')))
            if solution.is_integer:
                if solution.val > maxInt:
                    return False
                return solution
            else:
                decimal_approx = Constant(f'{solution[:7]}...')
                return decimal_approx
        else:
            return False

    def isSimplified(self):
        base = Expression(self.base)
        exponent = Expression(self.exponent)

        return base.isSimplified() and exponent.isSimplified()

    def isPolynomial(self):
        return Constant(self.exponent).is_digit and len(self.base) == 1

    def areLike(self, other):
        return (str(self.base) == str(other.base)) and (str(self.exponent) == str(other.exponent))

    def format(self):
        pattern = re.compile(r'^\(.+\)$')
        matches = pattern.findall(self.base)

        if len(matches) != 0:
            tmp_base = Constant(self.base[1:-1])
            if tmp_base.is_integer or len(tmp_base) == 1:
                self.base = tmp_base
                self.expression = f"{self.coefficient if self.coefficient != '1' else ''}{self.base}^{'{'}{self.exponent}{'}'}"

        # self.expression = f"{self.base}^{'{'}{self.exponent}{'}'}"

    def split(self, char):
        return self.expression.split(char)

    def replace(self, subStringToBeReplace, replacement):
        return self.expression.replace(subStringToBeReplace, replacement)

    def __str__(self):
        return str(self.expression)

    def __repr__(self):
        return str(self.expression)

    def __contains__(self, item):
        """ 'in' OPERATOR """
        return item in self.expression

    def __getitem__(self, index):
        """ [] OPERATOR """
        return self.expression[index]

    def __eq__(self, other):
        # return (str(self.base) == str(other.base)) and (str(self.exponent) == str(other.exponent))
        return self.expression == other.expression
class Polynomial(Exponential):
    def __init__(self, expression):
        super().__init__(expression)

class Radical(Expression):
    def __init__(self, expression):
        super().__init__(expression)
        # self.expression = expression
        if '[' in expression:
            self.is_square_root = False
            pattern = re.compile(r'\[.+]')
            matches = pattern.findall(expression)
            self.index = matches[0][1:-1]

        else:
            self.index = '2'
            self.is_square_root = True

        self.coefficient = ''
        if expression[0] == 's':
            self.coefficient = '1'
        elif expression[0:2] == '+s':
            self.coefficient = '1'
        elif expression[0:2] == '-s':
            self.coefficient = '-'
        else:
            for i in range(len(expression)):
                if expression[i:i + 4] == 'sqrt': break
                self.coefficient += expression[i]
        if self.coefficient[0] == '+': self.coefficient = self.coefficient[1:]

    def getRadicand(self) -> Expression:
        pattern = re.compile(r'{.+}')
        matches = pattern.findall(self.expression)
        expressionInside = matches[0][1:-1]

        return Expression(expressionInside)

    def computeRadical(self):
        if self.is_square_root:
            try:
                solution = Constant(str(eval(self.expression.replace('{', '(').replace('}', ')'))))
                if solution.is_integer:
                    return solution
                else:
                    decimal_approx = Constant(f"{solution[:7]}...")
                    return decimal_approx

            except:
                return False
        else:
            index = Constant(self.index)
            if index.is_digit:
                try:
                    solution = Constant(str(eval(f'{self.getRadicand()}**(1/{self.index})')))
                    return solution if solution.is_integer else Constant(f"{solution[:7]}...")
                except:
                    return False
            else:
                return False

    def __str__(self):
        return str(self.expression)

class Fraction:
    def __init__(self, expression):
        self.expression = expression
        numerator_pattern = re.compile(r'frac{.+}{')
        numerator_matches = numerator_pattern.findall(expression)

        denominator_pattern = re.compile(r'}{.+}')
        denominator_matches = denominator_pattern.findall(expression)

        if len(numerator_matches) != 0:
            self.numerator = numerator_matches[0][5:-2]
        else:
            self.numerator = None
        if len(denominator_matches) != 0:
            self.denominator = denominator_matches[0][2:-1]
        else:
            self.denominator = None

        if len(numerator_matches) == 0 and len(denominator_matches) == 0:
            self.numerator = expression
            if self.numerator[0] == '+': self.numerator = self.numerator[1:]
            self.denominator = '1'

    def reduceFraction(self):
        numerator = castToFloatOrInt(self.numerator)
        denominator = castToFloatOrInt(self.denominator)

        numeratorFactors = set(getFactors(numerator))
        denominatorFactors = set(getFactors(denominator))

        commonFactors = numeratorFactors.intersection(denominatorFactors)
        gcf = max(commonFactors)

        reducedNumerator = numerator // gcf
        reducedDenominator = denominator // gcf

        return Fraction(f"frac{'{'}{reducedNumerator}{'}'}{'{'}{reducedDenominator}{'}'}")

    def computeFraction(self, reduce=False):
        numerator = Constant(self.numerator)
        denominator = Constant(self.denominator)
        if numerator.is_integer and denominator.is_integer:
            solution = Constant(str(eval(f'{self.numerator}/{self.denominator}')))
            if solution.is_integer:
                if solution.val > maxInt:
                    return False
                return solution
            else:
                if len(solution) > 7 and not reduce:
                    decimal_approx = Constant(f'{solution[:7]}...')
                else:
                    if reduce:
                        # TRY TO REDUCE FRACTION
                        reducedFraction = self.reduceFraction()
                        if (reducedFraction.numerator != numerator) and (reducedFraction.denominator != denominator):
                            return Fraction(
                                f"frac{'{'}{reducedFraction.numerator}{'}'}{'{'}{reducedFraction.denominator}{'}'}")
                        else:
                            decimal_approx = solution
                            return decimal_approx
                    else:
                        decimal_approx = solution
                        return decimal_approx

                return decimal_approx
        else:
            return False

    def isSimplified(self):
        numerator = Expression(self.numerator)
        denominator = Expression(self.denominator)
        if numerator.isSimplified() and denominator.isSimplified():
            numerator, denominator = Constant(str(numerator)), Constant(str(denominator))
            if numerator.is_integer and denominator.is_integer:
                reducedFraction = self.reduceFraction()
                return reducedFraction.numerator == self.numerator and reducedFraction.denominator == self.denominator
            else:
                return True
        else:
            return False

    def replace(self, subStringToBeReplace, replacement):
        return self.expression.replace(subStringToBeReplace, replacement)

    def split(self, char):
        return self.expression.split(char)

    def __str__(self):
        # sign = self.expression[0]
        # if sign != '+' and sign != '-': sign = ''
        # return f"{sign}frac{'{'}{self.numerator}{'}'}{'{'}{self.denominator}{'}'}"
        return self.expression

    def __repr__(self):
        return self.expression
        # sign = self.expression[0]
        # if sign != '+' and sign != '-': sign = ''
        # return f"{sign}frac{'{'}{self.numerator}{'}'}{'{'}{self.denominator}{'}'}"

    def __len__(self):
        return len(self.expression)

    def __contains__(self, item):
        """ 'in' OPERATOR """
        return item in self.expression

    def __getitem__(self, index):
        """ [] OPERATOR """
        if isinstance(index, slice):
            return Fraction(self.expression[index])
        return self.expression[index]

class Constant(Expression):
    def __init__(self, expression):
        super().__init__(expression)
        if '+' in expression or '-' in expression:
            if isDigit(expression[1:]):
                self.is_digit = True
            else:
                self.is_digit = False
        else:
            if isDigit(expression):
                self.is_digit = True
            else:
                self.is_digit = False

        if self.is_digit:
            if '.' in self.expression:
                if self.expression.split('.')[1] == '0':
                    self.expression = self.expression[:-2]
                    self.is_integer = True
                else:
                    self.is_integer = False
            else:
                if 'frac' not in self.expression:
                    self.is_integer = True
                else:
                    self.is_integer = False
        else:
            self.is_integer = False

        if self.is_integer:
            self.val = int(self.expression)

    def __len__(self):
        return len(self.expression)

    def __getitem__(self, index):
        """ [] OPERATOR """
        return self.expression[index]

    def __eq__(self, other):
        """ DOUBLE EQUAL TO OPERATOR """
        return str(self.expression) == str(other)

class Equation:
    def __init__(self, equation):
        self.equation = equation
    # TODO

MAX_SIZE_OF_NUM_BEFORE_CONVERTED_TO_STANDARD_FORM = 10 ** 20

def simplifyExpression(expression: Expression, keyword=None, Steps=None, groupedTerms=None, recursiveCall=False, finalResult=None):
    expression = Expression(expression.replace(' ', ''))

    radical_product_pattern = re.compile(r'sqrt{.+}sqrt{.+}')
    matches = radical_product_pattern.findall(str(expression))
    if len(matches) > 0:
        return {'steps': [], 'finalResult': latexify(str(expression))}

    if Steps is None: Steps = []
    if keyword is None: keyword = 'simplify'

    # FORMAT
    redundantParenPattern = re.compile(r'^\(.+\)$')
    matches = redundantParenPattern.findall(str(expression))
    if len(matches) != 0:
        checkExpression = expression[1:-1]
        # if '(' not in checkExpression and ')' not in checkExpression:
        #     expression = expression[1:-1]
        if parenIsBalanced(checkExpression):
            mainStep = createMainStep(r'\text{Remove Redundant Parentheses}',
                                      latexify(f'{expression}={checkExpression}'))
            Steps.append(mainStep)
            newExpression = Expression(checkExpression)
            return simplifyExpression(newExpression, keyword=keyword, Steps=Steps, finalResult=finalResult)

    specialFunctions = getSpecialFunctions()

    """ MULTIPLY TERMS """

    if '*' in expression or len(matches) > 0:
        for term in expression.getTerms():
            if term[0] == '+': term = term[1:]
            if '*' in term and type(term) != Fraction:
                if '(' in term:
                    numberOfTermsInParen = 0
                    termsInParen = []
                    termsNotInParen = ''
                    termToAdd = ''
                    i = 0
                    while i < len(str(term)):
                        if term[i] == '(':
                            for j in range(i + 1, len(str(term))):
                                if term[j] == ')':
                                    if parenIsBalanced(term[i:j + 1]):
                                        """ ADD TERM IN PAREN """
                                        numberOfTermsInParen += 1
                                        termsInParen.append(term[i:j + 1])
                                        i = j + 1
                                        break
                            termsNotInParen += termToAdd
                            termToAdd = ''
                        else:
                            termToAdd += term[i]
                        i += 1

                    if numberOfTermsInParen != 0:
                        """ GRABS THE LAST TERMS BEING MULTIPLIED IN: (25x^{2}+6x+3)*5x*4 """
                        if termsNotInParen == '' and i != j: termsNotInParen += term[j + 1:]
                        """ GRABS THE LAST TERMS BEING MULTIPLIED IN: 2x*3*(x+2)*4*2x*(x+1)*3x """
                        if termsNotInParen != '' and i != j: termsNotInParen += term[j + 2:]

                    if termsNotInParen != '':
                        if termsNotInParen[-1] == '*': termsNotInParen = termsNotInParen[:-1]

                    """ PRODUCT TO THE LEFT AND RIGHT """
                    leftProductPattern = re.compile('[\w{}*^+-]+\*\(')
                    leftProductMatches = leftProductPattern.findall(str(term))

                    rightProductPattern = re.compile('\)\*[\w{}*^+-]+')
                    rightProductMatches = rightProductPattern.findall(str(term))

                    termToMultiply = ''
                    if (len(leftProductMatches) > 0 or len(rightProductMatches) > 0) and numberOfTermsInParen == 1:
                        cpyTerm = term
                        if len(leftProductMatches) > 0: termToMultiply += leftProductMatches[0][0:-2]
                        if len(rightProductMatches) > 0:
                            termToMultiply += rightProductMatches[0][1:]
                            if len(leftProductMatches) > 0:
                                lMatch = leftProductMatches[0] if len(leftProductMatches) > 0 else ''
                                rMatch = rightProductMatches[0]
                                term = f"{lMatch[:-1]}{rMatch[2:]}{term[len(lMatch) - 2: -len(rMatch) + 1]}"
                                expression = Expression(expression.replace(str(cpyTerm), str(term)))
                            else:
                                rMatch = rightProductMatches[0]
                                term = f"{rMatch[2:]}*{term[0:-(len(rMatch) - 1)]}"
                                expression = Expression(expression.replace(str(cpyTerm), str(term)))

                        if termToMultiply[0] == '*': termToMultiply = termToMultiply[1:]

                        if '*' in termToMultiply:
                            simplifiedTermToMultiply = getProduct2(termToMultiply.split('*'))
                            if termToMultiply != simplifiedTermToMultiply:
                                mainStep = createMainStep(r'\text{Multiply Terms (left to right)}',
                                                          latexify(f'{termToMultiply}={simplifiedTermToMultiply}'))
                                Steps.append(mainStep)
                                expression = Expression(
                                    expression.replace(str(termToMultiply), simplifiedTermToMultiply))
                                term = term.replace(termToMultiply, simplifiedTermToMultiply)

                                termToMultiply = simplifiedTermToMultiply

                        expressionInParen = Expression(str(term)[len(termToMultiply) + 2:-1])
                        if parenIsBalanced(str(expressionInParen)):
                            newExpression = ''
                            if termToMultiply != '-1':
                                for term2 in expressionInParen.getTerms():
                                    if term2[0] == '+':
                                        newExpression += f'+{termToMultiply}*{term2[1:]}'
                                    elif term2[0] == '-':
                                        newExpression += f'-{termToMultiply}*{term2[1:]}'
                                    else:
                                        newExpression += f'{termToMultiply}*{term2}'
                            else:
                                for term2 in expressionInParen.getTerms():
                                    if term2[0] == '+':
                                        newExpression += f'-{term2[1:]}'
                                    elif term2[0] == '-':
                                        newExpression += f'+{term2[1:]}'
                                    else:
                                        newExpression += f'-{term2}'

                            if newExpression[0] == '+': newExpression = newExpression[1:]
                            distributeStep = createMainStep(r'\text{Distribute Parentheses}',
                                                            f'{latexify(term)}={latexify(newExpression)}')

                            newExpression = Expression(newExpression)
                            Simplification = simplifyExpression(newExpression)
                            # ADD STEPS
                            steps = [distributeStep] + Simplification['steps']
                            simplification = parseLatex(Simplification['finalResult'])

                            # CREATE E-STEP
                            heading = f'{term}={simplification}'
                            e_step = createExpandableStep(latexify(f"{heading}"), steps)
                            if steps != []: Steps.append(e_step)

                            expression = Expression(expression.replace(str(term), simplification))
                    if numberOfTermsInParen > 1:
                        if termsNotInParen != '':
                            cpyTerm = term
                            termToMultiply = termsNotInParen
                            if '*' in termToMultiply:
                                multipliedTerm = getProduct2(termToMultiply.split('*'))
                                if termToMultiply != multipliedTerm:
                                    mainStep = createMainStep(r'\text{Multiply Terms (left to right)}',
                                                              latexify(f'{termToMultiply}={multipliedTerm}'))
                                    Steps.append(mainStep)
                                    if keyword == 'expand':
                                        delimiter = ''
                                    else:
                                        delimiter = ''
                                    term = f"{multipliedTerm}{joinList(termsInParen, delimiter)}"
                                    expression = Expression(expression.replace(str(cpyTerm), term))
                                    """ SIMPLIFY multipliedTerm """
                                    steps = []
                                    simplifiedTermToMultiply = str(
                                        simplifyImplicitProduct(Expression(multipliedTerm), steps))

                                    if simplifiedTermToMultiply != multipliedTerm:
                                        # CREATE E-STEP
                                        heading = f'{multipliedTerm}={simplifiedTermToMultiply}'
                                        e_step = createExpandableStep(latexify(f"{heading}"), steps)
                                        if steps != []: Steps.append(e_step)
                                        if simplifiedTermToMultiply == '1': simplifiedTermToMultiply = ''
                                        # if simplifiedTermToMultiply[0] == '1': simpl
                                        term = term.replace(multipliedTerm, simplifiedTermToMultiply)
                                        expression = Expression(
                                            expression.replace(multipliedTerm, simplifiedTermToMultiply))
                                        # COMBINE RESULTS STEP
                                        mainStep = createMainStep(r'\text{Combine Result}',
                                                                  latexify(f"{cpyTerm}={term}"))
                                        Steps.append(mainStep)

                                    if keyword == 'expand':
                                        termsToBeMultiplied = joinList(termsInParen, '')
                                        simplifiedTermsToBeMultiplied = distributeTerms(termsToBeMultiplied, Steps)
                                        expression = Expression(expression.replace(joinList(termsInParen, ''),
                                                                                   f"*({str(simplifiedTermsToBeMultiplied)})"))
                                        return simplifyExpression(expression, keyword, Steps, finalResult=finalResult)

                        else:
                            termsToBeMultiplied = joinList(termsInParen, '')
                            simplifiedTermsToBeMultiplied = distributeTerms(termsToBeMultiplied, Steps)
                            expression = Expression(
                                expression.replace(joinList(termsInParen, '*'), str(simplifiedTermsToBeMultiplied)))
                else:
                    if term[0] == '-': term = term[1:]
                    termsToBeMultiplied = term.split('*')
                    """ MOVE RADICALS TO THE BACK """
                    for i in range(len(termsToBeMultiplied)):
                        if termsToBeMultiplied[i][0:4] == 'sqrt':
                            termsToBeMultiplied.append(termsToBeMultiplied.pop(i))
                    if listIsInt(termsToBeMultiplied):
                        solution = product(termsToBeMultiplied)
                        productStep = createMainStep(r'\text{Multiply And Divide (left to right)}',
                                                     latexify(f'{term}={solution}'))
                        Steps.append(productStep)
                        expression = expression.replace(str(term), str(solution))
                    else:
                        """ CHECK FOR FRACTIONS """
                        for item in termsToBeMultiplied:
                            if 'frac' in item:
                                numerators, denominators = [], []
                                for term2 in termsToBeMultiplied:
                                    if 'frac' in term2:
                                        frac = Fraction(term2)
                                        """ CHECK IF PARENTHESES NEEDS TO BE ADDED TO THE NUMERATOR AND/OR DENOMINATOR """
                                        if not Expression(frac.numerator).isSingleExpression():
                                            numerators.append(f'({frac.numerator})')
                                        else:
                                            numerators.append(f'{frac.numerator}')

                                        if not Expression(frac.denominator).isSingleExpression():
                                            denominators.append(f'({frac.denominator})')
                                        else:
                                            denominators.append(f'{frac.denominator}')

                                    else:
                                        numerators.append(Fraction(term2).numerator)
                                        denominators.append(Fraction(term2).denominator)

                                numeratorProduct = joinList(numerators, '*')
                                denominatorProduct = joinList(denominators, '*')

                                productExpression = f"frac{'{'}{numeratorProduct}{'}'}{'{'}{denominatorProduct}{'}'}"

                                mainStep = createMainStep(
                                    r'\text{Convert Numbers To Fractions and Multiply Left To Right}',
                                    latexify(f"{term}={productExpression}"))
                                Steps.append(mainStep)

                                newExpression = expression.replace(str(term), productExpression)
                                return simplifyExpression(newExpression, keyword, Steps, finalResult=finalResult)

                        solution = getProduct2(termsToBeMultiplied)
                        productStep = createMainStep(r'\text{Multiply And Divide (left to right)}',
                                                     latexify(f'{term}={solution}'))
                        if str(term) != solution:
                            Steps.append(productStep)
                        expression = expression.replace(str(term), solution)
                    expression = Expression(expression)

                # Steps.append(createMainStep(r'\text{Combine Results}', latexify(f'{expression}')))
            else:
                pass

        expression = simplifyImplicitProduct(expression, Steps)

    expression = Expression(expression.replace('+-', '-').replace('++', '+').replace('--', '+'))

    if groupedTerms is None: groupedTerms = expression.getGroupedTerms()

    if keyword == 'combine':
        """ CONVERT ALL TERMS TO FRACTION """
        groupedTerms = createGroupedTermsDict()
        for term in expression.getTerms():
            if type(term) != Fraction:
                term = Fraction(str(term))
            groupedTerms['Fractions'].append(term)

    groupedExpressions = expression.getGroupedExpressions()

    isSingleGroup = False
    if finalResult == None: finalResult = ''

    """ GROUP TERMS """
    if len(groupedExpressions['list']) == 1:
        isSingleGroup = True

    if not isSingleGroup and str(expression) != groupedExpressions['strWithoutParen']:
        mainStep = createMainStep(r"\text{Group Terms}",
                                  rf"\displaystyle {latexify(expression)}={latexify(groupedExpressions['strWithoutParen'])}")
        Steps.append(mainStep)

    """ SIMPLIFY GROUPS """
    for group in groupedTerms:
        if groupedTerms[group] != []:
            if group == 'Exponential':
                simplifiedExponentials = []
                for exponential in groupedTerms['Exponential']:
                    base = Expression(exponential.base)
                    exponent = Expression(exponential.exponent)
                    coefficient = exponential.coefficient
                    if coefficient == '1': coefficient = ''

                    if base.isSingleExpression():
                        tmp_base = str(base)
                        pattern = re.compile(r'^\(.+\)$')
                        matches = pattern.findall(str(tmp_base))

                        if len(matches) != 0:
                            tmp_base = tmp_base[1:-1]
                        tmp_base = Expression(tmp_base)
                        if len(tmp_base.getGroupedTerms()['Radicals']) == 1 and len(tmp_base) == 1:
                            radical = tmp_base.getGroupedTerms()['Radicals'][0]
                            if str(radical.index) == str(exponent):
                                steps = []
                                exponentialRuleStepInfo = latexify(f'{exponential}={radical.getRadicand()}')
                                if exponentialRuleStepInfo[0] == '+': exponentialRuleStepInfo = exponentialRuleStepInfo[
                                                                                                1:]
                                exponentialRuleStep = createMainStep(
                                    r'\text{Apply exponential rule:}\ (\sqrt[n]{a})^n=a', exponentialRuleStepInfo)
                                steps.append(exponentialRuleStep)
                                base = Expression(str(radical.getRadicand()))
                                simplifiedBase = simplifyExpression(base)
                                # ADD STEPS
                                for step in simplifiedBase['steps']:
                                    if step['type'] == 'main-step':
                                        steps.append(step)
                                    elif step['type'] == 'e-step':
                                        for e_step in step['e-steps']:
                                            steps.append(e_step)
                                simplification = simplifiedBase['finalResult']
                                # CREATE AND ADD E-STEP
                                heading = latexify(f"{radical}={simplification}")
                                if heading[0] == '+' or heading[0] == '-': heading = heading[1:]
                                e_step = createExpandableStep(heading, steps)
                                if steps != []: Steps.append(e_step)
                                # UPDATE FINAL RESULT
                                sign = radical[0]
                                if (sign != '+' and sign != '-'): sign = '+'
                                finalResult += f'{sign}{simplification}'
                                break
                            else:
                                base = Expression(exponential.base)

                    if exponential.isSimplified():
                        steps = []
                        # COMPUTATION STEP
                        solutionToExponential = exponential.computeExponential()
                        if solutionToExponential != False and solutionToExponential.is_integer:
                            computationStep = createMainStep(r'\text{Compute Exponent}',
                                                             latexify(f'{exponential}={solutionToExponential}'))
                            if computationStep['info'][14] == '+' or computationStep['info'][14] == '-':
                                computationStep['info'] = computationStep['info'][15:]
                            steps.append(computationStep)
                            final_simplification = solutionToExponential
                            # CREATE AND ADD E-STEP
                            heading = latexify(f"{exponential}={solutionToExponential}")
                            if heading[0] == '+' or heading[0] == '-': heading = heading[1:]
                            e_step = createExpandableStep(heading, steps)
                            Steps.append(e_step)
                            # UPDATE FINAL RESULT
                            sign = final_simplification[0]
                            if (sign != '+' and sign != '-'): sign = '+'
                            finalResult += f'{sign}{final_simplification}'

                        else:
                            simplifiedExponentials.append(exponential)

                    else:
                        redundantParenMatches = redundantParenPattern.findall(str(base))
                        if len(redundantParenMatches) != 0:
                            base = base[1:-1]
                            exponential.base = str(base)
                        """ SIMPLIFY BASE """
                        simplifiedBase = simplifyExpression(base)
                        # CREATE E-STEPS
                        steps = []
                        for step in simplifiedBase['steps']:
                            if step['type'] == 'main-step':
                                steps.append(step)
                            elif step['type'] == 'e-step':
                                for e_step in step['e-steps']:
                                    steps.append(e_step)

                        base_simplification = Exponential(
                            f"{coefficient}({parseLatex(simplifiedBase['finalResult'])})^{'{'}{exponent}{'}'}")
                        base_simplification.format()
                        # SIMPLIFICATION STEP #1
                        simplificationStepInfo = latexify(f"{exponential}={base_simplification}")
                        if simplificationStepInfo[0] == '+' or simplificationStepInfo[
                            0] == '-': simplificationStepInfo = simplificationStepInfo[1:]
                        simplificationStep = createMainStep(r'\text{Simplify Base}', simplificationStepInfo)
                        temp_exponential = exponential
                        if temp_exponential[0] == '+': temp_exponential = temp_exponential[1:]
                        if str(temp_exponential) != str(base_simplification): steps.append(simplificationStep)

                        """ SIMPLIFY EXPONENT """
                        simplifiedExponent = simplifyExpression(exponent)
                        for step in simplifiedExponent['steps']:
                            if step['type'] == 'main-step':
                                steps.append(step)
                            elif step['type'] == 'e-step':
                                for e_step in step['e-steps']:
                                    steps.append(e_step)

                        exponent_simplification = Exponential(
                            f"{coefficient}{base_simplification.base}^{'{'}{parseLatex(simplifiedExponent['finalResult'])}{'}'}")
                        exponent_simplification.format()
                        # SIMPLIFICATION STEP #2
                        simplificationStepInfo = latexify(f"{base_simplification}={exponent_simplification}")
                        if simplificationStepInfo[0] == '+': simplificationStepInfo = simplificationStepInfo[1:]
                        simplificationStep = createMainStep(r'\text{Simplify Exponent}', simplificationStepInfo)
                        temp_exponent = exponent
                        if temp_exponent[0] == '+': temp_exponent = temp_exponent[1:]
                        if latexify(temp_exponent) != latexify(exponent_simplification.exponent): steps.append(
                            simplificationStep)

                        final_simplification = exponent_simplification

                        # COMPUTATION STEP
                        solutionToFinalExponential = final_simplification.computeExponential()
                        if solutionToFinalExponential != False and solutionToFinalExponential.is_integer:
                            finalStep = createMainStep(r'\text{Compute Exponential}',
                                                       latexify(f'{final_simplification}={solutionToFinalExponential}'))
                            steps.append(finalStep)
                            final_simplification = Exponential(solutionToFinalExponential)
                        else:
                            if str(final_simplification.exponent) == '0':
                                finalStep = createMainStep(r'\text{Apply exponent rule:}\ a^0=1',
                                                           latexify(f'{final_simplification}=1'))
                                steps.append(finalStep)
                                final_simplification = Exponential('1')
                            if str(final_simplification.base) == '0':
                                finalStep = createMainStep(r'\text{Apply exponent rule:}\ 0^a=0',
                                                           latexify(f'{final_simplification}=0'))
                                steps.append(finalStep)
                                final_simplification = Exponential('0')

                        if not Constant(str(final_simplification)).is_digit:
                            simplifiedExponentials.append(final_simplification)
                        else:
                            # UPDATE FINAL RESULT
                            sign = exponential[0]
                            if (sign != '+' and sign != '-'): sign = '+'
                            finalResult += f'{sign}{final_simplification}'

                        # CREATE AND ADD E-STEP
                        heading = latexify(f"{exponential}={final_simplification}")
                        if heading[0] == '+': heading = heading[1:]
                        e_step = createExpandableStep(heading, steps)
                        Steps.append(e_step)

                originalExponentialStr = getExponentialStr(groupedTerms['Exponential'])
                if len(simplifiedExponentials) > 0:
                    simplifiedExponentialStr = getExponentialStr(simplifiedExponentials)

                    if (originalExponentialStr != simplifiedExponentialStr) and len(simplifiedExponentials) > 1:
                        # COMBINE RESULTS STEP
                        Steps.append(createMainStep(r'\text{Combine Exponentials}',
                                                    latexify(f'{originalExponentialStr}={simplifiedExponentialStr}')))
                    finalSimplification = addExponentials(simplifiedExponentials)
                    if finalSimplification[0] == '+': finalSimplification = finalSimplification[1:]
                    # GROUP LIKE EXPONENTIALS STEP
                    groupedExponentials = groupLikeExponentials(simplifiedExponentials)
                    if groupedExponentials[0] == '+': groupedExponentials = groupedExponentials[1:]
                    groupExpStep = createMainStep(r'\text{Group Like Exponentials}',
                                                  latexify(f'{simplifiedExponentialStr}={groupedExponentials}'))
                    if simplifiedExponentialStr != groupedExponentials: Steps.append(groupExpStep)

                    # ADDITION STEP
                    additionStepInfo = latexify(f'{groupedExponentials}={finalSimplification}')
                    additionStep = createMainStep(r'\text{Add Like Exponentials}', additionStepInfo)
                    if str(simplifiedExponentialStr) != str(finalSimplification): Steps.append(additionStep)
                    # UPDATE FINAL RESULT
                    sign = finalSimplification[0]
                    if (sign != '+' and sign != '-'): sign = '+'
                    if finalSimplification[0] != '-':
                        finalResult += f'{sign}{finalSimplification}'
                    else:
                        finalResult += f'{sign}{finalSimplification[1:]}'

            elif group == 'Radicals':
                """ SIMPLIFY RADICALS """
                Radicals = groupedTerms['Radicals']
                for radical in Radicals:
                    if radical.coefficient[0] == '-': radical.coefficient = radical.coefficient[1:]
                    if radical.coefficient == '1': radical.coefficient = ''

                    radicalSimplified = False
                    radicand = radical.getRadicand()
                    if radicand.isSingleExpression():
                        if len(radicand.getGroupedTerms()['Exponential']) > 0:
                            radicand = radicand.getGroupedTerms()['Exponential'][0]
                            if radical.index == radicand.exponent:
                                steps = []
                                radicalRuleStepInfo = latexify(f'{radical}={radicand.base}')
                                if radicalRuleStepInfo[0] == '+': radicalRuleStepInfo = radicalRuleStepInfo[1:]
                                radicalRuleStep = createMainStep(r'\text{Apply radical rule:}\ \sqrt[n]{a^n}=a',
                                                                 radicalRuleStepInfo)
                                steps.append(radicalRuleStep)
                                radicand = Expression(str(radicand.base))
                                simplifiedRadicand = simplifyExpression(radicand)
                                # ADD STEPS
                                for step in simplifiedRadicand['steps']:
                                    if step['type'] == 'main-step':
                                        steps.append(step)
                                    elif step['type'] == 'e-step':
                                        for e_step in step['e-steps']:
                                            steps.append(e_step)
                                simplification = simplifiedRadicand['finalResult']
                                # CREATE AND ADD E-STEP
                                heading = latexify(f"{radical}={simplification}")
                                if heading[0] == '+' or heading[0] == '-': heading = heading[1:]
                                e_step = createExpandableStep(heading, steps)
                                if steps != []: Steps.append(e_step)
                                # UPDATE FINAL RESULT
                                sign = radical[0]
                                if (sign != '+' and sign != '-'): sign = '+'
                                finalResult += f'{sign}{simplification}'

                                radicalSimplified = True

                            else:
                                radicand = Expression(str(radicand))

                    if not radicalSimplified:
                        simplifiedRadicand = simplifyExpression(radicand)
                        # ADD STEPS
                        steps = []
                        for step in simplifiedRadicand['steps']:
                            if step['type'] == 'main-step':
                                steps.append(step)
                            elif step['type'] == 'e-step':
                                for e_step in step['e-steps']:
                                    steps.append(e_step)

                        simplification = f"{radical.coefficient}sqrt[{radical.index}]{'{'}{parseLatex(simplifiedRadicand['finalResult'])}{'}'}"
                        # SIMPLIFICATION STEP
                        simplificationStepInfo = latexify(f"{radical}={simplification}")
                        if simplificationStepInfo[0] == '+' or simplificationStepInfo[
                            0] == '-': simplificationStepInfo = simplificationStepInfo[1:]
                        simplificationStep = createMainStep(r'\text{Simplify}', simplificationStepInfo)
                        temp_radical = radical
                        if temp_radical[0] == '+' or temp_radical[0] == '-': temp_radical = temp_radical[1:]
                        if latexify(temp_radical) != latexify(simplification): steps.append(simplificationStep)
                        # COMPUTATION STEP
                        finalRadical = Radical(simplification)
                        solutionToFinalRadical = finalRadical.computeRadical()
                        if solutionToFinalRadical != False and solutionToFinalRadical.is_integer:
                            if finalRadical.coefficient == '1':
                                finalStep = createMainStep(r'\text{Compute Radical}',
                                                           latexify(f'{simplification}={solutionToFinalRadical}'))
                                steps.append(finalStep)
                                simplification = solutionToFinalRadical
                            else:
                                finalRadical.coefficient = Constant(finalRadical.coefficient)
                                if finalRadical.coefficient.is_digit:
                                    finalStep = createMainStep(r'\text{Compute Radical}',
                                                               latexify(
                                                                   f'{simplification}={finalRadical.coefficient}*{solutionToFinalRadical}'))
                                    steps.append(finalStep)
                                    simplification = f'{finalRadical.coefficient}*{solutionToFinalRadical}'
                                else:
                                    finalStep = createMainStep(r'\text{Compute Radical}',
                                                               latexify(
                                                                   f'{simplification}={solutionToFinalRadical}{finalRadical.coefficient}'))
                                    steps.append(finalStep)
                                    simplification = f'{solutionToFinalRadical}{finalRadical.coefficient}'
                        else:
                            index = Constant(finalRadical.index)
                            radicand = Constant(str(finalRadical.getRadicand()))

                            if radicand.is_integer and index.is_integer:
                                index, radicand = int(str(index)), int(str(radicand))
                                mpp = getMaxPerfectPower(index, radicand)
                                if mpp != 1 and mpp != radicand:
                                    # FACTOR STEP
                                    factoredResult = f"sqrt[{index}]{'{'}{mpp}{'}'}*sqrt[{index}]{'{'}{radicand // mpp}{'}'}"
                                    factorStepInfo = latexify(f"{finalRadical}={factoredResult}")
                                    factorStep = createMainStep(r'\text{Factor Radical}', factorStepInfo)
                                    steps.append(factorStep)
                                    # SIMPLIFICATION STEP 2
                                    firstFactorOfRadical = Radical(f"sqrt[{index}]{'{'}{mpp}{'}'}")
                                    secondFactorOfRadical = Radical(f"sqrt[{index}]{'{'}{radicand // mpp}{'}'}")
                                    simplificationStepInfo = latexify(
                                        f"{factoredResult}={firstFactorOfRadical.computeRadical()}{secondFactorOfRadical}")
                                    simplificationStep = createMainStep(r'\text{Simplify}', simplificationStepInfo)
                                    steps.append(simplificationStep)
                                    simplification = f"{firstFactorOfRadical.computeRadical()}{secondFactorOfRadical}"

                        # CREATE AND ADD E-STEP
                        heading = latexify(f"{radical}={simplification}")
                        if heading[0] == '+' or heading[0] == '-': heading = heading[1:]
                        e_step = createExpandableStep(heading, steps)
                        if steps != []: Steps.append(e_step)
                        # UPDATE NEW GROUPED TERMS AND FINAL RESULT
                        sign = radical[0]
                        if (sign != '+' and sign != '-'): sign = '+'
                        finalResult += f'{sign}{simplification}'

            elif group == 'Fractions':
                simplifiedFractions = []
                for fraction in groupedTerms['Fractions']:
                    """ CONSTANT TIMES A FRACTIONS """
                    fractionProductPattern = re.compile('\w+frac')
                    matches = fractionProductPattern.findall(str(fraction))
                    if len(matches) > 0:
                        termToMultiply = matches[0][:-4]
                        frac = Fraction(str(fraction)[len(termToMultiply):])
                        fraction = Fraction(
                            f"frac{'{'}{termToMultiply}{frac.numerator}{'}'}{'{'}{frac.denominator}{'}'}")

                    numerator = Expression(fraction.numerator)
                    denominator = Expression(fraction.denominator)

                    # if numerator[0] == '-' and len(numerator) == 1:
                    #     # PARSE frac{-5}{10} as -frac{5}{10}
                    #     fraction = Fraction(f"-frac{'{'}{numerator[1:]}{'}'}{'{'}{denominator}{'}'}")
                    #     numerator = Expression(fraction.numerator)
                    # elif (denominator[0] == '-' and len(denominator) == 1):
                    #     fraction = Fraction(f"-frac{'{'}{numerator}{'}'}{'{'}{denominator[1:]}{'}'}")
                    #     denominator = Expression(fraction.denominator)

                    """ SIMPLIFY NUMERATOR """
                    simplifiedNumerator = simplifyExpression(numerator)
                    # CREATE E-STEPS
                    steps = []
                    for step in simplifiedNumerator['steps']:
                        if step['type'] == 'main-step':
                            steps.append(step)
                        elif step['type'] == 'e-step':
                            for e_step in step['e-steps']:
                                steps.append(e_step)

                    numerator_simplification = Fraction(f"frac{'{'}{parseLatex(simplifiedNumerator['finalResult'])}{'}'}{'{'}{denominator}{'}'}")
                    # SIMPLIFICATION STEP 1
                    simplificationStepInfo = latexify(f"{fraction}={numerator_simplification}")
                    if simplificationStepInfo[0] == '+' or simplificationStepInfo[0] == '-': simplificationStepInfo = simplificationStepInfo[1:]
                    simplificationStep = createMainStep(r'\text{Simplify Numerator}', simplificationStepInfo)
                    temp_fraction = parseLatex(fraction)
                    if temp_fraction[0] == '+' or temp_fraction[0] == '-': temp_fraction = temp_fraction[1:]
                    if (str(temp_fraction) != str(
                        numerator_simplification)) and fraction.denominator != '1': steps.append(simplificationStep)

                    """ SIMPLIFY DENOMINATOR """
                    simplifiedDenominator = simplifyExpression(denominator)
                    # CREATE E-STEPS
                    for step in simplifiedDenominator['steps']:
                        if step['type'] == 'main-step':
                            steps.append(step)
                        elif step['type'] == 'e-step':
                            for e_step in step['e-steps']:
                                steps.append(e_step)

                    denominator_simplification = Fraction(f"frac{'{'}{numerator_simplification.numerator}{'}'}{'{'}{parseLatex(simplifiedDenominator['finalResult'])}{'}'}")
                    # SIMPLIFICATION STEP 2
                    simplificationStepInfo = latexify(f"{numerator_simplification}={denominator_simplification}")
                    if simplificationStepInfo[0] == '+' or simplificationStepInfo[
                        0] == '-': simplificationStepInfo = simplificationStepInfo[1:]
                    simplificationStep = createMainStep(r'\text{Simplify Denominator}', simplificationStepInfo)
                    temp_fraction = numerator_simplification
                    if temp_fraction[0] == '+' or temp_fraction[0] == '-': temp_fraction = temp_fraction[1:]
                    if str(temp_fraction) != str(denominator_simplification): steps.append(simplificationStep)

                    simplifiedFraction = denominator_simplification

                    # if len(Expression(simplifiedFraction.numerator)) == 1 and simplifiedFraction.numerator[0] == '-':
                    #     simplifiedFraction = Fraction(f"-frac{'{'}{simplifiedFraction.numerator[1:]}{'}'}{'{'}{simplifiedFraction.denominator}{'}'}")

                    # COMPUTATION STEP
                    fractionSplit = False
                    solutionToFraction = simplifiedFraction.computeFraction(True)
                    if solutionToFraction != False and type(solutionToFraction) == Fraction:
                        computationStep = createMainStep(r'\text{Reduce Fraction}',
                                                         latexify(f'{simplifiedFraction}={solutionToFraction}'))
                        steps.append(computationStep)
                        final_simplification = solutionToFraction
                    elif solutionToFraction != False and solutionToFraction.is_integer:
                        computationStep = createMainStep(r'\text{Divide The Numbers}',
                                                         latexify(f'{simplifiedFraction}={solutionToFraction}'))
                        steps.append(computationStep)
                        final_simplification = solutionToFraction
                    else:
                        if len(Expression(str(simplifiedFraction.denominator))) == 1:
                            numerator = Expression(simplifiedFraction.numerator)
                            denominator = Expression(simplifiedFraction.denominator)

                            numeratorTerms = numerator.getTerms()

                            """ SPLIT FRACTION """
                            if keyword == 'expand':
                                newFractions = []
                                if len(denominator) == 1:
                                    for n_term in numeratorTerms:
                                        if n_term[0] == '+' or n_term[0] == '-':
                                            sign = n_term[0]
                                            n_term = n_term[1:]
                                            newFraction = Fraction(
                                                f"{sign}frac{'{'}{n_term}{'}'}{'{'}{denominator}{'}'}")
                                            newFractions.append(newFraction)
                                        else:
                                            newFraction = Fraction(f"frac{'{'}{n_term}{'}'}{'{'}{denominator}{'}'}")
                                            newFractions.append(newFraction)

                                splitFractions = ''
                                for frac in newFractions:
                                    splitFractions += str(frac)
                                splitFractions = Expression(splitFractions)

                                splitFractionStepInfo = latexify(f'{simplifiedFraction}={splitFractions}')
                                splitFractionStep = createMainStep(
                                    r'\text{Apply The Fraction Rule:}\ \frac{a \pm b}{c}=\frac{a}{c}\pm\frac{b}{c}',
                                    splitFractionStepInfo)
                                if str(simplifiedFraction) != str(splitFractions):
                                    steps.append(splitFractionStep)
                                    fractionSplit = True

                            else:
                                splitFractions = Expression(str(simplifiedFraction))
                            """ DIVIDE FRACTIONS """
                            simplifiedSplitFractions = ''
                            divideFractionSteps = []
                            for split_fraction in splitFractions.getTerms():
                                sign = split_fraction[0]
                                if (sign != '+' and sign != '-'): sign = '+'
                                split_fraction = Fraction(str(split_fraction))
                                if len(Expression(split_fraction.numerator)) != 1 or len(
                                        Expression(split_fraction.denominator)) != 1:
                                    break
                                numerator, denominator = Exponential(split_fraction.numerator,
                                                                     CETAEIOCF=True), Exponential(
                                    split_fraction.denominator, CETAEIOCF=True)
                                if numerator.base == denominator.base:
                                    base = numerator.base
                                    if Constant(numerator.exponent).is_integer and Constant(
                                            denominator.exponent).is_integer:
                                        differenceInExp = int(numerator.exponent) - int(denominator.exponent)
                                        if differenceInExp == 0:
                                            simplifiedFraction = Fraction(
                                                f"frac{'{'}{numerator.coefficient}{'}'}{'{'}{denominator.coefficient}{'}'}")
                                            # if simplifiedFraction.computeFraction() != False:
                                            #     simplifiedFraction = simplifiedFraction.computeFraction()
                                            if simplifiedFraction.denominator == '1': simplifiedFraction = simplifiedFraction.numerator
                                            simplifiedSplitFractions += f"{sign}{simplifiedFraction}"
                                        elif differenceInExp > 0:
                                            numExponent = int(numerator.exponent) - int(denominator.exponent)
                                            simplifiedFraction = Fraction(
                                                f"frac{'{'}{numerator.coefficient}{base}^{'{'}{numExponent}{'}'}{'}'}{'{'}{denominator.coefficient}{'}'}")
                                            simplifiedSplitFractions += f"{sign}{simplifiedFraction}"
                                        else:
                                            numExponent = abs(int(numerator.exponent) - int(denominator.exponent))
                                            simplifiedFraction = Fraction(
                                                f"frac{'{'}{numerator.coefficient}{'}'}{'{'}{denominator.coefficient}{base}^{numExponent}{'}'}")
                                            simplifiedSplitFractions += f"{sign}{simplifiedFraction}"
                                else:
                                    simplifiedFraction = str(split_fraction)
                                    simplifiedSplitFractions += str(split_fraction)

                                if simplifiedFraction[0] == '+' or simplifiedFraction[
                                    0] == '-': simplifiedFraction = simplifiedFraction[1:]
                                # ADD CANCEL LIKE TERMS STEP
                                simplifiedFractionStepInfo = latexify(f'{split_fraction}={simplifiedFraction}')
                                if simplifiedFractionStepInfo[0] == '+' or simplifiedFractionStepInfo[
                                    0] == '-': simplifiedFractionStepInfo = simplifiedFractionStepInfo[1:]
                                simplifiedFractionStep = createMainStep(r'\text{Cancel like terms}',
                                                                        simplifiedFractionStepInfo)
                                tmp_fraction = split_fraction
                                if tmp_fraction[0] == '+' or tmp_fraction[0] == '-': tmp_fraction = tmp_fraction[1:]
                                if str(tmp_fraction) != str(simplifiedFraction): divideFractionSteps.append(
                                    simplifiedFractionStep)

                            if simplifiedSplitFractions == '': simplifiedSplitFractions = simplifiedFraction

                            # ADD DIVIDE FRACTION STEP
                            if simplifiedSplitFractions[0] == '+': simplifiedSplitFractions = simplifiedSplitFractions[
                                                                                              1:]
                            heading = latexify(f'{splitFractions}={simplifiedSplitFractions}')
                            divideFractionStepEStep = createExpandableStep(heading, divideFractionSteps)
                            if str(splitFractions) != str(simplifiedSplitFractions): steps.append(
                                divideFractionStepEStep)

                            final_simplification = simplifiedSplitFractions

                        else:
                            final_simplification = simplifiedFraction

                    # CREATE AND ADD E-STEP
                    cmp_fraction = parseLatex(fraction)
                    if cmp_fraction[0] == '+' or cmp_fraction[0] == '-': cmp_fraction = cmp_fraction[1:]
                    heading = latexify(f"{fraction}={final_simplification}")
                    if heading[0] == '+' or heading[0] == '-': heading = heading[1:]
                    e_step = createExpandableStep(heading, steps)
                    if str(cmp_fraction) != str(final_simplification):
                        Steps.append(e_step)
                    # UPDATE FINAL RESULT
                    sign = fraction[0]
                    if (sign != '+' and sign != '-'): sign = '+'
                    if keyword == 'combine': simplifiedFractions.append(Fraction(f'{sign}{final_simplification}'))
                    if fractionSplit and sign == '-':
                        finalResult += f'{sign}({final_simplification})'
                    else:
                        finalResult += f'{sign}{final_simplification}'

                if keyword == 'combine':
                    """ GET SUM OF FRACTIONS STRING """
                    fractionSumStr = ''
                    for frac in simplifiedFractions:
                        fractionSumStr += str(frac)
                    if fractionSumStr[0] == '+': fractionSumStr = fractionSumStr[1:]

                    denominators = [f.denominator if len(Expression(f.denominator)) == 1 else f'({f.denominator})' for f
                                    in simplifiedFractions]
                    termsType = 'Numbers'
                    seenDigitTerm = True
                    for term in denominators:
                        if Constant(term).is_digit and not seenDigitTerm:
                            termsType = 'Mixed'
                            break
                        if not Constant(term).is_digit:
                            termsType = 'Variables'
                            seenDigitTerm = False

                    if termsType == 'Mixed':
                        lcm = getLCM(denominators, listOfNumbers=False, termsType=termsType)
                    elif termsType == 'Variables':
                        lcm = getLCM(denominators, termsType=termsType)
                        if lcm[0] == '1': lcm = lcm[1:]
                        if lcm[-1] == '1': lcm = lcm[:-1]
                    else:
                        denominators = [int(f.denominator) for f in simplifiedFractions]
                        lcm = getLCM(denominators, listOfNumbers=True)

                    """ ADJUST FRACTIONS """
                    adjustedFractions = []
                    for frac in simplifiedFractions:
                        sign = frac.expression[0]
                        if not seenDigitTerm:
                            if frac.denominator[0] != '(' and len(Expression(frac.denominator)) > 1: frac.denominator = f'({frac.denominator})'
                            if len(Expression(frac.denominator)) == 1:
                                if '^' not in frac.denominator and '^' not in lcm:
                                    exp_denominator = Exponential(frac.denominator, cast_entire_term_as_exp=True)
                                    exp_lcm = Exponential(lcm, cast_entire_term_as_exp=True)
                                else:
                                    exp_denominator = Exponential(frac.denominator, CETAEIOCF=True)
                                    exp_lcm = Exponential(lcm, CETAEIOCF=True)

                                if exp_denominator.base == exp_lcm.base:
                                    lcmFactorExponentExpression = Expression(f'{Exponential(lcm).exponent}-{Exponential(frac.denominator).exponent}')
                                    lcmFactorExponentExpression = simplifyExpression(lcmFactorExponentExpression)['finalResult']
                                    if lcmFactorExponentExpression == '0':
                                        if str(exp_lcm) == str(exp_denominator):
                                            lcmFactor = '1'
                                        else:
                                            lcmFactor = f'{exp_lcm.coefficient}'
                                    else:
                                        lcmFactor = f"{Exponential(frac.denominator).base}^{'{'}{lcmFactorExponentExpression}{'}'}"
                                else:
                                    lcmFactor = getLCMFactor(frac.denominator, denominators)
                                if lcmFactor[0] == '1' and len(lcmFactor) > 1 and not Constant(lcmFactor).is_digit: lcmFactor = lcmFactor[1:]
                                if len(lcmFactor) > 1:
                                    if lcmFactor[-1] == '1': lcmFactor = lcmFactor[:-1]
                            else:
                                lcmFactor = getLCMFactor(f'({frac.denominator})', denominators)

                            if frac.numerator != '1':
                                if lcmFactor == '1': lcmFactor = ''
                                if len(Expression(frac.numerator)) == 1:
                                    adjustedFrac = Fraction(f"{sign}frac{'{'}{frac.numerator}{lcmFactor}{'}'}{'{'}{lcm}{'}'}")
                                else:
                                    adjustedFrac = Fraction(f"{sign}frac{'{'}({frac.numerator}){lcmFactor}{'}'}{'{'}{lcm}{'}'}")
                            else:
                                if numOccurrences(lcmFactor, '(') == 1 and Exponential(lcmFactor).exponent == '1':
                                    lcmFactor = Exponential(lcmFactor).base[1:-1]  # REMOVE UNNECESSARY PARENTHESES
                                adjustedFrac = Fraction(f"{sign}frac{'{'}{lcmFactor}{'}'}{'{'}{lcm}{'}'}")
                        else:
                            lcmFactor = lcm // int(frac.denominator)
                            if frac.numerator != '1':
                                if Constant(frac.numerator).is_digit:
                                    adjustedFrac = Fraction(
                                        f"{sign}frac{'{'}{int(frac.numerator) * lcmFactor}{'}'}{'{'}{lcm}{'}'}")
                                else:
                                    adjustedFrac = Fraction(f"{sign}frac{'{'}{lcmFactor}*{frac.numerator}{'}'}{'{'}{lcm}{'}'}")
                            else:
                                adjustedFrac = Fraction(f"{sign}frac{'{'}{lcmFactor}{'}'}{'{'}{lcm}{'}'}")

                        adjustedFractions.append(adjustedFrac)

                    adjustedFractionsStr = ''
                    for frac in adjustedFractions:
                        adjustedFractionsStr += str(frac)
                    if adjustedFractionsStr[0] == '+': adjustedFractionsStr = adjustedFractionsStr[1:]

                    # CREATE STEP
                    adjustFractionStepInfo = latexify(f"{fractionSumStr}={adjustedFractionsStr}")
                    adjustedFractionStep = createMainStep(r"\text{Adjust fractions based on their LCM of }" + latexify(str(lcm)), adjustFractionStepInfo)
                    Steps.append(adjustedFractionStep)

                    """ COMBINE FRACTIONS """
                    combinedNumerator = ''
                    for frac in adjustedFractions:
                        sign = frac.expression[0]
                        combinedNumerator += f'{sign}{frac.numerator}'

                    if combinedNumerator[0] == '+': combinedNumerator = combinedNumerator[1:]
                    combinedFraction = Fraction(f"frac{'{'}{convertToStandardForm(combinedNumerator)}{'}'}{'{'}{lcm}{'}'}")

                    # combinedFraction.numerator = convertToStandardForm(combinedNumerator)

                    # CREATE STEP
                    combineFractionStepInfo = latexify(f"{adjustedFractionsStr}={combinedFraction}")
                    combineFractionStep = createMainStep(r"\text{Apply The Fraction Rule:}\ \frac{a}{c}\pm\frac{b}{c}=\frac{a \pm b}{c}", combineFractionStepInfo)
                    Steps.append(combineFractionStep)
                    # UPDATE FINAL RESULT
                    originalFractionStr = ''
                    for frac in groupedTerms['Fractions']:
                        originalFractionStr += str(frac)
                    checkReplacement = finalResult.replace(originalFractionStr, str(combinedFraction))
                    """ 
                    checkReplacement IS USED TO CHECK IF finalResult != originalFractionStr. IF THAT'S THE CASE, THERE
                    WAS AN INTERMEDIATE SIMPLIFICATION STEP THAT TOOK PLACE AND originalFractionStr IS NO LONGER IN finalResult
                    AND THIS WOULD CAUSE finalResult.replace(originalFractionStr, str(combinedFraction)) TO DO NOTHING SO WE HAVE
                    TO GET THE UPDATED (SIMPLIFIED) RESULT WHICH IS fractionSumStr AND USE THAT INSTEAD.
                    EXAMPLE WHERE THIS HAPPENS: frac{1}{2}+frac{2}{5}+frac{1}{7}+frac{3}{9}
                    """
                    if checkReplacement[0] == '+': checkReplacement = checkReplacement[1:]
                    if checkReplacement != fractionSumStr:
                        finalResult = finalResult.replace(originalFractionStr, str(combinedFraction))
                    else:
                        finalResult = finalResult.replace(fractionSumStr, str(combinedFraction))

            elif group == 'Constants':
                """ SIMPLIFY CONSTANTS """
                Constants = groupedTerms['Constants']
                constantsExpression = createEStepHeadingFromGroup(Constants, False)
                simplifiedExpression = constantsExpression

                """ HANDLE PARENTHESES """
                if 'sdfsd' in constantsExpression:
                    expression = Expression(constantsExpression)
                    specialFunction = str(expression[:indexOf(expression, '(')])
                    for i in range(len(str(expression))):
                        currentExpressionToEvaluate = ''
                        if expression[i] == '(' and i == expression.getIndexOfInnerMostParen():
                            j = i + 1
                            while j < len(str(expression)):
                                if expression[j] != ')':
                                    currentExpressionToEvaluate += expression[j]
                                else:
                                    break
                                j += 1

                            currentExpressionToEvaluate = Expression(currentExpressionToEvaluate)
                            Simplification = simplifyExpression(currentExpressionToEvaluate)
                            # ADD STEPS
                            # steps = []
                            # for step in Simplification['steps']:
                            #     if step['type'] == 'main-step':
                            #         steps.append(step)
                            #     elif step['type'] == 'e-step':
                            #         for e_step in step['e-steps']:
                            #             steps.append(e_step)

                            steps = Simplification['steps']
                            simplification = parseLatex(Simplification['finalResult'])
                            if simplification != str(currentExpressionToEvaluate):
                                # CREATE E-STEP
                                if specialFunction not in specialFunctions:
                                    heading = f'({currentExpressionToEvaluate})={simplification}'
                                else:
                                    heading = f'{currentExpressionToEvaluate}={simplification}'

                                e_step = createExpandableStep(latexify(f"{heading}"), steps)
                                if steps != []: Steps.append(e_step)
                                # COMBINE STEP
                                if j < len(str(expression)) - 1:
                                    if expression[j + 1] == '^':
                                        # HANDLE EXPONENTIALS
                                        if len(simplification) > 1:
                                            # TODO: CORRECT IF STATEMENT SHOULD BE: if len(Expression(simplification)) > 1 BUT WE HAVE 3(2x+x)^{3-1} AS AN EDGE CASE
                                            newExpression = expression.replace(f'({currentExpressionToEvaluate})',
                                                                               f'({simplification})')
                                        else:
                                            # RETURN (2)^x as 2^x
                                            newExpression = expression.replace(f'({currentExpressionToEvaluate})',
                                                                               simplification)
                                    else:
                                        if specialFunction not in specialFunctions:
                                            newExpression = expression.replace(f'({currentExpressionToEvaluate})',
                                                                               simplification)
                                        else:
                                            newExpression = expression.replace(f'{currentExpressionToEvaluate}',
                                                                               simplification)

                                else:
                                    if specialFunction not in specialFunctions:
                                        newExpression = expression.replace(f'({currentExpressionToEvaluate})',
                                                                           simplification)
                                    else:
                                        newExpression = expression.replace(f'{currentExpressionToEvaluate}',
                                                                           simplification)

                                Steps.append(createMainStep(r'\text{Simplify}',
                                                            latexify(f"{expression}={newExpression}")))

                                newExpression = Expression(newExpression)
                                return simplifyExpression(newExpression, keyword, Steps, finalResult=finalResult)

                if '(' in constantsExpression:
                    for k, const in enumerate(Constants):
                        if const[0] == '+': const = const[1:]
                        if '(' in const:
                            expression = Expression(str(const))
                            specialFunction = str(expression[:indexOf(expression, '(')])
                            indexesOfOpenParen = []
                            indexesOfClosedParen = []
                            for i in range(len(str(expression))):
                                if expression[i] == '(': indexesOfOpenParen.append(i)
                                if expression[i] == ')': indexesOfClosedParen.append(i)

                            indexesOfClosedParen = reverseList(indexesOfClosedParen)
                            expressionsInsideParen = []

                            if expression[0] == '(' and expression[-1] == ')':
                                expressionsInsideParen.append(str(expression))
                            else:
                                for i in range(len(indexesOfOpenParen)):
                                    start = indexesOfOpenParen[i] + 1
                                    end = indexesOfClosedParen[i]
                                    expressionsInsideParen.append(expression[start: end])

                            expressionsInsideParen = reverseList(expressionsInsideParen)

                            for expr in expressionsInsideParen:
                                # TODO: tanh(frac{3x^{2}+x^{2}+3+4}{3x+x+ln(x+2x+1)+1+2})
                                break
                                currentExpressionToEvaluate = expr

                                Simplification = simplifyExpression(currentExpressionToEvaluate)
                                # ADD STEPS

                                steps = Simplification['steps']
                                simplification = parseLatex(Simplification['finalResult'])
                                if simplification != str(currentExpressionToEvaluate):
                                    for i in range(len(expressionsInsideParen)):
                                        expressionsInsideParen[i] = expressionsInsideParen[i].replace(str(expr),
                                                                                                      simplification)
                                    # CREATE E-STEP
                                    if specialFunction not in specialFunctions:
                                        heading = f'({currentExpressionToEvaluate})={simplification}'
                                    else:
                                        heading = f'{currentExpressionToEvaluate}={simplification}'

                                    e_step = createExpandableStep(latexify(f"{heading}"), steps)
                                    if steps != []: Steps.append(e_step)

                                    if specialFunction not in specialFunctions:
                                        newExpression = simplifiedExpression.replace(f'({currentExpressionToEvaluate})',
                                                                                     simplification)
                                    else:
                                        newExpression = simplifiedExpression.replace(f'{currentExpressionToEvaluate}',
                                                                                     simplification)

                                    Steps.append(createMainStep(r'\text{Simplify}',
                                                                latexify(f"{simplifiedExpression}={newExpression}")))
                                    simplifiedExpression = simplifiedExpression.replace(
                                        str(currentExpressionToEvaluate), simplification)

                            for i in range(len(str(expression))):

                                currentExpressionToEvaluate = ''

                                if expression[i] == '(' and i == expression.getIndexOfInnerMostParen():
                                    if specialFunction in specialFunctions:
                                        if i - len(specialFunction) != 0:
                                            specialFunction = ''
                                    j = i + 1
                                    while j < len(str(expression)):
                                        if expression[j] != ')':
                                            currentExpressionToEvaluate += expression[j]
                                        else:
                                            break
                                        j += 1

                                    currentExpressionToEvaluate = Expression(currentExpressionToEvaluate)
                                    Simplification = simplifyExpression(currentExpressionToEvaluate)
                                    # ADD STEPS

                                    steps = Simplification['steps']
                                    simplification = parseLatex(Simplification['finalResult'])
                                    if simplification.replace(' ', '') != str(currentExpressionToEvaluate):
                                        # CREATE E-STEP
                                        if (specialFunction not in specialFunctions) and (')(' not in const):
                                            heading = f'({currentExpressionToEvaluate})={simplification}'
                                        else:
                                            heading = f'{currentExpressionToEvaluate}={simplification}'

                                        e_step = createExpandableStep(latexify(f"{heading}"), steps)
                                        if steps != []: Steps.append(e_step)
                                        # COMBINE STEP
                                        if j < len(str(expression)) - 1:
                                            if expression[j + 1] == '^':
                                                # HANDLE EXPONENTIALS
                                                if len(simplification) > 1:
                                                    # TODO: CORRECT IF STATEMENT SHOULD BE: if len(Expression(simplification)) > 1 BUT WE HAVE 3(2x+x)^{3-1} AS AN EDGE CASE
                                                    newExpression = expression.replace(
                                                        f'({currentExpressionToEvaluate})',
                                                        f'({simplification})')
                                                else:
                                                    # RETURN (2)^x as 2^x
                                                    newExpression = expression.replace(
                                                        f'({currentExpressionToEvaluate})',
                                                        simplification)
                                            else:
                                                if specialFunction not in specialFunctions:
                                                    newExpression = expression.replace(
                                                        f'({currentExpressionToEvaluate})',
                                                        simplification)
                                                else:
                                                    newExpression = expression.replace(f'{currentExpressionToEvaluate}',
                                                                                       simplification)

                                        else:
                                            if (specialFunction not in specialFunctions) and (')(' not in const):
                                                newExpression = expression.replace(f'({currentExpressionToEvaluate})',
                                                                                   simplification)
                                            else:
                                                newExpression = expression.replace(f'{currentExpressionToEvaluate}',
                                                                                   simplification)

                                        Steps.append(createMainStep(r'\text{Simplify}',
                                                                    latexify(f"{expression}={newExpression}")))
                                        simplifiedExpression = simplifiedExpression.replace(str(const), newExpression)

                        const = str(const)
                        specialFunction = str(const[:indexOf(const, '(')])
                        """ COMPUTE SPECIAL FUNCTIONS """
                        if specialFunction in getSpecialFunctions():
                            ln = math.log
                            sin = math.sin
                            csc = lambda x: 1 / sin(x)
                            cos = math.cos
                            sec = lambda x: 1 / cos(x)
                            tan = math.tan
                            cot = lambda x: 1 / tan(x)

                            specialFunctionArg = const[len(specialFunction) + 1:-1]
                            pi_multiplication_pattern = re.compile('\w+pi')
                            symbol_multiplication_matches = pi_multiplication_pattern.findall(specialFunctionArg)

                            if len(symbol_multiplication_matches) > 0:
                                matchStr = symbol_multiplication_matches[0]
                                constantMultiple = matchStr[:-2]
                                specialFunctionArg = specialFunctionArg.replace(matchStr, f'{constantMultiple}*pi')
                            else:
                                """ REPLACE sin(2*pi) with sin(2pi) SO THAT sin(2pi) CAN GET REPLACED WITH 0 IN simplifyExpression """
                                const = const.replace('*', '')

                            if isDigit(specialFunctionArg, considerSpecialNumbers=True):
                                if 'frac' in specialFunctionArg:
                                    sign = specialFunctionArg[0]
                                    if sign != '-': sign = ''
                                    specialFunctionArg = Fraction(specialFunctionArg)
                                    specialFunctionArg = f"{sign}({specialFunctionArg.numerator})/({specialFunctionArg.denominator})"

                                solution = str(eval(f"{specialFunction}({specialFunctionArg})"))
                                solution = formatSpecialValues(solution)
                                # CREATE MAIN STEP
                                mainStep = createMainStep(r'\text{Evaluate Function}', latexify(f'{const}={solution}'))
                                Steps.append(mainStep)
                                constantsExpression = constantsExpression.replace(const, solution).replace('+-', '-')
                                simplifiedExpression = simplifiedExpression.replace(const, solution).replace('+-', '-')
                                Constants[k] = Constant(Constants[k].replace(const, solution).replace('+-', '-'))

                    if simplifiedExpression != constantsExpression:
                        simplifiedExpression = Expression(simplifiedExpression)
                        return simplifyExpression(simplifiedExpression, keyword, Steps, finalResult=finalResult)

                """ HANDLE MULTIPLICATION """
                # TODO
                if 'sdfsd' in constantsExpression:
                    expression = Expression(constantsExpression)
                    newExpression = expression
                    for term in expression.getTerms():
                        if term[0] == '+' or term[0] == '-': term = term[1:]
                        if '*' in term and type(term) != Fraction:
                            if '(' in term:
                                # CONSTANT MULTIPLE
                                pattern = re.compile('[\w{}^+-]+\*\(')
                                matches = pattern.findall(str(term))
                                if len(matches) > 0:
                                    termToMultiply = matches[0].split('*')[0]
                                    expressionInParen = Expression(str(term)[len(termToMultiply) + 2:-1])
                                    newExpression = ''
                                    for term2 in expressionInParen.getTerms():
                                        if term2[0] == '+':
                                            newExpression += f'+{termToMultiply}*{term2[1:]}'
                                        elif term2[0] == '-':
                                            newExpression += f'-{termToMultiply}*{term2[1:]}'
                                        else:
                                            newExpression += f'{termToMultiply}*{term2}'

                                    distributeStep = createMainStep(r'\text{Distribute Parentheses}',
                                                                    f'{latexify(term)}={latexify(newExpression)}')

                                    newExpression = Expression(newExpression)
                                    Simplification = simplifyExpression(newExpression)
                                    # ADD STEPS
                                    steps = [distributeStep] + Simplification['steps']
                                    simplification = parseLatex(Simplification['finalResult'])

                                    # CREATE E-STEP
                                    heading = f'{term}={simplification}'
                                    e_step = createExpandableStep(latexify(f"{heading}"), steps)
                                    if steps != []: Steps.append(e_step)

                                    newExpression = Expression(expression.replace(str(term), simplification))
                                    return simplifyExpression(newExpression, keyword, Steps, finalResult=finalResult)


                            else:
                                termsToBeMultiplied = term.split('*')
                                if listIsInt(termsToBeMultiplied):
                                    solution = product(termsToBeMultiplied)
                                    productStep = createMainStep(r'\text{Multiply And Divide (left to right)}',
                                                                 latexify(f'{term}={solution}'))
                                    Steps.append(productStep)
                                    newExpression = expression.replace(str(term), str(solution))
                                else:
                                    # if Constant(str(Exponential(termsToBeMultiplied[0]).exponent)).is_digit and Constant(str(Exponential(termsToBeMultiplied[1]).exponent)).is_digit:
                                    solution = getProduct2(termsToBeMultiplied)
                                    productStep = createMainStep(r'\text{Multiply And Divide (left to right)}',
                                                                 latexify(f'{term}={solution}'))
                                    if str(term) != solution:
                                        Steps.append(productStep)
                                    newExpression = expression.replace(str(term), solution)

                                newExpression = Expression(newExpression)
                                if str(newExpression) != str(expression):
                                    return simplifyExpression(newExpression, keyword, Steps, finalResult=finalResult)

                            # Steps.append(createMainStep(r'\text{Combine Results}', latexify(f'{expression}')))
                        else:
                            pass

                    for term in expression.getTerms():
                        product_pattern = re.compile(r'}\w')
                        matches = product_pattern.findall(str(term))
                        if len(matches) > 0:
                            sign = term[0]
                            if (sign != '+' and sign != '-'): sign = '+'
                            if term[0] == '+': term = term[1:]
                            productTerms = []
                            termToAdd = ''
                            for char in term:
                                termToAdd += char
                                if char == '}':
                                    termToAdd = Expression(termToAdd)
                                    termSimplification = simplifyExpression(termToAdd)
                                    simplifiedTerm = parseLatex(termSimplification['finalResult'])
                                    if simplifiedTerm != str(termToAdd):
                                        # CREATE AND ADD E-STEP
                                        heading = latexify(f'{termToAdd}={simplifiedTerm}')
                                        e_step = createExpandableStep(heading, termSimplification['steps'])
                                        Steps.append(e_step)
                                    productTerms.append(simplifiedTerm)
                                    termToAdd = ''

                            simplifiedProduct = getProduct2(productTerms)
                            newExpression = Expression(newExpression.replace(str(term), simplifiedProduct))

                    # return simplifyExpression(newExpression, keyword, Steps, finalResult=finalResult)

                Solution = simplifyConstants(constantsExpression, Constants)
                steps = Solution['Steps']
                simplification = Solution['finalExpression']

                # CREATE E-STEP
                heading = createEStepHeadingFromGroup(Constants, False)
                e_step = createExpandableStep(latexify(f"{heading}={simplification}"), steps)
                if steps != []: Steps.append(e_step)
                # UPDATE finalResult
                sign = ''
                if simplification[0] != '-' and simplification[0] != '': sign = '+'
                finalResult += f"{sign}{simplification}"

    if finalResult[0] == '+': finalResult = finalResult[1:]
    finalResult = formatExpression(finalResult)

    # CHECK IF EXPRESSION CAN BE SIMPLIFIED MORE
    if not recursiveCall:
        testExpression = Expression(finalResult)
        groupedTerms = testExpression.getGroupedTerms()

        newGroupedTerms = createGroupedTermsDict()
        termsAdded = set()
        for group in groupedTerms:
            if groupedTerms[group] != []:
                if group == 'Fractions':
                    for fraction in groupedTerms[group]:
                        if '^{1}' in fraction: fraction = Fraction(fraction.replace('^{1}', ''))
                        newGroupedTerms['Fractions'].append(fraction)

                elif group != 'Exponential':
                    if group == 'Radicals':
                        """ CHECK IF RADICAL CAN BE SIMPLIFIED USING THE RADICAL RULE """
                        for radical in groupedTerms[group]:
                            radicand = radical.getRadicand()
                            if radicand.isSingleExpression():
                                if len(radicand.getGroupedTerms()['Exponential']) > 0:
                                    radicand = radicand.getGroupedTerms()['Exponential'][0]
                                    if radical.index == radicand.exponent:
                                        newGroupedTerms['Radicals'].append(radical)
                                        termsAdded.add(str(radical))
                    for term in groupedTerms[group]:
                        if str(term) not in termsAdded:
                            newGroupedTerms['Constants'].append(Constant(str(term)))
                else:
                    newGroupedTerms['Exponential'] = groupedTerms['Exponential']

        testSolution = simplifyExpression(testExpression, groupedTerms=newGroupedTerms, recursiveCall=True)

        if testSolution['finalResult'] != latexify(finalResult):
            if Steps != []: Steps.append(createMainStep(r'\text{Combine Results}', latexify(f'{finalResult}')))
            for step in testSolution['steps']:
                if step['type'] == 'main-step':
                    Steps.append(step)
                elif step['type'] == 'e-step':
                    for e_step in step['e-steps']:
                        Steps.append(e_step)

            finalResult = parseLatex(testSolution['finalResult'])

    if len(Steps) == 1 and Steps[0]['type'] == 'e-step':
        return {'steps': Steps[0]['e-steps'], 'finalResult': latexify(finalResult)}

    return {'steps': Steps, 'finalResult': latexify(finalResult)}

def simplifyImplicitProduct(expression: Expression, Steps) -> Expression:
    if expression.isSingleExpression() and len(
            expression.getGroupedTerms()['Exponential']) == 1 and '*' not in expression:
        """ SINGLE EXPONENTIAL: 25x^{1+2} -> 25x^{3} """
        simplification = simplifyExpression(expression)
        expression = Expression(simplification['finalResult'])
        for step in simplification['steps']:
            Steps.append(step)
        return expression
    for k, term in enumerate(expression.getTerms()):
        """ SIMPLIFY 10x^{1+2}y^{a+2a} AS 10x^{3}y^{3a} """

        term = str(term)
        leftProductPattern = re.compile(r'[a-zA-Z]\w\^{')
        leftProductMatches = leftProductPattern.findall(term)

        rightProductPattern = re.compile(r'}\w')
        rightProductMatches = rightProductPattern.findall(term)

        if len(leftProductMatches) > 0 or len(rightProductMatches) > 0:

            sign = term[0]
            if (sign != '+' and sign != '-'): sign = '+'
            if term[0] == '+': term = term[1:]

            separatedTerms = []
            termToAdd = ''
            beginExpression = False
            i = 0
            while i < len(term):
                char = term[i]
                if Constant(char).is_digit:
                    termToAdd += char
                    i += 1
                else:
                    if term[i] == '^' and not beginExpression:
                        """ GET EXPONENT """
                        for j in range(i + 2, len(term) + 1):
                            if parenIsBalanced(term[i + 1:j], 'both'):
                                if len(separatedTerms) > 0:
                                    coefficient = Exponential(separatedTerms.pop()).coefficient
                                else:
                                    coefficient = ''
                                if coefficient == '1': coefficient = ''
                                exponent = term[i + 1: j]
                                exponential = f'{coefficient}{term[i - 1]}^{exponent}'
                                exponentialSimplification = simplifyExpression(Expression(exponential))
                                simplifiedExponential = parseLatex(exponentialSimplification['finalResult'])
                                if simplifiedExponential != exponential:
                                    # CREATE AND ADD E-STEP
                                    heading = latexify(f'{exponential}={simplifiedExponential}')
                                    e_step = createExpandableStep(heading, exponentialSimplification['steps'])
                                    Steps.append(e_step)

                                separatedTerms.append(simplifiedExponential)
                                i = j
                                termToAdd = ''
                                break
                    else:
                        if char == '{':
                            beginExpression = True
                            if joinList(separatedTerms[-4:], '') == 'sqrt':
                                separatedTerms = separatedTerms[:-4]
                                termToAdd += 'sqrt'

                        if not beginExpression and (char == '+' or char == '-') and i != 0:
                            """ leftProductMatches OR rightProductMatches WERE INVALID """
                            separatedTerms = []
                            break

                        if char != '-':
                            termToAdd += char
                        else:
                            """ FIXES sqrt{10x-2x} SO THAT sqrt{10x-2x} DOES NOT GET PARSED AS sqrt{10x-12x} """
                            if not beginExpression:
                                termToAdd += '-1'
                            else:
                                termToAdd += char

                        if beginExpression and '{' in termToAdd and parenIsBalanced(termToAdd, 'curly'):
                            termToSimplify = termToAdd
                            Simplification = simplifyExpression(Expression(termToSimplify))
                            simplifiedTerm = parseLatex(Simplification['finalResult'])
                            if simplifiedTerm != termToSimplify:
                                # CREATE AND ADD E-STEP
                                heading = latexify(f'{termToSimplify}={simplifiedTerm}')
                                e_step = createExpandableStep(heading, Simplification['steps'])
                                Steps.append(e_step)

                            separatedTerms.append(simplifiedTerm)
                            termToAdd = ''
                            beginExpression = False

                        if not beginExpression:
                            if termToAdd != '':
                                separatedTerms.append(termToAdd)
                                termToAdd = ''
                        i += 1

            if len(separatedTerms) > 0:
                simplifiedProduct = getProduct2(separatedTerms)
                expression = Expression(expression.replace(str(term), simplifiedProduct))

    return expression

def formatExpression(expression):
    return expression.replace('++', '+').replace('-+', '-').replace('+-', '-').replace('--', '+')

def formatSpecialValues(solution: str) -> str:
    MIN_VAL = 10 ** (-10)
    MAX_VAL = 10 ** (10)
    solution = solution.replace('0.7071067811865476',  'frac{sqrt{2}}{2}')\
                        .replace('0.7071067811865475', 'frac{sqrt{2}}{2}')\
                        .replace('0.8660254037844386','frac{sqrt{3}}{2}')\
                        .replace('0.49999999999999994', 'frac{1}{2}')\
                        .replace('0.5773502691896257', 'frac{sqrt{3}}{3}') \
                        .replace('1.7320508075688767', 'sqrt{3}')\
                        .replace('1.4142135623730951', 'sqrt{2}')\
                        .replace('1.414213562373095', 'sqrt{2}')\
                        .replace('0.5000000000000001','frac{1}{2}')

    if 'frac' not in solution:
        if Constant(solution).is_digit:
            if abs(float(solution)) < MIN_VAL:
                return '0'
            if float(solution) > MAX_VAL:
                return 'Undefined'
            if Constant(solution).is_integer:
                return str(Constant(solution).val)
    return solution

def simplifyConstants(expression, constants: list):
    numbers, variables, Steps = [], [], []
    for term in constants:
        if type(term) != Constant:
            raise TypeError(f'{term} is not a constant')
        if term.is_digit and 'frac' not in term:
            numbers.append(str(term))
        else:
            if term[0] != '+' and term[0] != '-':
                # ADD '+' SIGN TO TERM
                term = Constant('+' + str(term))
            variables.append(str(term))

    """ GROUP LIKE TERMS """
    numbersStr, variablesStr, newExpression = '', '', ''

    seen = set()
    for term in variables:
        start_of_var = get_start_of_var(term)
        var = get_var(term, start_of_var)
        if var not in seen:
            seen.add(var)
            for i in range(len(variables)):
                start_of_var_1 = get_start_of_var(variables[i])
                start_of_var_2 = get_start_of_var(term)
                if get_var(variables[i], start_of_var_1) == get_var(term, start_of_var_2):
                    newExpression += variables[i]
                    variablesStr += str(variables[i])

    for term in numbers:
        if term[0] != '+' and term[0] != '-': term = f"+{term}"
        newExpression += str(term)
        numbersStr += str(term)

    # FORMATTING
    if newExpression[0] == '+':
        newExpression = newExpression[1:]

    if expression != newExpression:
        mainStep = createMainStep(r'\text{Group Like Terms}', latexify(f'{expression}={newExpression}'))
        Steps.append(mainStep)

    """ DO COMPUTATION """
    if variablesStr != '':
        if variablesStr[0] == '+': variablesStr = variablesStr[1:]
        sumOfVariables = addVariables(variables)
        if sumOfVariables[0] == '+': sumOfVariables = sumOfVariables[1:]
        # FORMATTING
        if numbersStr == '' and sumOfVariables[0] == '+': sumOfVariables = sumOfVariables[1:]
        if newExpression != newExpression.replace(variablesStr, sumOfVariables):
            mainStep = createMainStep(r'\text{Add Like Terms Left to Right}',
                                      latexify(
                                          f'{newExpression}={newExpression.replace(variablesStr, sumOfVariables)}'))
            Steps.append(mainStep)
            newExpression = newExpression.replace(variablesStr, sumOfVariables)

    if numbersStr != '':
        if numbersStr[0] == '+': numbersStr = numbersStr[1:]
        sumOfNumbers = addNumbers(numbers)
        if numbersStr[0] == '-' and variablesStr != '' and sumOfNumbers > 0: sumOfNumbers = f'+{sumOfNumbers}'

        if newExpression != newExpression.replace(numbersStr, str(sumOfNumbers)):
            mainStep = createMainStep(r'\text{Add Numbers Left to Right}',
                                      latexify(
                                          f'{newExpression}={newExpression.replace(numbersStr, str(sumOfNumbers))}'))
            Steps.append(mainStep)
            newExpression = newExpression.replace(numbersStr, str(sumOfNumbers))

    finalExpression = newExpression
    finalExpression = finalExpression.replace('++', '+').replace('--', '+').replace('+-', '-').replace('-+',
                                                                                                       '-').replace(
        '+0', '').replace('-0', '')

    return {'finalExpression': finalExpression, 'Steps': Steps}

def get_start_of_var(term: str):
    """ RETURNS THE INDEX OF THE BEGINNING OF THE VARIABLE IN A TERM """
    start_of_var = None
    for i, char in enumerate(term):
        char = Constant(char)
        if (char != '+' and char != '-') and not char.is_digit:
            if start_of_var == None:
                start_of_var = i

    return start_of_var

def get_var(term: str, start_of_var: int):
    """ RETURNS THE VARIABLE OF A TERM. EXAMPLE get_var(+25xyz) --> xyz """
    return term[start_of_var:]

def get_coefficient(term: str, start_of_var: int):
    """ RETURNS THE COEFFICIENT OF A TERM. EXAMPLE get_coefficient(+25xyz) --> +25 """
    return term[:start_of_var]

def getFactors(num: int) -> list:
    factors = []
    for i in range(1, abs(num) + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def getLCM(terms: list, listOfNumbers=False, termsType=None):
    if termsType is None: termsType = 'Numbers'

    if termsType == 'Mixed':
        numberTerms, variableTerms = [], []
        for term in terms:
            if Constant(term).is_digit:
                numberTerms.append(term)
            else:
                variableTerms.append(term)

        variableLCM = getLCM(variableTerms, termsType='Variables')
        numbersLCM = product(numberTerms)

        lcm = f'{numbersLCM}{variableLCM}'
        if numbersLCM == 1: lcm = lcm[1:]

        return lcm

    elif termsType == 'Variables':
        lcm = ''
        maxPowersOfTerms = {}
        lcmTerms = []
        for term in terms:
            if len(Expression(term)) > 1 and (term[0] != '(' and term[-1] != ')'): term = f'({term})'

            term = Exponential(term, CETAEIOCF=True)

            if term.coefficient != '1':
                lcmTerms.append(f'*{term.coefficient}')

            if Constant(term.exponent).is_digit:
                if term.base not in maxPowersOfTerms:
                    maxPowersOfTerms.update({term.base: int(term.exponent)})
                else:
                    maxPower = maxPowersOfTerms[term.base]
                    if int(term.exponent) > maxPower:
                        maxPowersOfTerms.update({term.base: int(term.exponent)})

        for term in maxPowersOfTerms:
            termToAddToLCM = f"{term}^{'{'}{maxPowersOfTerms[term]}{'}'}"
            termToAddToLCM = termToAddToLCM.replace('^{1}', '')
            lcmTerms.append(termToAddToLCM)

        digitTerms = ''
        termsWithExponentsAndNoParen = ''
        termsWithoutExponent = ''
        termsWithParen = ''

        for term in lcmTerms:
            if term[0] == '*' or Constant(term).is_digit:
                digitTerms += term
            elif '^{' in term and '(' not in Exponential(term, CETAEIOCF=True).base:
                termsWithExponentsAndNoParen += term
            elif '^{' not in term and '(' not in term and Exponential(term, CETAEIOCF=True).exponent == '1':
                termsWithoutExponent += term
            else:
                termsWithParen += term

        for term in digitTerms:
            lcm += term
        for term in termsWithExponentsAndNoParen:
            lcm += term
        for term in termsWithoutExponent:
            lcm += term
        for term in termsWithParen:
            lcm += term

        if lcm[0] == '*': lcm = lcm[1:]
        return lcm
    else:
        multiples = []
        for num in terms:
            multiplesOfNum = {abs(num) * i for i in range(1, 500)}
            multiples.append(multiplesOfNum)
        commonMultiples = multiples[0].intersection(*multiples)
        return min(commonMultiples)

def getLCMFactor(fracDenominator: str, denominators: list):
    denominatorDigits = []
    denominatorVariables = []
    for term in denominators:
        if Constant(term).is_digit:
            denominatorDigits.append(term)
        else:
            denominatorVariables.append(term)

    fracDenominator = [fracDenominator]
    lcmFactorList = list_diff(denominators, fracDenominator)

    if len(denominatorDigits) > 1:
        variableLCMFactor = list_diff(denominatorVariables, fracDenominator)
        digitsLCM = product(denominatorDigits)
        denominatorCoefficient = float(Exponential(fracDenominator).coefficient)
        lcmFactor = f'{digitsLCM / denominatorCoefficient}'
        if Constant(lcmFactor).is_integer: lcmFactor = lcmFactor[:-2]
        for var in variableLCMFactor: lcmFactor += var
        return lcmFactor

    termsWithoutParen = ''
    termsWithParen = ''
    for term in lcmFactorList:
        if '(' in term:
            termsWithParen += term
        else:
            termsWithoutParen += term

    lcmFactor = ''
    for term in termsWithoutParen:
        lcmFactor += term
    for term in termsWithParen:
        lcmFactor += term

    return lcmFactor

def addNumbers(numbers: list, sum=0):
    if len(numbers) == 0:
        sum = str(sum)
        i = indexOf(sum, '.')
        return int(sum[:i]) if sum[i:] == '.0' else float(sum)
    elif len(numbers) == 1:
        if '+-' in numbers[0]: numbers[0] = numbers[0].replace('+-', '-')
        sum += float(str(numbers[0]))
        sum = str(sum)
        i = indexOf(sum, '.')
        return int(sum[:i]) if sum[i:] == '.0' else float(sum)
    x1 = float(str(numbers[0]))
    x2 = float(str(numbers[1]))

    sum += (x1 + x2)
    numbers = numbers[2:]
    return addNumbers(numbers, sum)

def addVariables(variables: list):
    """ INITIALIZE VARIABLE COEFFICIENTS """
    variableCoefficients = {}
    for term in variables:
        term = str(term)
        start_of_var = get_start_of_var(term)
        var = get_var(term, start_of_var)
        variableCoefficients.update({var: []})

    """ GET THE COEFFICIENT OF ALL THE VARIABLES """
    for term in variables:
        term = str(term)
        start_of_var = get_start_of_var(term)
        var = get_var(term, start_of_var)
        coefficient = get_coefficient(term, start_of_var)
        if coefficient == '-':
            coefficient = '-1'
        elif coefficient == '+' or coefficient == '':
            coefficient = '+1'

        variableCoefficients[var].append(coefficient)

    """ COMPUTE THE FINAL COEFFICIENT OF ALL THE VARIABLES """
    for var in variableCoefficients:
        finalCoefficient = addNumbers(variableCoefficients[var])
        variableCoefficients[var] = finalCoefficient

    simplifiedExpression = ''
    for var in variableCoefficients:
        coefficient = variableCoefficients[var]
        if str(coefficient)[0] != '+':
            simplifiedExpression += '+'
        if coefficient == 1: coefficient = ''
        if coefficient == -1: coefficient = '-'
        if coefficient != 0:
            simplifiedExpression += f'{coefficient}{var}'
        else:
            simplifiedExpression += '0'

    simplifiedExpression = simplifiedExpression.replace('++', '+').replace('--', '+').replace('+-', '-')
    if simplifiedExpression[-1] == '+': simplifiedExpression = simplifiedExpression[:-1]

    return simplifiedExpression

def addExponentials(Exponentials: list):
    """ ADDS LIST OF EXPONENTIALS """
    if len(Exponentials) == 1:
        return Exponentials[0]

    """ FORMAT EXPS SO THAT 2^{x}=2^{x} """
    tmpExponentials = []
    for exp in Exponentials:
        if exp.coefficient == '1':
            exp = Exponential(f"{exp.base}^{'{'}{exp.exponent}{'}'}")
            tmpExponentials.append(exp)
        else:
            exp = Exponential(f"{exp.base}^{'{'}{exp.exponent}{'}'}")
            tmpExponentials.append(exp)

    # Exponentials = tmpExponentials

    """ INITIALIZE EXPONENTIAL COEFFICIENTS """
    exponentialCoefficients = {}
    for exp in tmpExponentials:
        exponentialCoefficients.update({str(exp.exponential): []})

    """ GET THE COEFFICIENT OF ALL THE EXPONENTIALS """
    for exp in Exponentials:
        coefficient = exp.coefficient
        exponentialWithoutCoefficient = f"{exp.base}^{'{'}{exp.exponent}{'}'}"
        exponentialCoefficients[exponentialWithoutCoefficient].append(coefficient)

    """ COMPUTE THE FINAL COEFFICIENT OF ALL THE VARIABLES """
    for exp in exponentialCoefficients:
        finalCoefficient = addNumbers(exponentialCoefficients[exp])
        exponentialCoefficients[exp] = finalCoefficient

    simplifiedExponential = ''
    for exp in exponentialCoefficients:
        coefficient = exponentialCoefficients[exp]
        if str(coefficient)[0] != '+' and str(coefficient)[0] != '-':
            simplifiedExponential += '+'

        if coefficient == 0:
            simplifiedExponential += '0'
        elif coefficient == 1:
            simplifiedExponential += f'{exp}'
        elif coefficient == -1:
            simplifiedExponential += f'-{exp}'
        else:
            if Constant(Exponential(exp).base).is_digit:
                simplifiedExponential += f'{coefficient}*{exp}'
            else:
                simplifiedExponential += f'{coefficient}{exp}'

    """ FORMAT 2*x^2 + 2*2^x as 2x^2 + 2*2^x """

    simplifiedExponential = Expression(simplifiedExponential)

    newSimplifiedExponentials = ''
    for exponential in simplifiedExponential.getTerms():
        if '*' in exponential:
            sign = exponential[0]
            if (sign != '+' and sign != '-'): sign = '+'
            if sign == '-': sign = ''
            exponential = Exponential(exponential)
            if exponential.isPolynomial():
                coefficient, base, exponent = exponential.coefficient, exponential.base, exponential.exponent
                newSimplifiedExponentials += f"{sign}{coefficient}{base}^{'{'}{exponent}{'}'}"
            else:
                newSimplifiedExponentials += str(exponential)
        else:
            newSimplifiedExponentials += str(exponential)

    return newSimplifiedExponentials

def groupLikeExponentials(Exponentials: list):
    if len(Exponentials) == 1:
        return str(Exponentials[0])
    finalExponential = ''
    seen = set()
    for i in range(len(Exponentials)):
        if type(Exponentials[i]) == Exponential:
            Exponentials[i].format()

        expToHash = f"{Exponentials[i].base}^{'{'}{Exponentials[i].exponent}{'}'}"
        if expToHash not in seen:
            seen.add(expToHash)
            for j in range(i, len(Exponentials)):
                if Exponential.areLike(Exponentials[i], Exponentials[j]):
                    expToAdd = str(Exponentials[j])
                    if expToAdd[0] != '+' and expToAdd[0] != '-': expToAdd = f'+{expToAdd}'
                    finalExponential += expToAdd

    if finalExponential[0] == '+': finalExponential = finalExponential[1:]
    return finalExponential

def isDigit(item: str, considerSpecialNumbers=False):
    if considerSpecialNumbers:
        item = item.replace('pi', str(math.pi)).replace('e', str(math.e))
        if '*' in item and 'frac' not in item: item = str(eval(item))
    if item.isdigit():
        return True
    if 'frac' in item:
        if '*' in item:
            allProducts = item.split('*')
            allParenBalanced = True
            for term in allProducts:
                if not parenIsBalanced(term, 'both'):
                    allParenBalanced = False
            if allParenBalanced:
                # CASE: frac{x+1}{y+1}*frac{u+1}{v+1} -> Constant
                return False
            else:
                item = Fraction(item)
                if parenIsBalanced(item.numerator, 'both') and parenIsBalanced(item.denominator, 'both'):
                    simplifiedNumerator = simplifyExpression(item.numerator)['finalResult']
                    simplifiedDenominator = simplifyExpression(item.denominator)['finalResult']
                    return isDigit(simplifiedNumerator) and isDigit(simplifiedDenominator)
        else:
            item = Fraction(item)
            if parenIsBalanced(item.numerator, 'both') and parenIsBalanced(item.denominator, 'both'):
                simplifiedNumerator = simplifyExpression(item.numerator)['finalResult']
                simplifiedDenominator = simplifyExpression(item.denominator)['finalResult']
                return isDigit(simplifiedNumerator) and isDigit(simplifiedDenominator)

    if '.' in item:
        try:
            float(item)
            return True
        except:
            return False

    return False

def product(numbers: list):
    prod = 1
    for num in numbers:
        prod *= float(num)
    prod = Constant(str(prod))
    if prod.is_integer:
        return int(str(prod))
    else:
        return float(str(prod))

def getProduct2(terms: list):
    """ RETURNS THE ALGEBRAIC PRODUCT OF THE ITEMS IN terms """

    """ SEPARATE PRODUCT: [3x, 5x^{2}, 20uv^{2}xyz] -> [3x, 5x^{2}, 20u, v^{2}, x, y, ] """
    for k, term in enumerate(terms):
        if '*' in term:
            terms.pop(k)
            terms = terms + term.split('*')
            return getProduct2(terms)
        leftProductPattern = re.compile(r'[a-zA-Z]\w\^{')
        leftProductMatches = leftProductPattern.findall(term)

        rightProductPattern = re.compile(r'}\w')
        rightProductMatches = rightProductPattern.findall(term)

        nonExponentialProductPattern = re.compile(r'[a-zA-Z][a-zA-Z]')
        nonExponentialProductMatches = nonExponentialProductPattern.findall(term)

        if len(leftProductMatches) > 0 or len(rightProductMatches) or (
                len(nonExponentialProductMatches) > 0 and '^' not in term and 'sqrt' not in term):
            separatedTerms = []
            termToAdd = ''
            i = 0
            while i < len(term):
                char = term[i]
                if Constant(char).is_digit:
                    termToAdd += char
                    i += 1
                else:
                    if term[i] == '^':
                        """ GET EXPONENT """
                        for j in range(i + 2, len(term) + 1):
                            if parenIsBalanced(term[i + 1:j], 'both'):
                                coefficient = Exponential(separatedTerms.pop()).coefficient
                                if coefficient == '1': coefficient = ''
                                exponent = term[i + 1: j]
                                exponential = f'{coefficient}{term[i - 1]}^{exponent}'
                                separatedTerms.append(exponential)
                                i = j
                                termToAdd = ''
                                break
                    else:
                        termToAdd += char
                        separatedTerms.append(termToAdd)
                        termToAdd = ''
                        i += 1
            terms.pop(k)
            terms = terms + separatedTerms

    """ CHECK FOR FRACTIONS """
    for item in terms:
        if 'frac' in item:
            numerators, denominators = [], []
            for term in terms:
                numerators.append(Fraction(term).numerator)
                denominators.append(Fraction(term).denominator)

            numeratorProduct = getProduct2(numerators)
            denominatorProduct = getProduct2(denominators)

            finalProduct = f"frac{'{'}{numeratorProduct}{'}'}{'{'}{denominatorProduct}{'}'}"
            return finalProduct

    Coefficients = []

    """ GET COEFFICIENTS """
    for term in terms:
        # C = Exponential(str(term)).coefficient
        if Constant(term).is_digit:
            C = term
        else:
            C = Exponential(term, CETAEIOCF=True).coefficient
            if term[0] == '-' and C[0] != '-':
                """ FIXES term = -x """
                C = f'-{C}'
        Coefficients.append(C)

    seenTerms = {}
    for i, term in enumerate(terms):
        if term[0] == '+' or term[0] == '-': term = term[1:]
        term = Exponential(term, CETAEIOCF=True)

        if term.base not in seenTerms:
            seenTerms.update({str(term.base): term.exponent})
        else:
            if Constant(term.base).is_digit:
                pass
                # Coefficients[i-1] = '1'
            counter = seenTerms[term.base]
            seenTerms.update({term.base: f'{counter}+{term.exponent}'})

    finalCoefficient = product(Coefficients)
    if finalCoefficient == 1: finalCoefficient = ''

    finalProduct = f'{finalCoefficient}'

    for term in seenTerms:
        if (term != finalProduct and not Constant(term).is_digit) or finalProduct == '':
            # if term != finalProduct:
            finalProduct += f"{term}^{'{'}{seenTerms[term]}{'}'}"
        else:
            pass
            if term != finalProduct and not Constant(simplifyExpression(seenTerms[term])['finalResult']).is_digit:
                finalProduct += f"*{term}^{'{'}{seenTerms[term]}{'}'}"

    """ CONSTANT TIMES A FRACTION """
    fractionProductPattern = re.compile('\w+frac')
    matches = fractionProductPattern.findall(finalProduct)
    if len(matches) > 0:
        termToMultiply = matches[0][:-4]
        fraction = Fraction(finalProduct[len(termToMultiply):])
        newFraction = f"frac{'{'}{termToMultiply}*{fraction.numerator}{'}'}{'{'}{fraction.denominator}{'}'}"
        finalProduct = newFraction

    """ FORMAT RESULT """
    finalProduct = finalProduct.replace('^{1}', '')

    return finalProduct

def distributeTerms(expression: str, Steps: list) -> Expression:
    if ')(' not in expression:
        return Expression(expression)

    term1, term2, finalExpression = '', '', ''

    """ GET term1 """
    i = 0
    while i < len(expression):
        term1 += expression[i]
        if parenIsBalanced(term1, 'both'):
            break
        i += 1
    i += 1
    term1 = Expression(term1[1:-1])
    """ GET term2 """
    while i < len(expression):
        term2 += expression[i]
        if parenIsBalanced(term2, 'both'):
            break
        i += 1
    term2 = Expression(term2[1:-1])

    for i in range(len(term1.getTerms())):
        T1 = term1.getTerms()[i]
        if T1[0] == '+': T1 = T1[1:]
        for j in range(len(term2.getTerms())):
            T2 = term2.getTerms()[j]
            if T2[0] == '+': T2 = T2[1:]
            finalExpression += f"{T1}*{T2}+"

    """ REMOVE THE FIRST TWO TERMS THAT WERE JUST MULTIPLIED. (+4 FOR THE FOUR PARENTHESES REMOVED) """
    expression = expression[len(str(term1)) + len(str(term2)) + 4:]
    """ SIMPLIFY finalExpression """
    finalExpression = finalExpression[:-1]
    finalExpressionSimplification = simplifyExpression(Expression(finalExpression))
    simplifiedFinalExpression = parseLatex(finalExpressionSimplification['finalResult'])
    combineStep = createMainStep(r'\text{Combine Results}', latexify(f"{finalExpression}={simplifiedFinalExpression}"))
    finalExpressionSimplification['steps'].append(combineStep)
    """ CREATE AND ADD E-STEP """
    heading = latexify(f'({term1})({term2})={simplifiedFinalExpression}')
    e_steps = []
    if len(term1) == 2 and len(term2) == 2:
        foilStep = createMainStep(r'\text{Apply FOIL Method}: \\ (a+b)(c+d)=ac+ad+bc+bd',
                                  latexify(f"({term1})({term2})={finalExpression}"))
    else:
        foilStep = createMainStep(r'\text{Distribute Parentheses}', latexify(f"({term1})({term2})={finalExpression}"))

    # ADD FOIL STEP
    e_steps.append(foilStep)
    # CREATE AND ADD SIMPLIFICATION E-STEP
    # finalExpressionSimplificationEStepHeading = latexify(f'{finalExpression}={simplifiedFinalExpression}')
    # finalExpressionSimplificationESteps = createExpandableStep(finalExpressionSimplificationEStepHeading, finalExpressionSimplification['steps'])
    # e_steps.append(finalExpressionSimplificationESteps)
    for step in finalExpressionSimplification['steps']:
        e_steps.append(step)

    e_step = createExpandableStep(heading, e_steps)

    Steps.append(e_step)

    if expression != '':
        return distributeTerms(f"({simplifiedFinalExpression}){expression}", Steps)
    else:
        return distributeTerms(simplifiedFinalExpression, Steps)

def listIsInt(X: list):
    """ RETURNS THE TYPE OF THE ELEMENTS IN A LIST """
    isInt = True
    for item in X:
        if not Constant(item).is_digit or 'frac' in item:
            isInt = False

    return isInt

def castToFloatOrInt(num: str):
    """ '5.304' -> 5.304, '10' -> 10, '3.0' -> 3 """
    if Constant(num).is_integer:
        return Constant(num).val
    else:
        return float(num)

def multiplyTerms(terms: list):
    seenTerms = {}
    for term in terms:
        if term[0] == '+' or term[0] == '-': term = term[1:]
        if term not in seenTerms:
            seenTerms.update({term: 1})
        else:
            counter = seenTerms[term]
            seenTerms.update({term: counter + 1})

    product = ''
    for term in seenTerms:
        if '^' not in term:
            product += f"{term}^{'{'}{seenTerms[term]}{'}'}"
        else:
            product += f"*{term}^{'{'}{seenTerms[term]}{'}'}"

    product = product.replace('^{1}', '')
    return product

def isMatch(exp1, exp2):
    """ CHECK IF exp1 is CONTAINED IN exp2 """
    exp1, exp2 = parseLatex(exp1), parseLatex(exp2)
    fractionMatch = False
    radicalMatch = False
    if Expression(exp1).isSingleExpression() and Expression(exp2).isSingleExpression():
        if exp1[0:4] == 'frac' and exp2[0:4] == 'frac':
            exp1, exp2 = Fraction(exp1), Fraction(exp2)
            if (exp1.numerator in exp2.numerator) or (exp1.denominator in exp2.denominator):
                fractionMatch = True
            # if isMatch(exp1.numerator, exp2.numerator) or isMatch(exp1.denominator, exp2.denominator) or isMatch(exp1.denominator, exp2.denominator):
            #     fractionMatch = True
        if exp1[0:4] == 'sqrt' and exp2[0:4] == 'sqrt':
            exp1, exp2 = Radical(exp1), Radical(exp2)

            if isMatch(str(exp1.getRadicand()), str(exp2.getRadicand())):
                radicalMatch = True

        exp1 = str(exp1)
        exp2 = str(exp2)
    if exp1 in exp2 or fractionMatch or radicalMatch:
        return True
    else:
        return False

def convertToStandardForm(expression):
    if type(expression) != Expression: expression = Expression(expression)

    terms = expression.getTerms()

    newExpression = ''
    digits = ''
    termsWithoutParen = ''
    termsWithParen = ''
    for term in terms:
        term = str(term)
        if term[0] != '+' and term[0] != '-': term = f'+{term}'
        if Constant(term).is_digit:
            digits += term
        elif '(' in term:
            termsWithParen += term
        elif '^{' in term or 'sqrt{' in term or '*' in term:
            termsWithoutParen += term
        else:
            charDigits, variables, newTerm = '', '', ''
            for char in term:
                if Constant(char).is_digit or char in {'+', '-'}:
                    charDigits += char
                else:
                    variables += char

            for digit in charDigits:  newTerm += digit
            for var in variables: newTerm += var

            termsWithoutParen += newTerm

    for term in termsWithParen: newExpression += term
    for term in termsWithoutParen: newExpression += term
    for term in digits: newExpression += term

    if newExpression[0] == '+': newExpression = newExpression[1:]
    return newExpression

def getExponentialStr(exponentials: list):
    expStr = ''
    for exp in exponentials:
        exp = str(exp)
        if exp[0] != '+' and exp[0] != '-':
            exp = f'+{exp}'
        expStr += exp

    if expStr[0] == '+': expStr = expStr[1:]
    return expStr

def getMaxPerfectPower(index: int, radicand: int):
    n_powers = []
    for i in range(1, 100):
        # THIS WILL TAKE "i" 1-100 TO WHATEVER POWER WAS ENTERED
        powers = i ** index
        # THIS WILL APPEND THOSE POWERS THAT WERE CREATED TO THE "n_powers" LIST
        n_powers.append(powers)

    perfect_powers = []
    for i in range(len(n_powers)):
        # IF THE ROOT GOES INTO ONE OF THE LIST OF POWERS WITHOUT A REMAINDER, PRINT IT
        if radicand % n_powers[i] == 0:
            perfect_powers.append(n_powers[i])

    return perfect_powers[-1]

def solveEquation(equation: Equation):
    pass

def main():
    # E = Expression('tanh(frac{3x^{2}+x^{2}+3+4}{3x+x+ln(x+2x+1)+1+2})')
    # E = Expression('4u*5*v^{2}*x*(5x^{2}+3x^{2}+2x+1)')
    # E = Expression('20uv^{2}*5x^{2}+2uv^{2}*3x^{2}')
    # E = Expression('240x^{2}*(a+b)')

    # E = Expression('1*1*(x+3)*(x+2)*(x+5)*1*
    # E = Expression('frac{x+y}{a+b}*frac{u+v}{s+t}')
    # E = Expression('2x*3x*sqrt{5x^{2}+3x^{2}+2+3}*5u^{2}*u')

    # E = Expression('(frac{x+2}{x+3}+frac{x+4}{x+5})*(frac{x+6}{x+7}+frac{x+8}{x+9})*(frac{x+2}{x+3}+frac{x+4}{x+5})')
    # E = Expression('frac{x^{2}+2x+2}{x^{2}+3x+5}*frac{x+1}{x+2}')
    E = Expression('3-frac{1}{e^{6}}+1')
    print(simplifyExpression(E, keyword='combine'))


if __name__ == '__main__':
    main()