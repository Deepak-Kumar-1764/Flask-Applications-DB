from flask import render_template, request, redirect, session, url_for, flash, jsonify
from models import User, Data_Table, Question
from app import db
import uuid

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
    
    #Go to chat
    # @app.route('/chat')
    # def chat():
    #     return render_template('chat.html')

    @app.route('/chat', methods=['GET', 'POST'])
    def chat():
        # Extract session ID (generate one if it doesn't exist)
        session_id = session.get('session_id')
        if not session_id:
            session_id = str(uuid.uuid4())  # Generate a new UUID
            session['session_id'] = session_id

        if request.method == 'POST':
            question_text = request.form['question']
            fixed_answer = "Working on it."
            new_answer = fixed_answer

            # Check if the question already exists for the current session
            question = Question.query.filter_by(text=question_text).first()
            if not question:
                # Add the new question to the database
                new_question = Question(clint=session.get('username'), text=question_text, answer=fixed_answer, session_id=session_id)
                db.session.add(new_question)
                db.session.commit()
            else:
                # Update the existing question
                question.answer = new_answer
                db.session.commit()
                qa_pair = [question]
                return render_template('chat.html', qa=qa_pair)

        # Retrieve all questions for the current session
        qa_pairs = Question.query.filter_by(session_id=session_id).order_by(Question.id.asc()).all()
        return render_template('chat.html', qa=qa_pairs)
    
    #logout  
    @app.route('/logout')
    def logout():
        session.pop('session_id', None)  # Clear the session ID
        session.pop('username', None) 
        return redirect(url_for('login'))

    
