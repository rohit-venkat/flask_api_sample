#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from passlib.apps import custom_app_context as pwd_context
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

movies = [
    {
        "id": 1,
        "Title": "Star Wars: Episode V - The Empire Strikes Back",
        "Year": "1980",
        "Rated": "PG",
        "Released": "20 Jun 1980",
        "Runtime": "124 min",
        "Genre": "Action, Adventure, Fantasy",
        "Director": "Irvin Kershner",
        "Writer": "Leigh Brackett (screenplay), Lawrence Kasdan (screenplay), George Lucas (story)",
        "Actors": "Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams",
        "Plot": "After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.",
        "Language": "English",
        "Country": "USA",
        "Awards": "Won 1 Oscar. Another 15 wins & 16 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMjE2MzQwMTgxN15BMl5BanBnXkFtZTcwMDQzNjk2OQ@@._V1_SX300.jpg",
        "Metascore": "78",
        "imdbRating": "8.8"
    },
    {
        "id": 2,
        "Title": "Back to the Future",
        "Year": "1985",
        "Rated": "PG",
        "Released": "03 Jul 1985",
        "Runtime": "116 min",
        "Genre": "Adventure, Comedy, Sci-Fi",
        "Director": "Robert Zemeckis",
        "Writer": "Robert Zemeckis, Bob Gale",
        "Actors": "Michael J. Fox, Christopher Lloyd, Lea Thompson, Crispin Glover",
        "Plot": "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.",
        "Language": "English",
        "Country": "USA",
        "Awards": "Won 1 Oscar. Another 17 wins & 24 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMjA5NTYzMDMyM15BMl5BanBnXkFtZTgwNjU3NDU2MTE@._V1_SX300.jpg",
        "Metascore": "86",
        "imdbRating": "8.5"
    },
    {
        "id": 3,
        "Title": "Harold and Maude",
        "Year": "1971",
        "Rated": "N/A",
        "Released": "20 Dec 1971",
        "Runtime": "91 min",
        "Genre": "Comedy, Romance",
        "Director": "Hal Ashby",
        "Writer": "Colin Higgins",
        "Actors": "Ruth Gordon, Bud Cort, Vivian Pickles, Cyril Cusack",
        "Plot": "Young, rich, and obsessed with death, Harold finds himself changed forever when he meets lively septuagenarian Maude at a funeral.",
        "Language": "English",
        "Country": "USA",
        "Awards": "Nominated for 2 Golden Globes. Another 2 wins & 1 nomination.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTUxMjMwODMxMl5BMl5BanBnXkFtZTYwMDA3MDE5._V1_SX300.jpg",
        "Metascore": "N/A",
        "imdbRating": "8.1"
    },
    {
        "id": 4,
        "Title": "Army of Darkness",
        "Year": "1992",
        "Rated": "R",
        "Released": "19 Feb 1993",
        "Runtime": "81 min",
        "Genre": "Comedy, Fantasy, Horror",
        "Director": "Sam Raimi",
        "Writer": "Sam Raimi, Ivan Raimi",
        "Actors": "Bruce Campbell, Embeth Davidtz, Marcus Gilbert, Ian Abercrombie",
        "Plot": "A man is accidentally transported to 1300 A.D., where he must battle an army of the dead and retrieve the Necronomicon so he can return home.",
        "Language": "English",
        "Country": "USA",
        "Awards": "7 wins & 4 nominations.",
        "Poster": "https://images-na.ssl-images-amazon.com/images/M/MV5BODcyYzM4YTAtNGM5MS00NjU4LTk2Y2ItZjI5NjkzZTk0MmQ1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
        "Metascore": "57",
        "imdbRating": "7.6"
    },
    {
        "id": 5,
        "Title": "Léon: The Professional",
        "Year": "1994",
        "Rated": "R",
        "Released": "18 Nov 1994",
        "Runtime": "110 min",
        "Genre": "Crime, Drama, Thriller",
        "Director": "Luc Besson",
        "Writer": "Luc Besson",
        "Actors": "Jean Reno, Gary Oldman, Natalie Portman, Danny Aiello",
        "Plot": "Mathilda, a 12-year-old girl, is reluctantly taken in by Léon, a professional assassin, after her family is murdered. Léon and Mathilda form an unusual relationship, as she becomes his protégée and learns the assassin's trade.",
        "Language": "English, Italian",
        "Country": "France",
        "Awards": "3 wins & 8 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTgzMzg4MDkwNF5BMl5BanBnXkFtZTcwODAwNDg3OA@@._V1_SX300.jpg",
        "Metascore": "64",
        "imdbRating": "8.6"
    },
    {
        "id": 6,
        "Title": "La Femme Nikita",
        "Year": "1990",
        "Rated": "R",
        "Released": "01 Apr 1991",
        "Runtime": "118 min",
        "Genre": "Action, Thriller",
        "Director": "Luc Besson",
        "Writer": "Luc Besson",
        "Actors": "Anne Parillaud, Marc Duret, Patrick Fontana, Alain Lathière",
        "Plot": "Convicted felon Nikita, instead of going to jail, is given a new identity and trained, stylishly, as a top secret spy/assassin.",
        "Language": "French, Italian, English",
        "Country": "France, Italy",
        "Awards": "Nominated for 1 Golden Globe. Another 5 wins & 14 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTg0NjYzNjY1MF5BMl5BanBnXkFtZTgwOTk1Mzk5MDE@._V1_SX300.jpg",
        "Metascore": "56",
        "imdbRating": "7.4"
    },
    {
        "id": 7,
        "Title": "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb",
        "Year": "1964",
        "Rated": "PG",
        "Released": "29 Jan 1964",
        "Runtime": "95 min",
        "Genre": "Comedy, War",
        "Director": "Stanley Kubrick",
        "Writer": "Stanley Kubrick (screenplay), Terry Southern (screenplay), Peter George (screenplay), Peter George (based on the book: \"Red Alert\" by)",
        "Actors": "Peter Sellers, George C. Scott, Sterling Hayden, Keenan Wynn",
        "Plot": "An insane general triggers a path to nuclear holocaust that a war room full of politicians and generals frantically try to stop.",
        "Language": "English, Russian",
        "Country": "USA, UK",
        "Awards": "Nominated for 4 Oscars. Another 15 wins & 4 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTU2ODM2NTkxNF5BMl5BanBnXkFtZTcwOTMwMzU3Mg@@._V1_SX300.jpg",
        "Metascore": "96",
        "imdbRating": "8.5"
    },
    {
        "id": 8,
        "Title": "Citizen Kane",
        "Year": "1941",
        "Rated": "Approved",
        "Released": "05 Sep 1941",
        "Runtime": "119 min",
        "Genre": "Drama, Mystery",
        "Director": "Orson Welles",
        "Writer": "Herman J. Mankiewicz (original screen play), Orson Welles (original screen play)",
        "Actors": "Joseph Cotten, Dorothy Comingore, Agnes Moorehead, Ruth Warrick",
        "Plot": "Following the death of a publishing tycoon, news reporters scramble to discover the meaning of his final utterance.",
        "Language": "English",
        "Country": "USA",
        "Awards": "Won 1 Oscar. Another 8 wins & 10 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTQ2Mjc1MDQwMl5BMl5BanBnXkFtZTcwNzUyOTUyMg@@._V1_SX300.jpg",
        "Metascore": "N/A",
        "imdbRating": "8.4"
    },
    {
        "id": 9,
        "Title": "Red Dawn",
        "Year": "1984",
        "Rated": "PG-13",
        "Released": "10 Aug 1984",
        "Runtime": "114 min",
        "Genre": "Action, Drama, War",
        "Director": "John Milius",
        "Writer": "Kevin Reynolds (story), John Milius (screenplay), Kevin Reynolds (screenplay)",
        "Actors": "Patrick Swayze, C. Thomas Howell, Lea Thompson, Charlie Sheen",
        "Plot": "It is the dawn of World War III. In mid-western America, a group of teenagers bands together to defend their town, and their country, from invading Soviet forces.",
        "Language": "English, Russian, Spanish",
        "Country": "USA",
        "Awards": "1 nomination.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BNzgzNjcwMjI3MF5BMl5BanBnXkFtZTcwNDAxNTQyNA@@._V1_SX300.jpg",
        "Metascore": "N/A",
        "imdbRating": "6.3"
    },
    {
        "id": 10,
        "Title": "Better Off Dead...",
        "Year": "1985",
        "Rated": "PG",
        "Released": "11 Oct 1985",
        "Runtime": "97 min",
        "Genre": "Comedy, Romance",
        "Director": "Savage Steve Holland",
        "Writer": "Savage Steve Holland",
        "Actors": "John Cusack, David Ogden Stiers, Kim Darby, Demian Slade",
        "Plot": "A teenager has to deal with his girlfriend dumping him among family crises, homicidal paper boys, and a rival skier.",
        "Language": "English",
        "Country": "USA",
        "Awards": "N/A",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTI5MjEwNDg3M15BMl5BanBnXkFtZTcwODczNjYyMQ@@._V1_SX300.jpg",
        "Metascore": "N/A",
        "imdbRating": "7.3"
    }
]

users = []


def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    year = db.Column(db.Integer)
    rating = db.Column(db.String(5))
    released = db.Column(db.String(20))
    runtime = db.Column(db.String(15))
    genre = db.Column(db.Text(length=None))
    director = db.Column(db.String(256))
    writer = db.Column(db.String(256))
    actors = db.Column(db.String(512))
    plot = db.Column(db.Text(length=None))
    language = db.Column(db.String(100))
    country = db.Column(db.String(100))
    awards = db.Column(db.String(512))
    poster = db.Column(db.String(512))
    metascore = db.Column(db.String(5))
    imdbRating = db.Column(db.Float())
    
    def __repr__(self):
        return "<Movie {}>".format(repr(self.title))

    @property
    def json(self):
        return to_json(self, self.__class__)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password_hash = db.Column(db.String(512))

    @staticmethod
    def hash_password(password):
        return pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def save(self):
        global users
        if len(users) > 0:
            self.id = users[-1].id + 1
        else:
            self.id = 0
        users.append(self)

    def get_json(self):
        return {'user': self.username, 'id': self.id}
