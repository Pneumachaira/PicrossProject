from flask_app import app
from flask_app.controllers import likes, puzzles, solveds, users

if __name__ == "__main__":
	app.run(debug=True)