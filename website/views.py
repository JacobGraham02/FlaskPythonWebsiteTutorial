from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__) # A blueprint is a template for generating a section of a web application. Each time you apply the blueprint to a different place in your
# application, a new version of the blueprint's structure will be created.

@views.route('/') # Defining the route for the index endpoint
@login_required
def home():
    return render_template("home.html", user=current_user) # Reference the currently logged in user in the home.html template. 