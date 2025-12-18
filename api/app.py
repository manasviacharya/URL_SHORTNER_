from flask import Flask, render_template, request, redirect
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
        original_url = request.form["url"]
        short_code = generate_short()

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO urls (short_url, original_url) VALUES (%s, %s)",
            (short_code, original_url)
        )
        conn.commit()
        cursor.close()
        conn.close()

        short_url = request.host_url + short_code
        return render_template("shortened.html", short_url=short_url)

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
        return redirect(result[0])

    return "URL not found", 404
