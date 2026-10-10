from flask import Flask, render_template, request, session, redirect, url_for

import mysql.connector

app = Flask(__name__)

app.secret_key = "my_website_secret_key_123"


# ================= MYSQL CONNECTION =================

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="personal_website"
    )

    return connection


# ================= HOME =================

@app.route("/")
def home():
    return render_template("index.html")


# ================= SAVE PERSONAL DETAILS =================

@app.route("/save-personal-details", methods=["POST"])
def save_personal_details():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    dob = request.form["dob"]
    address = request.form["address"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO personal_details
        (name, email, phone, dob, address)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, email, phone, dob, address)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return "Personal details saved successfully!"



# ================= SAVE EDUCATION =================

@app.route("/save-education", methods=["POST"])
def save_education():

    degree = request.form["degree"]
    college = request.form["college"]
    year = request.form["year"]
    percentage = request.form["percentage"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO education
        (degree, college, year, percentage)
        VALUES (%s, %s, %s, %s)
    """

    values = (degree, college, year, percentage)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return "Education saved successfully!"




@app.route("/save-skills", methods=["POST"])
def save_skills():

    skill_name = request.form["skill_name"]
    skill_level = request.form["skill_level"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO skills
        (skill_name, skill_level)
        VALUES (%s, %s)
    """

    values = (skill_name, skill_level)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return "Skills saved successfully!"





# ================= SAVE COMMENT =================

@app.route("/save-comment", methods=["POST"])
def save_comment():

    name = request.form["name"]
    comment = request.form["comment"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO comments
        (name, comment)
        VALUES (%s, %s)
    """

    values = (name, comment)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return "Comment submitted successfully!"




# ================= LOGIN =================

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM users
        WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:
        session["username"] = username
        return "Login successful!"
    else:
        return "Invalid username or password."
    
    
    
    
    
    # ================= LOGOUT =================

@app.route("/logout")
def logout():

    session.pop("username", None)

    return "Logout successful!"





# ================= RUN =================



if __name__ == "__main__":
    app.run(debug=True)