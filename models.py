from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    "Connects app to database"
    db.app = app
    "Method init_app that initializes app to database"
    db.init_app(app)

# MODELS GO BELOW: DEFINE THE SCHEMA
# We use methods in models because we can write methods to do login/ logout methods. Ways to handle database and python interactions
class Pet(db.Model):
    __tablename__ = "pets"

    "Changes output(What gets printed out) of queries in our console"
    def __repr__(self):
        p = self
        return f"<Pet id = {p.id} name = {p.name} species = {p.species} hunger= {p.hunger}"

    "Syntax for creating a column in SQL. Specifies a SERIAL PRIMARY KEY for that id column"
    id = db.Column( db.Integer, primary_key=True, autoincrement=True )

    "Specifies a name column in the pets table that can have names be: 50 characters long, NOT NULL, and has to be a UNIQUE name"
    name = db.Column( db.String(50), nullable=False, unique=True )

    "Species column, 30 characters long and can be empty"
    species = db.Column( db.String(30), nullable=True )

    "Hunger column, that contains numbers, cannot be empty and is set to a default of 20"
    hunger = db.Column( db.Integer, nullable=False, default=20 )

    "Instance methods for pets"
    def greet(self):
        return f"Hi, I am {self.name} the {self.species}"

    def feed(self, amt=20):
        """Updates hunger based off of amt"""
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)

    "Class methods"
    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species = species).all()

    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger > 20).all()


