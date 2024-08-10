# Flask To-Do List Application

## Overview

This is a simple To-Do list application built with Flask. It allows users to create, view, edit, and delete tasks. The application uses SQLite as its database and includes styling through SCSS.

## Features

- Add new tasks
- View existing tasks
- Edit tasks
- Delete tasks

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **SQLite**: A lightweight database engine.
- **Flask-SCSS**: A Flask extension for integrating SCSS with Flask applications.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Deepak-Kumar-1764/Flask-Applications-DB.git
   cd Flask-Applications-DB
2. **Create and Activate a Virtual Environment**
  
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Required Packages**
    pip install -r requirements.txt
    Create a requirements.txt file with the following contents:
     Flask==2.1.2
     Flask-SQLAlchemy==2.5.1
     Flask-SCSS==0.2.2

     
4. **Initialize the Database**
    flask shell
 

      
5. **Run the Application**
    flask run
    
The application will be available at http://localhost:5000.

## Application Structure

- **app.py**: Main application file with routes and database models.
- **templates/**: Directory for HTML templates.
  - **index.html**: Template for the home page.
  - **edit.html**: Template for editing tasks.
- **static/**: Directory for static files (CSS, JavaScript).



## Usage

- **Homepage (`/`)**: View and add tasks.
  
  On the homepage, you can see a list of all current tasks and add new ones using the provided form.

- **Edit Task (`/edit/<int:id>`)**: Edit an existing task.
  
  To edit a task, navigate to `/edit/<int:id>`, where `<int:id>` is the ID of the task you want to modify. You can update the task's content and save the changes.

- **Delete Task (`/delete/<int:id>`)**: Delete a task.
  
  To delete a task, navigate to `/delete/<int:id>`, where `<int:id>` is the ID of the task you want to remove. The task will be deleted from the list.

