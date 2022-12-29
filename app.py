from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet

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
def home_page():
    """Shows home page"""
    return render_template('home.html')