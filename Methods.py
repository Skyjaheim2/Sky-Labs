import re

def parseLatex(latexString: str):
    latexString = latexString.replace('\left(', '(').replace('\\right)', ')').replace('\left\{', '{').replace('\\right\}', '}') \
        .replace('\cdot', '*').replace(r'\pi', 'pi').replace('\sqrt', 'sqrt').replace('\sqrt[2]', 'sqrt') \
        .replace(r'\frac', 'frac').replace('^1', '').replace('^{1}', '').replace(r'\lim', 'lim').replace(r'\to', '→')\
        .replace(r'\infty', 'infty')

    specialFunctions = getSpecialFunctions()
    for func in specialFunctions:
        latexString = latexString.replace(rf'\{func}', func)

    """ PARSE b^x as b^{x} """
    exponent_pattern = re.compile(r'\^[a-zA-Z0-9]')
    exponent_matches = exponent_pattern.findall(latexString)

    for match in exponent_matches:
        strToReplaceMatch = f"^{'{'}{match[1:]}{'}'}"
        latexString = latexString.replace(match, strToReplaceMatch)

    return latexString

def latexify(expression):
    expression = expression.replace('(', '\left(').replace(')', '\\right)').replace('*', '\cdot').replace('pi', r'\pi') \
                           .replace('sqrt', '\\sqrt').replace('sqrt[2]', 'sqrt').replace('frac', r'\frac').replace('^{1}', '')\
                           .replace('lim', r'\lim').replace('→', r'\to').replace(r'infty', r'\infty')

    """ REPLACE \sin with sin  """
    specialFunctions = getSpecialFunctions()
    for func in specialFunctions:
        expression = expression.replace(func, rf'\{func}')
    expression = expression.replace(r'\\', '\\')

    """ REPLACE \cdotx with \cdot x """
    multiplication_pattern = re.compile(r'\\cdot\w{1}')
    multiplication_matches = multiplication_pattern.findall(expression)

    for match in multiplication_matches:
        charToSpace = match[-1]
        if not charToSpace.isdigit():
            expression = expression.replace(match, f'{match[:-1]} {charToSpace}')

    symbolsToCatch = ['pi', 'phi', 'omega', 'rho', 'alpha', 'beta', 'partial']

    for symbol in symbolsToCatch:
        reExpression = fr'\\{symbol}' + '\w{1}'
        symbol_multiplication_pattern = re.compile(reExpression)
        symbol_multiplication_matches = symbol_multiplication_pattern.findall(expression)

        for match in symbol_multiplication_matches:
            charToSpace = match[-1]
            if not charToSpace.isdigit():
                expression = expression.replace(match, f'{match[:-1]} {charToSpace}')

    return expression

def getSpecialFunctions():
    return ['ln', 'sin', 'cos', 'tan', 'csc', 'sec', 'cot', 'sinh', 'cosh', 'tanh']

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
            if term[0] != '+' and term[0] != '-': term = f'+{term}'
            heading += str(term)
        if heading[0] == '+': heading = heading[1:]
        return heading

def parenIsBalanced(string, parenToCheckFor='normal'):
    numOpenParen = 0
    numClosedParen = 0
    if parenToCheckFor == 'normal':
        openParen = '('
        closedParen = ')'
    elif parenToCheckFor == 'curly':
        openParen = '{'
        closedParen = '}'
    else:
        for char in string:
            if (char == ')' or char == '}') and numOpenParen == 0:
                return False
            if char == '(' or char == '{':
                numOpenParen += 1
            elif char == ')' or char == '}':
                numClosedParen += 1
        return numOpenParen == numClosedParen

    for char in string:
        if char == closedParen and numOpenParen == 0:
            return False
        if char == openParen:
            numOpenParen += 1
        elif char == closedParen:
            numClosedParen += 1

    return numOpenParen == numClosedParen

def joinList(items: list, delimiter: str) -> str:
    strToReturn = ''
    for item in items:
        strToReturn += f'{item}{delimiter}'

    if strToReturn[-1] == delimiter:
        return strToReturn[:-1]
    else:
        return strToReturn

def indexOf(iterable, searchFor):
    for i, item in enumerate(iterable):
        if item == searchFor:
            return i
    return None

def getIndexOfLastOccurrence(expression: str, charToFind: str):
    indexes = []
    for i, char in enumerate(expression):
        if char == charToFind:
            indexes.append(i)

    return indexes[-1]

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

def reverseList(L):
    return L[::-1]