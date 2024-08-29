from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=False, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    data_tables = relationship('Data_Table', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Data_Table(db.Model):
    __tablename__ = 'data_table'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), db.ForeignKey('user.username'), nullable=False)
    stored_data = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
   

    # Define the relationship
    user = relationship('User', back_populates='data_tables')
