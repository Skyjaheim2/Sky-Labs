import os
from dotenv import load_dotenv

from flask import Flask, render_template, request
from models import *

# Check for environment variable
load_dotenv()
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# RUN 'python create.py in cmd'

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()