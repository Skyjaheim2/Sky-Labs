from math import floor

def parseLatex(latexString: str):
    latexString = latexString.replace('\left(', '(').replace('\\right)', ')').replace('\cdot', '*')
    return latexString

def latexify(expression):
    expression = expression.replace('(', '\left(').replace(')', '\\right)').replace('*', '\cdot')
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
                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Add and subtract [left to right]: {currentExpressionToEvaluate} = {result}',
                        'simplification': result
                    }
                    Steps.update({stepCounter: stepDictValue})
                    return simplify(result, stepCounter, Steps)
                elif operation == 'general-arithmetic':
                    expressionWithOrder = applyPEDMAS(currentExpressionToEvaluate)

                    stepCounter += 1
                    stepDictValue = {
                        'step': f'Apply PEDMAS: {currentExpressionToEvaluate} = {expressionWithOrder}',
                        'simplification': expressionWithOrder
                    }
                    Steps.update({stepCounter: stepDictValue})
                    return simplify(expressionWithOrder, stepCounter, Steps)
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
            expressionWithOrder = applyPEDMAS(expression)

            stepCounter += 1
            stepDictValue = {
                'step': f'Apply PEDMAS: {expression} = {expressionWithOrder}',
                'simplification': expressionWithOrder
            }
            Steps.update({stepCounter: stepDictValue})
            return simplify(expressionWithOrder, stepCounter, Steps)



def getOperationToPerform(expression):
    allOperations = getAllOperations(expression)

    if len(allOperations) == 0 and isSingleExpression(expression):
        return 'no-operation'

    if ('+' in allOperations or '-' in allOperations) and ('*' not in allOperations and '/' not in allOperations):
        numberOfAdditions = getNumOperation(expression, '+')
        numberOfSubtractions = getNumOperation(expression, '-')
        if numberOfAdditions > 1 or numberOfSubtractions > 1 or (numberOfAdditions + numberOfSubtractions > 1):
            return 'add-subtract-only'
    if len(allOperations) > 2:
        return 'general-arithmetic'

    if '+' in expression:
        numberOfAdditions = getNumOperation(expression, '+')
        if numberOfAdditions == 1:
            if isDigit(expression.split('+')[0]) and isDigit(expression.split('+')[1]):
                return 'arithmetic-add-single'

    elif '-' in expression:
        numberOfSubtractions = getNumOperation(expression, '-')
        if numberOfSubtractions == 1:
            if isDigit(expression.split('-')[0]) and isDigit(expression.split('-')[1]):
                return 'arithmetic-subtract-single'
    elif '*' in expression:
        numberOfMultiplications = getNumOperation(expression, '*')
        if numberOfMultiplications == 1:
            if isDigit(expression.split('*')[0]) and isDigit(expression.split('*')[1]):
                return 'arithmetic-multiply-single'
    elif '/' in expression:
        numberOfDivisions = getNumOperation(expression, '/')
        if numberOfDivisions == '1':
            if isDigit(expression.split('/')[0]) and isDigit(expression.split('/')[1]):
                return 'arithmetic-divide-single'

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
                return str(float(num))
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

def getIndexOfInnerMostParen(expression, paren):
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

def applyPEDMAS(expression):
    i = 0
    while i < len(expression):
        # TODO - PARENTHESES, EXPONENTS
        if expression[i] == '*':
            firstTerm, secondTerm = expression[i-1], expression[i+1]
            expression = expression.replace(f'{firstTerm}*{secondTerm}', f'({firstTerm}*{secondTerm})')
            i += 1
        i += 1
    return expression

def isDigit(numString):
    try:
        numString = float(numString)
    except ValueError:
        return False
    return True






def main():
    # print(simplify('((1+1)*2)')[0])
    print(simplify('(1+2+((3+9)))'))

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
