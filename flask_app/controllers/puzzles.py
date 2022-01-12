from flask_app import app #This one handles all of the routing
from flask import render_template, redirect, request, session, flash
from flask_app.models.puzzle import Puzzle
from flask_app.models.user import User

@app.route("/")
def index():
    puzzles = Puzzle.get_recent_puzzles()
    topScorers = User.top_scorers()
    topCreators = User.top_creators()
    topPuzzles = Puzzle.top_puzzles()
    return render_template("index.html", puzzles = puzzles, topScorers = topScorers, topCreators = topCreators, topPuzzles = topPuzzles)

@app.route("/allPuzzles")
def all_puzzles():
    puzzles = Puzzle.get_all_puzzles()
    return render_template("allPuzzles.html", puzzles = puzzles)

@app.route("/myPuzzles")
def my_puzzles():
    if "username" not in session:
        flash("Must be logged in to view that page")
        return redirect("/loginPage")
    data = {
        "user_id": session["user_id"]
    }
    puzzles = Puzzle.get_puzzles_by_creator(data)
    return render_template("myPuzzles.html", puzzles = puzzles)

@app.route("/puzzle/<int:id>")
def solvePuzzle(id):
    data = {
        "id": id
    }
    puzzle = Puzzle.get_puzzle_by_id(data)
    i = 0
    print(len(puzzle.grid[0]))
    while (i * 5 < len(puzzle.grid[0])-1): #i = 25
        if (puzzle.grid[0][0+i*5] == "0"):
            puzzle.columns[0].append(0)
        else:
            puzzle.columns[0][len(puzzle.columns[0])-1] += 1
        i += 1   
    if len(puzzle.columns[0]) == 6:
        puzzle.columns[0] = [0]
    i = 0
    while (i * 5 < len(puzzle.grid[0])-1): #i = 25
        if (puzzle.grid[0][1+i*5] == "0"):
            puzzle.columns[1].append(0)
        else:
            puzzle.columns[1][len(puzzle.columns[1])-1] += 1
        i += 1   
    if len(puzzle.columns[1]) == 6:
        puzzle.columns[1] = [0]
    i = 0
    while (i * 5 < len(puzzle.grid[0])-1): #i = 25
        if (puzzle.grid[0][2+i*5] == "0"):
            puzzle.columns[2].append(0)
        else:
            puzzle.columns[2][len(puzzle.columns[2])-1] += 1
        i += 1   
    if len(puzzle.columns[2]) == 6:
        puzzle.columns[2] = [0]
    i = 0
    while (i * 5 < len(puzzle.grid[0])-1): #i = 25
        if (puzzle.grid[0][3+i*5] == "0"):
            puzzle.columns[3].append(0)
        else:
            puzzle.columns[3][len(puzzle.columns[3])-1] += 1
        i += 1   
    if len(puzzle.columns[3]) == 6:
        puzzle.columns[3] = [0]
    i = 0
    while (i * 5 < len(puzzle.grid[0])-1): #i = 25
        if (puzzle.grid[0][4+i*5] == "0"):
            puzzle.columns[4].append(0)
        else:
            puzzle.columns[4][len(puzzle.columns[4])-1] += 1
        i += 1
    if len(puzzle.columns[4]) == 6:
        puzzle.columns[4] = [0]
    i = 0
    #Time for the rows!
    while(i * 5 < len(puzzle.grid[0])-1):
        if (puzzle.grid[0][0+i] == "0"): #i = 0
            puzzle.rows[0].append(0)
        else:
            puzzle.rows[0][len(puzzle.rows[0])-1] += 1
        i += 1
    if len(puzzle.rows[0]) == 6:
        puzzle.rows[0] = [0]
    i = 0
    while(i * 5 < len(puzzle.grid[0])-1):
        if (puzzle.grid[0][5+i] == "0"): #i = 0
            puzzle.rows[1].append(0)
        else:
            puzzle.rows[1][len(puzzle.rows[1])-1] += 1
        i += 1
    if len(puzzle.rows[1]) == 6:
        puzzle.rows[1] = [0]
    i = 0
    while(i * 5 < len(puzzle.grid[0])-1):
        if (puzzle.grid[0][10+i] == "0"): #i = 0
            puzzle.rows[2].append(0)
        else:
            puzzle.rows[2][len(puzzle.rows[2])-1] += 1
        i += 1
    if len(puzzle.rows[2]) == 6:
        puzzle.rows[2] = [0]
    i = 0
    while(i * 5 < len(puzzle.grid[0])-1):
        if (puzzle.grid[0][15+i] == "0"): #i = 0
            puzzle.rows[3].append(0)
        else:
            puzzle.rows[3][len(puzzle.rows[3])-1] += 1
        i += 1
    if len(puzzle.rows[3]) == 6:
        puzzle.rows[3] = [0]
    i = 0
    while(i * 5 < len(puzzle.grid[0])-1):
        if (puzzle.grid[0][20+i] == "0"): #i = 0
            puzzle.rows[4].append(0)
        else:
            puzzle.rows[4][len(puzzle.rows[4])-1] += 1
        i += 1
    if len(puzzle.rows[4]) == 6:
        puzzle.rows[4] = [0]
    if puzzle.value[0] == 1:
        return render_template("solve5x5.html", puzzle=puzzle)
    if puzzle.value[0] == 5:
        return render_template("solve10x10.html", puzzle=puzzle)
    if puzzle.value[0] == 10:
        return render_template("solve15x15.html", puzzle=puzzle)

@app.route("/create5x5")
def create5x5():
    if "username" not in session:
        flash("Must be logged in to create a puzzle")
        return redirect("/loginPage")
    return render_template("create5x5.html")

@app.route("/create10x10")
def create10x10():
    if "username" not in session:
        flash("Must be logged in to create a puzzle")
        return redirect("/loginPage")
    return render_template("create10x10.html")

@app.route("/submit5x5", methods=["POST"])
def submit5x5():
    data = [
        request.form["1"], request.form["2"], request.form["3"], request.form["4"], request.form["5"],
        request.form["6"], request.form["7"], request.form["8"], request.form["9"], request.form["10"],
        request.form["11"], request.form["12"], request.form["13"], request.form["14"], request.form["15"],
        request.form["16"], request.form["17"], request.form["18"], request.form["19"], request.form["20"],
        request.form["21"], request.form["22"], request.form["23"], request.form["24"], request.form["25"],
    ]
    aString = ""
    for each in data:
        aString += each
    if aString == "0000000000000000000000000":
        flash("Can't submit an empty picross!")
        return redirect("/create5x5")
    if request.form["name"] == "":
        flash("Must have a title!")
        return redirect("/create5x5")
    data = {
        "name": request.form["name"],
        "grid": aString,
        "value": 1,
        "user_id": session["user_id"]
    }
    Puzzle.add_puzzle(data)
    flash("Puzzle successfully created!")
    return redirect("/")
