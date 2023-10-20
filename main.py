from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello World! </p>"

@app.route("/quick-start")
def references():
    return render_template("quick_start_blog.html")
