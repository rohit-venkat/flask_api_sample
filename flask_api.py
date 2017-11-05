#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime
from flask import Flask, jsonify, abort, request, url_for, g
from flask_httpauth import HTTPBasicAuth
from models import db, User, Movie
from bootstrap_models import movies

auth = HTTPBasicAuth()

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'flask_api.db')
))

db.init_app(app)


@app.route("/api/movies/", methods=['GET'])
@auth.login_required
def get_all_movies():
    """
    only called in response to a 'GET' request.

    return a list of all movie objects
    """
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    end = limit + offset

    filter_query = request.args.get('filter', None)

    return_movies = []

    if filter_query:
        filter_query = filter_query.replace("+"," ")
        filters = filter_query.split(',')
        for filter_str in filters:
            [return_movies.append(movie) for movie in Movie.query.filter(or_(
                    Movie.title.like(filter_str),
                    Movie.year.like(filter_str),
                    Movie.rating.like(filter_str),
                    Movie.runtime.like(filter_str),
                    Movie.genre.like(filter_str),
                    Movie.director.like(filter_str),
                    Movie.writer.like(filter_str),
                    Movie.actors.like(filter_str),
                    Movie.plot.like(filter_str),
                    Movie.language.like(filter_str),
                    Movie.country.like(filter_str),
                    Movie.awards.like(filter_str)
                ))]

    else:
        return_movies = Movie.query.offset(offset).limit(limit).all()


    return jsonify({"movies": [movie.json for movie in return_movies]})

    # Uncomment to return a URI rather than strict ID for objects.
    # return jsonify({'movies': [convert_id_to_uri(movie) for movie in return_movies]})


@app.route('/api/movies/', methods=['POST'])
@auth.login_required
def create_movie_object():
    """
    only called in response to a 'POST' request.

    Creates and persists a new movie object

    return the saved movie object
    """

    # Check to see if the json is there, and if it has the required fields.
    if not request.json or not 'Title' in request.json or not 'Year' in request.json:
        abort(400, {'message': 'Required fields Title, Year not in request.'})
        # abort(400)

    # Generate a new object from the request to save to DB.
    movie = Movie(
                title=request.json['Title'],
                year=request.json['Year'],
                rating=request.json.get('Rated', u""),
                released=request.json.get('Released', u""),
                runtime=request.json.get('Runtime', u""),
                genre=request.json.get('Genre', u""),
                director=request.json.get('Director', u""),
                writer=request.json.get('Writer', u""),
                actors=request.json.get('Actors', u""),
                plot=request.json.get('Plot', u""),
                language=request.json.get('Language', u""),
                country=request.json.get('Country', u""),
                awards=request.json.get('Awards', u""),
                poster=request.json.get('Poster', u""),
                metascore=request.json.get('Metascore', u""),
                imdbRating=request.json.get('imdbRating', u"")
            )

    # save the new object. If you using an ORM, would be something like
    # object.save()
    db.session.add(movie)
    db.session.commit()

    return jsonify({'movie': Movie.query.get(movie.id).json}), 201


@app.route('/api/movies/<int:movie_id>', methods=['GET'])
@auth.login_required
def get_movie_by_id(movie_id):
    """
    only called in response to a 'GET' request.

    return a movie object by id
    """
    movie = Movie.query.get(movie_id)
    if not movie:
        abort(404)

    return jsonify({'movie': movie.json})
    # return jsonify({'movie': convert_id_to_uri(movie[0])})


