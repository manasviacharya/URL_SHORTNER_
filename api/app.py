from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector
import random
import string

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT", 3306))
    )

def generate_short_url(length=5):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":
        original_url = request.form.get("url")
        short_url = generate_short_url()

        cursor.execute(
            "SELECT short_url FROM urls WHERE short_url = %s",
            (short_url,)
        )
        while cursor.fetchone():
            short_url = generate_short_url()
            cursor.execute(
                "SELECT short_url FROM urls WHERE short_url = %s",
                (short_url,)
            )

        cursor.execute(
            "INSERT INTO urls (short_url, original_url) VALUES (%s, %s)",
            (short_url, original_url)
        )
        conn.commit()

        base_url = request.host_url.rstrip("/")
        return render_template(
            "shortened.html",
            shortened_url=f"{base_url}/{short_url}"
        )

    return render_template("index.html")


@app.route("/<short_url>")
def redirect_url(short_url):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT original_url FROM urls WHERE short_url = %s",
        (short_url,)
    )
    result = cursor.fetchone()

    if result:
        return redirect(result[0])

    return "URL not found", 404
