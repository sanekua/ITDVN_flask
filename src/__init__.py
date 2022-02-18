

import config
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates')
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/greetings', methods=['POST'])
def greetings():
    name = request.form.get('name')
    if not name:
        return {"message":"PLease WENter a value"},400

    return render_template('greetings.html', name=name)

from . import routes
from .database import models2
#from .database.models import movies_actors