from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__) # A blueprint is a template for generating a section of a web application. Each time you apply the blueprint to a different place in your
# application, a new version of the blueprint's structure will be created.

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    data = request.form
    print(data)
    # Second argument to render_template passes variables to the template defined in the first argument. 
    return render_template("login.html", text="Testing", user="Jacob")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if (request.method == 'POST'):
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        passwordFirst = request.form.get('passwordFirst')
        passwordConfirm = request.form.get('passwordConfirm')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters', category='error')
        elif passwordFirst != passwordConfirm:
            flash('Your passwords do not match', category='error')
        elif len(passwordFirst) < 7:
            flash('Your password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(passwordFirst, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            
            flash('Your account was successfully created', category='success')
            
            return redirect(url_for('views.home')) # Redirect to the url that is associated with the blueprint's function name
            
    return render_template("signup.html")