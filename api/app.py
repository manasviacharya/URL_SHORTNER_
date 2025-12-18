from flask import Flask, render_template, request
import mysql.connector
import os
import string, random

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT") or 3306)
    )

def generate_short():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO urls (short_url, original_url) VALUES (%s, %s)",
            ("test123", "https://example.com")
        )
        conn.commit()

        cursor.close()
        conn.close()

        return "INSERT OK"

    return render_template("index.html")



@app.route("/<short_code>")
def redirect_url(short_code):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT original_url FROM urls WHERE short_url = %s",
        (short_code,)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        return result[0], 302
    return "URL not found", 404
