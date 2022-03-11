from flask import Blueprint, render_template

auth = Blueprint('auth', __name__) # A blueprint is a template for generating a section of a web application. Each time you apply the blueprint to a different place in your
# application, a new version of the blueprint's structure will be created.



@auth.route('/login') 
def login():
    # Second argument to render_template passes variables to the template defined in the first argument. 
    return render_template("login.html", text="Testing", user="Jacob")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up')
def sign_up():
    return render_template("signup.html")