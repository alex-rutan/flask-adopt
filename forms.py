"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class AddPetForm(FlaskForm):
    """Form for adding pets."""
    
    name = StringField("Pet Name")
    
    species = StringField("Species")
    
    photo_url = StringField("Photo URL")
    
    age = StringField("Age")
    
    notes = TextAreaField("Notes")


