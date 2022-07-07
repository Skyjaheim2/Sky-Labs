# class ArithmeticExpression:
#     def __init__(self, expression):
#         self.expression = expression
#
#     """ INSTANCE METHODS """
#
#     def getOperationToPerform(self):
#         allOperations = self.getAllOperations()
#
#         if len(allOperations) == 0 and self.isSingleExpression():
#             return 'no-operation'
#         if 'frac' in self.expression:
#             return 'fraction-arithmetic'
#
#         if 'sqrt' in self.expression:
#             isRadicalOnly = True
#             seenTerms = set()
#             for term in self.expression:
#                 if term not in 'sqrt':
#                     seenTerms.add(term)
#                 if term == '}':
#                     seenTerms.clear()
#                 if term in ['+', '-', '*', '/'] and '{' not in seenTerms:
#                     isRadicalOnly = False
#
#             if isRadicalOnly:
#                 return 'radical'
#             else:
#                 return 'general-arithmetic'
#
#         if '^' in self.expression:
#             operationsInfo = self.getOperationsOnExponent(returnWithCounter=True)
#             operationsOnExponent = operationsInfo[0]
#             operationsCounter = operationsInfo[1]
#
#             if operationsOnExponent != 'no-operation':
#                 """ IF THE ONLY OPERATION IS MULTIPLICATION THEN WE WANT TO RETURN THAT AS A SEPARATE OPERATION SO WE CAN APPLY THE EXPONENT RULE FOR PRODUCTS """
#                 if operationsOnExponent == {'*'} and operationsCounter > 1:
#
#                     allExponentsInExpression = self.getAllExponentsInExpression()
#                     baseToCheckFor = Exponential(allExponentsInExpression[0]).base
#
#                     baseMatched = True
#                     for expression in allExponentsInExpression:
#                         expression = Exponential(expression)
#                         if expression.base != baseToCheckFor:
#                             baseMatched = False
#
#                     if baseMatched:
#                         pass
#
#                         return 'arithmetic-exponent-multiply'
#
#             exponentIndex = indexOf(str(self.expression), '^')
#             exponentData = self.splitExpression(exponentIndex, '^', binarySplit=False)
#
#             base = ArithmeticExpression(exponentData[0])
#             exponent = ArithmeticExpression(exponentData[1])
#
#             if '{' in exponent:
#                 # CHECKING TO THE RIGHT OF THE EXPONENT
#                 isSingleExponent = False
#                 exponentEndIndex = indexOf(exponent, '}')
#                 if base.isSingleExpression():
#                     if exponentEndIndex == len(exponent) - 1:
#                         isSingleExponent = True
#                     else:
#                         isSingleExponent = False
#                 else:
#                     expressionToTheLeftOfExponent = ArithmeticExpression(self.expression[:exponentIndex])
#                     if '(' not in expressionToTheLeftOfExponent:
#                         return 'general-arithmetic'
#                     indexWhereExponentEnds = expressionToTheLeftOfExponent.getIndexOfInnerMostParen()
#
#                     if (expressionToTheLeftOfExponent[:indexWhereExponentEnds] == '') and exponentEndIndex == len(
#                             exponent) - 1:
#                         isSingleExponent = True
#
#                 return 'arithmetic-exponent-single' if isSingleExponent else 'general-arithmetic'
#
#             else:
#                 exponentData = self.splitExpression(exponentIndex, '^', binarySplit=False)
#                 base = ArithmeticExpression(exponentData[0])
#                 exponent = ArithmeticExpression(exponentData[1])
#                 if base.isSingleExpression():
#                     if exponent.isSingleExpression():
#                         return 'arithmetic-exponent-single'
#                     else:
#                         return 'general-arithmetic'
#                 else:
#                     # CHECKING TO THE RIGHT OF THE EXPONENT
#                     if not exponent.isSingleExpression():
#                         return 'general-arithmetic'
#                     isSingleExponent = False
#                     # CHECKING TO THE LEFT OF THE EXPONENT
#                     expressionToTheLeftOfExponent = ArithmeticExpression(self.expression[:exponentIndex])
#                     if '(' not in expressionToTheLeftOfExponent:
#                         return 'general-arithmetic'
#                     indexWhereExponentEnds = expressionToTheLeftOfExponent.getIndexOfInnerMostParen()
#
#                     if (expressionToTheLeftOfExponent[:indexWhereExponentEnds] == ''):
#                         isSingleExponent = True
#
#                     return 'arithmetic-exponent-single' if isSingleExponent else 'general-arithmetic'
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
#         expression = expression.replace('(', '').replace(')', '')
#         allPossibleOperations = ['+', '-', '*', '/', '^']
#         allOperationsInExpression = set()
#         for operation in allPossibleOperations:
#             if operation in expression:
#                 allOperationsInExpression.add(operation)
#
#         if 'sqrt' in expression:
#             return False
#
#         if '...e' in expression:
#             if getNumOperation(expression, '+') == 1 or getNumOperation(expression, '-') == 1:
#                 return True
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
#         numOpenParen = self.getNumOpenParen()
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
#             otherOperators = getRestrictedOperators('-')
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
#                     while ((self.expression[j] not in allOperators) or (operation == 'multiply-only')) and (
#                             self.expression[j] != operator and self.expression[j] != '}'):
#                         secondTerm += self.expression[j]
#                         j += 1
#                         operation = None
#                         if j == len(self.expression):
#                             break
#
#                     return (firstTerm, secondTerm)
#
#     def applyPEMDAS(self):
#         newExpression = self.expression
#
#         if 'sqrt' in newExpression:
#             newExpression = wrapRadicalInParen(self.expression)
#             return ArithmeticExpression(newExpression)
#         if '^' in newExpression:
#             newExpression = wrapExponentInParen(self.expression)
#             return ArithmeticExpression(newExpression)
#             # newExpression = self.expression
#
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
#                                 while self.expression[k] not in getRestrictedOperators('*') and self.expression[
#                                     k] != '}':
#                                     """ GET THE NUM AFTER THE LAST '*' """
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
#                     newExpression = newExpression.replace(expressionToReplace, expressionWithOrder)
#                     return ArithmeticExpression(newExpression)
#
#                 Terms = self.splitExpression(i, '*', operation='arithmetic-multiply-single')
#                 firstTerm, secondTerm = Terms[0], Terms[1]
#                 newExpression = newExpression.replace(f"{firstTerm.replace('-', '')}*{secondTerm}",
#                                                       f"({firstTerm.replace('-', '')}*{secondTerm})")
#                 i += 1
#             i += 1
#
#         return ArithmeticExpression(newExpression)
#
#     def applyExponentsToSingleExpressions(self):
#         """
#         RETURNS A COPY OF THE EXPRESSION WITH SINGLE EXPRESSIONS RAISED TO THE FIRST POWER
#         FOR EXAMPLE: 2*3*5^2*3 --> 2^1*3^1*5^2*3^1
#         """
#         numbersInExpression = self.expression.split('*')
#         expressionWithExponents = ''
#         for i in range(len(numbersInExpression)):
#             if '^' not in numbersInExpression[i]:
#                 # THIS CHECK IS TO NOT INCLUDE '*' AT THE END OF THE EXPRESSION. FOR EXAMPLE: 2^2*2^3*
#                 if i != len(numbersInExpression) - 1:
#                     expressionWithExponents += f"{numbersInExpression[i]}^1*"
#                 else:
#                     expressionWithExponents += f"{numbersInExpression[i]}^1"
#             else:
#                 # THIS CHECK IS TO NOT INCLUDE '*' AT THE END OF THE EXPRESSION. FOR EXAMPLE: 2^2*2^{1+2+3}*
#                 if i != len(numbersInExpression) - 1:
#                     expressionWithExponents += f"{numbersInExpression[i]}*"
#                 else:
#                     expressionWithExponents += f"{numbersInExpression[i]}"
#
#         return ArithmeticExpression(expressionWithExponents)
#
#     def getOperationsOnExponent(self, returnWithIndex=False, returnWithCounter=False):
#         """ RETURNS AN ARRAY WITH ALL THE OPERATIONS TO BE PERFORMED IN AN EXPONENTIAL EXPRESSION """
#         expression = self.applyExponentsToSingleExpressions()
#         operationsOnExponentWithIndex = []
#         operationsOnExponent = set()
#         allOperations = ['+', '-', '*', '/']
#         operationCounter = 0
#         for i in range(len(expression)):
#             if expression[i] in allOperations:
#                 if expression[i - 1] == '}' or expression[i - 2] == '^':
#                     operationsOnExponentWithIndex.append({expression[i]: i})
#                     operationsOnExponent.add(expression[i])
#                     operationCounter += 1
#
#         if operationsOnExponent != set():
#             return operationsOnExponentWithIndex if returnWithIndex else (
#                 operationsOnExponent, operationCounter) if returnWithCounter else operationsOnExponent
#         else:
#             return 'no-operation'
#
#     def getAllExponentsInExpression(self):
#         """ RETURNS AN ARRAY OF ALL THE EXPONENTS IN AN EXPRESSION """
#         expression = self.applyExponentsToSingleExpressions()
#         allOperations = ['+', '-', '*', '/', '^']
#         currentExpressionStartIndex = 0
#         allExponentExpressions = []
#         for i in range(len(expression)):
#             if (expression[i] in allOperations and expression[i - 1] == '}') or (
#                     expression[i] == '}' and i == len(expression) - 1) or (
#                     expression[i] in allOperations and expression[i - 2] == '^'):
#                 exponentExpression = expression[currentExpressionStartIndex: i]
#                 if i == len(expression) - 1:
#                     exponentExpression += '}'
#                 allExponentExpressions.append(exponentExpression)
#                 currentExpressionStartIndex = i + 1
#
#         return allExponentExpressions
#
#     def convertOutOfStandardForm(self):
#         if '...e' in self.expression:
#             expressionAsArr = self.expression.split('...e')
#             powerOf10 = expressionAsArr[1]
#             newExpression = f"{float(expressionAsArr[0]) * 10 ** float(powerOf10):.0f}"
#             return ArithmeticExpression(newExpression)
#         return self
#
#     def replace(self, subStringToBeReplace, replacement):
#         return self.expression.replace(subStringToBeReplace, replacement)
#
#     def split(self, char):
#         return self.expression.split(char)
#
#     """ DUNDER METHODS """
#
#     def __add__(self, other):
#         if type(other) != ArithmeticExpression:
#             return 'Only two expression can be added'
#         try:
#             Result = evaluateArithmetic(f"{self.expression}+{other.expression}")[1]
#         except:
#             return 'Something went wrong'
#
#         return ArithmeticExpression(Result)
#
#     def __str__(self):
#         return self.expression
#
#     def __repr__(self):
#         return f"{self.expression}"
#
#     def __len__(self):
#         return len(self.expression)
#
#     def __contains__(self, item):
#         """ 'in' OPERATOR """
#         return item in self.expression
#
#     def __getitem__(self, index):
#         """ [] OPERATOR """
#         return self.expression[index]
#
#     def __eq__(self, other):
#         """ DOUBLE EQUAL TO OPERATOR """
#         return str(self.expression) == str(other)
#
#     def __gt__(self, other):
#         """ GREATER THAN OPERATOR """
#         if type(other) == int or type(other) == float:
#             other = ArithmeticExpression(str(other))
#         if not self.isSingleExpression():
#             raise ValueError('Comparison can only be made when expression is a single expression')
#         if type(other) != ArithmeticExpression and type(other) != int and type(other) != float:
#             raise TypeError(f"'>' not supported between instances of '{type(self.expression)}' and '{other}'")
#
#         return float(self.expression) > float(other.expression)
#
#     def __ge__(self, other):
#         """ GREATER THAN OR EQUAL TO OPERATOR """
#         if type(other) == int or type(other) == float:
#             other = ArithmeticExpression(str(other))
#         if not self.isSingleExpression():
#             raise ValueError('Comparison can only be made when expression is a single expression')
#         if type(other) != ArithmeticExpression and type(other) != int and type(other) != float:
#             raise TypeError(f"'>=' not supported between instances of '{type(self.expression)}' and '{other}'")
#
#         return float(self.expression) >= float(other.expression)
#
#     def __lt__(self, other):
#         """ LESS THAN OPERATOR """
#         if type(other) == int or type(other) == float:
#             other = ArithmeticExpression(str(other))
#         if not self.isSingleExpression():
#             raise ValueError('Comparison can only be made when expression is a single expression')
#         if type(other) != ArithmeticExpression and type(other) != int and type(other) != float:
#             raise TypeError(f"'<' not supported between instances of '{type(self.expression)}' and '{other}'")
#
#         return float(self.expression) < float(other.expression)
#
#     def __le__(self, other):
#         """ LESS THAN OR EQUAL TO OPERATOR """
#         if type(other) == int or type(other) == float:
#             other = ArithmeticExpression(str(other))
#         if not self.isSingleExpression():
#             raise ValueError('Comparison can only be made when expression is a single expression')
#         if type(other) != ArithmeticExpression and type(other) != int and type(other) != float:
#             raise TypeError(f"'<=' not supported between instances of '{type(self.expression)}' and '{other}'")
#
#         return float(self.expression) <= float(other.expression)
class Stack():
    def __init__(self):
        self.items = []

    # ADDS ITEM TO THE TOP OF THE STACK
    def push(self, item):
        self.items.append(item)

    # REMOVES AND RETURNS THE TOP ELEMENT OF THE STACK
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # RETURNS TRUE IF THE STACK IS EMPTY ELSE RETURN FALSE
    def is_empty(self):
        return self.items == []

    # RETURNS THE TOP ELEMENT OF THE STACK
    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def get_stack(self):
        return self.items