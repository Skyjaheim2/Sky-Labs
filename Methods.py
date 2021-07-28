from math import floor, pi, e


class ArithmeticExpression:
    def __init__(self, expression):
        self.expression = expression

    """ INSTANCE METHODS """

    def getOperationToPerform(self):
        allOperations = self.getAllOperations()

        if len(allOperations) == 0 and self.isSingleExpression():
            return 'no-operation'

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



def parseLatex(latexString: str):
    latexString = latexString.replace('\left(', '(').replace('\\right)', ')').replace('\cdot', '*').replace('\\pi', f'{pi}')\
                             .replace('e', f'{e}')
    return latexString

def latexify(expression):
    expression = expression.replace('(', '\left(').replace(')', '\\right)').replace('*', '\cdot').replace(f'{pi}', '\pi')\
                           .replace(f'{e}', 'e')
    return expression


MAX_SIZE_OF_NUM_BEFORE_CONVERTED_TO_STANDARD_FORM = 10**20

def evaluateArithmetic(expression, stepCounter=None, Steps=None, returnStepsAsArray=False):
    if type(expression) != ArithmeticExpression:
        expression = ArithmeticExpression(expression)
    if Steps is None:
        Steps = {}
    if stepCounter is None:
        stepCounter = 0
    if expression.isSingleExpression():

        if expression >= MAX_SIZE_OF_NUM_BEFORE_CONVERTED_TO_STANDARD_FORM:
            expression = convertToStandardForm(str(expression))
        if returnStepsAsArray:
            stepsAsArray = []
            for step in Steps:
                stepsAsArray.append(Steps[step])
            return (stepsAsArray, str(expression), stepCounter)
        return (Steps, str(expression), stepCounter)

    allOperators = ['+','-','*','/']
    operation = expression.getOperationToPerform()

    # expression = expression.convertOutOfStandardForm()

    if '++' in expression:
        simplifiedExpression = expression.replace('++', '+')
        expression = simplifiedExpression

        stepDictValue = {
            'step': f'Apply rule: a++b = a+b',
            'simplification': f'{simplifiedExpression}'
        }
        stepCounter += 1
        Steps.update({stepCounter: stepDictValue})

        return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)

    if '+-' in expression:
        simplifiedExpression = expression.replace('+-', '-')
        expression = simplifiedExpression

        stepDictValue = {
            'step': f'Apply rule: a+-b = a-b',
            'simplification': f'{simplifiedExpression}'
        }
        stepCounter += 1
        Steps.update({stepCounter: stepDictValue})

        return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)

    if '--' in expression:
        simplifiedExpression = expression.replace('--', '+')
        expression = simplifiedExpression

        stepDictValue = {
            'step': f'Apply rule: a--b = a+b',
            'simplification': f'{simplifiedExpression}'
        }
        stepCounter += 1
        Steps.update({stepCounter: stepDictValue})

        return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)



    """ CHECK OPERATIONS """
    if operation == 'general-arithmetic' and '(' not in expression:
        expressionWithOrder = expression.applyPEMDAS()

        stepDictValue = {
            'step': f'Apply PEMDAS: {expression} = {expressionWithOrder}',
            'simplification': f'{expressionWithOrder}'
        }
        expression = ArithmeticExpression(expressionWithOrder)
        stepCounter += 1
        Steps.update({stepCounter: stepDictValue})

    elif operation == 'arithmetic-exponent-multiply':
        allExponentsInExpression = expression.getAllExponentsInExpression()
        baseToUse = Exponential(allExponentsInExpression[0]).base

        exponents = []
        for expression in allExponentsInExpression:
            expression = Exponential(expression)
            if expression.exponent.isSingleExpression():
                exponents.append(f"{expression.exponent}")
            else:
                exponents.append(f"({expression.exponent})")

        operation = '+'
        newExponent = operation.join(exponents)

        simplifiedExpression = ArithmeticExpression(f"{baseToUse}^{'{'}{newExponent}{'}'}")

        stepCounter += 1
        stepDictValue = {
            'step': f"Apply rule exponent: a^b * a^c = a^{'{'}b+c{'}'}",
            'simplification': f"{simplifiedExpression}"
        }

        Steps.update({stepCounter: stepDictValue})
        return evaluateArithmetic(simplifiedExpression, stepCounter, Steps, returnStepsAsArray)




    elif operation == 'arithmetic-exponent-single':
        exponentIndex = indexOf(str(expression), '^')
        exponentData = expression.splitExpression(exponentIndex, '^', binarySplit=False)

        base = ArithmeticExpression(exponentData[0])
        exponent = ArithmeticExpression(exponentData[1])

        if base == 1:
            result = '1'
            stepCounter += 1
            stepDictValue = {
                'step': f'Apply rule exponent: 1^a = 1',
                'simplification': f"{result}"
            }
            Steps.update({stepCounter: stepDictValue})
            return evaluateArithmetic(ArithmeticExpression(result), stepCounter, Steps, returnStepsAsArray)


        if '{' in exponent:
            expressionInExponent = ArithmeticExpression(exponent.replace('{', '').replace('}', ''))
            if expressionInExponent.isSingleExpression():
                expressionInExponent = expressionInExponent.replace('{', '').replace('}', '')
                if base.isSingleExpression():
                    result = castToFloatOrInt(eval(f"{base}**{expressionInExponent}"), True)
                    SF = convertToStandardForm
                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Calculate exponent: {expression} = {SF(result, True)}',
                        'simplification': f"{SF(result, True)}"
                    }
                    Steps.update({stepCounter: stepDictValue})
                    return evaluateArithmetic(ArithmeticExpression(result), stepCounter, Steps, returnStepsAsArray)
            else:
                Simplification = evaluateArithmetic(expressionInExponent, returnStepsAsArray=True)
                result = Simplification[1]
                stepsAsArray = Simplification[0]

                for stepToAdd in stepsAsArray:
                    stepDictValue = {
                        'step': f"{stepToAdd['step']}",
                        'simplification': expression.replace(f'{expressionInExponent}', f"{stepToAdd['simplification']}")
                    }
                    stepCounter += 1
                    Steps.update({stepCounter: stepDictValue})

                simplifiedExpression = expression.replace(f'{expressionInExponent}', result)
                expression = simplifiedExpression

                return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)

        else:
            if base.isSingleExpression():
                result = castToFloatOrInt(eval(f"{base}**{exponent}"), True)
                SF = convertToStandardForm

                stepCounter += 1
                stepDictValue = {
                    'step': f'Calculate exponent: {expression} = {SF(result, True)}',
                    'simplification': f"{SF(result, True)}"
                }
                Steps.update({stepCounter: stepDictValue})
                return evaluateArithmetic(ArithmeticExpression(result), stepCounter, Steps, returnStepsAsArray)

    elif operation == 'multiply-only':
        result = performOperation(expression, operation='multiply-only')
        stepCounter += 1
        stepDictValue = {
            'step': f'Multiply [left to right]: {expression} = {result}',
            'simplification': result
        }
        Steps.update({stepCounter: stepDictValue})
        return evaluateArithmetic(result, stepCounter, Steps, returnStepsAsArray)

    elif operation == 'add-subtract-only' and '(' not in expression:
        result = performOperation(expression)
        stepCounter += 1
        stepDictValue = {
            'step': f'Add and subtract [left to right]: {expression} = {result}',
            'simplification': result
        }
        Steps.update({stepCounter: stepDictValue})
        return evaluateArithmetic(result, stepCounter, Steps, returnStepsAsArray)

    """ CHECK FOR PARENTHESES """
    if ('(' in expression and ')' in expression) or expression.isSingleExpression():

        for i in range(len(expression)):
            currentExpressionToEvaluate = ''
            if expression[i] == '(' and i == expression.getIndexOfInnerMostParen():
                for j in range(i + 1, len(expression)):
                    if expression[j] != ')':
                        currentExpressionToEvaluate += expression[j]
                    else:
                        break

                currentExpressionToEvaluate = ArithmeticExpression(currentExpressionToEvaluate)
                Simplification = evaluateArithmetic(currentExpressionToEvaluate, returnStepsAsArray=True)
                result = Simplification[1]
                stepsAsArray = Simplification[0]

                for stepToAdd in stepsAsArray:
                    stepDictValue = {
                        'step': wrapStepInParen(f"{stepToAdd['step']}"),
                        'simplification': expression.replace(f'({currentExpressionToEvaluate})',
                                                             f"({stepToAdd['simplification']})")
                    }
                    stepCounter += 1
                    Steps.update({stepCounter: stepDictValue})

                simplifiedExpression = expression.replace(f'({currentExpressionToEvaluate})', result)
                expression = simplifiedExpression

                return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)

    for i in range(len(expression)):

        if expression[i] in allOperators:
            operator = expression[i]
            operationMessage = getOperationMessage(operator)
            Terms = expression.splitExpression(i, operator, operation=operation)
            firstTerm, secondTerm = Terms[0], Terms[1]

            if firstTerm != '' and secondTerm != '':
                # firstTerm = f"{float(firstTerm):.20f}"
                # secondTerm = f"{float(secondTerm):.20f}"

                # result = castToFloatOrInt(f"{float(eval(f'{firstTerm} {operator} {secondTerm}')):.10f}", True)
                result = castToFloatOrInt(eval(f"float(firstTerm) {operator} float(secondTerm)"), True)
                simplifiedExpression = expression.replace(f'{firstTerm}{operator}{secondTerm}', result)
                expression = simplifiedExpression

                stepDictValue = {
                    'step': f'{operationMessage} the first and second term: {firstTerm}{operator}{secondTerm} = {result}',
                    'simplification': f'{simplifiedExpression}'
                }
                stepCounter += 1
                Steps.update({stepCounter: stepDictValue})

                return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)




