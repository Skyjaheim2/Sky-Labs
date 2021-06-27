from math import floor, pi, e

def parseLatex(latexString: str):
    latexString = latexString.replace('\left(', '(').replace('\\right)', ')').replace('\cdot', '*').replace('\\pi', f'{pi}')\
                             .replace('e', f'{e}')
    return latexString

def latexify(expression):
    expression = expression.replace('(', '\left(').replace(')', '\\right)').replace('*', '\cdot').replace(f'{pi}', '\pi')\
                           .replace(f'{e}', 'e')
    return expression

def simplify(expression: str, stepCounter=None, Steps=None):
    """ RETURNS  """
    if Steps is None:
        Steps = {}
    if stepCounter is None:
        stepCounter = 0

    if '(' in expression and ')' in expression or isSingleExpression(expression):
        numOpenParen = getNumOpenParen(expression)
        if numOpenParen == 0:
            return (Steps, expression, stepCounter)

        for i in range(len(expression)):
            currentExpressionToEvaluate = ''
            if expression[i] == '(' and i == getIndexOfInnerMostParen(expression, '('):
                for j in range(i+1, len(expression)):
                    if expression[j] != ')':
                        currentExpressionToEvaluate += expression[j]
                    else:
                        break
                operation = getOperationToPerform(currentExpressionToEvaluate)
                if operation == 'arithmetic-add-single':
                    firstTerm, secondTerm = currentExpressionToEvaluate.split('+')[0], currentExpressionToEvaluate.split('+')[1]
                    result = castToFloatOrInt(float(firstTerm) + float(secondTerm), True)
                    simplifiedExpression = expression.replace(f'({firstTerm}+{secondTerm})', result)
                    expression = simplifiedExpression
                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Simplify inside the parentheses: ({firstTerm}+{secondTerm}) = {result}',
                        'simplification': simplifiedExpression
                    }
                    Steps.update({stepCounter: stepDictValue})
                    return simplify(expression, stepCounter, Steps)
                elif operation == 'arithmetic-subtract-single':
                    firstTerm, secondTerm = currentExpressionToEvaluate.split('-')[0], currentExpressionToEvaluate.split('-')[1]
                    result = castToFloatOrInt(float(firstTerm) - float(secondTerm), True)
                    simplifiedExpression = expression.replace(f'({firstTerm}-{secondTerm})', result)
                    expression = simplifiedExpression
                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Simplify inside the parentheses: ({firstTerm}-{secondTerm}) = {result}',
                        'simplification': simplifiedExpression
                    }
                    Steps.update({stepCounter: stepDictValue})
                    return simplify(expression, stepCounter, Steps)
                elif operation == 'arithmetic-multiply-single':
                    firstTerm, secondTerm = currentExpressionToEvaluate.split('*')[0], currentExpressionToEvaluate.split('*')[1]
                    result = castToFloatOrInt(float(firstTerm) * float(secondTerm), True)
                    simplifiedExpression = expression.replace(f'({firstTerm}*{secondTerm})', result)
                    expression = simplifiedExpression
                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Simplify inside the parentheses: ({firstTerm}*{secondTerm}) = {result}',
                        'simplification': simplifiedExpression
                    }
                    Steps.update({stepCounter: stepDictValue})
                    return simplify(expression, stepCounter, Steps)
                elif operation == 'add-subtract-only':
                    result = addAndSubtractTerms(currentExpressionToEvaluate)
                    simplifiedExpression = expression.replace(f'({currentExpressionToEvaluate})', result)
                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Simplify inside the parentheses by adding and subtracting [left to right]: ({currentExpressionToEvaluate}) = ({result})',
                        'simplification': simplifiedExpression
                    }
                    Steps.update({stepCounter: stepDictValue})
                    expression = simplifiedExpression
                    return simplify(expression, stepCounter, Steps)
                elif operation == 'general-arithmetic':
                    expressionWithOrder = applyPEMDAS(currentExpressionToEvaluate)
                    simplifiedExpression = expression.replace(f'{currentExpressionToEvaluate}', expressionWithOrder)

                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Simplify inside the parentheses by applying PEMDAS: {currentExpressionToEvaluate} = {expressionWithOrder}',
                        'simplification': simplifiedExpression
                    }
                    Steps.update({stepCounter: stepDictValue})
                    return simplify(simplifiedExpression, stepCounter, Steps)
                elif operation == 'no-operation':
                    result = currentExpressionToEvaluate
                    simplifiedExpression = expression.replace(f'({currentExpressionToEvaluate})', f'{result}')
                    expression = simplifiedExpression
                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Remove parentheses: ({currentExpressionToEvaluate}) = {result}',
                        'simplification': simplifiedExpression
                    }
                    Steps.update({stepCounter: stepDictValue})
                    return simplify(expression, stepCounter, Steps)

    else:
        operation = getOperationToPerform(expression)
        if operation == 'arithmetic-add-single':
            firstTerm, secondTerm = expression.split('+')[0], expression.split('+')[1]
            result = castToFloatOrInt(float(firstTerm) + float(secondTerm), True)
            stepCounter += 1
            stepDictValue = {
                'step': f'Add the first and second term: {firstTerm}+{secondTerm} = {result}',
                'simplification': result
            }
            Steps.update({stepCounter: stepDictValue})
            return simplify(result, stepCounter, Steps)
        elif operation == 'arithmetic-subtract-single':
            firstTerm, secondTerm = expression.split('-')[0], expression.split('-')[1]
            result = castToFloatOrInt(float(firstTerm) - float(secondTerm), True)
            stepCounter += 1
            stepDictValue = {
                'step': f'Subtract the first and second term: {firstTerm}-{secondTerm} = {result}',
                'simplification': result
            }
            Steps.update({stepCounter: stepDictValue})
            return simplify(result, stepCounter, Steps)
        elif operation == 'arithmetic-multiply-single':
            firstTerm, secondTerm = expression.split('*')[0], expression.split('*')[1]
            result = castToFloatOrInt(float(firstTerm) * float(secondTerm), True)
            stepCounter += 1
            stepDictValue = {
                'step': f'Multiply the first and second term: {firstTerm}*{secondTerm} = {result}',
                'simplification': result
            }
            Steps.update({stepCounter: stepDictValue})
            return simplify(result, stepCounter, Steps)
        elif operation == 'add-subtract-only':
            result = addAndSubtractTerms(expression)
            stepCounter += 1
            stepDictValue = {
                'step': f'Add and subtract [left to right]: {expression} = {result}',
                'simplification': result
            }
            Steps.update({stepCounter: stepDictValue})
            return simplify(result, stepCounter, Steps)
        elif operation == 'general-arithmetic':
            expressionWithOrder = applyPEMDAS(expression)

            stepCounter += 1
            stepDictValue = {
                'step': f'Apply PEMDAS: {expression} = {expressionWithOrder}',
                'simplification': expressionWithOrder
            }
            Steps.update({stepCounter: stepDictValue})
            return simplify(expressionWithOrder, stepCounter, Steps)

