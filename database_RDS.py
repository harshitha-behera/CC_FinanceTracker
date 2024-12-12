# DB instance identifier: finance-db
# username: admin
# password: Finance_cc_123
# host: finance-db.chqgogsusg06.us-east-1.rds.amazonaws.com
# port: 3306


import pymysql

# try:
#     connection = pymysql.connect(
#         host='finance-db.chqgogsusg06.us-east-1.rds.amazonaws.com',
#         user= 'admin',
#         password='Finance_cc_123',
#         port=3306
#     )
#     print("Connection successful!")
# except pymysql.err.OperationalError as e:
#     print(f"OperationalError: {e}")
# except Exception as ex:
#     print(f"An error occurred: {ex}")
# finally:
#     if 'connection' in locals() and connection:
#         connection.close()


# Connect to AWS RDS instance
connection = pymysql.connect(
    host='finance-db.chqgogsusg06.us-east-1.rds.amazonaws.com',
    user='admin',
    password='Finance_cc_123',
    port=3306
)

cursor = connection.cursor()

# Create and use the database
cursor.execute("CREATE DATABASE IF NOT EXISTS Tracker")
cursor.execute("USE `Tracker`")

# Create Tracker table
# create_tracker_table = """
# CREATE TABLE Tracker (
#     Name VARCHAR(200),
#     Description VARCHAR(200),
#     Amount DECIMAL(10, 2),
#     IncomeExpense BOOLEAN,
#     Category VARCHAR(100),
#     PRIMARY KEY (Name)
# )
# """
# cursor.execute(create_tracker_table)

# Create Login table
# create_login_table = """
# CREATE TABLE Login (
#     username VARCHAR(200) PRIMARY KEY,
#     password VARCHAR(200) NOT NULL
# )
# """
# cursor.execute(create_login_table)

# Create Signup table
# create_signup_table = """
# CREATE TABLE Signup (
#     username VARCHAR(200) PRIMARY KEY,
#     password VARCHAR(200) NOT NULL
# )
# """
# cursor.execute(create_signup_table)

# Insert data into Tracker
def insert_tracker_data(Name, Description, Amount, IncomeExpense, Category):
    cursor.execute(
        "INSERT INTO Tracker (Name, Description, Amount, IncomeExpense, Category) VALUES (%s, %s, %s, %s, %s)",
        (Name, Description, Amount, IncomeExpense, Category)
    )
    connection.commit()

# Get data from Tracker
def get_tracker_data():
    cursor.execute("SELECT * FROM Tracker")
    table = cursor.fetchall()
    return table

# Insert data into Login
def insert_login_data(username, password):
    cursor.execute(
        "INSERT INTO Login (username, password) VALUES (%s, %s)",
        (username, password)
    )
    connection.commit()

# Insert data into Signup
def insert_signup_data(username, password):
    cursor.execute(
        "INSERT INTO Signup (username, password) VALUES (%s, %s)",
        (username, password)
    )
    connection.commit()

# Get data from Login
def get_login_data():
    cursor.execute("SELECT * FROM Login")
    return cursor.fetchall()

# Get data from Signup
def get_signup_data():
    cursor.execute("SELECT * FROM Signup")
    return cursor.fetchall()


# Update an existing record in the Tracker table
def update_tracker_data(username, description, amount, income_expense, category):
    cursor.execute(
        """UPDATE Tracker 
           SET Amount = %s, IncomeExpense = %s, Category = %s 
           WHERE Name = %s AND Description = %s""",
        (amount, income_expense, category, username, description)
    )
    connection.commit()
