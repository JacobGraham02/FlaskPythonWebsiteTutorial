from website import create_app

app = create_app()
if __name__ == '__main__': # Only if we run (not import) main.py then we run the Flask application. If debug property is equal to True, the web server will re-run (like nodemon)
    # if a change is detected in the source code. 
    app.run(debug=True)