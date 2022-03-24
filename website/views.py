from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__) # A blueprint is a template for generating a section of a web application. Each time you apply the blueprint to a different place in your
# application, a new version of the blueprint's structure will be created.

@views.route('/', methods=['GET', 'POST']) # Defining the route for the index endpoint
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash("Your note must be  greater than 1 character", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Your note was added", category='success')
    return render_template("home.html", user=current_user) # Reference the currently logged in user in the home.html template. 