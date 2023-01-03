from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet

"""SQLAlchemy with Flask:Add on product to integrate Flask on SQLAlchemy

    Benefits:
        - Ties SQLAlchemy session with our current Flask session

"""

app = Flask(__name__)

"Specifies we are communicating with postgreSQL and specifies which database to connect to"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Halo03117!@localhost:5432/pet_shop_db'

"Set to False to avoid warning"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"Print all SQL statements to the terminal(Helpful for debugging)"
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)

app.config['SECRET_KEY'] = 'cats'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def list_pets():
    """Shows list of all pets in db"""
    all_pets = Pet.query.all()
    return render_template('list.html', pets=all_pets)

@app.route('/', methods = ["POST"])
def create_pet():
    name = request.form["name"]
    species = request.form["species"]
    hunger = request.form["hunger"]
    hunger = int(hunger) if hunger else None

    new_pet = Pet(name = name, species = species, hunger=hunger)
    db.session.add(new_pet)
    db.session.commit()
    return redirect(f"/{new_pet.id}")

@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """Show details about a single pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('details.html', pet=pet)

@app.route('/species/<species_id>')
def show_pets_by_species(species_id):
    pets = Pet.get_by_species(species_id)
    return render_template("/species.html", pets=pets, species=species_id)