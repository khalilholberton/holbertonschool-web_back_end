#!/usr/bin/env python3
""" Simple Flask app """

from flask import Flask, request, render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ This class configure available languages in our app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def hello():
    """
    return 1-index.html template
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    This function determine the best match with our supported languages
    """
    locale = request.args.get('locale')  # if key doesn't exist, returns None
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
