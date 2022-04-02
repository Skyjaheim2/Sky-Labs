from math import floor, pi, e, sqrt
from exceptions import *
import re


maxInt = 1000000000000000
class ArithmeticExpression:
    def __init__(self, expression):
        self.expression = expression

    """ INSTANCE METHODS """

    def getOperationToPerform(self):
        allOperations = self.getAllOperations()

        if len(allOperations) == 0 and self.isSingleExpression():
            return 'no-operation'
        if 'frac' in self.expression:
            return 'fraction-arithmetic'

        if 'sqrt' in self.expression:
            isRadicalOnly = True
            seenTerms = set()
            for term in self.expression:
                if term not in 'sqrt':
                    seenTerms.add(term)
                if term == '}':
                    seenTerms.clear()
                if term in ['+', '-', '*', '/'] and '{' not in seenTerms:
                    isRadicalOnly = False

            if isRadicalOnly:
                return 'radical'
            else:
                return 'general-arithmetic'

        if '^' in self.expression:
            operationsInfo = self.getOperationsOnExponent(returnWithCounter=True)
            operationsOnExponent = operationsInfo[0]
            operationsCounter = operationsInfo[1]

            if operationsOnExponent != 'no-operation':
                """ IF THE ONLY OPERATION IS MULTIPLICATION THEN WE WANT TO RETURN THAT AS A SEPARATE OPERATION SO WE CAN APPLY THE EXPONENT RULE FOR PRODUCTS """
                if operationsOnExponent == {'*'} and operationsCounter > 1:

                    allExponentsInExpression = self.getAllExponentsInExpression()
                    baseToCheckFor = Exponential(allExponentsInExpression[0]).base

                    baseMatched = True
                    for expression in allExponentsInExpression:
                        expression = Exponential(expression)
                        if expression.base != baseToCheckFor:
                            baseMatched = False

                    if baseMatched:
                        pass

                        return 'arithmetic-exponent-multiply'

            exponentIndex = indexOf(str(self.expression), '^')
            exponentData = self.splitExpression(exponentIndex, '^', binarySplit=False)

            base = ArithmeticExpression(exponentData[0])
            exponent = ArithmeticExpression(exponentData[1])

            if '{' in exponent:
                # CHECKING TO THE RIGHT OF THE EXPONENT
                isSingleExponent = False
                exponentEndIndex = indexOf(exponent, '}')
                if base.isSingleExpression():
                    if exponentEndIndex == len(exponent) - 1:
                        isSingleExponent = True
                    else:
                        isSingleExponent = False
                else:
                    expressionToTheLeftOfExponent = ArithmeticExpression(self.expression[:exponentIndex])
                    if '(' not in expressionToTheLeftOfExponent:
                        return 'general-arithmetic'
                    indexWhereExponentEnds = expressionToTheLeftOfExponent.getIndexOfInnerMostParen()

                    if (expressionToTheLeftOfExponent[:indexWhereExponentEnds] == '') and exponentEndIndex == len(
                            exponent) - 1:
                        isSingleExponent = True

                return 'arithmetic-exponent-single' if isSingleExponent else 'general-arithmetic'

            else:
                exponentData = self.splitExpression(exponentIndex, '^', binarySplit=False)
                base = ArithmeticExpression(exponentData[0])
                exponent = ArithmeticExpression(exponentData[1])
                if base.isSingleExpression():
                    if exponent.isSingleExpression():
                        return 'arithmetic-exponent-single'
                    else:
                        return 'general-arithmetic'
                else:
                    # CHECKING TO THE RIGHT OF THE EXPONENT
                    if not exponent.isSingleExpression():
                        return 'general-arithmetic'
                    isSingleExponent = False
                    # CHECKING TO THE LEFT OF THE EXPONENT
                    expressionToTheLeftOfExponent = ArithmeticExpression(self.expression[:exponentIndex])
                    if '(' not in expressionToTheLeftOfExponent:
                        return 'general-arithmetic'
                    indexWhereExponentEnds = expressionToTheLeftOfExponent.getIndexOfInnerMostParen()

                    if (expressionToTheLeftOfExponent[:indexWhereExponentEnds] == ''):
                        isSingleExponent = True

                    return 'arithmetic-exponent-single' if isSingleExponent else 'general-arithmetic'

        if ('+' in allOperations or '-' in allOperations) and ('*' not in allOperations and '/' not in allOperations):
            numberOfAdditions = self.getNumOperation('+', self.expression)
            numberOfSubtractions = self.getNumOperation('-', self.expression)
            if numberOfAdditions > 1 or numberOfSubtractions > 1 or (numberOfAdditions + numberOfSubtractions > 1):
                return 'add-subtract-only'
        if ('*' in allOperations) and ('+' not in allOperations and '/' not in allOperations):
            numberOfMultiplication = self.getNumOperation('*', self.expression)
            termsToBeMultiplied = self.expression.split('*')

            couldBeMultiplyOnly = True

            for term in termsToBeMultiplied:
                if not self.isSingleExpression(term):
                    couldBeMultiplyOnly = False

            if numberOfMultiplication > 1 and couldBeMultiplyOnly:
                return 'multiply-only'

        if '+' in self.expression:
            numberOfAdditions = self.getNumOperation('+', self.expression)
            if numberOfAdditions == 1:
                if isDigit(self.expression.split('+')[0]) and isDigit(self.expression.split('+')[1]):
                    return 'arithmetic-add-single'

        if '-' in self.expression:
            numberOfSubtractions = self.getNumOperation('-', self.expression)
            if numberOfSubtractions == 1:
                if isDigit(self.expression.split('-')[0]) and isDigit(self.expression.split('-')[1]):
                    return 'arithmetic-subtract-single'
        if '*' in self.expression:
            numberOfMultiplications = self.getNumOperation('*', self.expression)
            if numberOfMultiplications == 1:
                if isDigit(self.expression.split('*')[0]) and isDigit(self.expression.split('*')[1]):
                    return 'arithmetic-multiply-single'
            if numberOfMultiplications > 1:
                pass
        if '/' in self.expression:
            numberOfDivisions = self.getNumOperation('/', self.expression)
            if numberOfDivisions == '1':
                if isDigit(self.expression.split('/')[0]) and isDigit(self.expression.split('/')[1]):
                    return 'arithmetic-divide-single'

        if len(allOperations) >= 2:
            return 'general-arithmetic'

    def isSingleExpression(self, expression=None):
        if expression == None:
            expression = self.expression

        expression = expression.replace('(', '').replace(')', '')
        allPossibleOperations = ['+', '-', '*', '/', '^']
        allOperationsInExpression = set()
        for operation in allPossibleOperations:
            if operation in expression:
                allOperationsInExpression.add(operation)

        if 'sqrt' in expression:
            return False

        if '...e' in expression:
            if getNumOperation(expression, '+') == 1 or getNumOperation(expression, '-') == 1:
                return True
        if len(allOperationsInExpression) == 0:
            return True
        elif len(allOperationsInExpression) == 1:
            operation = list(allOperationsInExpression)[0]
            numOperation = self.getNumOperation(operation, expression)
            if numOperation > 1:
                return False
            else:
                checkExpression = expression.split(operation)
                if checkExpression[0] != '':
                    return False
        else:
            return False
        return True

    def getNumOperation(self, operation, expression=None):
        if expression == None:
            expression = self.expression
        result = 0
        for term in expression:
            if term == operation:
                result += 1

        return result

    def getNumOpenParen(self):
        counter = 0
        for i in range(len(self.expression)):
            if self.expression[i] == '(':
                counter += 1
        return counter

    def getAllOperations(self):
        allPossibleOperations = ['+', '-', '*', '/', '^']
        allOperationsInExpression = set()
        for term in self.expression:
            if term in allPossibleOperations:
                allOperationsInExpression.add(term)

        return allOperationsInExpression

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

    def splitExpression(self, index, operator, binarySplit=True, operation=None):
        """
        A BINARY SPLIT OF THE expression 2+43*21-5 ON THE OPERATOR '*' AT INDEX 4 RETURNS ('43', '21')
        A NON-BINARY SPLIT OF THE expression 2+43*21-5 ON THE OPERATOR '*' AT INDEX 4 RETURNS ('2+43', '21-5')
        """
        if not binarySplit:
            for i in range(len(self.expression)):
                if i == index:
                    firstTerm, secondTerm = '', ''
                    """ GET FIRST TERM """
                    j = 0
                    while True:
                        if self.expression[j] == operator:
                            break
                        firstTerm += self.expression[j]
                        j += 1
                    """ GET SECOND TERM """
                    j = i + 1
                    while True:
                        if j == len(self.expression):
                            break
                        if self.expression[j] == operator:
                            break
                        secondTerm += self.expression[j]
                        j += 1

                    return (firstTerm, secondTerm)
        else:
            otherOperators = getRestrictedOperators('-')
            allOperators = ['+', '-', '*', '/']
            for i in range(len(self.expression)):
                if i == index:
                    firstTerm, secondTerm = '', ''
                    """ GET FIRST TERM """
                    j = i - 1
                    while self.expression[j] not in otherOperators and j >= 0:
                        firstTerm += self.expression[j]
                        if self.expression[j] == '-':
                            break
                        j -= 1
                    firstTerm = reverse(firstTerm)
                    """ GET SECOND TERM """
                    j = i + 1
                    while ((self.expression[j] not in allOperators) or (operation == 'multiply-only')) and (
                            self.expression[j] != operator and self.expression[j] != '}'):
                        secondTerm += self.expression[j]
                        j += 1
                        operation = None
                        if j == len(self.expression):
                            break

                    return (firstTerm, secondTerm)

    def applyPEMDAS(self):
        newExpression = self.expression

        if 'sqrt' in newExpression:
            newExpression = wrapRadicalInParen(self.expression)
            return ArithmeticExpression(newExpression)
        if '^' in newExpression:
            newExpression = wrapExponentInParen(self.expression)
            return ArithmeticExpression(newExpression)
            # newExpression = self.expression

        i = 0
        while i < len(self.expression):
            # TODO - PARENTHESES, EXPONENTS
            if self.expression[i] == '*':
                allOperators = ['+', '-', '*', '/']
                # if i != len(expression)-2:
                if getNextOperator(self.expression, i) == '*':
                    expressionWithOrder = '('
                    expressionToReplace = ''
                    """
                    j IS OUR STATING INDEX, MEANING THE INDEX WHERE WE WILL START APPLYING PEMDAS, SO IT HAS TO BE SET EQUAL
                    TO THE FIRST NUMBER/CHAR THAT WILL BE INCLUDED IN PARENTHESES.
                    IN THE EXPRESSION S = '1+936*24*24*5', i WILL BE EQUAL TO 5 AND j SHOULD BE EQUAL TO 2 SINCE S[j] = S[2] = 9
                    AND WE WILL START APPLYING PEMDAS AT 9: 1+(936*24*24*5)
                    """
                    j = i
                    while self.expression[j - 1] not in allOperators:
                        j -= 1

                    while True:
                        if self.expression[j] == '*':
                            if getNextOperator(self.expression, j) != '*':
                                k = j
                                while self.expression[k] not in getRestrictedOperators('*') and self.expression[
                                    k] != '}':
                                    """ GET THE NUM AFTER THE LAST '*' """
                                    expressionWithOrder += self.expression[k]
                                    expressionToReplace += self.expression[k]
                                    if k + 1 == len(self.expression):
                                        break
                                    k += 1
                                break
                        expressionWithOrder += self.expression[j]
                        expressionToReplace += self.expression[j]
                        j += 1
                        if j == len(self.expression):
                            break
                    expressionWithOrder += ')'

                    newExpression = newExpression.replace(expressionToReplace, expressionWithOrder)
                    return ArithmeticExpression(newExpression)

                Terms = self.splitExpression(i, '*', operation='arithmetic-multiply-single')
                firstTerm, secondTerm = Terms[0], Terms[1]
                newExpression = newExpression.replace(f"{firstTerm.replace('-', '')}*{secondTerm}",
                                                      f"({firstTerm.replace('-', '')}*{secondTerm})")
                i += 1
            i += 1

        return ArithmeticExpression(newExpression)

    def applyExponentsToSingleExpressions(self):
        """
        RETURNS A COPY OF THE EXPRESSION WITH SINGLE EXPRESSIONS RAISED TO THE FIRST POWER
        FOR EXAMPLE: 2*3*5^2*3 --> 2^1*3^1*5^2*3^1
        """
        numbersInExpression = self.expression.split('*')
        expressionWithExponents = ''
        for i in range(len(numbersInExpression)):
            if '^' not in numbersInExpression[i]:
                # THIS CHECK IS TO NOT INCLUDE '*' AT THE END OF THE EXPRESSION. FOR EXAMPLE: 2^2*2^3*
                if i != len(numbersInExpression) - 1:
                    expressionWithExponents += f"{numbersInExpression[i]}^1*"
                else:
                    expressionWithExponents += f"{numbersInExpression[i]}^1"
            else:
                # THIS CHECK IS TO NOT INCLUDE '*' AT THE END OF THE EXPRESSION. FOR EXAMPLE: 2^2*2^{1+2+3}*
                if i != len(numbersInExpression) - 1:
                    expressionWithExponents += f"{numbersInExpression[i]}*"
                else:
                    expressionWithExponents += f"{numbersInExpression[i]}"

        return ArithmeticExpression(expressionWithExponents)

    def getOperationsOnExponent(self, returnWithIndex=False, returnWithCounter=False):
        """ RETURNS AN ARRAY WITH ALL THE OPERATIONS TO BE PERFORMED IN AN EXPONENTIAL EXPRESSION """
        expression = self.applyExponentsToSingleExpressions()
        operationsOnExponentWithIndex = []
        operationsOnExponent = set()
        allOperations = ['+', '-', '*', '/']
        operationCounter = 0
        for i in range(len(expression)):
            if expression[i] in allOperations:
                if expression[i - 1] == '}' or expression[i - 2] == '^':
                    operationsOnExponentWithIndex.append({expression[i]: i})
                    operationsOnExponent.add(expression[i])
                    operationCounter += 1

        if operationsOnExponent != set():
            return operationsOnExponentWithIndex if returnWithIndex else (
            operationsOnExponent, operationCounter) if returnWithCounter else operationsOnExponent
        else:
            return 'no-operation'

    def getAllExponentsInExpression(self):
        """ RETURNS AN ARRAY OF ALL THE EXPONENTS IN AN EXPRESSION """
        expression = self.applyExponentsToSingleExpressions()
        allOperations = ['+', '-', '*', '/', '^']
        currentExpressionStartIndex = 0
        allExponentExpressions = []
        for i in range(len(expression)):
            if (expression[i] in allOperations and expression[i - 1] == '}') or (
                    expression[i] == '}' and i == len(expression) - 1) or (
                    expression[i] in allOperations and expression[i - 2] == '^'):
                exponentExpression = expression[currentExpressionStartIndex: i]
                if i == len(expression) - 1:
                    exponentExpression += '}'
                allExponentExpressions.append(exponentExpression)
                currentExpressionStartIndex = i + 1

        return allExponentExpressions

    def convertOutOfStandardForm(self):
        if '...e' in self.expression:
            expressionAsArr = self.expression.split('...e')
            powerOf10 = expressionAsArr[1]
            newExpression = f"{float(expressionAsArr[0]) * 10 ** float(powerOf10):.0f}"
            return ArithmeticExpression(newExpression)
        return self

    def replace(self, subStringToBeReplace, replacement):
        return self.expression.replace(subStringToBeReplace, replacement)

    def split(self, char):
        return self.expression.split(char)

    """ DUNDER METHODS """

    def __add__(self, other):
        if type(other) != ArithmeticExpression:
            return 'Only two expression can be added'
        try:
            Result = evaluateArithmetic(f"{self.expression}+{other.expression}")[1]
        except:
            return 'Something went wrong'

        return ArithmeticExpression(Result)

    def __str__(self):
        return self.expression

    def __repr__(self):
        return f"{self.expression}"

    def __len__(self):
        return len(self.expression)

    def __contains__(self, item):
        """ 'in' OPERATOR """
        return item in self.expression

    def __getitem__(self, index):
        """ [] OPERATOR """
        return self.expression[index]

    def __eq__(self, other):
        """ DOUBLE EQUAL TO OPERATOR """
        return str(self.expression) == str(other)

    def __gt__(self, other):
        """ GREATER THAN OPERATOR """
        if type(other) == int or type(other) == float:
            other = ArithmeticExpression(str(other))
        if not self.isSingleExpression():
            raise ValueError('Comparison can only be made when expression is a single expression')
        if type(other) != ArithmeticExpression and type(other) != int and type(other) != float:
            raise TypeError(f"'>' not supported between instances of '{type(self.expression)}' and '{other}'")

        return float(self.expression) > float(other.expression)

    def __ge__(self, other):
        """ GREATER THAN OR EQUAL TO OPERATOR """
        if type(other) == int or type(other) == float:
            other = ArithmeticExpression(str(other))
        if not self.isSingleExpression():
            raise ValueError('Comparison can only be made when expression is a single expression')
        if type(other) != ArithmeticExpression and type(other) != int and type(other) != float:
            raise TypeError(f"'>=' not supported between instances of '{type(self.expression)}' and '{other}'")

        return float(self.expression) >= float(other.expression)

    def __lt__(self, other):
        """ LESS THAN OPERATOR """
        if type(other) == int or type(other) == float:
            other = ArithmeticExpression(str(other))
        if not self.isSingleExpression():
            raise ValueError('Comparison can only be made when expression is a single expression')
        if type(other) != ArithmeticExpression and type(other) != int and type(other) != float:
            raise TypeError(f"'<' not supported between instances of '{type(self.expression)}' and '{other}'")

        return float(self.expression) < float(other.expression)

    def __le__(self, other):
        """ LESS THAN OR EQUAL TO OPERATOR """
        if type(other) == int or type(other) == float:
            other = ArithmeticExpression(str(other))
        if not self.isSingleExpression():
            raise ValueError('Comparison can only be made when expression is a single expression')
        if type(other) != ArithmeticExpression and type(other) != int and type(other) != float:
            raise TypeError(f"'<=' not supported between instances of '{type(self.expression)}' and '{other}'")

        return float(self.expression) <= float(other.expression)

