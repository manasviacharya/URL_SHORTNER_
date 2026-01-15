# 🔗 URL Shortener Web Application

A modern, lightweight, and containerised **URL Shortener** built using **Flask**, deployed with **Docker**, and hosted on **Render**.  
The application converts long URLs into short, shareable links and redirects users seamlessly to the original destination.

---

## 🛠️ Tech Stack

![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Render](https://img.shields.io/badge/Deployment-Render-purple)
![Python](https://img.shields.io/badge/Python-3.11-blue)

---

## 🚀 Live Demo

🔗 **Live Application**  
https://url-shortner-01by.onrender.com

> ⚠️ On Render’s free tier, the service may take **30–60 seconds** to wake up after inactivity.

---

## 🧠 Project Overview

This application allows users to:
- Submit a long URL
- Receive a shortened URL
- Use the shortened URL to redirect to the original link

The system demonstrates **backend development**, **database integration**, **containerisation**, and **cloud deployment**.

---

## 🧱 System Architecture and Logic Flow

<p align="center">
  <img width="750" src="./docs/ChatGPT Image Jan 15, 2026, 07_11_07 PM.png" alt="System Architecture and Logic Flow Diagram">
</p>

### Architecture Explanation

1. The user interacts with the application via a web browser.
2. Requests are routed to a **Render-hosted Docker container**.
3. **Gunicorn** acts as the WSGI server.
4. **Flask** handles routing and application logic.
5. **SQLite** stores URL mappings locally.

---

### Logic Description

1. User enters a long URL.
2. Application generates a random short code.
3. Short code uniqueness is checked.
4. URL mapping is stored in the database.
5. Shortened URL is returned.
6. Short URL redirects to the original link.

---

## ✨ Features

- 🔗 URL shortening
- 🔄 Automatic redirection
- 🎯 Unique short URL generation
- 🐳 Dockerised application
- ☁️ Cloud deployed
- 📄 Clean UI

---

## 🛠 Tech Stack Details

| Layer | Technology |
|------|-----------|
| Backend | Flask (Python) |
| Web Server | Gunicorn |
| Database | SQLite |
| Containerisation | Docker |
| Cloud Platform | Render |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
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
├── static/
│   └── styles.css
│
└── docs/
    └── architecture-and-logic.png
```

## 🐍 Core Backend Logic
Short URL Generation
```python 
def generate_short_url(length=5):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

Database Insert
cursor.execute(
    "INSERT INTO urls (short_url, original_url) VALUES (?, ?)",
    (short_url, original_url)
)
conn.commit()
```

## 📦 Dependencies
Flask==3.0.0
gunicorn==21.2.0

## 🐳 Docker Configuration

```dockerfile
Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

```
## Run Locally
docker build -t url-shortener .
docker run -p 5000:5000 url-shortener

## ☁️ Deployment on Render

Deployed as a Docker Web Service

Dockerfile auto-detected

Port 5000 exposed

SQLite used to avoid paid databases

## ⚠️ Data Persistence Note

SQLite data is ephemeral on Render free tier

Data resets on redeploy or restart

Accepted for academic/demo purposes

## 🎓 Academic Relevance

This project demonstrates:

Flask backend development

Database operations

Docker containerisation

Cloud deployment workflows

Real-world deployment constraints

## 👩‍💻 Author

Manasvi Acharya
GitHub: https://github.com/manasviacharya

## 📜 License

Educational use only.