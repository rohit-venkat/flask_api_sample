#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import requests
from requests.auth import HTTPBasicAuth
app = Flask(__name__)

@app.route("/")
def display_movies():
    r = requests.get('http://localhost:5000/api/movies', auth=('twaits', 'Passphrase1'))
    movies = r.json()['movies']
    return render_template('base.html', movies=movies)


@app.route("/movies/<int:movie_id>")
def display_movie(movie_id):
    url = "http://localhost:5000/api/movies/" + str(movie_id)
    r = requests.get(url, auth=('twaits', 'Passphrase1'))
    movie = r.json()['movie']
    return render_template('movie.html', movie=movie)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
