import os
from flask import Flask, render_template, request, redirect, jsonify
import json

app = Flask(__name__)

from Methods import evaluateArithmetic, parseLatex, latexify
from methodsDiscreteMath import solveDiscreteMath
from calculusMethods import solveCalculus
from test import simplifyExpression, Expression



@app.route("/")
def index():
    return render_template("index.html")



@app.route("/algebra")
def algebra():
    return render_template("algebra.html")

@app.route("/discrete_math")
def discreteMath():
    return render_template("discrete_math.html")

@app.route("/calculus")
def calculus():
    return render_template('calculus.html')

@app.route("/probability")
def probability():
    return render_template('probability.html')

@app.route("/physics")
def physics():
    return render_template('physics.html')

@app.route("/solve/<string:liveSolve>", methods=["POST"])
def solve(liveSolve):
    userInput = request.form.get('userInput')
    subjectAndTopic = json.loads(request.form.get('subjectAndTopic'))

    print(f"Subject And Topic: {subjectAndTopic}")
    print(f'Before parse: {userInput}')
    userInput = parseLatex(userInput)
    print(f'After parse: {userInput}')

    if subjectAndTopic['subject'] == 'algebra':
        try:
            Simplification = evaluateArithmetic(userInput)
        except:
            return "Unable To Solve"

        Steps, result, stepCounter = Simplification[0], Simplification[1], Simplification[2]

        if liveSolve == 'true':
            return result

        if Steps != -1:

            # CONVERT ALL STEPS TO LATEX
            for stepNum in Steps:
                Steps.update({stepNum: {'step': latexify(Steps[stepNum]["step"]),
                                        'simplification': latexify(Steps[stepNum]["simplification"])}})

            Steps.update({stepCounter + 1: f'{latexify(userInput)} = {result}'})
            return jsonify(Steps)
        else:
            return 'Unable To Solve'


    if subjectAndTopic['subject'] == 'discreteMath':
        Solution = solveDiscreteMath(subjectAndTopic['selectedTopic'], userInput)
    if subjectAndTopic['subject'] == 'calculus':
        # Solution = solveCalculus(subjectAndTopic['selectedTopic'], userInput)
        # Solution = evaluateArithmetic(userInput)
        userInput = Expression(userInput)
        Solution = simplifyExpression(userInput)
        return jsonify(Solution)









if __name__ == '__main__':
    app.run(debug=True)