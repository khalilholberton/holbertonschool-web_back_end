#!/usr/bin/env python3
""" Simple Flask app """

from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ This class configure available languages in our app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/")
def hello():
    """
    return 1-index.html template
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    This function determine the best match with our supported languages
    """
    locale = request.args.get('locale')  # if key doesn't exist, returns None
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Ths function returns a user dictionary
    """
    userID = request.GET.get('login_as')  # if val doesn't exist, returns None
    if int(userID) in users:
        return users[int(user)]
    return None


@app.before_request
def before_request():
    """
    use get_user to find a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run()