def getOperationMessage(operator):
    if operator == '+':
        return 'Add'
    elif operator == '-':
        return 'Subtract'
    elif operator == '*':
        return 'Multiply'
    elif operator == '/':
        return 'divide'

def castToFloatOrInt(num, castToString=False):
    if not isDigit(str(num)):
        raise ValueError(f"{num} is not a digit")
    else:
        if isFloat(num):
            if castToString:
                return str(round(float(num), 5))
            else:
                return float(num)
        if isInt(num):
            if castToString:
                return str(int(num))
            else:
                return int(num)

def isInt(floatNum):
    return floor(floatNum) - floatNum == 0

def isFloat(floatNum):
    return floor(floatNum) - floatNum != 0

def addAndSubtractTerms(expression):
    if isSingleExpression(expression):
        return expression
    for i in range(len(expression)):
        if expression[i] == '+':
            Terms = splitAdditionOrSubtraction(expression, i)
            firstTerm, secondTerm = Terms[0], Terms[1]
            result = castToFloatOrInt(float(firstTerm) + float(secondTerm), True)
            simplifiedExpression = expression.replace(f'{firstTerm}+{secondTerm}', result)
            expression = simplifiedExpression
            return addAndSubtractTerms(expression)
        elif expression[i] == '-':
            Terms = splitAdditionOrSubtraction(expression, i)
            firstTerm, secondTerm = Terms[0], Terms[1]
            result = castToFloatOrInt(float(firstTerm) - float(secondTerm), True)
            simplifiedExpression = expression.replace(f'{firstTerm}-{secondTerm}', result)
            expression = simplifiedExpression
            return addAndSubtractTerms(expression)

