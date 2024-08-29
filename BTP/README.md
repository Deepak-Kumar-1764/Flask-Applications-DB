# Flask Authentication and Data Storage Application

This project is a Flask web application featuring user authentication, data storage, and management. It includes functionalities for user registration, login, data storage, and retrieval. Additionally, it provides a simple task management feature.

## Features

- **User Authentication**: Users can register, log in, and log out. Passwords are securely hashed.
- **Data Storage**: Authenticated users can store and manage their data.
- **Task Management**: Users can add, edit, and delete tasks.
- **Responsive Design**: The interface is designed to be user-friendly and responsive.

## Technologies Used

- **Flask**: Web framework for building the application.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Database for storing user and task data.
- **HTML/CSS**: Frontend technologies for designing the user interface.
- **Flask-SCSS**: For compiling SCSS files into CSS.

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Deepak-Kumar-1764/your-repository-name.git
   cd your-repository-name


## Setup

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv

3. **Activate the Virtual Environment**
  - Windows
    ```bash
    venv\Scripts\activate
  - macOs/Linux
    ```bash 
    source venv/bin/activate
4. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

# Configuration
  ## Set Up the Flask Application
  Ensure your Flask app is configured correctly. For development purposes, you can set the SECRET_KEY and database URI directly in your app.py or config.py.
# Database Migrations
   Flask-Migrate is used to handle database schema changes. Follow these steps to initialize and manage your database:
  1. **Initialize the Migration Repository**
       This creates the migrations folder which will contain the migration scripts.
      ```bash
     flask db init
  2. **Create a Migration Script**
      This command auto-generates a migration script based on changes detected in your models.
      ```bash
     flask db migrate -m "Initial Migration"
  3. **Apply the Migrationt**
    This updates the database schema based on the migration script.
      ```bash
      flask db upgrade
 4. **Apply the Migrationt**
   This rolls back the database schema to the previous version.
      ```bash
      flask db downgrade
# Running the Application
  To start the Flask application, use:
  ```bash
    flask run




   


