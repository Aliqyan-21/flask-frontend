from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<h1>Hello, World!</h1>"
    return render_template("base.html")
