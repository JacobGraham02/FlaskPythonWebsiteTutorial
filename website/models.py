# Importing an object {db} from the current package (current folder)
from . import db
# UserMixin is a module that can be used by our user objects to give properties specific to flask logins. Is inherited by user objects
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    # Foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# UserMixin allows Flask to use information about currently logged in user
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    
    # Completing the foreign key relationship with the Note class.
    notes = db.relationship('Note')


