# Start the youtube video from 9:10: https://www.youtube.com/watch?v=dam0GPOAvVI&list=LL&index=3
from flask import Flask

def create_app():
    app = Flask(__name__) # represents name of file that was ran when Flask is initialized
    app.config['SECRET_KEY'] = '(nY*AtNuz$KBm6B/FT[w,[79K9h<x3r_}bfgcUz{%/]uS^ne' # Secure session and cookie information for our website. Specifically, this is going to be our secret key. 
    
    from .views import views
    from .auth import auth
    
    # How do you access the blueprint file that is registered in views and auth. Every path that you define for the blueprint must be prefixed by url_prefix. 
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(auth, url_prefix='/')
    
    return app