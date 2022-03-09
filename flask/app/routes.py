from app import app
from flask import render_template, flash, redirect, url_for, request

# from app.form import LoginForm, CAD_Upload_form
import os


@app.route("/error")
def error(description):
    return render_template("error.html", title="error", description=description)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/page1")
def page1():
    return render_template("page1.html", title="page1")

@app.route("/page2")
def page2():
    return render_template("page2.html", title="page2")

@app.route("/page3")
def page3():
    return render_template("page3.html", title="page3")

if __name__ == "__main__":
    app.run(debug=True)
