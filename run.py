# run.py
# file is used to run the webapp
# file will call create_app from src/__init__.py uppon run
from src import create_app


#Creating the flask application
app = create_app()
app.app_context().push()


#running the app
if __name__ == '__main__':
    app.run(debug=True)
