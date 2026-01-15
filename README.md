🔗 URL Shortener Web Application

A lightweight and scalable URL Shortener web application built using Flask, containerised with Docker, and deployed on Render. The application allows users to convert long URLs into short links and redirects users to the original URL when the short link is accessed.

🚀 Live Demo

🔗 Deployed Application:

https://url-shortner-01by.onrender.com


⚠️ Note: On Render free tier, the application may take 30–60 seconds to wake up if inactive.

🛠️ Tech Stack

Backend: Flask (Python)

Database: SQLite (for deployment simplicity)

Web Server: Gunicorn

Containerisation: Docker

Deployment Platform: Render

Version Control: Git & GitHub

✨ Features

Generate short URLs for long links

Redirect short URLs to the original URL

Automatic uniqueness handling for short links

Clean and minimal UI

Dockerised for easy deployment

Deployed on cloud with public access

📁 Project Structure
URL_SHORTNER_/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── shortened.html
│
└── static/
    └── styles.css

⚙️ How It Works

User enters a long URL in the web form.

The application generates a unique short identifier.

The short URL is stored in a SQLite database.

When the short URL is accessed, the user is redirected to the original URL.

🐳 Docker Setup (Local)
Prerequisites

Docker installed

Build and Run
docker build -t url-shortener .
docker run -p 5000:5000 url-shortener


Access the app at:

http://localhost:5000

☁️ Deployment on Render

The application is deployed as a Docker Web Service

SQLite is used to avoid paid database dependencies

No environment variables are required

Gunicorn is used as the production WSGI server

Deployment Highlights

Automatic builds from GitHub

Free-tier compatible

Public URL provided by Render

📌 Important Notes

SQLite database is ephemeral on Render free tier.

Data resets on redeployment or restart.

This design choice is intentional for academic/demo purposes.

🎓 Academic Context

This project demonstrates:

Backend web development using Flask

Database integration

Docker containerisation

Cloud deployment workflow

Real-world debugging and deployment constraints

SQLite was chosen for deployment due to free-tier limitations of managed databases while preserving application functionality.

👩‍💻 Author

Manasvi Acharya
GitHub: https://github.com/manasviacharya

📜 License

This project is for educational purposes.

✅ Status

✔️ Dockerised

✔️ Deployed

✔️ Submission-ready