# flask_api_sample
simple example of using flask to generate an api

## Setup

This project has a Vagrant-backed platform and standard setup. The Vagrant box is Ubuntu 14.04 and is provided by Hashicorp. Running `vagrant up` will stand up the VM and provision it with the dependencies required to run this application. The operator will need to `vagrant ssh` into the VM and start the services as described below in the section "How to Use".

Alternatively, the following Python modules may be installed by hand directly on your computer to meet the application's requirements for a local (bare metal) run.

[Flask](http://flask.pocoo.org/)
:   `pip install Flask`

[Requests](http://docs.python-requests.org/en/latest/)
:   `pip install requests`

[flask-httpauth](https://flask-httpauth.readthedocs.org/en/latest/)
:   `pip install flask-httpauth`

[passlib](https://pythonhosted.org/passlib/)
:   `pip install passlib`

## How to Use

From a command line at the root of the project, run

	python flask_api.py

A list of `curl` commands to test the REST API is included in `curl_commands.txt`.

To test the api service using the Front End flask app, open another terminal window and run 

	python front_end.py

This sample uses a simple list of objects as our data store. The principles can be easily transferred to using a backend of your choice.

On the browser go to either `http://localhost:5001` (if running locally) or `http://localhost:8000` (if running in the VM) to view the front end portion.

You can run tests from the command line by running 

	python api_tests.py

## Future Work

This demo/example would work great with a simple mongo backend and ORM implementation in the code.

Also, it would be nice to set up a [Vagrant]('https://www.vagrantup.com/') script for launching a VM with all the dependencies pre-installed so users could see it working without installing and configuring dependencies themselves.

## Acknowledgements

In preparing this demo, I consulted and pulled from a few tutorials online:

* [Designing a RESTful API with Python and Flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [RESTful Authentication with Flask](http://blog.miguelgrinberg.com/post/restful-authentication-with-flask)
* [How to Build an API with Python and Flask](http://tech.pro/tutorial/1213/how-to-build-an-api-with-python-and-flask)
* [PassLib Tutorials](https://pythonhosted.org/passlib/)
