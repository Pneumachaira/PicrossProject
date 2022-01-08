from flask_app import app #This one handles all of the routing
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.controllers import solveds, puzzles, likes
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/loginPage")
def loginPage():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    data = {
        "username": request.form["username"],
        "password": request.form["password"],
        "confirmation": request.form["confirmation"]
    }
    if not User.validate(data):
        return redirect("/loginPage")
    if not User.unique_username(data):
        return redirect("/loginPage")
    data["password"] = bcrypt.generate_password_hash(data["password"])
    User.add_user(data)
    flash("Account created successfully!")
    return redirect("/loginPage")

@app.route("/login", methods=["POST"])
def login():
    data = {
        "username": request.form["username"],
        "password": request.form["password"]
    }
    user_in_db = User.get_user_by_username(data)
    if not user_in_db:
        flash("Invalid Username/Password")
        return redirect("/loginPage")
    if not bcrypt.check_password_hash(user_in_db.password, data["password"]):
        flash("Invalid Username/Password")
        return redirect("/loginPage")
    session["username"] = user_in_db.username
    session["user_id"] = user_in_db.id
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")