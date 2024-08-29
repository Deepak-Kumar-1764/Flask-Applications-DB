from flask import render_template, request, redirect, session, url_for, flash
from models import User, Data_Table
from app import db

def register_routes(app):
    
    #login page template
    @app.route("/")
    def home():
        return render_template("login.html")
    
    # Login 
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session['username'] = username
                return redirect(url_for('main'))
            else:
                flash('Please enter correct username and password', 'error')
        return render_template("login.html")
    


    # Register
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            user = User.query.filter_by(username=username).first()
            email_user = User.query.filter_by(email=email).first()
            parts = email.split('@')
            
            if parts[1] != "gmail.com":
                flash('Invalid email', 'error')
                return render_template('register.html')
            
            if user:
                flash('Username already exists', 'error')
                return render_template('register.html')
            if email_user:
                flash('Email id already registered', 'error')
                return render_template('register.html')
            if confirm_password != password:
                flash('Both passwords are not the same', 'error')
                return render_template('register.html')
            
            new_user = User(name=name, username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            flash('Registration successful', 'success')
            return render_template('register.html')
        
        return render_template('register.html')
    

    #main page template
    @app.route('/login/store')
    def main():
        return render_template('main.html')
    

    #storing data
    @app.route("/store", methods=["POST", "GET"])
    def store():
        if request.method == "POST":
            stored_data = request.form.get('content')
            if not stored_data or stored_data.strip() == '':
                flash('Please type any text/message in the box', 'error')
                return render_template('main.html', flag=False)
            else:
                username = session.get('username')
                user = User.query.filter_by(username=username).first()
            if not user:
                flash('Please log in to store data', 'error')
                return redirect(url_for('home'))
            else:
                add_new_data = Data_Table(user_name=user.username,stored_data=stored_data)
                db.session.add(add_new_data)
                db.session.commit()
                flash('Data stored successfully!', 'success')
                return redirect(url_for('success'))
        else:
           return render_template("main.html", flag=False)
    

    #successfully Stored
    @app.route('/success')
    def success():
        return render_template('main.html', flag=True)
    
    #logout  
    @app.route('/logout')
    def logout():
        session.pop('username', None) 
 
        return redirect(url_for('login'))

    