class Exponential:
    def __init__(self, expression, cast_as_non_exponential=False, cast_entire_term_as_exp=False):
        self.expression = expression
        self.exponential = self.expression
        sign = self.exponential[0]
        if self.exponential[0] == '+' or self.exponential[0] == '-': self.exponential = self.exponential[1:]

        if sign != '+' and sign != '-': sign = ''
        if sign == '+': sign = ''

        expression = str(self.exponential)

        if expression[0] == '(' and expression[-1] == ')':
            tmp_expression = expression[1:-1]
            if len(Expression(tmp_expression)) > 1:
                self.coefficient = '1'
                self.base = expression
                self.exponent = '1'
                return
            else:
                expression = tmp_expression

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
                base_pattern = re.compile(r".+\^{")
                base_matches = base_pattern.findall(expression)
                self.base = base_matches[0][:-2]

                if '^' in self.base and not parenIsBalanced(self.base, 'both'):  # NESTED EXPONENTS
                    self.base = Exponential(self.base).base

                exponent_pattern = re.compile(r"(\^{.+}$|[0-9a-zA-Z]$)")
                exponent_matches = exponent_pattern.findall(expression)
                if '{' in exponent_matches[0] and '}' in exponent_matches[0]:
                    self.exponent = exponent_matches[0][2:-1]
                else:
                    self.exponent = exponent_matches[0]

                if not parenIsBalanced(self.base, 'both') or not parenIsBalanced(self.exponent, 'both'):
                    newExp = Exponential(self.expression, cast_as_non_exponential=True)
                    self.coefficient, self.base, self.exponent = newExp.coefficient, newExp.base, newExp.exponent
                    return

            else:
                i_lc = getIndexOfLastOccurrence(expression, '^')
                exponentData = splitAtIndex(expression, i_lc)
                self.base = exponentData[0]
                self.exponent = exponentData[1]

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
        else:
            self.coefficient = coefficient
            if self.coefficient[-1] == '*': self.coefficient = self.coefficient[:-1]
            if len(self.base) == len(coefficient)+1:
                # if Constant(expression[len(coefficient)]).is_digit and '*' in expression: self.base = expression[len(coefficient)]
                if not Constant(expression[len(coefficient)]).is_digit or '*' in expression: self.base = expression[len(coefficient)]
            else:
                if self.base[len(coefficient)] == '(' and self.base[-1] == ')':
                    self.base = expression[len(coefficient): len(coefficient)+1]
                    i = 1
                    while not parenIsBalanced(self.base, 'both') or self.base == '':
                        self.base = expression[len(coefficient): len(self.coefficient) + i]
                        i += 1
            self.coefficient = f"{sign}{self.coefficient}"

    def computeExponential(self):
        base = Constant(self.base)
        exponent = Constant(self.exponent)
        if base.is_digit and exponent.is_digit:
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
        return (str(self.base) == str(other.base)) and (str(self.exponent) == str(other.exponent))