@app.route('/api/movies/<int:movie_id>', methods=['PUT'])
@auth.login_required
def update_task(movie_id):

    # Get the object to update

    movie = Movie.query.get(movie_id)

    # Validate the data
    # Does the object exits?
    if not movie == 0:
        abort(404)

    # Is there json in the request?
    if not request.json:
        abort(400, {'message': 'No json found in request'})

    # Are the values valid types?
    for key in movies[0]:
        if key in request.json and type(request.json[key]) is not type(movies[0][key]):
            message = "%s is %s. %s passed in from request" % (key, type(movies[0][key]), type(request.json[key]))
            abort(400, {'message': message})


    # This is a sample:
    # We could write a test case for each field individually.
    # if 'Title' in request.json and type(request.json['Title']) != unicode:
    #     abort(400, {'message': 'Title is not unicode'})

    # Once everything looks good, update the object.
    # Here we are saying use the value from the request if it exists,
    # otherwise, default to the value already stored.
    
    movie.title=request.json['Title'],
    movie.year=request.json['Year'],
    movie.rating=request.json.get('Rated', u""),
    movie.released=request.json.get('Released', u""),
    movie.runtime=request.json.get('Runtime', u""),
    movie.genre=request.json.get('Genre', u""),
    movie.director=request.json.get('Director', u""),
    movie.writer=request.json.get('Writer', u""),
    movie.actors=request.json.get('Actors', u""),
    movie.plot=request.json.get('Plot', u""),
    movie.language=request.json.get('Language', u""),
    movie.country=request.json.get('Country', u""),
    movie.awards=request.json.get('Awards', u""),
    movie.poster=request.json.get('Poster', u""),
    movie.metascore=request.json.get('Metascore', u""),
    movie.imdbRating=request.json.get('imdbRating', u"")

    return jsonify({'movie': movie.json})


@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
@auth.login_required
def delete_task(movie_id):
    # Get the object to delete
    movie = [movie for movie in movies if movie['id'] == movie_id]

    movie = Movie.query.get(movie_id)

    # Does the object exits?
    if not movie:
        abort(404)

    # Delete the object from the data store
    db.session.delete(movie)
    db.session.commit()

    # Return success!
    return jsonify({'result': True})


@app.route('/api/users/', methods=['GET'])
def get_users():
    return jsonify({"users":[user.json for user in User.query.all()]})


@app.route('/api/users/', methods=['POST'])
def create_user():
    """
    only called in response to a 'POST' request.

    Creates and persists a new user object

    return the saved user object
    """

    # Check to see if the json is there, and if it has the required fields.
    if not request.json or not 'user' in request.json or not 'password' in request.json:
        abort(400, {'message': 'Required fields "user", "password" not in request.'})

    user = User(request.json['user'], password_hash=User.hash_password(request.json['password']))

    # save the new object. If you using an ORM, would be something like
    # object.save()
    db.session.add(user)
    db.session.commit()

    return jsonify({'user': user.get_json()}), 201


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


#########################
# Custom Error Handling #
#########################

@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description['message'],
                        'status_code': 400,
                        'status': 'Bad Request'})
    return response, 400


####################
# Helper Functions #
####################


def convert_id_to_uri(movie):
    tmp = {}
    for field in movie:
        if field == 'id':
            tmp['uri'] = url_for('get_movie_by_id',
                                 movie_id=movie['id'],
                                 _external=True)
        else:
            tmp[field] = movie[field]
    return tmp


#########################
# Flask CLI Commands    #
#########################

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()

    admin = User(username='twaits', password_hash=User.hash_password('Passphrase1'))
    db.session.add(admin)
    db.session.commit()

    for movie in movies:
        m = Movie(
                title=movie['Title'],
                year=movie['Year'],
                rating=movie['Rated'],
                released=movie['Released'],
                runtime=movie['Runtime'],
                genre=movie['Genre'],
                director=movie['Director'],
                writer=movie['Writer'],
                actors=movie['Actors'],
                plot=movie['Plot'],
                language=movie['Language'],
                country=movie['Country'],
                awards=movie['Awards'],
                poster=movie['Poster'],
                metascore=movie['Metascore'],
                imdbRating=movie['imdbRating']
            )
        db.session.add(m)
        db.session.commit()

    print('Initialized the database.')


if __name__ == "__main__":
    app.run(debug=True)
