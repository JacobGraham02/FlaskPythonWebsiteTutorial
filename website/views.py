from flask import Blueprint

views = Blueprint('views', __name__) # A blueprint is a template for generating a section of a web application. Each time you apply the blueprint to a different place in your
# application, a new version of the blueprint's structure will be created.

@views.route('/') # Defining the route for the index endpoint
def home():
    return "<h1>Test</h1>"