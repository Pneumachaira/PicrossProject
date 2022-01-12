from flask_app import app #This one handles all of the routing
from flask import render_template, redirect, request, session

from flask_app.models.puzzle import Puzzle
from flask_app.models.solved import Solved

@app.route("/solved/<int:id>")
def solved(id):
    data = {
        "id": id,
        "puzzle_id": id,
        "user_id": session["user_id"]
    }
    puzzle = Puzzle.get_puzzle_by_id(data)
    Solved.first_time_solved(data)
    return render_template("solved.html", puzzle=puzzle)