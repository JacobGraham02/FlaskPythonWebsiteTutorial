from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__) # A blueprint is a template for generating a section of a web application. Each time you apply the blueprint to a different place in your
# application, a new version of the blueprint's structure will be created.

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('A user associated with this email does not exist', category='error')
        
    # data = request.form
    # print(data)
    # Second argument to render_template passes variables to the template defined in the first argument. 
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if (request.method == 'POST'):
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        passwordFirst = request.form.get('passwordFirst')
        passwordConfirm = request.form.get('passwordConfirm')
        
        user = User.query.filter_by(email=email).first()
        if (user):
            flash('An account associated with this email already exists', category='error')
        
        elif len(email) < 4:
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
            
    return render_template("signup.html", user=current_user)