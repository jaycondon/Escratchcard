from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'some_secret'

import ESCGProject.views
from ESCGProject.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
