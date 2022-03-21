from flask import Blueprint, render_template, request

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
            pass
        elif len(firstName) < 2:
            pass
        elif passwordFirst != passwordConfirm:
            pass
        elif len(passwordFirst) < 7:
            pass
        else:
            pass
    return render_template("signup.html")