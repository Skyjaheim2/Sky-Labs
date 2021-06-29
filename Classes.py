from math import floor
from Methods import getAllOperations, isDigit, getNumOpenParen, reverse, getRestricredOperators, getNextOperator, evaluateArithmetic

# class arithmeticExpression:
#     def __init__(self, expression):
#         self.expression = expression
#
#     """ INSTANCE METHODS """
#
#     def getOperationToPerform(self):
#         allOperations = getAllOperations(self.expression)
#
#         if len(allOperations) == 0 and self.isSingleExpression():
#             return 'no-operation'
#
#         # if '^' in expression:
#         #     if '{' in expression:
#         #         pass
#         #     else:
#         #         exponent = expression.split('^')[1]
#         #         if isDigit(exponent):
#         #             return 'arithmetic-exponent'
#
#         if ('+' in allOperations or '-' in allOperations) and ('*' not in allOperations and '/' not in allOperations):
#             numberOfAdditions = self.getNumOperation('+', self.expression)
#             numberOfSubtractions = self.getNumOperation('-', self.expression)
#             if numberOfAdditions > 1 or numberOfSubtractions > 1 or (numberOfAdditions + numberOfSubtractions > 1):
#                 return 'add-subtract-only'
#         if ('*' in allOperations) and ('+' not in allOperations and '/' not in allOperations):
#             numberOfMultiplication = self.getNumOperation('*', self.expression)
#             termsToBeMultiplied = self.expression.split('*')
#
#             couldBeMultiplyOnly = True
#
#             for term in termsToBeMultiplied:
#                 if not self.isSingleExpression(term):
#                     couldBeMultiplyOnly = False
#
#             if numberOfMultiplication > 1 and couldBeMultiplyOnly:
#                 return 'multiply-only'
#
#         if '+' in self.expression:
#             numberOfAdditions = self.getNumOperation('+', self.expression)
#             if numberOfAdditions == 1:
#                 if isDigit(self.expression.split('+')[0]) and isDigit(self.expression.split('+')[1]):
#                     return 'arithmetic-add-single'
#
#         if '-' in self.expression:
#             numberOfSubtractions = self.getNumOperation('-', self.expression)
#             if numberOfSubtractions == 1:
#                 if isDigit(self.expression.split('-')[0]) and isDigit(self.expression.split('-')[1]):
#                     return 'arithmetic-subtract-single'
#         if '*' in self.expression:
#             numberOfMultiplications = self.getNumOperation('*', self.expression)
#             if numberOfMultiplications == 1:
#                 if isDigit(self.expression.split('*')[0]) and isDigit(self.expression.split('*')[1]):
#                     return 'arithmetic-multiply-single'
#             if numberOfMultiplications > 1:
#                 pass
#         if '/' in self.expression:
#             numberOfDivisions = self.getNumOperation('/', self.expression)
#             if numberOfDivisions == '1':
#                 if isDigit(self.expression.split('/')[0]) and isDigit(self.expression.split('/')[1]):
#                     return 'arithmetic-divide-single'
#
#         if len(allOperations) >= 2:
#             return 'general-arithmetic'
#
#     def isSingleExpression(self, expression=None):
#         if expression == None:
#             expression = self.expression
#
#         allPossibleOperations = ['+', '-', '*', '/', '^']
#         allOperationsInExpression = set()
#         for operation in allPossibleOperations:
#             if operation in expression:
#                 allOperationsInExpression.add(operation)
#         if len(allOperationsInExpression) == 0:
#             return True
#         elif len(allOperationsInExpression) == 1:
#             operation = list(allOperationsInExpression)[0]
#             numOperation = self.getNumOperation(operation, expression)
#             if numOperation > 1:
#                 return False
#             else:
#                 checkExpression = expression.split(operation)
#                 if checkExpression[0] != '':
#                     return False
#         else:
#             return False
#         return True
#
#     def getNumOperation(self, operation, expression=None):
#         if expression == None:
#             expression = self.expression
#         result = 0
#         for term in expression:
#             if term == operation:
#                 result += 1
#
#         return result
#
#     def getNumOpenParen(self):
#         counter = 0
#         for i in range(len(self.expression)):
#             if self.expression[i] == '(':
#                 counter += 1
#         return counter
#
#     def getAllOperations(self):
#         allPossibleOperations = ['+', '-', '*', '/', '^']
#         allOperationsInExpression = set()
#         for term in self.expression:
#             if term in allPossibleOperations:
#                 allOperationsInExpression.add(term)
#
#         return allOperationsInExpression
#
#     def getIndexOfInnerMostParen(self):
#         paren = '('
#         if paren not in self.expression:
#             raise ValueError(f"{paren} not in expression")
#
#         numOpenParen = getNumOpenParen(self.expression)
#         parenCounter = 0
#         for i in range(len(self.expression)):
#             if self.expression[i] == paren:
#                 parenCounter += 1
#             if parenCounter == numOpenParen:
#                 return i
#
#     def splitExpression(self, index, operator, binarySplit=True, operation=None):
#         """
#         A BINARY SPLIT OF THE expression 2+43*21-5 ON THE OPERATOR '*' AT INDEX 4 RETURNS ('43', '21')
#         A NON-BINARY SPLIT OF THE expression 2+43*21-5 ON THE OPERATOR '*' AT INDEX 4 RETURNS ('2+43', '21-5')
#         """
#         if not binarySplit:
#             for i in range(len(self.expression)):
#                 if i == index:
#                     firstTerm, secondTerm = '', ''
#                     """ GET FIRST TERM """
#                     j = 0
#                     while True:
#                         if self.expression[j] == operator:
#                             break
#                         firstTerm += self.expression[j]
#                         j += 1
#                     """ GET SECOND TERM """
#                     j = i + 1
#                     while True:
#                         if j == len(self.expression):
#                             break
#                         if self.expression[j] == operator:
#                             break
#                         secondTerm += self.expression[j]
#                         j += 1
#
#                     return (firstTerm, secondTerm)
#         else:
#             otherOperators = getRestricredOperators('-')
#             allOperators = ['+', '-', '*', '/']
#             for i in range(len(self.expression)):
#                 if i == index:
#                     firstTerm, secondTerm = '', ''
#                     """ GET FIRST TERM """
#                     j = i - 1
#                     while self.expression[j] not in otherOperators and j >= 0:
#                         firstTerm += self.expression[j]
#                         if self.expression[j] == '-':
#                             break
#                         j -= 1
#                     firstTerm = reverse(firstTerm)
#                     """ GET SECOND TERM """
#                     j = i + 1
#                     while ((self.expression[j] not in allOperators) or (operation == 'multiply-only')) and self.expression[j] != operator:
#                         secondTerm += self.expression[j]
#                         j += 1
#                         operation = None
#                         if j == len(self.expression):
#                             break
#
#                     return (firstTerm, secondTerm)
#
#     def applyPEMDAS(self):
#         i = 0
#         while i < len(self.expression):
#             # TODO - PARENTHESES, EXPONENTS
#             if self.expression[i] == '*':
#                 allOperators = ['+', '-', '*', '/']
#                 # if i != len(expression)-2:
#                 if getNextOperator(self.expression, i) == '*':
#                     expressionWithOrder = '('
#                     expressionToReplace = ''
#                     """
#                     j IS OUR STATING INDEX, MEANING THE INDEX WHERE WE WILL START APPLYING PEMDAS, SO IT HAS TO BE SET EQUAL
#                     TO THE FIRST NUMBER/CHAR THAT WILL BE INCLUDED IN PARENTHESES.
#                     IN THE EXPRESSION S = '1+936*24*24*5', i WILL BE EQUAL TO 5 AND j SHOULD BE EQUAL TO 2 SINCE S[j] = S[2] = 9
#                     AND WE WILL START APPLYING PEMDAS AT 9: 1+(936*24*24*5)
#                     """
#                     j = i
#                     while self.expression[j - 1] not in allOperators:
#                         j -= 1
#
#                     while True:
#                         if self.expression[j] == '*':
#                             if getNextOperator(self.expression, j) != '*':
#                                 k = j
#                                 while self.expression[k] not in getRestricredOperators('*'):
#                                     expressionWithOrder += self.expression[k]
#                                     expressionToReplace += self.expression[k]
#                                     if k + 1 == len(self.expression):
#                                         break
#                                     k += 1
#                                 break
#                         expressionWithOrder += self.expression[j]
#                         expressionToReplace += self.expression[j]
#                         j += 1
#                         if j == len(self.expression):
#                             break
#                     expressionWithOrder += ')'
#
#                     self.expression = self.expression.replace(expressionToReplace, expressionWithOrder)
#                     return self.expression
#
#                 Terms = self.splitExpression(i, '*', operation='arithmetic-multiply-single')
#                 firstTerm, secondTerm = Terms[0], Terms[1]
#                 self.expression = self.expression.replace(f"{firstTerm.replace('-', '')}*{secondTerm}",
#                                                 f"({firstTerm.replace('-', '')}*{secondTerm})")
#                 i += 1
#             i += 1
#         return self.expression
#
#
#     """ DUNDER METHODS """
#
#     def __add__(self, other):
#         if type(other) != arithmeticExpression:
#             return 'Only two expression can be added'
#         try:
#             Result = evaluateArithmetic(f"{self.expression}+{other.expression}")[1]
#         except:
#             return 'Something went wrong'
#
#         return arithmeticExpression(Result)
#
#     def __str__(self):
#         return self.expression
#
#     def __len__(self):
#         return len(self.expression)
#
#     def __contains__(self, item):
#         return item in self.expression




