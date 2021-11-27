# https://flask.palletsprojects.com/en/2.0.x/quickstart
# A Minimal Application
# HTML Escaping
# Routing
# Static Files
# Rendering Templates
# Accessing Request Data
# Redirects and Errors
# About Responses
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"