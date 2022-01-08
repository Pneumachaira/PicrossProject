from flask_app.config.mysqlconnection import connectToMySQL #These ones access the database
#from flask_app.models import [other table file]

class Class:
    def __init__(self, data):
        self.one = data["example"]
        self.two = data["example"]

    @classmethod
    def method_name(cls, data_sometimes):
        query = "[PUT PARAMETERS HERE]"
        #use connectToMySQL(database).query_deb(query, data_sometimes)
        return 0