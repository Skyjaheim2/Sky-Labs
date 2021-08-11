import os
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

from Methods import *


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve/<string:liveSolve>", methods=["POST"])
def solve(liveSolve):
    userInput = request.form.get('userInput')
    print(f'Before parse: {userInput}')
    userInput = parseLatex(userInput)
    print(f'After parse: {userInput}')

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





if __name__ == '__main__':
    app.run(debug=True)