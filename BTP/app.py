#Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()

#My app
def create_app():
    app = Flask(__name__)
    app.secret_key = "Deepak@Hemant"

    #Configure SQL Alchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATONS"] = False
    
    db.init_app(app)
    from routes import register_routes
    register_routes(app)
    migrate = Migrate(app,db)

    return app
   