def performOperation(expression, operation=None):
    if isSingleExpression(expression):
        return expression

    allOperators = ['+','-','*','/']
    for i in range(len(expression)):
        if expression[i] in allOperators:
            operator = expression[i]
            Terms = splitExpression(expression, i, operator, operation=operation)
            if Terms[0] and Terms[1] != '':
                firstTerm, secondTerm = Terms[0], Terms[1]
                result = castToFloatOrInt(eval(f'float(firstTerm) {operator} float(secondTerm)'), True)
                simplifiedExpression = expression.replace(f'{firstTerm}{operator}{secondTerm}', result)
                expression = simplifiedExpression

                return performOperation(expression, operation)

def splitAdditionOrSubtraction(expression, index):
    for i in range(len(expression)):
        if i == index:
            firstTerm, secondTerm = '', ''
            # GET FIRST TERM
            j = 0
            while True:
                if expression[j] == '+' or expression[j] == '-':
                    break
                firstTerm += expression[j]
                j+= 1
            # GET SECOND TERM
            j = i+1
            while True:
                if j == len(expression):
                    break
                if expression[j] == '+' or expression[j] == '-':
                    break
                secondTerm += expression[j]
                j += 1

            return (firstTerm, secondTerm)

def splitExpression(expression, index, operator, binarySplit=True, operation=None):
    """
    A BINARY SPLIT OF THE expression 2+43*21-5 ON THE OPERATOR '*' AT INDEX 4 RETURNS ('43', '21')
    A NON-BINARY SPLIT OF THE expression 2+43*21-5 ON THE OPERATOR '*' AT INDEX 4 RETURNS ('2+43', '21-5')
    """
    if not binarySplit:
        for i in range(len(expression)):
            if i == index:
                firstTerm, secondTerm = '', ''
                """ GET FIRST TERM """
                j = 0
                while True:
                    if expression[j] == operator:
                        break
                    firstTerm += expression[j]
                    j+= 1
                """ GET SECOND TERM """
                j = i+1
                while True:
                    if j == len(expression):
                        break
                    if expression[j] == operator:
                        break
                    secondTerm += expression[j]
                    j += 1

                return (firstTerm, secondTerm)
    else:
        otherOperators = getRestrictedOperators('-')
        allOperators = ['+','-','*','/']
        for i in range(len(expression)):
            if i == index:
                firstTerm, secondTerm = '', ''
                """ GET FIRST TERM """
                j = i-1
                while expression[j] not in otherOperators and j >=0:
                    firstTerm += expression[j]
                    if expression[j] == '-':
                        break
                    j -=1
                firstTerm = reverse(firstTerm)
                """ GET SECOND TERM """
                j = i + 1
                while ((expression[j] not in allOperators) or (operation == 'multiply-only')) and expression[j] != operator:
                    secondTerm += expression[j]
                    j += 1
                    operation = None
                    if j == len(expression):
                        break

                return (firstTerm, secondTerm)

