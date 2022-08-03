from flask import flask

app = flask("Hello World")

@app.route("/")
def hello():
    return "Hello World"