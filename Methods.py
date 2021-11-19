from math import floor, pi, e, sqrt



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
                if term in ['+','-','*','/'] and '{' not in seenTerms:
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

                    if (expressionToTheLeftOfExponent[:indexWhereExponentEnds] == '') and exponentEndIndex == len(exponent) - 1:
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
                    while ((self.expression[j] not in allOperators) or (operation == 'multiply-only')) and (self.expression[j] != operator and self.expression[j] != '}'):
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
                                while self.expression[k] not in getRestrictedOperators('*') and self.expression[k] != '}':
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
            return operationsOnExponentWithIndex if returnWithIndex else (operationsOnExponent, operationCounter) if returnWithCounter else operationsOnExponent
        else:
            return 'no-operation'

    def getAllExponentsInExpression(self):
        """ RETURNS AN ARRAY OF ALL THE EXPONENTS IN AN EXPRESSION """
        expression = self.applyExponentsToSingleExpressions()
        allOperations = ['+', '-', '*', '/', '^']
        currentExpressionStartIndex = 0
        allExponentExpressions = []
        for i in range(len(expression)):
            if (expression[i] in allOperations and expression[i - 1] == '}') or (expression[i] == '}' and i == len(expression) - 1) or (expression[i] in allOperations and expression[i - 2] == '^'):
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
            newExpression = f"{float(expressionAsArr[0])*10**float(powerOf10):.0f}"
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
    def __init__(self, expression):
        self.expression = expression
        expression = ArithmeticExpression(expression)
        if '^' not in expression:
            self.base = expression
            self.exponent = ArithmeticExpression('1')
        else:
            exponentIndex = indexOf(str(expression), '^')
            exponentData = expression.splitExpression(exponentIndex, '^', binarySplit=False)

            self.base = ArithmeticExpression(exponentData[0])
            self.exponent = ArithmeticExpression(exponentData[1])

            if '{' in self.exponent:
                expressionInExponent = self.exponent.replace('{', '').replace('}', '')
                self.exponent = ArithmeticExpression(expressionInExponent)

    def __str__(self):
        return self.expression
    def __repr__(self):
        return self.expression

class Radical(ArithmeticExpression):
    def __init__(self, expression):
        super().__init__(expression)
        if type(expression) != ArithmeticExpression:
            self.expression = ArithmeticExpression(expression)
        else:
            self.expression = expression

    def getExpressionInsideRadical(self):
        expressionInside = ''
        for i in range(len(self.expression)):
            if self.expression[i] == '{' and self.expression[:i].replace('+', '').replace('-', '') == 'sqrt':
                j = i+1
                while j != len(self.expression)-1:
                    expressionInside += self.expression[j]
                    j += 1

        return ArithmeticExpression(expressionInside)

    def __str__(self):
        return str(self.expression)

class Fraction(ArithmeticExpression):
    def __init__(self, expression):
        super().__init__(expression)
        self.fraction_expression = expression

    def getNumerator(self):
        numOpenCurlyParen = 0
        numClosedCurlyParen = 0
        numerator = ''

        for i in range(4, len(self.fraction_expression)):
            if self.fraction_expression[i] == '{':
                numOpenCurlyParen += 1
            elif self.fraction_expression[i] == '}':
                numClosedCurlyParen += 1

            if numOpenCurlyParen == numClosedCurlyParen:
                numerator = self.fraction_expression[5:i]
                return ArithmeticExpression(numerator)

    def getDenominator(self):
        return ArithmeticExpression(self.fraction_expression[7+len(self.getNumerator()):len(self.fraction_expression)-1])

def parseLatex(latexString: str):
    latexString = latexString.replace('\left(', '(').replace('\\right)', ')').replace('\left\{', '{').replace('\\right\}', '}')\
                             .replace('\cdot', '*').replace(r'\pi', 'pi').replace('\sqrt', 'sqrt')\
                             .replace(r'\frac', 'frac')
    return latexString

def latexify(expression):
    expression = expression.replace('(', '\left(').replace(')', '\\right)').replace('*', '\cdot').replace('pi', r'\pi')\
                           .replace('sqrt', '\\sqrt').replace('frac',r'\frac')
    return expression


MAX_SIZE_OF_NUM_BEFORE_CONVERTED_TO_STANDARD_FORM = 10**20

