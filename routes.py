from main import app
from flask import render_template


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/info")
def info():
    return render_template("info.html")