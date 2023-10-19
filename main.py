from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello World! </p>"

@app.route("/references")
def references():
    return render_template("references.html")
