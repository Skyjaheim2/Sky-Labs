import hashlib
from datetime import date, datetime, timedelta, tzinfo

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func


db = SQLAlchemy()

class EST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours = -5)

    def tzname(self, dt):
        return "EST"

    def dst(self, dt):
        return timedelta(0)

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)

	def addUser(self):
		newUser = User(name=self.name, email=self.email, password=hash_password(self.password))

		checkUser = User.query.filter(and_(User.name == self.name, User.password == hash_password(self.password))).all()

		if len(checkUser) != 0:
			return -1 # USER ALREADY EXIST
		else:
			db.session.add(newUser)
			db.session.commit()

class History(db.Model):
	__tablename__ = "history"
	id = db.Column(db.Integer, primary_key=True)
	keyword = db.Column(db.String, nullable=True)
	expression = db.Column(db.String, nullable=False)
	subject = db.Column(db.String, nullable=False)
	date = db.Column(db.Date, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

	now = datetime.now(EST()).date()

	def addHistory(self):
		newHistory = History(keyword=self.keyword, expression=self.expression, subject=self.subject, date=History.now, user_id=self.user_id)
		lastHistory = History.query.filter_by(user_id=self.user_id).all()[-1]
		print(f"New history: {newHistory.expression}")
		print(f"Last History: {lastHistory.expression}")
		print(newHistory.expression == lastHistory.expression)
		if newHistory.expression != lastHistory.expression:
			db.session.add(newHistory)
			db.session.commit()

	

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    if hash_password(password) == hash:
        return True
    return False

