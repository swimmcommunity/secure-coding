In this Playlist we will get to know important coding practices when dealing with web applications. As an example, we will use [Flask](https://palletsprojects.com/p/flask/). Most of the Units will be relevant for any web framework, but some will be specific to Flask.

Even if you are not acquainted with Flask, we are sure you can gain a lot from this playlist.

# What is Flask?
> Flask is a lightweight [WSGI](https://wsgi.readthedocs.io/) web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around [Werkzeug](https://palletsprojects.com/p/werkzeug) and [Jinja](https://palletsprojects.com/p/jinja) and has become one of the most popular Python web application frameworks. ([Source](https://palletsprojects.com/p/flask/))

# A small Flask app
Look how easy it is to create a web app with Flask:
```
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```

# Make sure you can run our Flask server
In the upcoming Units we will use a Flask server.

Make sure you have `Flask` installed:

`pip3 install Flask`

Then run:

`python3 ./python/server.py`

Next, open your browser, and browse to:
`http://127.0.0.1:5000/`

You should be able to see this greeting message:

![image.png](https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FqCAjeLJBCFTjhwWoTpZo%2Fimg%2F0ee3e027-509c-4799-a5c7-4b673cc9401a.png?alt=media&token=17ca4acc-acc4-40b0-8f0d-a97bdd36f2d7)

# Hands-on Units
Sometimes you will have walkthroughs to read through, and sometimes - hands-on Units to solve. In this case you will be asked to make some tests pass (use `swimm test` as a shortcut for that) and will be presented with the files necessary for you to edit after you `swimm play`.