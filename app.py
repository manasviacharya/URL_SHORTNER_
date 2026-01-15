import random
import os
import string
import mysql.connector
import time

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# LOCAL DATABASE CONNECTION
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "url_shortner")

conn = None

while conn is None:
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    except mysql.connector.Error:
        print("MySQL not ready yet, retrying in 2 seconds...")
        time.sleep(2)

cursor = conn.cursor(buffered=True)


def generate_short_url(length=5):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # handle form submit
        original_url = request.form.get("url")
        short_url = generate_short_url()

        # ensure uniqueness
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

        final_url = request.host_url + short_url
        return render_template("shortened.html", short_url=final_url)
    return render_template("index.html")

@app.route("/<short_url>")
def redirect_url(short_url):
    cursor.execute(
        "SELECT original_url FROM urls WHERE short_url = %s",
        (short_url,)
    )
    result = cursor.fetchone()

    if result:
        return redirect(result[0])

    return "URL not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