# def evaluateArithmetic(expression, stepCounter=None, Steps=None, returnStepsAsArray=False):
#     if type(expression) != ArithmeticExpression:
#         expression = ArithmeticExpression(expression)
#     if Steps is None:
#         Steps = {}
#     if stepCounter is None:
#         stepCounter = 0
#     if expression.isSingleExpression():
#
#         if expression >= MAX_SIZE_OF_NUM_BEFORE_CONVERTED_TO_STANDARD_FORM:
#             expression = convertToStandardForm(str(expression))
#         if returnStepsAsArray:
#             stepsAsArray = []
#             for step in Steps:
#                 stepsAsArray.append(Steps[step])
#             return (stepsAsArray, str(expression), stepCounter)
#         return (Steps, str(expression), stepCounter)
#
#     allOperators = ['+','-','*','/']
#     operation = expression.getOperationToPerform()
#
#     # expression = expression.convertOutOfStandardForm()
#
#     if '++' in expression:
#         simplifiedExpression = expression.replace('++', '+')
#         expression = simplifiedExpression
#
#         stepDictValue = {
#             'step': f'Apply rule: a++b = a+b',
#             'simplification': f'{simplifiedExpression}'
#         }
#         stepCounter += 1
#         Steps.update({stepCounter: stepDictValue})
#
#         return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)
#
#     if '+-' in expression:
#         simplifiedExpression = expression.replace('+-', '-')
#         expression = simplifiedExpression
#
#         stepDictValue = {
#             'step': f'Apply rule: a+-b = a-b',
#             'simplification': f'{simplifiedExpression}'
#         }
#         stepCounter += 1
#         Steps.update({stepCounter: stepDictValue})
#
#         return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)
#
#     if '--' in expression:
#         simplifiedExpression = expression.replace('--', '+')
#         expression = simplifiedExpression
#
#         stepDictValue = {
#             'step': f'Apply rule: a--b = a+b',
#             'simplification': f'{simplifiedExpression}'
#         }
#         stepCounter += 1
#         Steps.update({stepCounter: stepDictValue})
#
#         return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)
#
#
#
#     """ CHECK OPERATIONS """
#     if operation == 'general-arithmetic' and '(' not in expression:
#         expressionWithOrder = expression.applyPEMDAS()
#
#         stepDictValue = {
#             'step': f'Apply PEMDAS: {expression} = {expressionWithOrder}',
#             'simplification': f'{expressionWithOrder}'
#         }
#         expression = ArithmeticExpression(expressionWithOrder)
#         stepCounter += 1
#         Steps.update({stepCounter: stepDictValue})
#
#     elif operation == 'radical':
#         expression = Radical(expression)
#         expressionInsideRadical = expression.getExpressionInsideRadical()
#
#         if expressionInsideRadical.isSingleExpression():
#             simplifiedExpression = castToFloatOrInt(sqrt(float(str(expressionInsideRadical))), True)
#
#             stepCounter += 1
#             stepDictValue = {
#                 'step': f"Simplify Radical: sqrt{'{'}{expressionInsideRadical}{'}'} = {simplifiedExpression}",
#                 'simplification': f"{simplifiedExpression}"
#             }
#
#             Steps.update({stepCounter: stepDictValue})
#             return evaluateArithmetic(simplifiedExpression, stepCounter, Steps, returnStepsAsArray)
#
#         else:
#             Simplification = evaluateArithmetic(expressionInsideRadical, returnStepsAsArray=True)
#             result = Simplification[1]
#             stepsAsArray = Simplification[0]
#
#             for stepToAdd in stepsAsArray:
#                 stepDictValue = {
#                     'step': stepToAdd['step'],
#                     'simplification': expression.replace(f"{expressionInsideRadical}", f"{stepToAdd['simplification']}")
#                 }
#                 stepCounter += 1
#                 Steps.update({stepCounter: stepDictValue})
#
#             simplifiedExpression = expression.replace(f"{expressionInsideRadical}", result)
#             return evaluateArithmetic(simplifiedExpression, stepCounter, Steps, returnStepsAsArray)
#
#     elif operation == 'fraction-arithmetic':
#         expression = Fraction(expression)
#
#         # expression = frac{1+2+3}{5+2}
#         Steps = []
#
#         numerator = expression.getNumerator()
#         denominator = expression.getDenominator()
#
#         simplifiedNumerator = evaluateArithmetic(numerator)[1]
#         simplifiedDenominator = evaluateArithmetic(denominator)[1]
#
#         if not numerator.isSingleExpression():
#             stepToAdd = {}
#             stepToAdd['id'], stepToAdd['type'] = 1, 'e-step'
#             stepToAdd['heading'] = rf"\displaystyle \text{'{'}Simplify Numerator:{'}'}\ {latexify(expression.getNumerator())}={simplifiedNumerator}"
#             stepToAdd['e-steps'] = []
#
#             intermediateSteps = evaluateArithmetic(numerator)[0]
#
#             for stepNum in intermediateSteps:
#                 currentStep = intermediateSteps[stepNum]
#                 currentStep['type'] = 'main-step'
#                 currentStep['description'] = currentStep['step'].split(':')[0]
#                 currentStep['description'] = rf"\text{'{'}{currentStep['description']}{'}'}"
#                 currentStep['info'] = latexify(currentStep['step'].split(':')[1].lstrip())
#
#                 del currentStep['step']
#                 del currentStep['simplification']
#                 stepToAdd['e-steps'].append(currentStep)
#
#             Steps.append(stepToAdd)
#
#         if not denominator.isSingleExpression():
#             stepToAdd = {}
#             stepToAdd['id'], stepToAdd['type'] = 1, 'e-step'
#             stepToAdd['heading'] = rf"\displaystyle \text{'{'}Simplify Denominator:{'}'}\ {latexify(denominator)}={simplifiedDenominator}"
#             stepToAdd['e-steps'] = []
#
#             intermediateSteps = evaluateArithmetic(denominator)[0]
#
#             for stepNum in intermediateSteps:
#                 currentStep = intermediateSteps[stepNum]
#                 currentStep['type'] = 'main-step'
#                 currentStep['description'] = currentStep['step'].split(':')[0]
#                 currentStep['description'] = rf"\text{'{'}{currentStep['description']}{'}'}"
#                 currentStep['info'] = latexify(currentStep['step'].split(':')[1].lstrip())
#
#                 del currentStep['step']
#                 del currentStep['simplification']
#                 stepToAdd['e-steps'].append(currentStep)
#
#             Steps.append(stepToAdd)
#
#
#         return {'steps': Steps, 'finalResult': rf"\frac{'{'}{simplifiedNumerator}{'}'}{'{'}{simplifiedDenominator}{'}'}"}
#
#     elif operation == 'arithmetic-exponent-multiply':
#         allExponentsInExpression = expression.getAllExponentsInExpression()
#         baseToUse = Exponential(allExponentsInExpression[0]).base
#
#         exponents = []
#         for expression in allExponentsInExpression:
#             expression = Exponential(expression)
#             if expression.exponent.isSingleExpression():
#                 exponents.append(f"{expression.exponent}")
#             else:
#                 exponents.append(f"({expression.exponent})")
#
#         operation = '+'
#         newExponent = operation.join(exponents)
#
#         simplifiedExpression = ArithmeticExpression(f"{baseToUse}^{'{'}{newExponent}{'}'}")
#
#         stepCounter += 1
#         stepDictValue = {
#             'step': f"Apply rule exponent: a^b * a^c = a^{'{'}b+c{'}'}",
#             'simplification': f"{simplifiedExpression}"
#         }
#
#         Steps.update({stepCounter: stepDictValue})
#         return evaluateArithmetic(simplifiedExpression, stepCounter, Steps, returnStepsAsArray)
#
#
#     elif operation == 'arithmetic-exponent-single':
#         exponentIndex = indexOf(str(expression), '^')
#         exponentData = expression.splitExpression(exponentIndex, '^', binarySplit=False)
#
#         base = ArithmeticExpression(exponentData[0])
#         exponent = ArithmeticExpression(exponentData[1])
#
#         if base == 1:
#             result = '1'
#             stepCounter += 1
#             stepDictValue = {
#                 'step': f'Apply rule exponent: 1^a = 1',
#                 'simplification': f"{result}"
#             }
#             Steps.update({stepCounter: stepDictValue})
#             return evaluateArithmetic(ArithmeticExpression(result), stepCounter, Steps, returnStepsAsArray)
#
#
#         if '{' in exponent:
#             expressionInExponent = ArithmeticExpression(exponent.replace('{', '').replace('}', ''))
#             if expressionInExponent.isSingleExpression():
#                 expressionInExponent = expressionInExponent.replace('{', '').replace('}', '')
#                 if base.isSingleExpression():
#                     result = castToFloatOrInt(eval(f"{base}**{expressionInExponent}"), True)
#                     SF = convertToStandardForm
#                     stepCounter += 1
#                     stepDictValue = {
#                         'step': f'Calculate exponent: {expression} = {SF(result, True)}',
#                         'simplification': f"{SF(result, True)}"
#                     }
#                     Steps.update({stepCounter: stepDictValue})
#                     return evaluateArithmetic(ArithmeticExpression(result), stepCounter, Steps, returnStepsAsArray)
#             else:
#                 Simplification = evaluateArithmetic(expressionInExponent, returnStepsAsArray=True)
#                 result = Simplification[1]
#                 stepsAsArray = Simplification[0]
#
#                 for stepToAdd in stepsAsArray:
#                     stepDictValue = {
#                         'step': f"{stepToAdd['step']}",
#                         'simplification': expression.replace(f'{expressionInExponent}', f"{stepToAdd['simplification']}")
#                     }
#                     stepCounter += 1
#                     Steps.update({stepCounter: stepDictValue})
#
#                 simplifiedExpression = expression.replace(f'{expressionInExponent}', result)
#                 expression = simplifiedExpression
#
#                 return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)
#
#         else:
#             if base.isSingleExpression():
#                 result = castToFloatOrInt(eval(f"{base}**{exponent}"), True)
#                 SF = convertToStandardForm
#
#                 stepCounter += 1
#                 stepDictValue = {
#                     'step': f'Calculate exponent: {expression} = {SF(result, True)}',
#                     'simplification': f"{SF(result, True)}"
#                 }
#                 Steps.update({stepCounter: stepDictValue})
#                 return evaluateArithmetic(ArithmeticExpression(result), stepCounter, Steps, returnStepsAsArray)
#
#     elif operation == 'multiply-only':
#         result = performOperation(expression, operation='multiply-only')
#         stepCounter += 1
#         stepDictValue = {
#             'step': f'Multiply [left to right]: {expression} = {result}',
#             'simplification': result
#         }
#         Steps.update({stepCounter: stepDictValue})
#         return evaluateArithmetic(result, stepCounter, Steps, returnStepsAsArray)
#
#     elif operation == 'add-subtract-only' and '(' not in expression:
#         result = performOperation(expression)
#         stepCounter += 1
#         stepDictValue = {
#             'step': f'Add and subtract [left to right]: {expression} = {result}',
#             'simplification': result
#         }
#         Steps.update({stepCounter: stepDictValue})
#         return evaluateArithmetic(result, stepCounter, Steps, returnStepsAsArray)
#
#     """ CHECK FOR PARENTHESES """
#     if ('(' in expression and ')' in expression) or expression.isSingleExpression():
#
#         for i in range(len(expression)):
#             currentExpressionToEvaluate = ''
#             if expression[i] == '(' and i == expression.getIndexOfInnerMostParen():
#                 for j in range(i + 1, len(expression)):
#                     if expression[j] != ')':
#                         currentExpressionToEvaluate += expression[j]
#                     else:
#                         break
#
#                 currentExpressionToEvaluate = ArithmeticExpression(currentExpressionToEvaluate)
#                 Simplification = evaluateArithmetic(currentExpressionToEvaluate, returnStepsAsArray=True)
#                 result = Simplification[1]
#                 stepsAsArray = Simplification[0]
#
#                 for stepToAdd in stepsAsArray:
#                     stepDictValue = {
#                         'step': wrapStepInParen(f"{stepToAdd['step']}"),
#                         'simplification': expression.replace(f'({currentExpressionToEvaluate})',
#                                                              f"({stepToAdd['simplification']})")
#                     }
#                     stepCounter += 1
#                     Steps.update({stepCounter: stepDictValue})
#
#                 simplifiedExpression = expression.replace(f'({currentExpressionToEvaluate})', result)
#                 expression = simplifiedExpression
#
#                 return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)
#
#     for i in range(len(expression)):
#
#         if expression[i] in allOperators:
#             operator = expression[i]
#             operationMessage = getOperationMessage(operator)
#             Terms = expression.splitExpression(i, operator, operation=operation)
#             firstTerm, secondTerm = Terms[0], Terms[1]
#
#             if firstTerm != '' and secondTerm != '':
#                 # firstTerm = f"{float(firstTerm):.20f}"
#                 # secondTerm = f"{float(secondTerm):.20f}"
#
#                 # result = castToFloatOrInt(f"{float(eval(f'{firstTerm} {operator} {secondTerm}')):.10f}", True)
#                 result = castToFloatOrInt(eval(f"float(firstTerm) {operator} float(secondTerm)"), True)
#                 simplifiedExpression = expression.replace(f'{firstTerm}{operator}{secondTerm}', result)
#                 expression = simplifiedExpression
#
#                 stepDictValue = {
#                     'step': f'{operationMessage} the first and second term: {firstTerm}{operator}{secondTerm} = {result}',
#                     'simplification': f'{simplifiedExpression}'
#                 }
#                 stepCounter += 1
#                 Steps.update({stepCounter: stepDictValue})
#
#                 return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)
#
# def getOperationMessage(operator):
#     if operator == '+':
#         return 'Add'
#     elif operator == '-':
#         return 'Subtract'
#     elif operator == '*':
#         return 'Multiply'
#     elif operator == '/':
#         return 'divide'
#
# def castToFloatOrInt(num, castToString=False):
#     if not isDigit(str(num)):
#         raise ValueError(f"{num} is not a digit")
#     else:
#         if isFloat(num):
#             if castToString:
#                 return str(round(float(num), 5))
#             else:
#                 return float(num)
#         if isInt(num):
#             if castToString:
#                 return str(int(num))
#             else:
#                 return int(num)
#
# def isInt(floatNum):
#     return floor(floatNum) - floatNum == 0
#
# def isFloat(floatNum):
#     return floor(floatNum) - floatNum != 0
#
# def addAndSubtractTerms(expression):
#     if isSingleExpression(expression):
#         return expression
#     for i in range(len(expression)):
#         if expression[i] == '+':
#             Terms = splitAdditionOrSubtraction(expression, i)
#             firstTerm, secondTerm = Terms[0], Terms[1]
#             result = castToFloatOrInt(float(firstTerm) + float(secondTerm), True)
#             simplifiedExpression = expression.replace(f'{firstTerm}+{secondTerm}', result)
#             expression = simplifiedExpression
#             return addAndSubtractTerms(expression)
#         elif expression[i] == '-':
#             Terms = splitAdditionOrSubtraction(expression, i)
#             firstTerm, secondTerm = Terms[0], Terms[1]
#             result = castToFloatOrInt(float(firstTerm) - float(secondTerm), True)
#             simplifiedExpression = expression.replace(f'{firstTerm}-{secondTerm}', result)
#             expression = simplifiedExpression
#             return addAndSubtractTerms(expression)
#
# def performOperation(expression, operation=None):
#     if isSingleExpression(expression):
#         return expression
#     expression = expression.replace('(', '').replace(')', '')
#     allOperators = ['+','-','*','/']
#     for i in range(len(expression)):
#         if expression[i] in allOperators:
#             operator = expression[i]
#             Terms = splitExpression(expression, i, operator, operation=operation)
#             if Terms[0] and Terms[1] != '':
#                 firstTerm, secondTerm = Terms[0], Terms[1]
#                 result = castToFloatOrInt(eval(f'float(firstTerm) {operator} float(secondTerm)'), True)
#                 simplifiedExpression = expression.replace(f'{firstTerm}{operator}{secondTerm}', result)
#                 expression = simplifiedExpression
#
#                 return performOperation(expression, operation)
#
# def splitAdditionOrSubtraction(expression, index):
#     for i in range(len(expression)):
#         if i == index:
#             firstTerm, secondTerm = '', ''
#             # GET FIRST TERM
#             j = 0
#             while True:
#                 if expression[j] == '+' or expression[j] == '-':
#                     break
#                 firstTerm += expression[j]
#                 j+= 1
#             # GET SECOND TERM
#             j = i+1
#             while True:
#                 if j == len(expression):
#                     break
#                 if expression[j] == '+' or expression[j] == '-':
#                     break
#                 secondTerm += expression[j]
#                 j += 1
#
#             return (firstTerm, secondTerm)
#
# def splitExpression(expression, index, operator, binarySplit=True, operation=None):
#     """
#     A BINARY SPLIT OF THE expression 2+43*21-5 ON THE OPERATOR '*' AT INDEX 4 RETURNS ('43', '21')
#     A NON-BINARY SPLIT OF THE expression 2+43*21-5 ON THE OPERATOR '*' AT INDEX 4 RETURNS ('2+43', '21-5')
#     """
#     if not binarySplit:
#         for i in range(len(expression)):
#             if i == index:
#                 firstTerm, secondTerm = '', ''
#                 """ GET FIRST TERM """
#                 j = 0
#                 while True:
#                     if expression[j] == operator:
#                         break
#                     firstTerm += expression[j]
#                     j+= 1
#                 """ GET SECOND TERM """
#                 j = i+1
#                 while True:
#                     if j == len(expression):
#                         break
#                     if expression[j] == operator:
#                         break
#                     secondTerm += expression[j]
#                     j += 1
#
#                 return (firstTerm, secondTerm)
#     else:
#         otherOperators = getRestrictedOperators('-')
#         allOperators = ['+','-','*','/']
#         for i in range(len(expression)):
#             if i == index:
#                 firstTerm, secondTerm = '', ''
#                 """ GET FIRST TERM """
#                 j = i-1
#                 while expression[j] not in otherOperators and j >=0:
#                     firstTerm += expression[j]
#                     if expression[j] == '-':
#                         break
#                     j -=1
#                 firstTerm = reverse(firstTerm)
#                 """ GET SECOND TERM """
#                 j = i + 1
#                 while ((expression[j] not in allOperators) or (operation == 'multiply-only')) and expression[j] != operator:
#                     secondTerm += expression[j]
#                     j += 1
#                     operation = None
#                     if j == len(expression):
#                         break
#
#                 return (firstTerm, secondTerm)
# def getRestrictedOperators(restrictedOperator):
#     """ RETURNS ALL OPERATORS EXCEPT THE ONE PASS AS PARAMETER """
#     allOperators = {'+', '-', '*', '/'}
#     return allOperators.symmetric_difference(restrictedOperator)
#
# def reverse(iterable):
#     return iterable[::-1]
#
# def getNextOperator(expression, index):
#     """ RETURNS THE NEXT OPERATOR AFTER AN EXPRESSION AT A GIVEN INDEX """
#     isNegativeNumber = False
#     if expression[index+1] == '-':
#         isNegativeNumber = True
#
#     allOperators = ['+', '-', '*', '/']
#     i = index+1
#     if isNegativeNumber:
#         i += 1
#     while i < len(expression):
#         if expression[i] in allOperators:
#             return expression[i]
#         i += 1
#

