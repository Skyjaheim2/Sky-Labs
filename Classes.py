from math import floor
from Methods import isDigit, reverse, getRestrictedOperators, getNextOperator, evaluateArithmetic


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
    pass



main()