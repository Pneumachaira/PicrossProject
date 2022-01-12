from flask_app.config.mysqlconnection import connectToMySQL #These ones access the database
#from flask_app.models import [other table file]

class Solved:
    def __init__(self, data):
        self.puzzles_user_id = data["puzzles_user_id"]
        self.puzzle_id = data["puzzle_id"]
        self.user_id = data["user_id"]

    @classmethod
    def first_time_solved(cls,data):
        query = "SELECT * FROM solved WHERE user_id = %(user_id)s AND puzzle_id = %(puzzle_id)s"
        solved_db = connectToMySQL("picross_schema").query_db(query,data)
        if len(solved_db) < 1:
            query = "UPDATE users SET solvepoints = solvepoints + 1 WHERE id = %(user_id)s"
            connectToMySQL("picross_schema").query_db(query,data)
            query = "INSERT INTO solved (user_id, puzzle_id) VALUES (%(user_id)s, %(puzzle_id)s)"
            connectToMySQL("picross_schema").query_db(query,data)