#
# def wrapStepInParen(stepExpression):
#     """ WRAPS A STEP EXPRESSION IN PARENTHESES: Add and subtract [left to right]: 1+2+3+4 = 10 = Add ... : (1+2+3+4) = (10) """
#     cpyStepExpression = stepExpression    # GET THE stepExpression BEFORE .split()
#     if ':' in stepExpression:
#         stepExpression = stepExpression.split(':')
#         stepWords = stepExpression[0]
#         expressionToWrap = stepExpression[1].lstrip()
#
#         if alreadyWrapped(expressionToWrap):
#             return cpyStepExpression
#
#         newExpression = '('
#         checkForEqual = True
#         wrapExpressionAfterEqualSign = False
#         for i in range(len(expressionToWrap)):
#             if checkForEqual:
#                 if expressionToWrap[i + 1] == '=':
#                     newExpression += ')'
#                     checkForEqual = False
#                     wrapExpressionAfterEqualSign = True
#             if wrapExpressionAfterEqualSign:
#                 if newExpression[i] == '=':
#                     newExpression += '('
#             newExpression += expressionToWrap[i]
#         newExpression += ')'
#
#         return f"{stepWords}: {newExpression}"
#     else:
#         return stepExpression
#
# def wrapExponentInParen(expression: str):
#     if '^' in expression:
#         allOperations = ['+','-','*','/','^']
#         indexOfExponent = indexOf(expression, '^')
#         """ GET THE BASE """
#         if expression[indexOfExponent - 1] != ')':
#             # BASE IS SINGLE EXPRESSION
#             i = indexOfExponent-1
#             """ GET THE NUMBER BEFORE '^' """
#             base = ''
#             while i >= 0 and expression[i] not in allOperations:
#                 base += expression[i]
#                 i -= 1
#             base = reverse(base)
#         else:
#             # BASE IS NOT SINGLE EXPRESSION
#             base = ''
#             expressionToTheLeftOfExponent = ArithmeticExpression(expression[:indexOfExponent])
#             indexWhereExponentEnds = expressionToTheLeftOfExponent.getIndexOfInnerMostParen()
#             for i in range(indexWhereExponentEnds, indexOfExponent):
#                 base += expression[i]
#
#         exponentIsSingleExpression = False
#         # GET THE EXPONENT
#         if expression[indexOfExponent + 1] != '{':
#             exponentIsSingleExpression = True
#             exponent = ''
#             i = indexOfExponent+1
#             if i == len(expression)-1:
#                 exponent = expression[indexOfExponent + 1]
#             else:
#                 """ GET THE ENTER NUM AFTER '^' """
#                 while i < len(expression) and expression[i] not in allOperations:
#                     exponent += expression[i]
#                     i += 1
#         else:
#             # EXPONENT IS NOT A SINGLE EXPRESSION
#             exponent = ''
#             i = indexOfExponent+2
#             while expression[i] != '}':
#                 exponent += expression[i]
#                 i += 1
#
#         if exponentIsSingleExpression:
#             expression = expression.replace(f"{base}^{exponent}", f"({base}^{exponent})")
#         else:
#             expression = expression.replace(f"{base}^{'{'}{exponent}{'}'}", f"({base}^{'{'}{exponent}{'}'})")
#
#
#         return expression
#
# def wrapRadicalInParen(expression: str):
#     wrappedExpression = ''
#     addedClosingParen = False
#     for i in range(len(expression)):
#         if expression[i:i+4] == 'sqrt':
#             wrappedExpression += '('
#         if i > 0 and expression[i-1] == '}':
#             wrappedExpression += ')'
#             addedClosingParen = True
#         wrappedExpression += expression[i]
#
#     if not addedClosingParen:
#         wrappedExpression += ')'
#
#     return wrappedExpression
#
# def alreadyWrapped(expression):
#     wrappedParentheses = 0
#     if expression[0] == '(':
#         wrappedParentheses += 1
#     if expression[-1] == ')':
#         wrappedParentheses += 1
#     for i in range(len(expression)):
#         if expression[i] == '=':
#             if expression[i-2] == ')':
#                 wrappedParentheses += 1
#             if expression[i+2] == '(':
#                 wrappedParentheses += 1
#             break
#     return wrappedParentheses == 4
#
# def isSingleExpression(expression):
#     allPossibleOperations = ['+', '-', '*', '/', '^']
#     allOperationsInExpression = set()
#     for operation in allPossibleOperations:
#         if operation in expression:
#             allOperationsInExpression.add(operation)
#     if len(allOperationsInExpression) == 0:
#         return True
#     elif len(allOperationsInExpression) == 1:
#         operation = list(allOperationsInExpression)[0]
#         numOperation = getNumOperation(expression, operation)
#         if numOperation > 1:
#             return False
#         else:
#             checkExpression = expression.split(operation)
#             if checkExpression[0] != '':
#                 return False
#     else:
#         return False
#     return True
#
# def getNumOperation(expression, operation):
#     result = 0
#     for term in expression:
#         if term == operation:
#             result += 1
#
#     return result


