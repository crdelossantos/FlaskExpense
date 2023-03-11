from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path




app = Flask(__name__)
path_name=str(Path.cwd())
app.config['SECRET_KEY'] = "JLKJJJO3IURYoiouolnojojouuoo=5y9y9youjuy952oohhbafdnoglhoho"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenseDB.db'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+path_name+"/expenseDB.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


from application import routes