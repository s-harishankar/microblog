from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Hari'}
    posts = [
        {
            'author': {'username':'Tom Brady'},
            'body': 'Sports & spirit'
        },
        {
            'author': {'username':'Virat Kohli'},
            'body': 'A Masterclass in Cricket, Country & Courtship'
        }
    ]
    return render_template('index.html',title='Home',user=user, posts = posts)