# def convertToStandardForm(num: str, autoConvert=False):
#     try:
#         float(num)
#     except:
#         raise ValueError(f'{num} is not a valid number')
#
#     doConversion = True
#     if autoConvert:
#         if float(num) <= MAX_SIZE_OF_NUM_BEFORE_CONVERTED_TO_STANDARD_FORM:
#             doConversion = False
#
#
#     if doConversion:
#         if float(num) > 1:
#             standardForm = ''
#             decimalPlacesMoves = len(num)-1
#             for i in range(len(num)):
#                 if i == 1:
#                     standardForm += '.'
#                 if num[i] == '0':
#                     """ REMOVE TRAILING ZEROES IF ANY """
#                     charsToCheck = num[i:]
#                     for j in range(len(charsToCheck)):
#                         if charsToCheck[j] != '0':
#                             standardForm += charsToCheck
#                             break
#                     break
#                 standardForm += num[i]
#
#             roundedStandardForm = str(round(float(standardForm), 5))
#
#             if len(standardForm) != len(roundedStandardForm):
#                 roundedStandardForm += '...'
#
#             roundedStandardForm += f'e+{decimalPlacesMoves}'
#
#             return roundedStandardForm
#         else:
#             i = 2 # START i AT THE FIRST ZERO AFTER THE DECIMAL POINT
#             decimalPlacesMoves = 1
#             indexOfFirstNoneZeroDigit = None
#             while i < len(num):
#                 if num[i] != '0':
#                     indexOfFirstNoneZeroDigit = i
#                     break
#                 i += 1
#                 decimalPlacesMoves += 1
#
#             standardForm = ''
#             charsToCheck = num[indexOfFirstNoneZeroDigit:]
#             for i in range(len(charsToCheck)):
#                 if i == 1:
#                     standardForm += '.'
#                 standardForm += charsToCheck[i]
#
#             standardForm += f'e-{decimalPlacesMoves}'
#             return standardForm
#     else:
#         return num
# def isDigit(numString: str):
#     allOperations = ['+', '*', '/', '^']
#     operationInExpression = False
#     for operation in allOperations:
#         if operation in numString:
#             operationInExpression = True
#     if operationInExpression:
#         for i in range(len(numString)):
#             if numString[i] in allOperations:
#                 operator = numString[i]
#                 if operator == '^':
#                     if '{' in numString:
#                         pass
#                     else:
#                         exponentResult = splitExpression(numString, i, operator)
#                         base = exponentResult[0]
#                         exponent = exponentResult[1]
#                         baseIsDigit = isDigit(base)
#                         exponentIsDigit = isDigit(exponent)
#
#                         if baseIsDigit and exponentIsDigit:
#                             return True
#     else:
#         try:
#             numString = float(numString)
#         except ValueError:
#             return False
#         return True

