from flask import Flask

app = Flask("Hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contatos")
def contatos():
    return "Jean Auday"

    """<html>

        <head> 
            <title> Contatos </title>
        </head>

        <body>
            <p><h3> Jean Auday</p>
        </body>


    </html>"""