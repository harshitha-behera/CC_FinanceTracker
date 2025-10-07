# Enhanced Personal Finance Tracker

A full-stack **Flask-based Personal Finance Tracker** web application integrated with **AWS RDS (MySQL)** for data storage.  
Users can sign up, log in, and track income and expenses securely with real-time updates and visual analytics (via Chart.js).

---

## Features

- User Authentication – Sign up and log in functionality with session management  
- Secure Database Integration – AWS RDS MySQL backend for storing users and tracker data  
- Income/Expense Tracking – Add, update, and view transactions with categories  
- Dynamic Charts – Pie chart visualization of savings vs expenses using Chart.js  
- Responsive UI – Clean and interactive interface with hover animations  
- Session Management – Flask session used to handle user login state securely

---

## Project Structure

finance-tracker/
│
├── app.py # Flask backend (main application logic)

├── database_RDS.py # AWS RDS database connection and helper functions

├── tracker.sql # Database creation script

├── templates/

│ 
└── index.html # Frontend HTML with login, signup, and tracker UI

│
└── README.md # Documentation file


---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Python (Flask) |
| Database | AWS RDS (MySQL) |
| Frontend | HTML5, CSS3, JavaScript |
| Visualization | Chart.js |
| Cloud | AWS RDS |
| Security | Flask session |

---

## Requirements

Ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- MySQL (for local testing) or AWS RDS instance
- Internet access to load Chart.js and AWS SDK from CDN

---

## Setup Instructions

### 1. Clone the Repository


git clone https://github.com/<your-username>/finance-tracker.git
cd finance-tracker


### 2. Install Dependencies

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows


Then install the required packages:

pip install flask pymysql


### 3. Configure AWS RDS Connection

Edit the database_RDS.py file with your AWS RDS credentials:

connection = pymysql.connect(
    host='your-rds-endpoint.amazonaws.com',
    user='your-username',
    password='your-password',
    port=3306
)


Make sure your RDS instance is publicly accessible (or add your IP to inbound rules).

### 4. Create the Database

You can run the SQL script directly in MySQL Workbench or command line:

CREATE DATABASE finance_tracker;


The tables (Signup, Login, Tracker) will be created automatically when database_RDS.py runs for the first time.

### 5. Run the Application

Run the Flask server locally:

python app.py


or

flask run --host=0.0.0.0 --debug


By default, the app runs on:

http://127.0.0.1:5000


#### Future Improvements

Use password hashing (e.g., werkzeug.security) for better security

Add transaction delete/edit functionality

Deploy Flask app to AWS EC2 or Elastic Beanstalk

Add monthly and yearly spending summaries

Create bar and line charts for trends

Replace localStorage with full API integration for persistence


#### Security Note

This project is for learning/demo purposes.
Before deploying to production:

Always use hashed passwords (e.g., generate_password_hash)

Store secrets in environment variables

Restrict database access to trusted IPs only

## Author

#### Name: Harshitha Behera
#### GitHub: https://github.com/harshitha-behera

#### Email: harshithabehera999@gmail.com
