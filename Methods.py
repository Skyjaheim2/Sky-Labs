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

    numOpenParen = getNumOpenParen(expression)
    if numOpenParen == 0:
        return (Steps, expression, stepCounter)

    for i in range(len(expression)):
        currentExpressionToEvaluate = ''
        if (i+1) == numOpenParen:
            for j in range(i+1, len(expression)):
                if expression[j] != ')':
                    currentExpressionToEvaluate += expression[j]
                else:
                    break
            operation = getOperationToPerform(currentExpressionToEvaluate)
            if operation == 'arithmetic-add':
                firstTerm, secondTerm = currentExpressionToEvaluate.split('+')[0], currentExpressionToEvaluate.split('+')[1]
                result = str(int(firstTerm) + int(secondTerm))
                simplifiedExpression = expression.replace(f'({firstTerm}+{secondTerm})', result)
                expression = simplifiedExpression
                stepCounter += 1
                stepDictValue = {
                    'step': f'Simplify inside the brackets: ({firstTerm}+{secondTerm}) = {result}',
                    'simplification': simplifiedExpression
                }
                Steps.update({stepCounter: stepDictValue})
                return simplify(expression, stepCounter, Steps)
            elif operation == 'arithmetic-subtract':
                firstTerm, secondTerm = currentExpressionToEvaluate.split('-')[0], currentExpressionToEvaluate.split('-')[1]
                result = str(int(firstTerm) - int(secondTerm))
                simplifiedExpression = expression.replace(f'({firstTerm}-{secondTerm})', result)
                expression = simplifiedExpression
                stepCounter += 1
                stepDictValue = {
                    'step': f'Simplify inside the brackets: ({firstTerm}-{secondTerm}) = {result}',
                    'simplification': simplifiedExpression
                }
                Steps.update({stepCounter: stepDictValue})
                return simplify(expression, stepCounter, Steps)
            elif operation == 'arithmetic-multiply':
                firstTerm, secondTerm = currentExpressionToEvaluate.split('*')[0], currentExpressionToEvaluate.split('*')[1]
                result = str(int(firstTerm) * int(secondTerm))
                simplifiedExpression = expression.replace(f'({firstTerm}*{secondTerm})', result)
                expression = simplifiedExpression
                stepCounter += 1
                stepDictValue = {
                    'step': f'Simplify inside the brackets: ({firstTerm}*{secondTerm}) = {result}',
                    'simplification': simplifiedExpression
                }
                Steps.update({stepCounter: stepDictValue})
                return simplify(expression, stepCounter, Steps)


def getOperationToPerform(expression):
    if '+' in expression:
        if expression.split('+')[0].isdigit() and expression.split('+')[1].isdigit():
            return 'arithmetic-add'
    elif '-' in expression:
        if expression.split('-')[0].isdigit() and expression.split('-')[1].isdigit():
            return 'arithmetic-subtract'
    elif '*' in expression:
        if expression.split('*')[0].isdigit() and expression.split('*')[1].isdigit():
            return 'arithmetic-multiply'
    elif '/' in expression:
        if expression.split('/')[0].isdigit() and expression.split('/')[1].isdigit():
            return 'arithmetic-divide'


def getNumOpenParen(expression):
    counter = 0
    for i in range(len(expression)):
        if expression[i] == '(':
            counter += 1
    return counter







def main():
    # print(simplify('((1+1)*2)')[0])

    Steps = {1: {'step': 'Simplify inside the brackets: (1+1) = 2', 'simplification': '(2*2)'},
           2: {'step': 'Simplify inside the brackets: (2*2) = 4', 'simplification': '4'}}

    print(Steps)
    print()
    for stepNum in Steps:
        Steps.update({stepNum: {'step': latexify(Steps[stepNum]["step"]), 'simplification': latexify(Steps[stepNum]["simplification"])}})

    print(Steps)






if __name__ == '__main__':
    main()