""" TESTING """


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


class Expression:
    def __init__(self, expression):
        self.expression = expression
        self.__Terms = []

    def getTerms(self):
        if self.__Terms != []:
            return self.__Terms
        isCompleteTerm = True
        numOpenCurlyParen, numClosedCurlyParen, numOpenParen, numClosedParen = 0, 0, 0, 0
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
            elif self.expression[i] == '}':
                numClosedCurlyParen += 1
            elif self.expression[i] == ')':
                numClosedParen += 1
            # CHECK FOR COMPLETED TERM
            if not isCompleteTerm:
                if (numOpenCurlyParen == numClosedCurlyParen) and (numOpenParen == numClosedParen):
                    isCompleteTerm = True
                    numOpenCurlyParen, numClosedCurlyParen, numOpenParen, numClosedParen = 0, 0, 0, 0
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

    @staticmethod
    def castTerms(Terms):
        for i in range(len(Terms)):
            if 'frac' in Terms[i][0:5]:
                Terms[i] = Fraction(Terms[i])
            elif 'sqrt' in Terms[i][0:5]:
                Terms[i] = Radical(Terms[i])
            elif '^' in Terms[i]:
                base = Terms[i].split('^')[0]
                exponent = Terms[i].split('^')[1]
                if parenIsBalanced(base) and parenIsBalanced(exponent):
                    Terms[i] = Exponential(Terms[i])
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
        return len(self.expression)

    def __contains__(self, item):
        """ 'in' OPERATOR """
        return item in self.expression

    def __getitem__(self, index):
        """ [] OPERATOR """
        return self.expression[index]


