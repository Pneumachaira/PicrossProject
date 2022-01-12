from flask_app import app #This one handles all of the routing
from flask import render_template, redirect, request, session

from flask_app.models.like import Like

@app.route("/like/<int:id>/<int:creator>")
def like(id, creator):
    data = {
        "puzzle_id": id,
        "creator_id": creator,
        "user_id": session["user_id"]
    }
    Like.first_time_liked(data)
    return redirect("/")