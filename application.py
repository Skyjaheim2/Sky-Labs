import os
import json
from flask import Flask, session, render_template, request, redirect, jsonify
from flask_session import Session
from dotenv import load_dotenv

from sqlalchemy import and_
import datetime
from datetime import date, timedelta, tzinfo, datetime
from pytz import timezone
from math import inf


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SESSION_PERMANENT'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
# The maximum number of items the session stores
# before it starts deleting some, default 500
app.config['SESSION_FILE_THRESHOLD'] = 500
# db.init_app(app)

# ENABLE SESSION
Session(app)

from Methods import parseLatex, latexify, simplifyExpression, Expression
from methodsDiscreteMath import solveDiscreteMath
from calculusMethods import solveCalculus


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

    keyword = None
    allKeyWords = ['simplify', 'combine']
    splitInput = userInput.split(' ')
    print(userInput)
    if len(splitInput) > 1:
        keyword = splitInput[0][:-1]
        if keyword in allKeyWords:
            userInput = splitInput[1]
        else:
            keyword = None



    print(f"Subject And Topic: {subjectAndTopic}")
    print(f"Keyword: {keyword}")
    print(f'Before parse: {userInput}')
    userInput = parseLatex(userInput)
    print(f'After parse: {userInput}')

    if subjectAndTopic['subject'] == 'algebra':
        # return ""
        userInput = Expression(userInput)
        Solution = simplifyExpression(userInput, keyword=keyword)
        return jsonify(Solution)

    if subjectAndTopic['subject'] == 'discreteMath':
        Solution = solveDiscreteMath(subjectAndTopic['selectedTopic'], userInput)
    if subjectAndTopic['subject'] == 'calculus':
        userInput = Expression(userInput)
        Solution = simplifyExpression(userInput)
        return jsonify(Solution)









if __name__ == '__main__':
    app.run(debug=True)