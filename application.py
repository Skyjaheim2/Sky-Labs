import os
import json
import hashlib
import datetime

from flask import Flask, session, render_template, request, redirect, jsonify
from flask_session import Session
from dotenv import load_dotenv

from sqlalchemy import and_
from models import *


from datetime import date, timedelta, tzinfo, datetime
from pytz import timezone
from math import inf

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

from Methods import parseLatex, latexify, simplifyExpression, Expression, reverseList
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

@app.route("/solve/<string:requestFromHistory>", methods=["POST"])
def solve(requestFromHistory):
    userInput = request.form.get('userInput')
    subjectAndTopic = json.loads(request.form.get('subjectAndTopic'))

    keyword = None
    allKeyWords = ['simplify', 'combine']
    splitInput = userInput.split(' ')
   
    if len(splitInput) > 1:
        keyword = splitInput[0][:-1]
        if keyword in allKeyWords:
            userInput = splitInput[1]
        else:
            keyword = None

    if app.config['TESTING']:
        print(f"Subject And Topic: {subjectAndTopic}")
        print(f"Keyword: {keyword}")
        print(f'Before parse: {userInput}')
        print(f'After parse: {parseLatex(userInput)}')

     # ADD HISTORY
    if 'user_id' in session and requestFromHistory == 'false':
        history = History(keyword=keyword, expression=userInput, subject=subjectAndTopic['subject'], user_id=session['user_id'])
        history.addHistory()

    userInput = parseLatex(userInput)
    if subjectAndTopic['subject'] == 'algebra':
        
        userInput = Expression(userInput)
        if not app.config['TESTING']:
            try:
                Solution = simplifyExpression(userInput, keyword=keyword)
                return jsonify(Solution)
            except:
                return "Unable to solve"
        else:
            Solution = simplifyExpression(userInput, keyword=keyword)
            return jsonify(Solution)


    if subjectAndTopic['subject'] == 'discreteMath':
        Solution = solveDiscreteMath(subjectAndTopic['selectedTopic'], userInput)
    if subjectAndTopic['subject'] == 'calculus':
        userInput = Expression(userInput)
        Solution = simplifyExpression(userInput)
        return jsonify(Solution)


def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    if hash_password(password) == hash:
        return True
    return False





if __name__ == '__main__':
    app.run(debug=True)