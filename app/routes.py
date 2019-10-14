from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Karan'}
    posts = [
        {
            'author': {'username': 'Namal'},
            'body': 'Hmm...'
        },
        {
            'author': {'username': 'Karan'},
            'body': 'Marianne on Netflix was a scary show!'
        },
        {
            'author': {'username': 'Snehal'},
            'body': 'The Mazda MX-5 is the best looking car :)'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
