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

A list of `curl` commands to test the REST API is included in `curl_commands.txt`.

To test the api service using the Front End flask app, open another command line and run `python front_end.py`.

This sample uses a simple list of objects as our data store. The principles can be easily transferred to using a backend of your choice.

On the browser go to `http://localhost:5001` to view the front end portion.

You can run tests from the command line by running `python api_tests.py`.

## Future Work

This demo/example would work great with a simple mongo backend and ORM implementation in the code.

Also, it would be nice to set up a [Vagrant]('https://www.vagrantup.com/') script for launching a VM with all the dependencies pre-installed so users could see it working without installing and configuring dependencies themselves.

## Acknowledgements

In preparing this demo, I consulted and pulled from a few tutorials online:

* [Designing a RESTful API with Python and Flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [RESTful Authentication with Flask](http://blog.miguelgrinberg.com/post/restful-authentication-with-flask)
* [How to Build an API with Python and Flask](http://tech.pro/tutorial/1213/how-to-build-an-api-with-python-and-flask)
* [PassLib Tutorials](https://pythonhosted.org/passlib/)
