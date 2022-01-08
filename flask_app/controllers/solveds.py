from flask_app import app #This one handles all of the routing
from flask import render_template, redirect, request, session

@app.route("/solved/<int:id>")
def solved(id):
    data = {
        "puzzle_id": id,
        "user_id": session["user_id"]
    }
    return render_template("index.html")