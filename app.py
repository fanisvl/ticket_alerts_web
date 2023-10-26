from flask import Flask, render_template
from database import get_upcoming

app = Flask(__name__)

@app.route("/")
def home():
    upcoming_movies = upcoming()
    return render_template("index.html", movies=upcoming_movies)


@app.route("/api/upcoming")
def upcoming():
    return get_upcoming()