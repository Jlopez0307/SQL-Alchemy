from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    "Connects app to database"
    db.app = app
    "Method init_app that initializes app to database"
    db.init_app(app)

# MODELS GO BELOW: DEFINE THE SCHEMA
class Pet(db.Model):
    __tablename__ = "pets"

    "Syntax for creating a column in SQL. Specifies a SERIAL PRIMARY KEY for that id column"
    id = db.Column( db.Integer, primary_key=True, autoincrement=True )

    "Specifies a name column in the pets table that can have names be: 50 characters long, NOT NULL, and has to be a UNIQUE name"
    name = db.Column( db.String(50), nullable=False, unique=True )

    "Species column, 30 characters long and can be empty"
    species = db.Column( db.String(30), nullable=True )

    "Hunger column, that contains numbers, cannot be empty and is set to a default of 20"
    hunger = db.Column( db.Integer, nullable=False, default=20 )