def getRestrictedOperators(restrictedOperator):
    """ RETURNS ALL OPERATORS EXCEPT THE ONE PASS AS PARAMETER """
    allOperators = {'+', '-', '*', '/'}
    return allOperators.symmetric_difference(restrictedOperator)

def reverse(iterable):
    return iterable[::-1]

def getNextOperator(expression, index):
    """ RETURNS THE NEXT OPERATOR AFTER AN EXPRESSION AT A GIVEN INDEX """
    isNegativeNumber = False
    if expression[index+1] == '-':
        isNegativeNumber = True

    allOperators = ['+', '-', '*', '/']
    i = index+1
    if isNegativeNumber:
        i += 1
    while i < len(expression):
        if expression[i] in allOperators:
            return expression[i]
        i += 1

def isDigit(numString: str):
    allOperations = ['+','*','/','^']
    operationInExpression = False
    for operation in allOperations:
        if operation in numString:
            operationInExpression = True
    if operationInExpression:
        for i in range(len(numString)):
            if numString[i] in allOperations:
                operator = numString[i]
                if operator == '^':
                    if '{' in numString:
                        pass
                    else:
                        exponentResult = splitExpression(numString, i, operator)
                        base = exponentResult[0]
                        exponent = exponentResult[1]
                        baseIsDigit = isDigit(base)
                        exponentIsDigit = isDigit(exponent)

                        if baseIsDigit and exponentIsDigit:
                            return True
    else:
        try:
            numString = float(numString)
        except ValueError:
            return False
        return True

def wrapStepInParen(stepExpression):
    """ WRAPS A STEP EXPRESSION IN PARENTHESES: Add and subtract [left to right]: 1+2+3+4 = 10 = Add ... : (1+2+3+4) = (10) """
    cpyStepExpression = stepExpression    # GET THE stepExpression BEFORE .split()
    if ':' in stepExpression:
        stepExpression = stepExpression.split(':')
        stepWords = stepExpression[0]
        expressionToWrap = stepExpression[1].lstrip()

        if alreadyWrapped(expressionToWrap):
            return cpyStepExpression

        newExpression = '('
        checkForEqual = True
        wrapExpressionAfterEqualSign = False
        for i in range(len(expressionToWrap)):
            if checkForEqual:
                if expressionToWrap[i + 1] == '=':
                    newExpression += ')'
                    checkForEqual = False
                    wrapExpressionAfterEqualSign = True
            if wrapExpressionAfterEqualSign:
                if newExpression[i] == '=':
                    newExpression += '('
            newExpression += expressionToWrap[i]
        newExpression += ')'

        return f"{stepWords}: {newExpression}"
    else:
        return stepExpression

