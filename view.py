from app import app
from flask import render_template

@app.route('/')
# @app.route('/blog')
def index():
    name = 'Ivan'
    return render_template('index.html', n=name)
