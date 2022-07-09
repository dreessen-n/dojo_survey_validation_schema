# models.dojo
# Import mysqlconnection config
from flask_app.config.mysqlconnection import connectToMySQL
# Import the flash 
from flask import flash

"""
Import other models files for access to classes.
We import the file rather than the class to avoid circular import
Example: from flask_app.models import ninja 
"""

class Dojo:
    def __init__(self,data):
        """Define a Dojo"""
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_dojo(cls,data):
        """Add dojo to the db"""
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL('dojo_survey_validation_schema').query_db(query,data)

    @classmethod
    def display_dojo(cls, data):
        """Display the Dojo info"""
        query = "SELECT * FROM dojos WHERE id = %(dojo.id)s;"
        results = connectToMySQL('dojo_survey_validation_schema').query_db(query,data)
        return cls(results[0])
        
    @staticmethod
    def validate_dojo(dojo):
        """Validate the add a dojo form"""
        is_valid = True # We assume this is true
        if len(dojo['name']) < 3:
            flash("The Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("The Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['language']) < 3:
            flash("The Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("The Comment must be at least 3 characters.")
            is_valid = False
        return is_valid
