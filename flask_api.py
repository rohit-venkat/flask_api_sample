#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime
from flask import Flask, jsonify, abort, request, url_for, g
from flask_httpauth import HTTPBasicAuth
from models import db, User, Movie
from bootstrap_models import movies
from flask_restful import Api
from resources import (
    MovieResource, 
    MovieListResource, 
    UserResource, 
    UserListResource
)

auth = HTTPBasicAuth()

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'flask_api.db')
))

api = Api(app)
db.init_app(app)

api.add_resource(MovieListResource, '/api2/movies/', endpoint='movies')
api.add_resource(MovieResource, '/api2/movies/<int:id>', endpoint='movie')
api.add_resource(UserListResource, '/api2/users/', endpoint='users' )
api.add_resource(UserResource, '/api2/users/<string:username>', endpoint='user' )

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
            [return_movies.append(movie) for movie in Movie.query.filter(
                    Movie.title.like(filter_str) |
                    Movie.year.like(filter_str) |
                    Movie.rating.like(filter_str) |
                    Movie.runtime.like(filter_str) |
                    Movie.genre.like(filter_str) |
                    Movie.director.like(filter_str) |
                    Movie.writer.like(filter_str) |
                    Movie.actors.like(filter_str) |
                    Movie.plot.like(filter_str) |
                    Movie.language.like(filter_str) |
                    Movie.country.like(filter_str) |
                    Movie.awards.like(filter_str)
                )]

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
    if not request.json or not 'title' in request.json or not 'year' in request.json:
        abort(400, {'message': 'Required fields Title, Year not in request.'})
        # abort(400)

    # Generate a new object from the request to save to DB.
    movie = Movie(
                title=request.json['title'],
                year=request.json['year'],
                rating=request.json.get('rating', None),
                released=request.json.get('released', None),
                runtime=request.json.get('runtime', None),
                genre=request.json.get('genre', None),
                director=request.json.get('director', None),
                writer=request.json.get('writer', None),
                actors=request.json.get('actors', None),
                plot=request.json.get('plot', None),
                language=request.json.get('language', None),
                country=request.json.get('country', None),
                awards=request.json.get('awards', None),
                poster=request.json.get('poster', None),
                metascore=request.json.get('metascore', None),
                imdbRating=request.json.get('imdbRating', None)
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
    if not movie:
        abort(404)

    # Is there json in the request?
    if not request.json:
        abort(400, {'message': 'No json found in request'})

    # Are the values valid types?
    for key in movies[0]:
        key_type = type(request.json[key])
        if key in request.json and (key_type is not type(None) and key_type is not type(movies[0][key])):
            message = "%s is %s. %s passed in from request" % (key, type(movies[0][key]), type(request.json[key]))
            abort(400, {'message': message})


    # This is a sample:
    # We could write a test case for each field individually.
    # if 'Title' in request.json and type(request.json['Title']) != unicode:
    #     abort(400, {'message': 'Title is not unicode'})

    # Once everything looks good, update the object.
    # Here we are saying use the value from the request if it exists,
    # otherwise, default to the value already stored.
    
    movie.title=request.json['title']
    movie.year=request.json['year']
    movie.rating=request.json.get('rating', None)
    movie.released=request.json.get('released', None)
    movie.runtime=request.json.get('runtime', None)
    movie.genre=request.json.get('genre', None)
    movie.director=request.json.get('director', None)
    movie.writer=request.json.get('writer', None)
    movie.actors=request.json.get('actors', None)
    movie.plot=request.json.get('plot', None)
    movie.language=request.json.get('language', None)
    movie.country=request.json.get('country', None)
    movie.awards=request.json.get('awards', None)
    movie.poster=request.json.get('poster', None)
    movie.metascore=request.json.get('metascore', None)
    movie.imdbRating=request.json.get('imdbRating', None)

    db.session.commit()

    return jsonify({'movie': movie.json})


@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
@auth.login_required
def delete_task(movie_id):
    # Get the object to delete
    movie = Movie.query.get(movie_id)

    # Does the object exits?
    if not movie:
        abort(404)

    # Delete the object from the data store
    db.session.delete(movie)
    db.session.commit()

    # Return success!
    return jsonify({'message': 'Movie with ID %d has been deleted.' % movie_id}), 204


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

    user = User(username=request.json['user'], password_hash=User.hash_password(request.json['password']))

    # save the new object. If you using an ORM, would be something like
    # object.save()
    db.session.add(user)
    db.session.commit()

    return jsonify({'user': user.json}), 201


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
                title=movie['title'],
                year=movie['year'],
                rating=movie['rating'],
                released=movie['released'],
                runtime=movie['runtime'],
                genre=movie['genre'],
                director=movie['director'],
                writer=movie['writer'],
                actors=movie['actors'],
                plot=movie['plot'],
                language=movie['language'],
                country=movie['country'],
                awards=movie['awards'],
                poster=movie['poster'],
                metascore=movie['metascore'],
                imdbRating=movie['imdbRating']
            )
        db.session.add(m)
        db.session.commit()

    print('Initialized the database.')


if __name__ == "__main__":
    app.run(debug=True)
