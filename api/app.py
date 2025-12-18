import os
import random
import string

import mysql.connector
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT", 3306))
    )

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":
        original_url = request.form.get("url")

        chars = string.ascii_letters + string.digits
        short_url = "".join(random.choice(chars) for _ in range(5))

        cursor.execute(
            "INSERT INTO urls (short_url, original_url) VALUES (%s, %s)",
            (short_url, original_url)
        )
        conn.commit()

        base_url = request.host_url.rstrip("/")
        return render_template(
            "index.html",
            shortened_url=f"{base_url}/{short_url}"
        )

    return render_template("index.html", shortened_url=None)

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
