import os
import psycopg
from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "my_website_secret_key_123")


# ================= POSTGRESQL CONNECTION =================

def get_db_connection():
    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        raise Exception("DATABASE_URL is not configured")

    return psycopg.connect(database_url)


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

    cursor.execute(query, (name, email, phone, dob, address))

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

    cursor.execute(query, (degree, college, year, percentage))

    connection.commit()
    cursor.close()
    connection.close()

    return "Education saved successfully!"


# ================= SAVE SKILLS =================

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

    cursor.execute(query, (skill_name, skill_level))

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

    cursor.execute(query, (name, comment))

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