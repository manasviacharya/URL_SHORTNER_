import random
import string
import sqlite3
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

conn = sqlite3.connect("urls.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_url TEXT UNIQUE NOT NULL,
    original_url TEXT NOT NULL
)
""")
conn.commit()

def generate_short_url(length=5):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form.get("url")

        short_url = generate_short_url()

        # Ensure uniqueness
        cursor.execute(
            "SELECT short_url FROM urls WHERE short_url = ?",
            (short_url,)
        )
        while cursor.fetchone():
            short_url = generate_short_url()
            cursor.execute(
                "SELECT short_url FROM urls WHERE short_url = ?",
                (short_url,)
            )

        cursor.execute(
            "INSERT INTO urls (short_url, original_url) VALUES (?, ?)",
            (short_url, original_url)
        )
        conn.commit()

        final_url = request.host_url + short_url
        return render_template("shortened.html", short_url=final_url)

    return render_template("index.html")


@app.route("/<short_url>")
def redirect_url(short_url):
    cursor.execute(
        "SELECT original_url FROM urls WHERE short_url = ?",
        (short_url,)
    )
    result = cursor.fetchone()

    if result:
        return redirect(result[0])

    return "URL not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
