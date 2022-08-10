from flask import Flask, render_template

app = Flask("Hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contatos")
def contatos():
    return "Jean Auday"

    


   