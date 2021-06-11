import os
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

from Methods import *


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solve", methods=["POST"])
def solve():
    userInput = request.form.get('userInput')
    print(f'Before parse: {userInput}')
    userInput = parseLatex(userInput)
    print(f'After parse: {userInput}')

    if '(' in userInput or ')' in userInput:
        Simplification = simplify(userInput)
        # print(Simplification)
        Steps, result, stepCounter = Simplification[0], Simplification[1], Simplification[2]

        if Steps != -1:
            Steps.update({stepCounter+1: f'{userInput} = {result}'})
            # Steps = {
            #     1: 'Hey there'
            # }
            print(Steps)
            for step in Steps:
                Steps.update({step: latexify(Steps[step])})
            return jsonify(Steps)

    return 'Unable To Solve'





if __name__ == '__main__':
    app.run(debug=True)