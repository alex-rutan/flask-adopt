"""Seed file to make sample data for Users and Posts"""

from models import Pet
from app import app, db

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add users
spike = Pet(name='Spike', species='porcupine', photo_url='', age='baby')
odin = Pet(name='Odin', species='dog', photo_url='', age='young')
bob = Pet(name='Bob', species='bob', photo_url='', age='adult')

# Add new user objects to session, so they'll persist
db.session.add(spike)
db.session.add(odin)
db.session.add(bob)

# Commit--otherwise, this never gets saved!
db.session.commit()