def evaluateArithmetic(expression, stepCounter=None, Steps=None, returnStepsAsArray=False):
    if Steps is None:
        Steps = {}
    if stepCounter is None:
        stepCounter = 0
    if isSingleExpression(expression):
        if returnStepsAsArray:
            stepsAsArray = []
            for step in Steps:
                stepsAsArray.append(Steps[step])
            return (stepsAsArray, expression, stepCounter)
        return (Steps,expression, stepCounter)

    allOperators = ['+','-','*','/']
    operation = getOperationToPerform(expression)

    if '++' in expression:
        simplifiedExpression = expression.replace('++', '+')
        expression = simplifiedExpression

        stepDictValue = {
            'step': f'Apply rule: a++b = a+b',
            'simplification': simplifiedExpression
        }
        stepCounter += 1
        Steps.update({stepCounter: stepDictValue})

        return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)

    if '+-' in expression:
        simplifiedExpression = expression.replace('+-', '-')
        expression = simplifiedExpression

        stepDictValue = {
            'step': f'Apply rule: a+-b = a-b',
            'simplification': simplifiedExpression
        }
        stepCounter += 1
        Steps.update({stepCounter: stepDictValue})

        return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)

    if '--' in expression:
        simplifiedExpression = expression.replace('--', '+')
        expression = simplifiedExpression

        stepDictValue = {
            'step': f'Apply rule: a--b = a+b',
            'simplification': simplifiedExpression
        }
        stepCounter += 1
        Steps.update({stepCounter: stepDictValue})

        return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)


    if operation == 'general-arithmetic' and '(' not in expression:
        expressionWithOrder = applyPEMDAS(expression)

        stepDictValue = {
            'step': f'Apply PEMDAS: {expression} = {expressionWithOrder}',
            'simplification': expressionWithOrder
        }
        expression = expressionWithOrder
        stepCounter += 1
        Steps.update({stepCounter: stepDictValue})

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

    for i in range(len(expression)):
        if ('(' in expression and ')' in expression) or isSingleExpression(expression):

            for i in range(len(expression)):
                currentExpressionToEvaluate = ''
                if expression[i] == '(' and i == getIndexOfInnerMostParen(expression, '('):
                    for j in range(i + 1, len(expression)):
                        if expression[j] != ')':
                            currentExpressionToEvaluate += expression[j]
                        else:
                            break

                    Simplification = evaluateArithmetic(currentExpressionToEvaluate, returnStepsAsArray=True)
                    result = Simplification[1]
                    stepsAsArray = Simplification[0]

                    for stepToAdd in stepsAsArray:
                        stepDictValue = {
                            'step': wrapStepInParen(f"{stepToAdd['step']}"),
                            'simplification': expression.replace(f'({currentExpressionToEvaluate})', f"({stepToAdd['simplification']})")
                        }
                        stepCounter += 1
                        Steps.update({stepCounter: stepDictValue})

                    simplifiedExpression = expression.replace(f'({currentExpressionToEvaluate})', result)
                    expression = simplifiedExpression

                    return evaluateArithmetic(expression, stepCounter, Steps, returnStepsAsArray)

        if expression[i] in allOperators:
            operator = expression[i]
            operationMessage = getOperationMessage(operator)
            Terms = splitExpression(expression, i, operator, operation=operation)
            firstTerm, secondTerm = Terms[0], Terms[1]

            if firstTerm != '' and secondTerm != '':
                result = castToFloatOrInt(eval(f'float(firstTerm) {operator} float(secondTerm)'), True)
                simplifiedExpression = expression.replace(f'{firstTerm}{operator}{secondTerm}', result)
                expression = simplifiedExpression

                stepDictValue = {
                    'step': f'{operationMessage} the first and second term: {firstTerm}{operator}{secondTerm} = {result}',
                    'simplification': simplifiedExpression
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


def getOperationToPerform(expression):
    allOperations = getAllOperations(expression)

    if len(allOperations) == 0 and isSingleExpression(expression):
        return 'no-operation'

    if ('+' in allOperations or '-' in allOperations) and ('*' not in allOperations and '/' not in allOperations):
        numberOfAdditions = getNumOperation(expression, '+')
        numberOfSubtractions = getNumOperation(expression, '-')
        if numberOfAdditions > 1 or numberOfSubtractions > 1 or (numberOfAdditions + numberOfSubtractions > 1):
            return 'add-subtract-only'
    if ('*' in allOperations) and ('+' not in allOperations and '/' not in allOperations):
        numberOfMultiplication = getNumOperation(expression, '*')
        termsToBeMultiplied = expression.split('*')

        couldBeMultiplyOnly = True

        for term in termsToBeMultiplied:
            if not isSingleExpression(term):
                couldBeMultiplyOnly = False

        if numberOfMultiplication > 1 and couldBeMultiplyOnly:
            return 'multiply-only'

    if '+' in expression:
        numberOfAdditions = getNumOperation(expression, '+')
        if numberOfAdditions == 1:
            if isDigit(expression.split('+')[0]) and isDigit(expression.split('+')[1]):
                return 'arithmetic-add-single'

    if '-' in expression:
        numberOfSubtractions = getNumOperation(expression, '-')
        if numberOfSubtractions == 1:
            if isDigit(expression.split('-')[0]) and isDigit(expression.split('-')[1]):
                return 'arithmetic-subtract-single'
    if '*' in expression:
        numberOfMultiplications = getNumOperation(expression, '*')
        if numberOfMultiplications == 1:
            if isDigit(expression.split('*')[0]) and isDigit(expression.split('*')[1]):
                return 'arithmetic-multiply-single'
        if numberOfMultiplications > 1:
            pass
    if '/' in expression:
        numberOfDivisions = getNumOperation(expression, '/')
        if numberOfDivisions == '1':
            if isDigit(expression.split('/')[0]) and isDigit(expression.split('/')[1]):
                return 'arithmetic-divide-single'

    if len(allOperations) >= 2:
        return 'general-arithmetic'

def getNumOperation(expression, operation):
    allPossibleOperations = ['+', '-', '*', '/']
    result = 0
    for term in expression:
        if term == operation:
            result += 1

    return result

def isSingleExpression(expression):
    allPossibleOperations = ['+', '-', '*', '/']
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

def getNumOpenParen(expression):
    counter = 0
    for i in range(len(expression)):
        if expression[i] == '(':
            counter += 1
    return counter

def getAllOperations(expression):
    allPossibleOperations = ['+', '-', '*', '/']
    allOperationsInExpression = set()
    for term in expression:
        if term in allPossibleOperations:
            allOperationsInExpression.add(term)

    return allOperationsInExpression

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

def getIndexOfInnerMostParen(expression, paren=None):
    if paren == None:
        paren = '('
    if paren not in expression:
        raise ValueError(f"{paren} not in expression")
    if paren == '(':
        numOpenParen = getNumOpenParen(expression)
        parenCounter = 0
        for i in range(len(expression)):
            if expression[i] == paren:
                parenCounter += 1
            if parenCounter == numOpenParen:
                return i

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
        otherOperators = getRestricredOperators('-')
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

def getRestricredOperators(restrictedOperator):
    """ RETURNS ALL OPERATORS EXCEPT THE ONE PASS AS PARAMETER """
    allOperators = {'+', '-', '*', '/'}
    return allOperators.symmetric_difference(restrictedOperator)

def reverse(iterable):
    return iterable[::-1]

def applyPEMDAS(expression):
    i = 0
    while i < len(expression):
        # TODO - PARENTHESES, EXPONENTS
        if expression[i] == '*':
            allOperators = ['+', '-', '*', '/']
            # if i != len(expression)-2:
            if getNextOperator(expression, i) == '*':
                expressionWithOrder = '('
                expressionToReplace = ''
                """
                j IS OUR STATING INDEX, MEANING THE INDEX WHERE WE WILL START APPLYING PEMDAS, SO IT HAS TO BE SET EQUAL
                TO THE FIRST NUMBER/CHAR THAT WILL BE INCLUDED IN PARENTHESES.
                IN THE EXPRESSION S = '1+936*24*24*5', i WILL BE EQUAL TO 5 AND j SHOULD BE EQUAL TO 2 SINCE S[j] = S[2] = 9
                AND WE WILL START APPLYING PEMDAS AT 9: 1+(936*24*24*5)
                """
                j = i
                while expression[j-1] not in allOperators:
                    j -= 1

                while True:
                    if expression[j] == '*':
                        if getNextOperator(expression, j) != '*':
                            k = j
                            while expression[k] not in getRestricredOperators('*'):
                                expressionWithOrder += expression[k]
                                expressionToReplace += expression[k]
                                if k+1 == len(expression):
                                    break
                                k += 1
                            break
                    expressionWithOrder += expression[j]
                    expressionToReplace += expression[j]
                    j += 1
                    if j == len(expression):
                        break
                expressionWithOrder += ')'

                expression = expression.replace(expressionToReplace, expressionWithOrder)
                return expression

            Terms = splitExpression(expression, i, '*', operation = 'arithmetic-multiply-single')
            firstTerm, secondTerm = Terms[0], Terms[1]
            expression = expression.replace(f"{firstTerm.replace('-', '')}*{secondTerm}", f"({firstTerm.replace('-', '')}*{secondTerm})")
            i += 1
        i += 1
    return expression

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

def isDigit(numString):
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





def main():
    # print(simplify('((1+1)*2)')[0])
    print(evaluateArithmetic('23-125*11+18')[0])

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