class Monomial:
    def __init__(self, poly_string):
        self.poly_string = poly_string
        self.leading_coefficient = float(self.__getLeadingCoefficient(poly_string))
        self.sign = '+' if (poly_string[0] == '+' or poly_string[0] != '-') else '-'
        self.degree = float(poly_string.split('^')[1]) if '^' in poly_string else 1.0 if 'x' in poly_string else 0


    def getSign(self, other, operation):
        if operation == 'add':
            return '+' if self.leading_coefficient + other.leading_coefficient > 0 else '-'

    def __getLeadingCoefficient(self, poly_string):
        return poly_string[0:indexOf(poly_string, 'x')]

    def __str__(self):
        return self.poly_string

class Polynomial:
    def __init__(self, poly_string):
        self.poly_string = poly_string
        self.leading_coefficient = float(self.removeSign(poly_string)[0])
        self.degree = float(poly_string.split()[0].split('^')[1] if '^' in poly_string else 0)
        self.powers = [float(item.split('^')[1]) if '^' in item else 1.0 for item in poly_string.split()]

    @staticmethod
    def removeSign(poly_string):
        return poly_string.replace('+', '').replace('-', '')

    def Evaluate(self, value):
        return eval(self.poly_string.replace('x', f'*{value}').replace('^', '**'))


    def __add__(self, other):
        newPolynomial = ''

        for P1 in self.poly_string.split():
            likeTerms = False
            P1 = Monomial(P1)
            for P2 in other.poly_string.split():
                P2 = Monomial(P2)
                if P1.degree == P2.degree:
                    likeTerms = True
                    newPolynomial += f"{Monomial.getSign(P1, P2, 'add')}{P1.leading_coefficient + P2.leading_coefficient}x^{P1.degree} "

            if not likeTerms:
                newPolynomial += f"{P1.sign}{abs(P1.leading_coefficient)}x^{P1.degree} "
        newPolynomial = Polynomial(newPolynomial)
        return newPolynomial



    def __str__(self):
        formattedPolyString = ''

        for i, item in enumerate(self.poly_string.split()):
            if i == 0:
                # REMOVE '+' FROM THE BEGINNING OF THE POLYNOMIAL
                if '+' in item:
                    item = item.replace('+', '')
            if floatCanBeTurnedIntoAnInt(str(Monomial(item).leading_coefficient)):
                # TURN THE LEADING COEFFICIENT TO AN INT IF IN THE FORM 'num.0'
                item = f"{item[0] if i != 0 and item[0] != '-' else ''}{int(Monomial(item).leading_coefficient)}x^{Monomial(item).degree}"

            if floatCanBeTurnedIntoAnInt(str(Monomial(item).degree)):
                # TURN THE DEGREE TO AN INT IF IN THE FORM 'num.0'
                item = f"{item[:indexOf(item, '^')]}^{int(Monomial(item).degree)}"
            if Monomial(item).degree == 0:
                # REMOVE 'x^0' FROM TERM
                item = f"{item[:indexOf(item, 'x')]}"

            formattedPolyString += f"{item} "

        return formattedPolyString.rstrip()

def indexOf(iterable, searchFor):
    for i, item in enumerate(iterable):
        if item == searchFor:
            return i
    return None

def floatCanBeTurnedIntoAnInt(floatString):
    """ RETURNS TRUE IF A FLOAT CAN BE TURNED INTO AN INT WITHOUT LOSING DECIMAL PLACES: Example: '12.0' -> True, '14.45' -> False """
    floatString = floatString.split('.')
    return floatString[1] == '0'



def main():
    expression1 = arithmeticExpression('2+4+6+8+10')
    expression2 = arithmeticExpression('1+2*3*4+5')

    print('J' in expression1)



main()