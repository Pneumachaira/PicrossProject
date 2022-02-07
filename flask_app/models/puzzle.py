from flask_app.config.mysqlconnection import connectToMySQL #These ones access the database
from flask_app.models import user

class Puzzle:
    def __init__(self, data):
        self.id = data["id"],
        self.grid = data["grid"],
        self.name = data["name"],
        self.value = data["value"],
        self.created_at = data["created_at"],
        self.updated_at = data["updated_at"],
        self.user_id = data["user_id"]
        self.columns = [[0],[0],[0],[0],[0]]
        self.rows = [[0],[0],[0],[0],[0]]
        self.likes = data["likes"]

    @classmethod
    def get_all_puzzles(cls):
        query = "SELECT * FROM puzzles JOIN users ON user_id = users.id"
        puzzles_db = connectToMySQL("picross_schema").query_db(query)
        puzzle_list = []
        for each in puzzles_db:
            puzzle_instance = Puzzle(each)
            puzzle_instance.creator = user.User(each)
            puzzle_list.append(puzzle_instance)
        return puzzle_list

    @classmethod
    def get_all_puzzles_alphabet(cls):
        query = "SELECT * FROM puzzles JOIN users ON user_id = users.id ORDER BY name ASC"
        puzzles_db = connectToMySQL("picross_schema").query_db(query)
        puzzle_list = []
        for each in puzzles_db:
            puzzle_instance = Puzzle(each)
            puzzle_instance.creator = user.User(each)
            puzzle_list.append(puzzle_instance)
        return puzzle_list

    @classmethod
    def get_recent_puzzles(cls):
        query = "SELECT * FROM puzzles JOIN users ON user_id = users.id ORDER BY puzzles.id DESC LIMIT 10"
        puzzles_db = connectToMySQL("picross_schema").query_db(query)
        puzzle_list = []
        for each in puzzles_db:
            puzzle_instance = Puzzle(each)
            puzzle_instance.creator = user.User(each)
            puzzle_list.append(puzzle_instance)
        return puzzle_list

    @classmethod
    def get_puzzle_by_id(cls,data):
        query = "SELECT * FROM puzzles WHERE id = %(id)s"
        puzzle_db = connectToMySQL("picross_schema").query_db(query,data)
        if len(puzzle_db) < 1:
            return False
        puzzle = Puzzle(puzzle_db[0])
        return puzzle

    @classmethod
    def add_puzzle(cls,data):
        query = "INSERT INTO puzzles (grid, name, value, user_id) VALUES (%(grid)s, %(name)s, %(value)s, %(user_id)s)"
        return connectToMySQL("picross_schema").query_db(query,data)

    @classmethod
    def top_puzzles(cls):
        query = "SELECT * FROM puzzles ORDER BY likes DESC LIMIT 3"
        return connectToMySQL("picross_schema").query_db(query)

    @classmethod
    def get_puzzles_by_creator(cls,data):
        query = "SELECT * FROM puzzles WHERE user_id = %(user_id)s"
        return connectToMySQL("picross_schema").query_db(query,data)