class Polynomial(Exponential):
    def __init__(self, expression):
        super().__init__(expression)

class Radical(ArithmeticExpression):
    def __init__(self, expression):
        super().__init__(expression)
        self.expression = expression
        if '[' in expression:
            self.is_square_root = False
            pattern = re.compile(r'\[.+]')
            matches = pattern.findall(expression)
            self.index = matches[0][1:-1]

        else:
            self.index = '2'
            self.is_square_root = True

        self.coefficient = ''
        if expression[0] == 's': self.coefficient = '1'
        elif expression[0:2] == '+s': self.coefficient = '1'
        elif expression[0:2] == '-s': self.coefficient = '-'
        else:
            for i in range(len(expression)):
                if expression[i:i+4] == 'sqrt': break
                self.coefficient += expression[i]
        if self.coefficient[0] == '+': self.coefficient = self.coefficient[1:]

    def getRadicand(self):
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

        if len(numerator_matches) == 0 or len(denominator_matches) == 0:
            self.numerator = expression
            if self.numerator[0] == '+': self.numerator = self.numerator[1:]
            self.denominator = '1'
            # raise ExpressionFormatError(expression)
        else:
            self.numerator = numerator_matches[0][5:-2]
            self.denominator = denominator_matches[0][2:-1]

    def reduceFraction(self):
        numerator = int(self.numerator)
        denominator = int(self.denominator)

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
        if numerator.is_digit and denominator.is_digit:
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
                            return Fraction(f"frac{'{'}{reducedFraction.numerator}{'}'}{'{'}{reducedFraction.denominator}{'}'}")
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
        sign = self.expression[0]
        if sign != '+' and sign != '-': sign = ''
        return f"{sign}frac{'{'}{self.numerator}{'}'}{'{'}{self.denominator}{'}'}"

    def __len__(self):
        return len(self.expression)

    def __contains__(self, item):
        """ 'in' OPERATOR """
        return item in self.expression

    def __getitem__(self, index):
        """ [] OPERATOR """
        if isinstance(index, slice):
            return Expression(self.expression[index])
        return self.expression[index]


