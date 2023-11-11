from flask import Flask, render_template, request
from database import get_upcoming, get_movie, post_alert
import json

app = Flask(__name__)

@app.route("/")
def home():
    upcoming_movies = get_upcoming()
    return render_template("index.html", movies=upcoming_movies)

@app.route('/movie/<int:movie_id>')
def movie_page(movie_id):

    movie_data = get_movie(movie_id)    
    if movie_data:
        return render_template('movie.html', movie_data=movie_data)
    else:
        return "404: Movie not found"

@app.route("/api/upcoming")
def upcoming():
    return get_upcoming()

@app.route('/alert_created', methods=['POST'])
def create_alert():
    email = request.form.get('email')
    movie_data = json.loads(request.form.get('movie_data').replace("'", '"')) # replace sigle quotes with double quotes for valid json
    post_alert(email, movie_data['title'])
    return render_template("alert_created.html", movie_data=movie_data, email=email)