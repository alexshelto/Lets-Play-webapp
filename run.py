# run.py
# file is used to run the webapp
# file will call create_app from src/__init__.py uppon run
from src import create_app
from src import db

#Creating the flask application
app = create_app()
app.app_context().push()

with app.app_context():
    db.create_all()

#running the app
if __name__ == '__main__':
    app.run(debug=True)