def parseLatex(latexString: str):
    latexString = latexString.replace('\left(', '(').replace('\\right)', ')').replace('\left\{', '{').replace('\\right\}', '}')\
                             .replace('\cdot', '*').replace(r'\pi', 'pi').replace('\sqrt', 'sqrt').replace('\sqrt[2]','sqrt')\
                             .replace(r'\frac', 'frac').replace('^1','').replace('^{1}', '')

    """ PARSE b^x as b^{x} """
    exponent_pattern = re.compile(r'\^[a-zA-Z0-9]')
    exponent_matches = exponent_pattern.findall(latexString)

    for match in exponent_matches:
        strToReplaceMatch = f"^{'{'}{match[1:]}{'}'}"
        latexString = latexString.replace(match, strToReplaceMatch)

    return latexString

def latexify(expression):
    expression = expression.replace('(', '\left(').replace(')', '\\right)').replace('*', '\cdot').replace('pi', r'\pi')\
                           .replace('sqrt', '\\sqrt').replace('sqrt[2]','sqrt').replace('frac',r'\frac').replace('^{1}', '')

    """ REPLACE \cdotx with \cdot x """
    multiplication_pattern = re.compile(r'\\cdot\w{1}')
    multiplication_matches = multiplication_pattern.findall(expression)

    for match in multiplication_matches:
        charToSpace = match[-1]
        if not charToSpace.isdigit():
            expression = expression.replace(match, f'{match[:-1]} {charToSpace}')

    pi_multiplication_pattern = re.compile(r'\\pi\w{1}')
    pi_multiplication_matches = pi_multiplication_pattern.findall(expression)

    for match in pi_multiplication_matches:
        charToSpace = match[-1]
        if not charToSpace.isdigit():
            expression = expression.replace(match, f'{match[:-1]} {charToSpace}')


    return expression


MAX_SIZE_OF_NUM_BEFORE_CONVERTED_TO_STANDARD_FORM = 10**20


class Expression:
    def __init__(self, expression):
        self.expression = expression
        self.__Terms = []

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
            if ((self.expression[i] == '+' or self.expression[i] == '-') and isCompleteTerm):
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
            radical_pattern = re.compile(r".*[)0-9]sqrt")
            radical_matches = radical_pattern.findall(Terms[i])
            if len(radical_matches) > 0:
                if not parenIsBalanced(radical_matches[0], 'both'):
                    radical_matches = []

            fraction_pattern = re.compile(r".*[)0-9]frac")
            fraction_matches = fraction_pattern.findall(Terms[i])

            exponent_pattern = re.compile(r"^[0-9a-zA-Z()+-]+\^{*.+")
            exponent_matches = exponent_pattern.findall(Terms[i])

            exponent_product = re.compile(r'[a-z]\^{.+}[a-z]\^{.+}')
            matches = exponent_product.findall(str(Terms[i]))

            if  len(matches) > 0:
                Terms[i] = Constant(Terms[i])
            elif 'frac' in Terms[i][0:5] or fraction_matches != []:
                Terms[i] = Fraction(Terms[i])
            elif ('sqrt' in Terms[i][0:5] and parenIsBalanced(Terms[i][0:5])) or radical_matches != []:
                Terms[i] = Radical(Terms[i])
            elif '^' in Terms[i] or exponent_matches != []:
                base = Terms[i].split('^')[0]
                if base[0] == '+': base = base[1:]
                if base[0] == '-': base = base[1:]
                exponent = Terms[i].split('^')[1]
                if exponent[-1] == ')':
                    Terms[i] = Constant(Terms[i])
                elif parenIsBalanced(base) and parenIsBalanced(exponent):
                    Terms[i] = Exponential(Terms[i])
                    # exponent = Constant(Terms[i].exponent)
                    # if exponent.is_integer:
                    #     Terms[i] = Constant(str(Terms[i]))
                else:
                    Terms[i] = Constant(Terms[i])
            else:
                Terms[i] = Constant(Terms[i])
        return Terms

    def replace(self, subStringToBeReplace, replacement):
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

