import re
from Algebra import Expression, Fraction, Exponential, Radical, Constant, Polynomial, simplifyExpression
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

            limitTerm = term
            term = term[I + 2:-1]
            cpyTerm = term

            isInfiniteLimit = approachVal == 'infty' or approachVal == '-infty'
            isPolynomial = Expression(term).isPolynomial()
            isSingleExpression = len(Expression(term)) == 1

            useDirectSubstitution = True

            if isInfiniteLimit:
                useDirectSubstitution = False
            else:
                pass

            # if (approachVal != 'infty' and approachVal != '-infty') and (not Expression(term).isPolynomial() or len(Expression(term)) == 1):
            if useDirectSubstitution:
                if Constant(term).is_digit or limitingVar not in term:
                    limitStep = createMainStep(r"\text{Apply Limit Law:}\lim_{x\to a}\left[c\right]=c",
                                               latexify(f"{limitTerm}={term}"))
                    Steps.append(limitStep)
                    finalResult += f"{term}"
                else:
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
                    limitingTermSimplification = simplifyExpression(Expression(limitingTerm), specialOperations='limit')

                    limitESteps = []
                    """ CREATE LIMIT STEP """

                    limitStep = createMainStep(r'\text{Plug in the value}\ ' + latexify(f"{limitingVar}={approachVal}"), latexify(f'{cpyTerm}={limitingTerm}'))
                    limitESteps.append(limitStep)
                    """ SIMPLIFICATION STEPS """
                    for step in limitingTermSimplification['steps']:
                        limitESteps.append(step)

                    limitEStepHeading = latexify(f"lim_{'{'}{limitExpression}{'}'}({cpyTerm})") +  f"={limitingTermSimplification['finalResult']}"
                    limitEStep = createExpandableStep(f"{limitEStepHeading}", limitESteps)
                    if limitESteps != []:
                        Steps.append(limitEStep)
                    if limitingTermSimplification['finalResult'] != 'diverges':
                        finalResult += f"{sign}{parseLatex(limitingTermSimplification['finalResult'])}"
                    else:
                        finalResult = 'diverges'
                        break

            else:
                if Constant(term).is_digit or limitingVar not in term:
                    limitStep = createMainStep(r"\text{Apply Limit Law:}\lim_{x\to a}\left[c\right]=c",
                                               latexify(f"{limitTerm}={term}"))
                    Steps.append(limitStep)
                    finalResult += f"{term}"
                elif Expression(term).isPolynomial():
                    if float(Polynomial(term).getLeadingTerm().coefficient) > 0 and int(Polynomial(term).getLeadingTerm().exponent) % 2 == 0:
                        limitStep = createMainStep(r"\text{Apply Infinite Limit Property:}"
                                                   r"\lim_{x\to\pm\infty}\left( ax^{n}+\dots+bx+c \right)=\infty,"
                                                   r"a>0, n\ \text{is even}", latexify(f"lim_{'{'}{limitExpression}{'}'}({cpyTerm})=infty"))

                        Steps.append(limitStep)
                        finalResult += f"{sign}infty"
                    elif float(Polynomial(term).getLeadingTerm().coefficient) > 0 and int(Polynomial(term).getLeadingTerm().exponent) % 2 != 0:
                        limitStep = createMainStep(r"\text{Apply Infinite Limit Property:}"
                                                   r"\lim_{x\to\pm\infty}\left( ax^{n}+\dots+bx+c \right)=\infty,"
                                                   r"a>0, n\ \text{is odd}",
                                                   latexify(f"lim_{'{'}{limitExpression}{'}'}({cpyTerm})=infty"))

                        Steps.append(limitStep)
                        finalResult += f"{sign}infty"
                    elif float(Polynomial(term).getLeadingTerm().coefficient) < 0 and int(Polynomial(term).getLeadingTerm().exponent) % 2 == 0:
                        limitStep = createMainStep(r"\text{Apply Infinite Limit Property:}"
                                                   r"\lim_{x\to\pm\infty}\left( ax^{n}+\dots+bx+c \right)=-\infty,"
                                                   r"a<0, n\ \text{is even}",
                                                   latexify(f"lim_{'{'}{limitExpression}{'}'}({cpyTerm})=-infty"))

                        Steps.append(limitStep)
                        finalResult += f"{sign}-infty"

                    elif float(Polynomial(term).getLeadingTerm().coefficient) < 0 and int(Polynomial(term).getLeadingTerm().exponent) % 2 != 0:
                        limitStep = createMainStep(r"\text{Apply Infinite Limit Property:}"
                                                   r"\lim_{x\to\pm\infty}\left( ax^{n}+\dots+bx+c \right)=-\infty,"
                                                   r"a<0, n\ \text{is odd}",
                                                   latexify(f"lim_{'{'}{limitExpression}{'}'}({cpyTerm})=-infty"))

                        Steps.append(limitStep)
                        finalResult += f"{sign}-infty"

                else:
                    if len(Expression(term)) > 1:
                        """ USE LIMIT SUM LAW """
                        newExpression = ''
                        for term in Expression(term).getTerms():
                            sign = term[0]
                            if (sign != '+' and sign != '-'):
                                sign = '+'
                            if term[0] == '+':
                                term = term[1:]
                            newExpression += f"{sign}lim_{'{'}{limitExpression}{'}'}({term})"

                        if newExpression[0] == '+': newExpression = newExpression[1:]
                        limitLawStep = createMainStep(r"\text{Apply Limit Law:}"
                                                      r"\lim_{x\to a}\left[f(x)\pm g(x)\right]=\lim_{x\to a}f(x)\pm \lim_{x\to a}g(x)", latexify(f"{expression}={newExpression}"))
                        Steps.append(limitLawStep)
                        return evaluateCalculusExpression(Expression(newExpression), keyword, Steps, finalResult)

                    else:
                        if len(Expression(term).getGroupedTerms()['Radicals']) > 0:
                            newExpression = f"{sign}sqrt{'{'}lim_{'{'}{limitExpression}{'}'}({Radical(term).getRadicand()}){'}'}"
                            if newExpression[0] == '+': newExpression = newExpression[1:]
                            limitLawStep = createMainStep(r"\text{Apply Limit Law:}"
                                                          r"\lim_{x\to a}\left[\sqrt{f(x)}\right]=\sqrt{\lim_{x\to a}\left( f(x) \right)}",
                                                          latexify(f"{limitTerm}={newExpression}"))
                            Steps.append(limitLawStep)
                            newExpression = Radical(newExpression)
                            limitToEvaluate = newExpression.getRadicand()
                            limitSolution = evaluateCalculusExpression(limitToEvaluate)
                            for step in limitSolution['steps']:
                                if step['type'] == 'main-step':
                                    Steps.append(step)
                                elif step['type'] == 'e-step':
                                    for e_step in step['e-steps']:
                                        Steps.append(e_step)

                            newExpression = Expression(f"sqrt{'{'}{parseLatex(limitSolution['finalResult'])}{'}'}")
                            combineResultsStep = createMainStep(r"\text{Combine Results}", latexify(f"{limitTerm}={newExpression}"))
                            Steps.append(combineResultsStep)
                            return evaluateCalculusExpression(newExpression, Steps=Steps, finalResult=finalResult)

                        elif len(Expression(term).getGroupedTerms()['Exponential']) > 0:
                            term = Exponential(term)
                            newExpression = f"{sign}{term.base}^{'{'}lim_{'{'}{limitExpression}{'}'}({term.exponent}){'}'}"
                            if newExpression[0] == '+': newExpression = newExpression[1:]
                            limitLawStep = createMainStep(r"\text{Apply Limit Law:}"
                                                          r"\lim_{x\to a}\left[f(x)\right]^b=\left[ \lim_{x\to a}\left( f(x) \right) \right]^b",
                                                          latexify(f"{limitTerm}={newExpression}"))
                            Steps.append(limitLawStep)
                            newExpression = Exponential(newExpression)
                            limitToEvaluate = Expression(newExpression.exponent)
                            limitSolution = evaluateCalculusExpression(limitToEvaluate)
                            for step in limitSolution['steps']:
                                if step['type'] == 'main-step':
                                    Steps.append(step)
                                elif step['type'] == 'e-step':
                                    for e_step in step['e-steps']:
                                        Steps.append(e_step)


                            newExpression = Expression(f"{term.base}^{'{'}{parseLatex(limitSolution['finalResult'])}{'}'}")

                            combineResultsStep = createMainStep(r"\text{Combine Results}",
                                                                latexify(f"{limitTerm}={newExpression}"))
                            Steps.append(combineResultsStep)
                            return evaluateCalculusExpression(newExpression, Steps=Steps, finalResult=finalResult)

                        elif len(Expression(term).getGroupedTerms()['Fractions']) > 0:
                            newExpression = f"{sign}frac{'{'}lim_{'{'}{limitExpression}{'}'}({Fraction(term).numerator}){'}'}{'{'}lim_{'{'}{limitExpression}{'}'}({Fraction(term).denominator}){'}'}"
                            if newExpression[0] == '+': newExpression = newExpression[1:]
                            limitLawStep = createMainStep(r"\text{Apply Limit Law:}"
                                                          r"\lim_{x\to a}\left[\cfrac{f(x)}{g(x)}\right]="
                                                          r"\cfrac{\lim_{x\to a}f(x)}{\lim_{x\to a}g(x)}",
                                                          latexify(f"{limitTerm}={newExpression}"))
                            Steps.append(limitLawStep)
                            newExpression = Fraction(newExpression)
                            numeratorLimitToEvaluate   = newExpression.numerator
                            denominatorLimitToEvaluate = newExpression.denominator

                            numeratorLimitSolution   = evaluateCalculusExpression(Expression(numeratorLimitToEvaluate))
                            denominatorLimitSolution = evaluateCalculusExpression(Expression(denominatorLimitToEvaluate))

                            """ CREATE E-STEPS FOR NUMERATOR AND DENOMINATOR """
                            numeratorEStep = createExpandableStep(
                                latexify(f"{numeratorLimitToEvaluate}={parseLatex(numeratorLimitSolution['finalResult'])}"),
                                numeratorLimitSolution['steps'])

                            denominatorEStep = createExpandableStep(
                                latexify(f"{denominatorLimitToEvaluate}={parseLatex(denominatorLimitSolution['finalResult'])}"),
                                denominatorLimitSolution['steps'])

                            """ ADD STEPS """
                            Steps.append(numeratorEStep)
                            Steps.append(denominatorEStep)

                            """ COMBINE STEP"""
                            newExpression = Expression(f"frac{'{'}{parseLatex(numeratorLimitSolution['finalResult'])}{'}'}{'{'}{parseLatex(denominatorLimitSolution['finalResult'])}{'}'}")
                            combineResultsStep = createMainStep(r"\text{Combine Results}",
                                                                latexify(f"{limitTerm}={newExpression}"))
                            Steps.append(combineResultsStep)
                            return evaluateCalculusExpression(newExpression, Steps=Steps, finalResult=finalResult)

        else:
            finalResult += f"{sign}{term}"

    if finalResult[0] == '+': finalResult = finalResult[1:]

    """ SIMPLIFY FINAL RESULT """
    if keyword is None:
        testExpression = Expression(finalResult)
        if len(testExpression) > 1 and len(testExpression.getGroupedTerms()['Fractions']) > 0:
            keyword = 'combine'
    finalResultSimplification = simplifyExpression(Expression(finalResult), keyword=keyword, specialOperations='limit')
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

    E = Expression('lim_{x→infty}(frac{3t^{2}+5t+2}{sqrt{x^{2}+2x+1}})')
    E = Expression('lim_{x→infty}(e^{-t}cos(3t-frac{pi}{2}))')
    E = Expression('lim_{x→infty}(frac{e^{-t}cos(pi+3t)}{sqrt{x^{2}+5x+3}})')
    print(evaluateCalculusExpression(E))

if __name__ == '__main__':
    main()