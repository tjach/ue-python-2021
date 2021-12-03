# https://flask.palletsprojects.com/en/2.0.x/quickstart
# A Minimal Application
# HTML Escaping
# Routing
# Static Files
# Rendering Templates
# Accessing Request Data
# Redirects and Errors
# About Responses


from flask import Flask, url_for, render_template, request
from markupsafe import escape
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route("/foo")
# def handle_foo():
#     return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    url_for('static', filename='plik.txt')
    return f"Hello, {escape(name)}!"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('templatka.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/login')
def login():
    redirect("endpoint", 202)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

from flask import jsonify

@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])