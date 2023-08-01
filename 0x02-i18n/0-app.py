from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Returns the index page"""
    return render_template('0-index.html')