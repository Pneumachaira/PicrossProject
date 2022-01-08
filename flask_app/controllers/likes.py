from flask_app import app #This one handles all of the routing
from flask import render_template, redirect, request, session

@app.route("/21323")
def index2():
    return render_template("index.html")