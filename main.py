from flask import flask
from flask_ask import Ask, statement


app = Flask(__name__)
ask = Ask(app,'/')

@ask.intent("HelloIntent")
def hello():
    return statement('Hello from Flask-Ask Zappa and BBrae')

