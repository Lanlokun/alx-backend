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
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Select a language translation to use for that request"""
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    
    login_as = request.args.get('login_as')
    if login_as:
        user = get_user(int(login_as))
        if user and user['locale'] in app.config['LANGUAGES']:
            return user['locale']
        
    return request.accept_languages.best_match(app.config['LANGUAGES'])

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """Returns a user dictionary or None if the ID cannot be found"""
    if login_as in users:
        return users.get(login_as)
    return None


@app.before_request
def before_request():
    """Find a user if any, and set it as a global on flask.g.user"""
    login_as = request.args.get('login_as')
    if login_as:
        user = get_user(int(login_as))
        if user:
            from flask import g
            g.user = user