class Constant(ArithmeticExpression):
    def __init__(self, expression):
        super().__init__(expression)
        if '+' in expression or '-' in expression:
            if isDigit2(expression[1:]):
                self.is_digit = True
            else:
                self.is_digit = False
        else:
            if isDigit2(expression):
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
                self.is_integer = True
        else:
            self.is_integer = False

        if self.is_integer:
            self.val = int(self.expression)

def simplifyExpression(expression: Expression, keyword=None, Steps=None, groupedTerms=None, recursiveCall=False):
    expression = Expression(expression.replace(' ', ''))
    # FORMAT
    pattern = re.compile(r'^\(.+\)$')
    matches = pattern.findall(str(expression))
    if len(matches) != 0:
        checkExpression = expression[1:-1]
        if '(' not in checkExpression and ')' not in checkExpression:
            expression = expression[1:-1]

    radical_product_pattern = re.compile(r'sqrt{.+}sqrt{.+}')
    matches = radical_product_pattern.findall(str(expression))
    if len(matches) > 0:
        return {'steps': [], 'finalResult': latexify(str(expression))}


    if Steps is None: Steps = []
    if keyword is None: keyword = 'simplify'


    """ MULTIPLY TERMS """
    if '*' in expression or len(matches)>0:
        for term in expression.getTerms():
            if term[0] == '+' or term[0] == '-': term = term[1:]
            if '*' in term and type(term) != Fraction:
                if '(' in term:
                    pass
                else:
                    termsToBeMultiplied = term.split('*')
                    if listIsInt(termsToBeMultiplied):
                        solution = product(termsToBeMultiplied)
                        productStep = createMainStep(r'\text{Multiply And Divide (left to right)}',
                                                    latexify(f'{term}={solution}'))
                        Steps.append(productStep)
                        expression = expression.replace(str(term), str(solution))
                    else:
                        # if Constant(str(Exponential(termsToBeMultiplied[0]).exponent)).is_digit and Constant(str(Exponential(termsToBeMultiplied[1]).exponent)).is_digit:
                        solution = getProduct2(termsToBeMultiplied)
                        productStep = createMainStep(r'\text{Multiply And Divide (left to right)}',
                                                    latexify(f'{term}={solution}'))
                        Steps.append(productStep)
                        expression = expression.replace(str(term), solution)
                # Steps.append(createMainStep(r'\text{Combine Results}', latexify(f'{expression}')))
            else:
                pass

        expression = Expression(expression)
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
                expression = Expression(expression.replace(str(term), simplifiedProduct))



    if groupedTerms is None: groupedTerms = expression.getGroupedTerms()

    if keyword == 'combine':
        """ CONVERT ALL TERMS TO FRACTION """
        groupedTerms = createGroupedTermsDict()
        for term in expression.getTerms():
            term = Fraction(str(term))
            groupedTerms['Fractions'].append(term)


    groupedExpressions = expression.getGroupedExpressions()

    isSingleGroup = False
    finalResult = ''


    """ GROUP TERMS """
    if len(groupedExpressions['list']) == 1:
        isSingleGroup = True

    if not isSingleGroup and str(expression) != groupedExpressions['strWithoutParen']:
        mainStep = createMainStep(r"\text{Group Terms}",rf"\displaystyle {latexify(expression)}={latexify(groupedExpressions['strWithoutParen'])}")
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
                        if len(tmp_base.getGroupedTerms()['Radicals']) == 1:
                            radical = tmp_base.getGroupedTerms()['Radicals'][0]
                            if str(radical.index) == str(exponent):
                                steps = []
                                exponentialRuleStepInfo = latexify(f'{exponential}={radical.getRadicand()}')
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
                            computationStep = createMainStep(r'\text{Compute Exponent}',latexify(f'{exponential}={solutionToExponential}'))
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

                        base_simplification = Exponential(f"{coefficient}({parseLatex(simplifiedBase['finalResult'])})^{'{'}{exponent}{'}'}")
                        base_simplification.format()
                        # SIMPLIFICATION STEP #1
                        simplificationStepInfo = latexify(f"{exponential}={base_simplification}")
                        if simplificationStepInfo[0] == '+' or simplificationStepInfo[0] == '-': simplificationStepInfo = simplificationStepInfo[1:]
                        simplificationStep = createMainStep(r'\text{Simplify Base}', simplificationStepInfo)
                        temp_exponential = exponential
                        if temp_exponential[0] == '+' or temp_exponential[0] == '-': temp_exponential = temp_exponential[1:]
                        if str(temp_exponential) != str(base_simplification): steps.append(simplificationStep)

                        """ SIMPLIFY EXPONENT """
                        simplifiedExponent = simplifyExpression(exponent)
                        for step in simplifiedExponent['steps']:
                            if step['type'] == 'main-step':
                                steps.append(step)
                            elif step['type'] == 'e-step':
                                for e_step in step['e-steps']:
                                    steps.append(e_step)

                        exponent_simplification = Exponential(f"{coefficient}{base_simplification.base}^{'{'}{parseLatex(simplifiedExponent['finalResult'])}{'}'}")
                        exponent_simplification.format()
                        # SIMPLIFICATION STEP #2
                        simplificationStepInfo = latexify(f"{base_simplification}={exponent_simplification}")
                        if simplificationStepInfo[0] == '+' or simplificationStepInfo[0] == '-': simplificationStepInfo = simplificationStepInfo[1:]
                        simplificationStep = createMainStep(r'\text{Simplify Exponent}', simplificationStepInfo)
                        temp_exponential = exponent
                        if temp_exponential[0] == '+' or temp_exponential[0] == '1': temp_exponential = temp_exponential[1:]
                        if latexify(temp_exponential) != latexify(exponent_simplification.exponent): steps.append(simplificationStep)

                        final_simplification = exponent_simplification

                        # COMPUTATION STEP
                        solutionToFinalExponential = final_simplification.computeExponential()
                        if solutionToFinalExponential != False and solutionToFinalExponential.is_integer:
                            finalStep = createMainStep(r'\text{Compute Exponential}', latexify(f'{final_simplification}={solutionToFinalExponential}'))
                            steps.append(finalStep)
                            final_simplification = Exponential(solutionToFinalExponential)
                        else:
                            if str(final_simplification.exponent) == '0':
                                finalStep = createMainStep(r'\text{Apply exponent rule:}\ a^0=1', latexify(f'{final_simplification}=1'))
                                steps.append(finalStep)
                                final_simplification = Exponential('1')
                            if str(final_simplification.base) == '0':
                                finalStep = createMainStep(r'\text{Apply exponent rule:}\ 0^a=0', latexify(f'{final_simplification}=0'))
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
                        if heading[0] == '+' or heading[0] == '-': heading = heading[1:]
                        e_step = createExpandableStep(heading, steps)
                        Steps.append(e_step)

                originalExponentialStr = getExponentialStr(groupedTerms['Exponential'])
                if len(simplifiedExponentials) > 0:
                    simplifiedExponentialStr = getExponentialStr(simplifiedExponentials)

                    if (originalExponentialStr != simplifiedExponentialStr) and len(simplifiedExponentials)>1:
                        # COMBINE RESULTS STEP
                        Steps.append(createMainStep(r'\text{Combine Exponentials}', latexify(f'{originalExponentialStr}={simplifiedExponentialStr}')))
                    finalSimplification = addExponentials(simplifiedExponentials)
                    if finalSimplification[0] == '+': finalSimplification = finalSimplification[1:]
                    # GROUP LIKE EXPONENTIALS STEP
                    groupedExponentials = groupLikeExponentials(simplifiedExponentials)
                    if groupedExponentials[0] == '+': groupedExponentials = groupedExponentials[1:]
                    groupExpStep = createMainStep(r'\text{Group Like Exponentials}', latexify(f'{simplifiedExponentialStr}={groupedExponentials}'))
                    if simplifiedExponentialStr != groupedExponentials: Steps.append(groupExpStep)

                    # ADDITION STEP
                    additionStepInfo = latexify(f'{groupedExponentials}={finalSimplification}')
                    additionStep = createMainStep(r'\text{Add Like Exponentials}', additionStepInfo)
                    if str(simplifiedExponentialStr) != str(finalSimplification): Steps.append(additionStep)
                    # UPDATE FINAL RESULT
                    sign = finalSimplification[0]
                    if (sign != '+' and sign != '-'): sign = '+'
                    finalResult += f'{sign}{finalSimplification}'

            elif group == 'Radicals':
                """ SIMPLIFY RADICALS """
                Radicals = groupedTerms['Radicals']
                for radical in Radicals:
                    if radical.coefficient[0] == '-': radical.coefficient = radical.coefficient[1:]
                    if radical.coefficient == '1': radical.coefficient = ''

                    radicand = radical.getRadicand()
                    if radicand.isSingleExpression():
                        if len(radicand.getGroupedTerms()['Exponential']) > 0:
                            radicand = radicand.getGroupedTerms()['Exponential'][0]
                            if radical.index == radicand.exponent:
                                steps = []
                                radicalRuleStepInfo = latexify(f'{radical}={radicand.base}')
                                radicalRuleStep = createMainStep(r'\text{Apply radical rule:}\ \sqrt[n]{a^n}=a',radicalRuleStepInfo)
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
                                break
                            else:
                                radicand = Expression(str(radicand))

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
                    if simplificationStepInfo[0] == '+' or simplificationStepInfo[0] == '-': simplificationStepInfo = simplificationStepInfo[1:]
                    simplificationStep = createMainStep(r'\text{Simplify}', simplificationStepInfo)
                    temp_radical = radical
                    if temp_radical[0] == '+' or temp_radical[0] == '-': temp_radical = temp_radical[1:]
                    if latexify(temp_radical) != latexify(simplification): steps.append(simplificationStep)
                    # COMPUTATION STEP
                    finalRadical = Radical(simplification)
                    solutionToFinalRadical = finalRadical.computeRadical()
                    if solutionToFinalRadical != False and solutionToFinalRadical.is_integer:
                        if finalRadical.coefficient == '1':
                            finalStep = createMainStep(r'\text{Compute Radical}', latexify(f'{simplification}={solutionToFinalRadical}'))
                            steps.append(finalStep)
                            simplification = solutionToFinalRadical
                        else:
                            finalRadical.coefficient = Constant(finalRadical.coefficient)
                            if finalRadical.coefficient.is_digit:
                                finalStep = createMainStep(r'\text{Compute Radical}',
                                                           latexify(f'{simplification}={finalRadical.coefficient}*{solutionToFinalRadical}'))
                                steps.append(finalStep)
                                simplification = f'{finalRadical.coefficient}*{solutionToFinalRadical}'
                            else:
                                finalStep = createMainStep(r'\text{Compute Radical}',
                                                           latexify(f'{simplification}={solutionToFinalRadical}{finalRadical.coefficient}'))
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
                                factoredResult = f"sqrt[{index}]{'{'}{mpp}{'}'}*sqrt[{index}]{'{'}{radicand//mpp}{'}'}"
                                factorStepInfo = latexify(f"{finalRadical}={factoredResult}")
                                factorStep = createMainStep(r'\text{Factor Radical}', factorStepInfo)
                                steps.append(factorStep)
                                # SIMPLIFICATION STEP 2
                                firstFactorOfRadical = Radical(f"sqrt[{index}]{'{'}{mpp}{'}'}")
                                secondFactorOfRadical = Radical(f"sqrt[{index}]{'{'}{radicand//mpp}{'}'}")
                                simplificationStepInfo = latexify(f"{factoredResult}={firstFactorOfRadical.computeRadical()}{secondFactorOfRadical}")
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
                    numerator = Expression(fraction.numerator)
                    denominator = Expression(fraction.denominator)
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
                    temp_fraction = fraction
                    if temp_fraction[0] == '+' or temp_fraction[0] == '-': temp_fraction = temp_fraction[1:]
                    if (str(temp_fraction) != str(numerator_simplification)) and fraction.denominator != '1': steps.append(simplificationStep)

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
                    simplificationStepInfo = latexify(f"{fraction}={denominator_simplification}")
                    if simplificationStepInfo[0] == '+' or simplificationStepInfo[0] == '-': simplificationStepInfo = simplificationStepInfo[1:]
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
                        computationStep = createMainStep(r'\text{Reduce Fraction}', latexify(f'{simplifiedFraction}={solutionToFraction}'))
                        steps.append(computationStep)
                        final_simplification = solutionToFraction
                    elif solutionToFraction != False and solutionToFraction.is_integer:
                        computationStep = createMainStep(r'\text{Divide The Numbers}', latexify(f'{simplifiedFraction}={solutionToFraction}'))
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
                                            newFraction = Fraction(f"{sign}frac{'{'}{n_term}{'}'}{'{'}{denominator}{'}'}")
                                            newFractions.append(newFraction)
                                        else:
                                            newFraction = Fraction(f"frac{'{'}{n_term}{'}'}{'{'}{denominator}{'}'}")
                                            newFractions.append(newFraction)

                                splitFractions = ''
                                for frac in newFractions:
                                    splitFractions += str(frac)
                                splitFractions = Expression(splitFractions)

                                splitFractionStepInfo = latexify(f'{simplifiedFraction}={splitFractions}')
                                splitFractionStep = createMainStep(r'\text{Apply The Fraction Rule:}\ \frac{a \pm b}{c}=\frac{a}{c}\pm\frac{b}{c}', splitFractionStepInfo)
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
                                if len(Expression(split_fraction.numerator)) != 1 or len(Expression(split_fraction.denominator)) != 1:
                                    break
                                numerator, denominator = Exponential(parseAsExponential(split_fraction.numerator)), Exponential(parseAsExponential(split_fraction.denominator))
                                if numerator.base == denominator.base:
                                    base = numerator.base
                                    if Constant(numerator.exponent).is_integer and Constant(denominator.exponent).is_integer:
                                        differenceInExp = int(numerator.exponent) - int(denominator.exponent)
                                        if differenceInExp == 0:
                                            simplifiedFraction = Fraction(f"frac{'{'}{numerator.coefficient}{'}'}{'{'}{denominator.coefficient}{'}'}")
                                            # if simplifiedFraction.computeFraction() != False:
                                            #     simplifiedFraction = simplifiedFraction.computeFraction()
                                            if simplifiedFraction.denominator == '1': simplifiedFraction = simplifiedFraction.numerator
                                            simplifiedSplitFractions += f"{sign}{simplifiedFraction}"
                                        elif differenceInExp > 0:
                                            numExponent = int(numerator.exponent) - int(denominator.exponent)
                                            simplifiedFraction = Fraction(f"frac{'{'}{numerator.coefficient}{base}^{'{'}{numExponent}{'}'}{'}'}{'{'}{denominator.coefficient}{'}'}")
                                            simplifiedSplitFractions += f"{sign}{simplifiedFraction}"
                                        else:
                                            numExponent = abs(int(numerator.exponent) - int(denominator.exponent))
                                            simplifiedFraction = Fraction(f"frac{'{'}{numerator.coefficient}{'}'}{'{'}{denominator.coefficient}{base}^{numExponent}{'}'}")
                                            simplifiedSplitFractions += f"{sign}{simplifiedFraction}"
                                else:
                                    simplifiedFraction = str(split_fraction)
                                    simplifiedSplitFractions += str(split_fraction)

                                if simplifiedFraction[0] == '+' or simplifiedFraction[0] == '-': simplifiedFraction = simplifiedFraction[1:]
                                # ADD CANCEL LIKE TERMS STEP
                                simplifiedFractionStepInfo = latexify(f'{split_fraction}={simplifiedFraction}')
                                if simplifiedFractionStepInfo[0] == '+' or simplifiedFractionStepInfo[0] == '-': simplifiedFractionStepInfo = simplifiedFractionStepInfo[1:]
                                simplifiedFractionStep = createMainStep(r'\text{Cancel like terms}', simplifiedFractionStepInfo)
                                tmp_fraction = split_fraction
                                if tmp_fraction[0] == '+' or tmp_fraction[0] == '-': tmp_fraction = tmp_fraction[1:]
                                if str(tmp_fraction) != str(simplifiedFraction): divideFractionSteps.append(simplifiedFractionStep)

                            if simplifiedSplitFractions == '': simplifiedSplitFractions = simplifiedFraction

                            # ADD DIVIDE FRACTION STEP
                            if simplifiedSplitFractions[0] == '+': simplifiedSplitFractions = simplifiedSplitFractions[1:]
                            heading = latexify(f'{splitFractions}={simplifiedSplitFractions}')
                            divideFractionStepEStep = createExpandableStep(heading, divideFractionSteps)
                            if str(splitFractions) != str(simplifiedSplitFractions): steps.append(divideFractionStepEStep)

                            final_simplification = simplifiedSplitFractions

                        else:
                            final_simplification = simplifiedFraction


                    # CREATE AND ADD E-STEP
                    cmp_fraction = fraction
                    if cmp_fraction[0] == '+' or cmp_fraction[0] == '-': cmp_fraction = cmp_fraction[1:]
                    heading = latexify(f"{fraction}={final_simplification}")
                    if heading[0] == '+' or heading[0] == '-': heading = heading[1:]
                    e_step = createExpandableStep(heading, steps)
                    if str(cmp_fraction) != str(final_simplification): Steps.append(e_step)
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

                    denominators = [f.denominator if len(Expression(f.denominator)) == 1 else f'({f.denominator})' for f in simplifiedFractions]
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
                                    exp_denominator = Exponential(frac.denominator)
                                    exp_lcm = Exponential(lcm)
                                if exp_denominator.base == exp_lcm.base:
                                    lcmFactorExponentExpression = Expression(f'{Exponential(lcm).exponent}-{Exponential(frac.denominator).exponent}')
                                    lcmFactorExponentExpression = simplifyExpression(lcmFactorExponentExpression)['finalResult']
                                    if lcmFactorExponentExpression == '0':
                                        lcmFactor = '1'
                                    else:
                                        lcmFactor = f"{Exponential(frac.denominator).base}^{'{'}{lcmFactorExponentExpression}{'}'}"
                                else:
                                    lcmFactor = getLCMFactor(frac.denominator, denominators)
                                if lcmFactor[0] == '1' and len(lcmFactor)>1 and not Constant(lcmFactor).is_digit: lcmFactor = lcmFactor[1:]
                                if len(lcmFactor) > 1:
                                    if lcmFactor[-1] == '1': lcmFactor = lcmFactor[:-1]
                            else:
                                lcmFactor = getLCMFactor(f'({frac.denominator})', denominators)
                            if lcmFactor == '1': lcmFactor = ''
                            if frac.numerator != '1':
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
                                    adjustedFrac = Fraction(f"{sign}frac{'{'}{int(frac.numerator)*lcmFactor}{'}'}{'{'}{lcm}{'}'}")
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
                    combineFractionStep = createMainStep(r"\text{Apply The Fraction Rule:}\ \frac{a}{c}\pm\frac{b}{c}=\frac{a \pm b}{c}",combineFractionStepInfo)
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

        for group in groupedTerms:
            if groupedTerms[group] != []:
                if group == 'Fractions':
                    for fraction in groupedTerms[group]:
                        if '^{1}' in fraction: fraction = Fraction(fraction.replace('^{1}', ''))
                        newGroupedTerms['Fractions'].append(fraction)
                elif group != 'Exponential':
                    for term in groupedTerms[group]:
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

