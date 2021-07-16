"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



@app.route('/')
def load_homepage():
    """Loads homepage that shows pet list and availability"""

    pets = Pet.query.all()

    return render_template(
        "home.html",
        pets=pets
    )
    
@app.route('/add', methods=["GET", "POST"])
def show_add_pet_form():
    """Add pet form; handle adding."""
    
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        flash(f'Added {name} as pet!')
        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def display_edit_pet_form(pet_id):
    """Displays information about the pet with option to make edits to the pet."""
    
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        flash(f'Edit to {pet.name} saved!')
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)
    