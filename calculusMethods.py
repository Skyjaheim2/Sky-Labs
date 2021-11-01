from math import floor
from Methods import latexify

class Monomial:
    def __init__(self, poly_string):
        self.poly_string = poly_string
        self.leading_coefficient = int(self.__getLeadingCoefficient(poly_string))
        self.sign = '+' if (poly_string[0] == '+' or poly_string[0] != '-') else '-'
        self.degree = int(poly_string.split('^')[1]) if '^' in poly_string else 1 if 'x' in poly_string else 0


    def getSign(self, other, operation):
        if operation == 'add':
            return '+' if self.leading_coefficient + other.leading_coefficient > 0 else '-'

    def __getLeadingCoefficient(self, poly_string):
        if poly_string[0] == 'x':
            return '1'
        if poly_string[0] == '-':
            return '-1'
        return poly_string[0:indexOf(poly_string, 'x')]

    def derivative(self):
        return Monomial(f"{self.leading_coefficient*self.degree}x^{self.degree-1}")

    def __str__(self):
        if self.degree == 0:
            return '0'
        elif self.degree == 1:
            return f'{self.leading_coefficient}x'
        else:
            return self.poly_string

    def __repr__(self):
        return self.__str__()

class Polynomial:
    foo = '5x^3+x^2'
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


def solveCalculus(topicAndExtensions, userInput):
    # topic = topicAndExtensions.split('→')[0]
    # extension = topicAndExtensions.split('→')[1]

    ESteps = [
        {'id': 1, 'type': 'main-step', 'description': r"\text{Apply Sum/Diff Rule:}\ (f \pm g)' = f' \pm g'", 'info': r"\displaystyle \frac{d}{dx}(5x^3+x^2)=\frac{d}{dx}(5x^3)+\frac{d}{dx}(x^2)"},
        {'id': 2, 'type': 'e-step', 'heading': r'\displaystyle \frac{d}{dx}(5x^3)=15x^2', 'e-steps': [
            {'id': 1, 'type': 'main-step', 'description': r"\text{Take the constant out:}\ (n* f)'=n* f'", 'info': r"\displaystyle \frac{d}{dx}(5x^3)=5*\frac{d}{dx}(x^3)", 'conclusion': r'5*\frac{d}{dx}(x^3)'},
            {'id': 2, 'type': 'main-step', 'description': r"\text{Apply the Power Rule}\: (x^n)'=nx^{n-1}", 'info': r"\displaystyle 5*\frac{d}{dx}(x^3)=5*3x^{3-1}", 'conclusion': '5*3x^{3-1}'},
            {'id': 3, 'type': 'main-step', 'description': r"\text{Simplify}", 'info': r"\displaystyle 5*3x^{3-1}=15x^2", 'conclusion': '15x^2'},
            {'id': 4, 'type': 'e-step', 'heading': r'\displaystyle \frac{d}{dx}(x^2)=2x', 'e-steps': [
                {'id': 1, 'type': 'main-step', 'description': r"\displaystyle \text{Apply the Power Rule:}\ (x^n)'=nx^{n-1}", 'info': r"\displaystyle \frac{d}{dx}(x^2)=2x^{2-1}", 'conclusion': r'2x^{2-1}'},
                {'id': 2, 'type': 'main-step', 'description': r"\text{Simplify}", 'info': r"\displaystyle 2x^{2-1}=2x", 'conclusion': '2x'},
                {'id': 3, 'type': 'e-step', 'heading': r'\displaystyle \frac{d}{dx}(x^2)=2x', 'e-steps': [
                    {'id': 1, 'type': 'main-step', 'description': r"\displaystyle \text{Apply the Power Rule:}\ (x^n)'=nx^{n-1}", 'info': r"\displaystyle \frac{d}{dx}(x^2)=2x^{2-1}", 'conclusion': r'2x^{2-1}'},
                    {'id': 2, 'type': 'main-step', 'description': r"\text{Simplify}", 'info': r"\displaystyle 2x^{2-1}=2x", 'conclusion': '2x'}
                ]},
            ]},

        ]},
        {'id': 3, 'type': 'e-step', 'heading': r'\displaystyle \frac{d}{dx}(x^2)=2x', 'e-steps': [
            {'id': 1, 'type': 'main-step', 'description': r"\displaystyle \text{Apply the Power Rule:}\ (x^n)'=nx^{n-1}", 'info': r"\displaystyle \frac{d}{dx}(x^2)=2x^{2-1}", 'conclusion': r'2x^{2-1}'},
            {'id': 2, 'type': 'main-step', 'description': r"\text{Simplify}", 'info': r"\displaystyle 2x^{2-1}=2x", 'conclusion': '2x'}
        ]},
    ]

    Steps = [
        {'id': 1, 'type': 'main-step', 'description': r"\text{Apply Sum/Diff Rule:}\ (f \pm g)' = f' \pm g'", 'info': r"\displaystyle \frac{d}{dx}(5x^3+x^2)=\frac{d}{dx}(5x^3)+\frac{d}{dx}(x^2)"},
        {'id': 2, 'type': 'e-step', 'heading': r'\displaystyle \frac{d}{dx}(5x^3)=15x^2', 'e-steps': [
            {'id': 1, 'type': 'main-step', 'description': r"\text{Take the constant out:}\ (n* f)'=n* f'", 'info': r"\displaystyle \frac{d}{dx}(5x^3)=5*\frac{d}{dx}(x^3)", 'conclusion': r'5*\frac{d}{dx}(x^3)'},
            {'id': 2, 'type': 'main-step', 'description': r"\text{Apply the Power Rule}\: (x^n)'=nx^{n-1}", 'info': r"\displaystyle 5*\frac{d}{dx}(x^3)=5*3x^{3-1}", 'conclusion': '5*3x^{3-1}'},
            {'id': 3, 'type': 'main-step', 'description': r"\text{Simplify}", 'info': r"\displaystyle 5*3x^{3-1}=15x^2", 'conclusion': '15x^2'},
        ]},
        {'id': 3, 'type': 'e-step', 'heading': r'\displaystyle \frac{d}{dx}(x^2)=2x', 'e-steps': [
            {'id': 1, 'type': 'main-step', 'description': r"\displaystyle \text{Apply the Power Rule:}\ (x^n)'=nx^{n-1}", 'info': r"\displaystyle \frac{d}{dx}(x^2)=2x^{2-1}", 'conclusion': r'2x^{2-1}'},
            {'id': 2, 'type': 'main-step', 'description': r"\text{Simplify}", 'info': r"\displaystyle 2x^{2-1}=2x", 'conclusion': '2x'}
        ]},


    ]
    Steps = convertStepsToLatex(Steps)
    finalResult = '15x^2+2x'

    return {'steps': Steps, 'finalResult': finalResult}


def convertStepsToLatex(Steps):
    for step in Steps:
        if step['type'] == 'main-step':
            step['description'] = latexify(step['description'])
            step['info'] = latexify(step['info'])
        elif step['type'] == 'e-step':
            step['heading'] = latexify(step['heading'])
            convertStepsToLatex(step['e-steps'])

    return Steps



def main():
    print(solveCalculus('', r'\frac{d}{dx}(5x^3+x^2)'))




main()