def wrapExponentInParen(expression: str):
    if '^' in expression:
        allOperations = ['+','-','*','/','^']
        indexOfExponent = indexOf(expression, '^')
        """ GET THE BASE """
        if expression[indexOfExponent - 1] != ')':
            # BASE IS SINGLE EXPRESSION
            i = indexOfExponent-1
            """ GET THE NUMBER BEFORE '^' """
            base = ''
            while i >= 0 and expression[i] not in allOperations:
                base += expression[i]
                i -= 1
            base = reverse(base)
        else:
            # BASE IS NOT SINGLE EXPRESSION
            base = ''
            expressionToTheLeftOfExponent = ArithmeticExpression(expression[:indexOfExponent])
            indexWhereExponentEnds = expressionToTheLeftOfExponent.getIndexOfInnerMostParen()
            for i in range(indexWhereExponentEnds, indexOfExponent):
                base += expression[i]

        exponentIsSingleExpression = False
        # GET THE EXPONENT
        if expression[indexOfExponent + 1] != '{':
            exponentIsSingleExpression = True
            exponent = ''
            i = indexOfExponent+1
            if i == len(expression)-1:
                exponent = expression[indexOfExponent + 1]
            else:
                """ GET THE ENTER NUM AFTER '^' """
                while i < len(expression) and expression[i] not in allOperations:
                    exponent += expression[i]
                    i += 1
        else:
            # EXPONENT IS NOT A SINGLE EXPRESSION
            exponent = ''
            i = indexOfExponent+2
            while expression[i] != '}':
                exponent += expression[i]
                i += 1

        if exponentIsSingleExpression:
            expression = expression.replace(f"{base}^{exponent}", f"({base}^{exponent})")
        else:
            expression = expression.replace(f"{base}^{'{'}{exponent}{'}'}", f"({base}^{'{'}{exponent}{'}'})")


        return expression

def alreadyWrapped(expression):
    wrappedParentheses = 0
    if expression[0] == '(':
        wrappedParentheses += 1
    if expression[-1] == ')':
        wrappedParentheses += 1
    for i in range(len(expression)):
        if expression[i] == '=':
            if expression[i-2] == ')':
                wrappedParentheses += 1
            if expression[i+2] == '(':
                wrappedParentheses += 1
            break
    return wrappedParentheses == 4

def isSingleExpression(expression):
    allPossibleOperations = ['+', '-', '*', '/', '^']
    allOperationsInExpression = set()
    for operation in allPossibleOperations:
        if operation in expression:
            allOperationsInExpression.add(operation)
    if len(allOperationsInExpression) == 0:
        return True
    elif len(allOperationsInExpression) == 1:
        operation = list(allOperationsInExpression)[0]
        numOperation = getNumOperation(expression, operation)
        if numOperation > 1:
            return False
        else:
            checkExpression = expression.split(operation)
            if checkExpression[0] != '':
                return False
    else:
        return False
    return True

def getNumOperation(expression, operation):
    result = 0
    for term in expression:
        if term == operation:
            result += 1

    return result

def indexOf(iterable, searchFor):
    for i, item in enumerate(iterable):
        if item == searchFor:
            return i
    return None

def convertToStandardForm(num: str, autoConvert=False):
    try:
        float(num)
    except:
        raise ValueError(f'{num} is not a valid number')

    doConversion = True
    if autoConvert:
        if float(num) <= MAX_SIZE_OF_NUM_BEFORE_CONVERTED_TO_STANDARD_FORM:
            doConversion = False


    if doConversion:
        if float(num) > 1:
            standardForm = ''
            decimalPlacesMoves = len(num)-1
            for i in range(len(num)):
                if i == 1:
                    standardForm += '.'
                if num[i] == '0':
                    """ REMOVE TRAILING ZEROES IF ANY """
                    charsToCheck = num[i:]
                    for j in range(len(charsToCheck)):
                        if charsToCheck[j] != '0':
                            standardForm += charsToCheck
                            break
                    break
                standardForm += num[i]

            roundedStandardForm = str(round(float(standardForm), 5))

            if len(standardForm) != len(roundedStandardForm):
                roundedStandardForm += '...'

            roundedStandardForm += f'e+{decimalPlacesMoves}'

            return roundedStandardForm
        else:
            i = 2 # START i AT THE FIRST ZERO AFTER THE DECIMAL POINT
            decimalPlacesMoves = 1
            indexOfFirstNoneZeroDigit = None
            while i < len(num):
                if num[i] != '0':
                    indexOfFirstNoneZeroDigit = i
                    break
                i += 1
                decimalPlacesMoves += 1

            standardForm = ''
            charsToCheck = num[indexOfFirstNoneZeroDigit:]
            for i in range(len(charsToCheck)):
                if i == 1:
                    standardForm += '.'
                standardForm += charsToCheck[i]

            standardForm += f'e-{decimalPlacesMoves}'
            return standardForm
    else:
        return num

