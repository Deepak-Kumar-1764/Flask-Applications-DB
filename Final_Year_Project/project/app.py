from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()  # Initialize migrate object

def create_app():
    app = Flask(__name__)
    app.secret_key = "Deepak@Hemant"

    # Configure SQL Alchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Corrected typo
    
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize migrate with app and db
    
    from routes import register_routes
    register_routes(app)

    return app
