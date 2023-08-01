from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

@app.route('/')
def index():
    """Returns the index page"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Select a language translation to use for that request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])