# # OOP - Done
# def getNumOpenParen(expression):
#     counter = 0
#     for i in range(len(expression)):
#         if expression[i] == '(':
#             counter += 1
#     return counter
# # OOP - Done
# def getAllOperations(expression):
#     allPossibleOperations = ['+', '-', '*', '/', '^']
#     allOperationsInExpression = set()
#     for term in expression:
#         if term in allPossibleOperations:
#             allOperationsInExpression.add(term)
#
#     return allOperationsInExpression
# # OOP - DONE
# def getIndexOfInnerMostParen(expression, paren=None):
#     if paren == None:
#         paren = '('
#     if paren not in expression:
#         raise ValueError(f"{paren} not in expression")
#     if paren == '(':
#         numOpenParen = getNumOpenParen(expression)
#         parenCounter = 0
#         for i in range(len(expression)):
#             if expression[i] == paren:
#                 parenCounter += 1
#             if parenCounter == numOpenParen:
#                 return i
# # OOP - DONE
# def applyPEMDAS(expression):
#     i = 0
#     while i < len(expression):
#         # TODO - PARENTHESES, EXPONENTS
#         if expression[i] == '*':
#             allOperators = ['+', '-', '*', '/']
#             # if i != len(expression)-2:
#             if getNextOperator(expression, i) == '*':
#                 expressionWithOrder = '('
#                 expressionToReplace = ''
#                 """
#                 j IS OUR STATING INDEX, MEANING THE INDEX WHERE WE WILL START APPLYING PEMDAS, SO IT HAS TO BE SET EQUAL
#                 TO THE FIRST NUMBER/CHAR THAT WILL BE INCLUDED IN PARENTHESES.
#                 IN THE EXPRESSION S = '1+936*24*24*5', i WILL BE EQUAL TO 5 AND j SHOULD BE EQUAL TO 2 SINCE S[j] = S[2] = 9
#                 AND WE WILL START APPLYING PEMDAS AT 9: 1+(936*24*24*5)
#                 """
#                 j = i
#                 while expression[j-1] not in allOperators:
#                     j -= 1
#
#                 while True:
#                     if expression[j] == '*':
#                         if getNextOperator(expression, j) != '*':
#                             k = j
#                             while expression[k] not in getRestricredOperators('*'):
#                                 expressionWithOrder += expression[k]
#                                 expressionToReplace += expression[k]
#                                 if k+1 == len(expression):
#                                     break
#                                 k += 1
#                             break
#                     expressionWithOrder += expression[j]
#                     expressionToReplace += expression[j]
#                     j += 1
#                     if j == len(expression):
#                         break
#                 expressionWithOrder += ')'
#
#                 expression = expression.replace(expressionToReplace, expressionWithOrder)
#                 return expression
#
#             Terms = splitExpression(expression, i, '*', operation = 'arithmetic-multiply-single')
#             firstTerm, secondTerm = Terms[0], Terms[1]
#             expression = expression.replace(f"{firstTerm.replace('-', '')}*{secondTerm}", f"({firstTerm.replace('-', '')}*{secondTerm})")
#             i += 1
#         i += 1
#     return expression
# # OOP - Done
# def getOperationToPerform(expression):
#     allOperations = getAllOperations(expression)
#
#     if len(allOperations) == 0 and isSingleExpression(expression):
#         return 'no-operation'
#
#     # if '^' in expression:
#     #     if '{' in expression:
#     #         pass
#     #     else:
#     #         exponent = expression.split('^')[1]
#     #         if isDigit(exponent):
#     #             return 'arithmetic-exponent'
#
#     if ('+' in allOperations or '-' in allOperations) and ('*' not in allOperations and '/' not in allOperations):
#         numberOfAdditions = getNumOperation(expression, '+')
#         numberOfSubtractions = getNumOperation(expression, '-')
#         if numberOfAdditions > 1 or numberOfSubtractions > 1 or (numberOfAdditions + numberOfSubtractions > 1):
#             return 'add-subtract-only'
#     if ('*' in allOperations) and ('+' not in allOperations and '/' not in allOperations):
#         numberOfMultiplication = getNumOperation(expression, '*')
#         termsToBeMultiplied = expression.split('*')
#
#         couldBeMultiplyOnly = True
#
#         for term in termsToBeMultiplied:
#             if not isSingleExpression(term):
#                 couldBeMultiplyOnly = False
#
#         if numberOfMultiplication > 1 and couldBeMultiplyOnly:
#             return 'multiply-only'
#
#     if '+' in expression:
#         numberOfAdditions = getNumOperation(expression, '+')
#         if numberOfAdditions == 1:
#             if isDigit(expression.split('+')[0]) and isDigit(expression.split('+')[1]):
#                 return 'arithmetic-add-single'
#
#     if '-' in expression:
#         numberOfSubtractions = getNumOperation(expression, '-')
#         if numberOfSubtractions == 1:
#             if isDigit(expression.split('-')[0]) and isDigit(expression.split('-')[1]):
#                 return 'arithmetic-subtract-single'
#     if '*' in expression:
#         numberOfMultiplications = getNumOperation(expression, '*')
#         if numberOfMultiplications == 1:
#             if isDigit(expression.split('*')[0]) and isDigit(expression.split('*')[1]):
#                 return 'arithmetic-multiply-single'
#         if numberOfMultiplications > 1:
#             pass
#     if '/' in expression:
#         numberOfDivisions = getNumOperation(expression, '/')
#         if numberOfDivisions == '1':
#             if isDigit(expression.split('/')[0]) and isDigit(expression.split('/')[1]):
#                 return 'arithmetic-divide-single'
#
#     if len(allOperations) >= 2:
#         return 'general-arithmetic'
# # OOP - Done