def formatExpression(expression):
    return expression.replace('++','+').replace('-+','-').replace('+-','-').replace('--','+')

def simplifyConstants(expression, constants: list):
    numbers, variables, Steps = [], [], []
    for term in constants:
        if type(term) != Constant:
            raise TypeError(f'{term} is not a constant')
        if term.is_digit:
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
                                      latexify(f'{newExpression}={newExpression.replace(numbersStr, str(sumOfNumbers))}'))
            Steps.append(mainStep)
            newExpression = newExpression.replace(numbersStr, str(sumOfNumbers))

    finalExpression = newExpression
    finalExpression = finalExpression.replace('++','+').replace('--','+').replace('+-','-').replace('-+','-').replace('+0','').replace('-0','')

    return {'finalExpression': finalExpression, 'Steps': Steps}

def createMainStep(description, info):
    mainStep = {'type': 'main-step', 'description': rf'\displaystyle {description}', 'info': rf'\displaystyle {info}'}
    return mainStep
def createExpandableStep(heading, e_steps: list):
    e_step = {'type': 'e-step', 'heading': rf'\displaystyle {heading}', 'e-steps': e_steps}
    return e_step

def createGroupedTermsDict():
    return {
        'Exponential': [],
        'Radicals': [],
        'Fractions': [],
        'Constants': [],
    }

