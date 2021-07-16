"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_URL = 'https://image.shutterstock.com/image-vector/no-image-available-vector-hand-260nw-745639717.jpg'

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Makes instance of Pet"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    
    name = db.Column(db.TEXT,
                    nullable=False)

    species = db.Column(db.TEXT,
                        nullable=False)

    photo_url =  db.Column(db.TEXT,
                            nullable=False,
                            default=DEFAULT_URL)

    age = db.Column(db.TEXT,
                    nullable=False)

    notes = db.Column(db.TEXT)

    available = db.Column(db.Boolean,
                            default=True) 