# # OOP - Done
# def simplify(expression: str, stepCounter=None, Steps=None):
#     """ RETURNS  """
#     if Steps is None:
#         Steps = {}
#     if stepCounter is None:
#         stepCounter = 0
#
#     if '(' in expression and ')' in expression or isSingleExpression(expression):
#         numOpenParen = getNumOpenParen(expression)
#         if numOpenParen == 0:
#             return (Steps, expression, stepCounter)
#
#         for i in range(len(expression)):
#             currentExpressionToEvaluate = ''
#             if expression[i] == '(' and i == getIndexOfInnerMostParen(expression, '('):
#                 for j in range(i+1, len(expression)):
#                     if expression[j] != ')':
#                         currentExpressionToEvaluate += expression[j]
#                     else:
#                         break
#                 operation = getOperationToPerform(currentExpressionToEvaluate)
#                 if operation == 'arithmetic-add-single':
#                     firstTerm, secondTerm = currentExpressionToEvaluate.split('+')[0], currentExpressionToEvaluate.split('+')[1]
#                     result = castToFloatOrInt(float(firstTerm) + float(secondTerm), True)
#                     simplifiedExpression = expression.replace(f'({firstTerm}+{secondTerm})', result)
#                     expression = simplifiedExpression
#                     stepCounter += 1
#                     stepDictValue = {
#                         'step': f'Simplify inside the parentheses: ({firstTerm}+{secondTerm}) = {result}',
#                         'simplification': simplifiedExpression
#                     }
#                     Steps.update({stepCounter: stepDictValue})
#                     return simplify(expression, stepCounter, Steps)
#                 elif operation == 'arithmetic-subtract-single':
#                     firstTerm, secondTerm = currentExpressionToEvaluate.split('-')[0], currentExpressionToEvaluate.split('-')[1]
#                     result = castToFloatOrInt(float(firstTerm) - float(secondTerm), True)
#                     simplifiedExpression = expression.replace(f'({firstTerm}-{secondTerm})', result)
#                     expression = simplifiedExpression
#                     stepCounter += 1
#                     stepDictValue = {
#                         'step': f'Simplify inside the parentheses: ({firstTerm}-{secondTerm}) = {result}',
#                         'simplification': simplifiedExpression
#                     }
#                     Steps.update({stepCounter: stepDictValue})
#                     return simplify(expression, stepCounter, Steps)
#                 elif operation == 'arithmetic-multiply-single':
#                     firstTerm, secondTerm = currentExpressionToEvaluate.split('*')[0], currentExpressionToEvaluate.split('*')[1]
#                     result = castToFloatOrInt(float(firstTerm) * float(secondTerm), True)
#                     simplifiedExpression = expression.replace(f'({firstTerm}*{secondTerm})', result)
#                     expression = simplifiedExpression
#                     stepCounter += 1
#                     stepDictValue = {
#                         'step': f'Simplify inside the parentheses: ({firstTerm}*{secondTerm}) = {result}',
#                         'simplification': simplifiedExpression
#                     }
#                     Steps.update({stepCounter: stepDictValue})
#                     return simplify(expression, stepCounter, Steps)
#                 elif operation == 'add-subtract-only':
#                     result = addAndSubtractTerms(currentExpressionToEvaluate)
#                     simplifiedExpression = expression.replace(f'({currentExpressionToEvaluate})', result)
#                     stepCounter += 1
#                     stepDictValue = {
#                         'step': f'Simplify inside the parentheses by adding and subtracting [left to right]: ({currentExpressionToEvaluate}) = ({result})',
#                         'simplification': simplifiedExpression
#                     }
#                     Steps.update({stepCounter: stepDictValue})
#                     expression = simplifiedExpression
#                     return simplify(expression, stepCounter, Steps)
#                 elif operation == 'general-arithmetic':
#                     expressionWithOrder = applyPEMDAS(currentExpressionToEvaluate)
#                     simplifiedExpression = expression.replace(f'{currentExpressionToEvaluate}', expressionWithOrder)
#
#                     stepCounter += 1
#                     stepDictValue = {
#                         'step': f'Simplify inside the parentheses by applying PEMDAS: {currentExpressionToEvaluate} = {expressionWithOrder}',
#                         'simplification': simplifiedExpression
#                     }
#                     Steps.update({stepCounter: stepDictValue})
#                     return simplify(simplifiedExpression, stepCounter, Steps)
#                 elif operation == 'no-operation':
#                     result = currentExpressionToEvaluate
#                     simplifiedExpression = expression.replace(f'({currentExpressionToEvaluate})', f'{result}')
#                     expression = simplifiedExpression
#                     stepCounter += 1
#                     stepDictValue = {
#                         'step': f'Remove parentheses: ({currentExpressionToEvaluate}) = {result}',
#                         'simplification': simplifiedExpression
#                     }
#                     Steps.update({stepCounter: stepDictValue})
#                     return simplify(expression, stepCounter, Steps)
#
#     else:
#         operation = getOperationToPerform(expression)
#         if operation == 'arithmetic-add-single':
#             firstTerm, secondTerm = expression.split('+')[0], expression.split('+')[1]
#             result = castToFloatOrInt(float(firstTerm) + float(secondTerm), True)
#             stepCounter += 1
#             stepDictValue = {
#                 'step': f'Add the first and second term: {firstTerm}+{secondTerm} = {result}',
#                 'simplification': result
#             }
#             Steps.update({stepCounter: stepDictValue})
#             return simplify(result, stepCounter, Steps)
#         elif operation == 'arithmetic-subtract-single':
#             firstTerm, secondTerm = expression.split('-')[0], expression.split('-')[1]
#             result = castToFloatOrInt(float(firstTerm) - float(secondTerm), True)
#             stepCounter += 1
#             stepDictValue = {
#                 'step': f'Subtract the first and second term: {firstTerm}-{secondTerm} = {result}',
#                 'simplification': result
#             }
#             Steps.update({stepCounter: stepDictValue})
#             return simplify(result, stepCounter, Steps)
#         elif operation == 'arithmetic-multiply-single':
#             firstTerm, secondTerm = expression.split('*')[0], expression.split('*')[1]
#             result = castToFloatOrInt(float(firstTerm) * float(secondTerm), True)
#             stepCounter += 1
#             stepDictValue = {
#                 'step': f'Multiply the first and second term: {firstTerm}*{secondTerm} = {result}',
#                 'simplification': result
#             }
#             Steps.update({stepCounter: stepDictValue})
#             return simplify(result, stepCounter, Steps)
#         elif operation == 'add-subtract-only':
#             result = addAndSubtractTerms(expression)
#             stepCounter += 1
#             stepDictValue = {
#                 'step': f'Add and subtract [left to right]: {expression} = {result}',
#                 'simplification': result
#             }
#             Steps.update({stepCounter: stepDictValue})
#             return simplify(result, stepCounter, Steps)
#         elif operation == 'general-arithmetic':
#             expressionWithOrder = applyPEMDAS(expression)
#
#             stepCounter += 1
#             stepDictValue = {
#                 'step': f'Apply PEMDAS: {expression} = {expressionWithOrder}',
#                 'simplification': expressionWithOrder
#             }
#             Steps.update({stepCounter: stepDictValue})
#             return simplify(expressionWithOrder, stepCounter, Steps)




def main():
    # print(simplify('((1+1)*2)')[0])

    expression = ArithmeticExpression('2^{2+1}*2^{3+2}*2^{4+3}*2^{1+4*3}')
    print(evaluateArithmetic(expression)[0])

    # print(applyPEMDAS('1+2*-3*-4*523+9'))

    pass

    # print(getAllOperations('1+1+5-5'))
    # print(addAndSubtractTerms('1+2+27-5'))





    # Steps = {1: {'step': 'Simplify inside the brackets: (1+1) = 2', 'simplification': '(2*2)'},
    #        2: {'step': 'Simplify inside the brackets: (2*2) = 4', 'simplification': '4'}}
    #
    # print(Steps)
    # print()
    # for stepNum in Steps:
    #     Steps.update({stepNum: {'step': latexify(Steps[stepNum]["step"]), 'simplification': latexify(Steps[stepNum]["simplification"])}})
    #
    # print(Steps)






if __name__ == '__main__':
    main()
