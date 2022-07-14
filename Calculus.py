import re
from Algebra import Expression, Fraction, Exponential, Radical, Constant, simplifyExpression
from Methods import latexify, indexOf, createMainStep, createExpandableStep, createGroupedTermsDict, parseLatex


def evaluateCalculusExpression(expression: Expression, keyword=None, Steps=None, groupedTerms=None, recursiveCall=False, finalResult=None):

    if Steps is None: Steps = []
    if finalResult == None: finalResult = ''

    for term in expression.getTerms():
        sign = term[0]
        if (sign != '+' and sign != '-'):
            sign = '+'
        if term[0] == '+':
            term = term[1:]
        if term[0:3] == 'lim' or term[1:4] == 'lim':
            """ EVALUATE LIMIT """
            I = indexOf(term, '}')
            limitExpression = term[5: I]
            limitingVar = limitExpression.split('→')[0]
            approachVal = limitExpression.split('→')[1]

            term = term[I+2:-1]
            cpyTerm = term

            implicitConstantProductPattern = re.compile(f'\d+{limitingVar}')
            implicitConstantProductMatches = implicitConstantProductPattern.findall(term)

            """ REPLACE ALL IMPLICIT PRODUCTS WITH EXPLICIT PRODUCTS: 23x -> 23*x """
            for match in implicitConstantProductMatches:
                termWithExplicitProduct = ''
                for char in match:
                    if Constant(char).is_digit:
                        termWithExplicitProduct += char
                    else:
                        termWithExplicitProduct += f'*{char}'
                term = term.replace(match, termWithExplicitProduct)

            """ GET LIMITING VALUE """
            limitingTerm = term.replace(limitingVar, approachVal)
            limitingTermSimplification = simplifyExpression(Expression(limitingTerm))

            limitESteps = []
            """ CREATE LIMIT STEP """
            limitStep = createMainStep(r'\text{Plug in the value}\ ' + f'{limitingVar}={approachVal}', latexify(f'{cpyTerm}={limitingTerm}'))
            limitESteps.append(limitStep)
            """ SIMPLIFICATION STEPS """
            for step in limitingTermSimplification['steps']:
                limitESteps.append(step)

            limitEStepHeading = latexify(f"lim_{'{'}{limitExpression}{'}'}({cpyTerm})") +  f"={limitingTermSimplification['finalResult']}"
            limitEStep = createExpandableStep(f"{limitEStepHeading}", limitESteps)
            if limitESteps != []:
                Steps.append(limitEStep)

            finalResult += f"{sign}{parseLatex(limitingTermSimplification['finalResult'])}"
        else:
            finalResult += f"{sign}{term}"

    if finalResult[0] == '+': finalResult = finalResult[1:]

    """ SIMPLIFY FINAL RESULT """
    if keyword is None:
        testExpression = Expression(finalResult)
        if len(testExpression) > 1 and len(testExpression.getGroupedTerms()['Fractions']) > 0:
            keyword = 'combine'
    finalResultSimplification = simplifyExpression(Expression(finalResult), keyword=keyword)
    if finalResult != parseLatex(finalResultSimplification['finalResult']):
        """ COMBINE RESULTS STEP """
        combineResultsStep = createMainStep(r'\text{Combine Results}', latexify(finalResult))
        if str(expression) != finalResult:
            Steps.append(combineResultsStep)
        finalResult = finalResultSimplification['finalResult']
    for step in finalResultSimplification['steps']:
        Steps.append(step)


    if len(Steps) == 1 and Steps[0]['type'] == 'e-step':
        return {'steps': Steps[0]['e-steps'], 'finalResult': latexify(finalResult)}

    return {'steps': Steps, 'finalResult': latexify(finalResult)}


def main():
    # E = Expression('lim_{x→3}(x^{2}t+3xt^{2}+t+2x)+2t^{2}+3t+2')
    # E = Expression('lim_{x→2}(frac{x^{2}+23x+1}{x+2})')
    E = Expression('lim_{x→2}(x^{2}+2)+4+lim_{x→3}(x^{3}+3)')
    print(evaluateCalculusExpression(E))

if __name__ == '__main__':
    main()