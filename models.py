import hashlib
import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func


db = SQLAlchemy()

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


def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    if hash_password(password) == hash:
        return True
    return False