def createEStepHeadingFromGroup(group: list, addParen: bool):
    if addParen:
        heading = '('
        for term in group:
            heading += str(term)
        heading += ')'
        return heading
    else:
        heading = ''
        for term in group:
            if isinstance(term, Constant):
                if term[0] != '+' and term[0] != '-': term = f'+{term}'
            heading += str(term)
        if heading[0] == '+': heading = heading[1:]
        return heading

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
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
def getLCM(terms: list, listOfNumbers=False, termsType=None):
    if termsType is None: termsType = 'Numbers'

    if termsType == 'Mixed':
        numberTerms, variableTerms = [], []
        for term in terms:
            if Constant(term).is_digit: numberTerms.append(term)
            else: variableTerms.append(term)

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
            term = Exponential(term)

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
            elif '^{' in term and '(' not in Exponential(term).base:
                termsWithExponentsAndNoParen += term
            elif '^{' not in term and '(' not in term and Exponential(term).exponent == '1':
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
            multiplesOfNum = {num * i for i in range(1, 500)}
            multiples.append(multiplesOfNum)
        commonMultiples = multiples[0].intersection(*multiples)
        return min(commonMultiples)
def getLCMFactor(fracDenominator: str, denominators: list):
    denominatorDigits = []
    denominatorVariables = []
    for term in denominators:
        if Constant(term).is_digit: denominatorDigits.append(term)
        else: denominatorVariables.append(term)

    fracDenominator = [fracDenominator]
    lcmFactorList = list_diff(denominators, fracDenominator)

    if len(denominatorDigits) > 1:
        variableLCMFactor = list_diff(denominatorVariables, fracDenominator)
        digitsLCM = product(denominatorDigits)
        denominatorCoefficient = float(Exponential(fracDenominator).coefficient)
        lcmFactor = f'{digitsLCM/denominatorCoefficient}'
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
            simplifiedExponential += f'{coefficient}*{exp}'

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
def parseAsExponential(expression):
    parsedExpression = ''
    if '^' not in expression:
        for char in expression:
            if Constant(char).is_digit or char == '-':
                parsedExpression += char
            else:
                parsedExpression += f"{char}^{'{'}1{'}'}"
        return parsedExpression
    else:
        return expression