def simplifyExpression(expression: Expression, Steps=None):
    if Steps == None:
        Steps = []

    groupedExpressions = expression.getGroupedExpressions()
    groupedTerms = expression.getGroupedTerms()
    isSingleGroup = False
    finalResult = ''

    # print(groupedExpressions['str'])

    """ GROUP TERMS """
    if len(groupedExpressions['list']) == 1:
        isSingleGroup = True

    if not isSingleGroup and str(expression) != groupedExpressions['strWithoutParen']:
        mainStep = createMainStep(r"\text{Group Terms}",rf"\displaystyle {latexify(expression)}={latexify(groupedExpressions['strWithoutParen'])}")
        Steps.append(mainStep)

    """ SIMPLIFY GROUPS """
    for group in groupedTerms:
        if groupedTerms[group] != []:
            if group == 'Exponents':
                ...
            elif group == 'Radicals':
                """ SIMPLIFY RADICALS """
                Radicals = groupedTerms['Radicals']
                for radical in Radicals:
                    radicand = Expression(str(radical.getExpressionInsideRadical()))
                    solutionToRadicand = simplifyExpression(radicand)
                    # CREATE E-STEP
                    # steps = solutionToRadicand['steps'][0]['e-steps']
                    steps = []
                    for step in solutionToRadicand['steps']:
                        if step['type'] == 'main-step':
                            steps.append(step)
                        elif step['type'] == 'e-step':
                            for e_step in step['e-steps']:
                                steps.append(e_step)

                    simplification = f"sqrt{'{'}{parseLatex(solutionToRadicand['finalResult'])}{'}'}"
                    heading = latexify(f"{radical}={simplification}")
                    if heading[0] == '+' or heading[0] == '-': heading = heading[1:]
                    finalStep = createMainStep(r'\text{Simplify}', heading)
                    steps.append(finalStep)
                    # ADD E-STEP
                    e_step = createExpandableStep(heading, steps)
                    Steps.append(e_step)
                    # UPDATE FINAL RESULT
                    sign = radical[0]
                    if (sign != '+' and sign != '-'): sign = '+'
                    finalResult += f'{sign}{simplification}'

            elif group == 'Fractions':
                ...
            elif group == 'Constants':
                """ SIMPLIFY CONSTANTS """
                Constants = groupedTerms['Constants']
                constantsExpression = createEStepHeadingFromGroup(Constants, False)
                Solution = simplifyConstants(constantsExpression, Constants)
                steps = Solution['Steps']
                simplification = Solution['finalExpression']
                # CREATE E-STEP
                addParen = True if not isSingleGroup else False
                heading = createEStepHeadingFromGroup(Constants, False)
                e_step = createExpandableStep(latexify(f"{heading}={simplification}"), steps)
                Steps.append(e_step)
                # UPDATE finalResult
                sign = ''
                if simplification[0] != '-' and simplification[0] != '': sign = '+'
                finalResult += f"{sign}{simplification}"

    if finalResult[0] == '+': finalResult = finalResult[1:]

    return {'steps': Steps, 'finalResult': latexify(finalResult)}

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
    """ GET ALL THE DISTINCT VARIABLES """
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

    for var in variableCoefficients:
        finalCoefficient = addNumbers(variableCoefficients[var])
        variableCoefficients[var] = finalCoefficient

    simplifiedExpression = ''
    for var in variableCoefficients:
        coefficient = variableCoefficients[var]
        if str(coefficient)[0] != '+':
            simplifiedExpression += '+'
        if coefficient == 1: coefficient = ''
        if coefficient != 0:
            simplifiedExpression += f'{coefficient}{var}'

    simplifiedExpression = simplifiedExpression.replace('++', '+').replace('--', '+').replace('+-', '-')
    if simplifiedExpression[-1] == '+': simplifiedExpression = simplifiedExpression[:-1]

    return simplifiedExpression

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




def indexOf(iterable, searchFor):
    for i, item in enumerate(iterable):
        if item == searchFor:
            return i
    return None


def main():
    # E = Expression('5+4+sqrt{1+2+sqrt{5a-a}}')
    # E = Expression('sqrt{1+2+a+a+3}')
    E = Expression('1+2+sqrt{25x+15x+sqrt{12x-6x+3}-13+5}+3')
    print(simplifyExpression(E))





if __name__ == '__main__':
    main()
