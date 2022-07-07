import os
import json
import hashlib
import datetime
import re

from flask import Flask, session, render_template, request, redirect, jsonify
from flask_session import Session
from dotenv import load_dotenv

from sqlalchemy import and_
from models import *


from datetime import date, timedelta, tzinfo, datetime
from pytz import timezone
from math import inf
from random import randint

# Check for environment variables
load_dotenv()
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


app = Flask(__name__)
app.config['TESTING'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SESSION_PERMANENT'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
# The maximum number of items the session stores
# before it starts deleting some, default 500
app.config['SESSION_FILE_THRESHOLD'] = 500
db.init_app(app)

# ENABLE SESSION
Session(app)

from Algebra import (parseLatex, latexify, simplifyExpression, Expression, reverseList, isMatch, solveEquation,
                     Equation)
from methodsDiscreteMath import solveDiscreteMath
from calculusMethods import solveCalculus


@app.route("/")
def index():
    return redirect("/algebra")

@app.route("/history")
def history():
    if 'user_id' in session:
        return render_template("history.html")
    else:
        return redirect("/")
    

@app.route("/loginUser/<string:userName>/<string:userPassword>", methods=['POST', 'GET'])
def loginUser(userName, userPassword):
    checkUser = User.query.filter(and_(User.name == userName, User.password == hash_password(userPassword))).all()

    if len(checkUser) != 0:
        session['user_id'] = checkUser[0].id
        session['logged_in'] = True
        return "Logged In"

    else:
        if request.method == 'GET':
            return "Signed Up"
        return "Invalid Credentials"


@app.route("/signUpUser/<string:userName>/<string:userEmail>/<string:userPassword>", methods=['POST'])
def signUpUser(userName, userEmail, userPassword):
    newUser = User(name=userName, email=userEmail, password=userPassword)
    if newUser.addUser() == -1:
        return "User already signed up"
    else:
        session['user_id'] = User.query.all()[-1].id
        session['logged_in'] = True
        return redirect(f"/loginUser/{userEmail}/{userPassword}")


@app.route("/signOut", methods=['POST'])
def signOut():
    session.clear()
    return "Signed Out"

@app.route("/checkIfUserIsStillLoggedIn", methods=['GET'])
def checkIfUserIsStillLoggedIn():
    return json.dumps(True) if 'logged_in' in session else json.dumps(False)

@app.route("/isTesting", methods=['GET'])
def isTesting():
    return json.dumps(app.config['TESTING'])


@app.route("/getUserHistory", methods=['GET'])
def getUserHistory():
    history = History.query.filter_by(user_id=session['user_id']).all()
    historyDictToReturn = {}

    seenDates = set()
    for item in history:
        f_date = item.date.strftime("%B %d, %Y")
        if f_date not in seenDates:
            seenDates.add(f_date)
            historyDictToReturn.update({f_date: [{
                'id': item.id,
                'keyword': item.keyword,
                'expression': item.expression,
                'subject': item.subject,
            }]})
        else:
            historyDictToReturn[f_date].append({
                'id': item.id,
                'keyword': item.keyword,
                'expression': item.expression,
                'subject': item.subject,
            })

    # REVERSE THE LISTS IN historyDictToReturn SO THAT IT DISPLAYS FROM NEWEST TO OLDEST WHEN TRAVERSED
    for item in historyDictToReturn:
        historyDictToReturn[item] = reverseList(historyDictToReturn[item])

    return json.dumps(historyDictToReturn)

@app.route("/deleteHistory/<string:historyItemID>", methods=['POST'])
def deleteHistory(historyItemID):
    history = History.query.get(historyItemID)
    if history != None:
        db.session.delete(history)
        db.session.commit()
        return "history deleted"
    else:
        return "history not found"

@app.route("/changelog")
def changelog():
    return render_template("changelog.html")

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

@app.route("/solve/<string:requestFromHistory>/<string:liveSolve>", methods=["POST"])
def solve(requestFromHistory, liveSolve):
    requestFromHistory, liveSolve = json.loads(requestFromHistory), json.loads(liveSolve)
    userInput = request.form.get('userInput')
    subjectAndTopic = json.loads(request.form.get('subjectAndTopic'))

    print(subjectAndTopic)

    keyword = None
    allKeywords = ['simplify', 'combine', 'graph', 'expand']

    inputsItems = userInput.split(' ')
    if inputsItems[0].replace('\\', '') in allKeywords:
        keyword = inputsItems[0].replace('\\', '')
        userInput = ''
        for item in inputsItems[1:]:
            userInput += item

    # ADD HISTORY
    if 'user_id' in session and requestFromHistory == False:
        fixedUserInput = latexify(parseLatex(userInput))  # REPLACES /cdotx with /cdot x
        history = History(keyword=keyword, expression=fixedUserInput, subject=subjectAndTopic['subject'],
                          user_id=session['user_id'])
        history.addHistory()

    # GRAPH A FUNCTION
    functionPattern = re.compile("^\w{1}\(\w{1}\)=")
    functionMatches = functionPattern.findall(parseLatex(userInput))

    if len(functionMatches) > 0 or keyword == 'graph':
        # TODO : functionProperties = getFunctionProperties(parseLatex(userInput))
        if keyword == 'graph':
            if '=' in userInput:
                functionName = userInput.split('=')[0]
                functionBody = userInput.split('=')[1]
                functionToGraph = f"{functionName}={functionBody}"
            else:
                functionToGraph = f"y={userInput}"
        else:
            functionToGraph = userInput

        functionToGraph = latexify(parseLatex(functionToGraph)) # FIX LATEX ERROR: \pix NOW GETS RETURNED AS \pi x
        # print(functionToGraph)
        return jsonify({'message': 'graph', 'content': {
            'functionToGraph': functionToGraph,
            'functionProperties': None
        }})

    if app.config['TESTING']:
        print(f"Subject And Topic: {subjectAndTopic}")
        print(f"Keyword: {keyword}")
        print(f'Before parse: {userInput}')
    print(f'After parse: {parseLatex(userInput)}')

    userInput = parseLatex(userInput)
    if subjectAndTopic['subject'] == 'algebra':

        if not app.config['TESTING'] or liveSolve == True:
            try:
                if '=' not in userInput:
                    userInput = Expression(userInput)
                    Solution = simplifyExpression(userInput, keyword=keyword)
                else:
                    userInput = Equation(userInput)
                    Solution = solveEquation(userInput)
                return jsonify({'message': 'solved', 'content': Solution})
            except:
                return jsonify({'message': 'unable to solve', 'content': None})
        else:
            Solution = simplifyExpression(userInput, keyword=keyword)
            return jsonify({'message': 'solved', 'content': Solution})


    if subjectAndTopic['subject'] == 'discreteMath':
        Solution = solveDiscreteMath(subjectAndTopic['selectedTopic'], userInput)
    if subjectAndTopic['subject'] == 'calculus':
        userInput = Expression(userInput)
        Solution = simplifyExpression(userInput)
        return jsonify({'message': 'solved', 'content': Solution})

@app.route("/getSuggestions", methods=["POST"])
def getSuggestions():
    enteredMath = request.form.get('enteredMath')
    allExamples = json.loads(request.form.get('allExamples'))

    json.loads(checkIfUserIsStillLoggedIn())

    allSuggestions = []
    # ADD SUGGESTIONS FROM EXAMPLES
    for example in allExamples:
        # fractionMatch = False
        # if Expression(enteredMath).isSingleExpression() and Expression(example).isSingleExpression():
        #     if enteredMath[1:5] == 'frac' and example[1:5] == 'frac':
        #         enteredMath, checkExp = Fraction(enteredMath), Fraction(example)
        #         if (enteredMath.numerator in checkExp.numerator) or (enteredMath.denominator in checkExp.denominator):
        #             fractionMatch = True
        #
        #     enteredMath = str(enteredMath)
        # if enteredMath in example or fractionMatch:
        #     allSuggestions.append(example)
        try:
            if isMatch(enteredMath, example):
                allSuggestions.append(example)
        except:
            pass

    # ADD SUGGESTIONS FROM HISTORY
    if json.loads(checkIfUserIsStillLoggedIn()):
        allHistory = json.loads(getUserHistory())
        for date in allHistory:
            for history in allHistory[date]:
                if history['keyword'] != None:
                    expToCheck = fr"\text{'{'}{history['keyword']}{'}'}\ {history['expression']}"
                else:
                    expToCheck = history['expression']
                try:
                    if isMatch(enteredMath, expToCheck):
                        allSuggestions.append(expToCheck)
                except:
                    pass

    numSuggestionsToReturn = 5
    if len(allSuggestions) > numSuggestionsToReturn:
        n = len(allSuggestions)

        randomSI = randint(0, n - numSuggestionsToReturn)
        randomEI = randomSI + numSuggestionsToReturn

        allSuggestions = allSuggestions[randomSI: randomEI]

    return jsonify(list(set(allSuggestions)))

@app.route("/test")
def test():
    return render_template("test.html")

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    if hash_password(password) == hash:
        return True
    return False





if __name__ == '__main__':
    app.run(debug=True)