def parenIsBalanced(string, parenToCheckFor='normal'):
    numOpenParen = 0
    numClosedParen = 0
    if parenToCheckFor == 'normal':
        openParen = '('
        closedParen = ')'
    else:
        openParen = '{'
        closedParen = '}'

    if parenToCheckFor == 'both':
        for char in string:
            if char == '(' or char == '{':
                numOpenParen += 1
            elif char == ')' or char == '}':
                numClosedParen += 1
        return numOpenParen == numClosedParen

    for char in string:
        if char == openParen:
            numOpenParen += 1
        elif char == closedParen:
            numClosedParen += 1

    return numOpenParen == numClosedParen

def isDigit2(item: str):
    if item.isdigit():
        return True
    if '.' in item:
        try:
            float(item)
            return True
        except:
            return False

def product(numbers: list):
    prod = 1
    for num in numbers:
        prod *= int(num)
    return prod
def getProduct2(terms: list):
    Coefficients = []

    """ GET COEFFICIENTS """
    for term in terms:
        # C = Exponential(str(term)).coefficient
        if Constant(term).is_digit:  C = term
        else:
            C = Exponential(term).coefficient
            # C = ''
            # for char in term:
            #     if not Constant(char).is_digit and char != '.':
            #         break
            #     else:
            #         if not Constant(char).is_digit:
            #             C += char
            # if C == '': C = '1'

        Coefficients.append(C)

    seenTerms = {}
    for i, term in enumerate(terms):
        if term[0] == '+' or term[0] == '-': term = term[1:]
        term = Exponential(term)

        if term.base not in seenTerms:
            seenTerms.update({str(term.base): term.exponent})
        else:
            if Constant(term.base).is_digit:
                Coefficients[i-1] = '1'
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
            # if term != finalProduct:
            #     finalProduct += f"*{term}^{'{'}{seenTerms[term]}{'}'}"

    finalProduct = finalProduct.replace('^{1}', '')


    return finalProduct

def listIsInt(X: list):
    """ RETURNS THE TYPE OF THE ELEMENTS IN A LIST """
    isInt = True
    for item in X:
        if not Constant(item).is_digit:
            isInt = False

    return isInt

def multiplyTerms(terms: list):
    seenTerms = {}
    for term in terms:
        if term[0] == '+' or term[0] == '-': term = term[1:]
        if term not in seenTerms:
            seenTerms.update({term: 1})
        else:
            counter = seenTerms[term]
            seenTerms.update({term: counter+1})

    product = ''
    for term in seenTerms:
        if '^' not in term:
            product += f"{term}^{'{'}{seenTerms[term]}{'}'}"
        else:
            product += f"*{term}^{'{'}{seenTerms[term]}{'}'}"

    product = product.replace('^{1}', '')
    return product

def indexOf(iterable, searchFor):
    for i, item in enumerate(iterable):
        if item == searchFor:
            return i
    return None

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

def getIndexOfLastOccurrence(expression: str, charToFind: str):
    indexes = []
    for i, char in enumerate(expression):
        if char == charToFind:
            indexes.append(i)

    return indexes[-1]
def getExponentialStr(exponentials: list):
    expStr = ''
    for exp in exponentials:
        exp = str(exp)
        if exp[0] != '+' and exp[0] != '-':
            exp = f'+{exp}'
        expStr += exp

    if expStr[0] == '+': expStr = expStr[1:]
    return expStr

def list_diff(A: list, B: list):
    """ RETURN THE SET DIFFERENCE OF LIST A AND B """
    newList = []
    for item in A:
        if item not in B:
            newList.append(item)
    return newList

def numOccurrences(expression, charToCheck):
    """ RETURNS THE NUMBER OF SPECIFIED OCCURRENCE IN A STRING """
    counter = 0
    for char in expression:
        if char == charToCheck:
            counter += 1
    return counter

def splitAtIndex(expression: iter, index: int):
    splitArray = [expression[0:index], expression[index + 1:]]
    return splitArray

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

def reverseList(L):
    return L[::-1]

def main():
    E = Expression('2*3x')
    # E = Expression('6+x^{2}*y^{3}')
    print(simplifyExpression(E, keyword='simplify'))





if __name__ == '__main__':
    main()
