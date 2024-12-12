from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from database_RDS import insert_signup_data, insert_login_data, get_login_data, insert_tracker_data, get_tracker_data, update_tracker_data

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    # Check if the username already exists in the Signup table
    existing_users = get_login_data()
    if any(user[0] == username for user in existing_users):
        return jsonify({"message": "Username already exists!"}), 400

    # Insert the new user into the Signup table
    insert_signup_data(username, password)

    # Also insert the user into the Login table for authentication purposes
    insert_login_data(username, password)

    return jsonify({"message": "Signup successful!"})

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validate the user's credentials in the Signup table
    existing_users = get_login_data()
    user = next((user for user in existing_users if user[0] == username and user[1] == password), None)

    if user:
        session['username'] = username  # Store username in session
        return jsonify({"message": "Login successful!", "username": username})
    else:
        return jsonify({"message": "Invalid username or password!"}), 401

@app.route('/tracker', methods=['GET', 'POST'])
def tracker():
    if 'username' not in session:
        return redirect(url_for('home'))  # Redirect to home if not logged in

    username = session['username']

    if request.method == 'POST':
        # Add or update tracker data
        description = request.form['description']
        amount = float(request.form['amount'])
        income_expense = request.form['transaction-type'] == 'income'
        category = request.form['category']

        # Check if the user already has a record with the same description
        existing_data = get_tracker_data(username)
        existing_record = next((record for record in existing_data if record[1] == description), None)

        if existing_record:
            # If record exists, update it
            update_tracker_data(username, description, amount, income_expense, category)
        else:
            # Otherwise, insert a new record
            insert_tracker_data(username, description, amount, income_expense, category)

    # Fetch tracker data specific to the logged-in user
    tracker_data = get_tracker_data(username)
    return render_template('tracker.html', username=username, tracker_data=tracker_data)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear the session
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
