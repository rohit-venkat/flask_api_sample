# flask_api_sample
simple example of using flask to generate an api

## Dependencies

[Flask](http://flask.pocoo.org/)
:   `pip install Flask`

[Requests](http://docs.python-requests.org/en/latest/)
:   `pip install requests`

[flask-httpauth](https://flask-httpauth.readthedocs.org/en/latest/)
:   `pip install flask-httpauth`

[passlib](https://pythonhosted.org/passlib/)
:   `pip install passlib`

## How to Use

From a command line run `python flask_api.py`.

Run `curl -i -H "Content-Type: application/json" -X POST -d '{"user":"twaits", "password":"Passphrase1"}' http://localhost:5000/api/users/` from the command line in order to have the user password needed to use the front end.

To test the api service using the Front End flask app, open another command line and run `python front_end.py`.

This sample uses a simple list of objects as our data store. The principles can be easily transferred to using a backend of your choice.

On the browser go to `http://localhost:5001` to view the front end portion.
