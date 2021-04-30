from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app


posts = [
    {'author': 'Evgenii',
    'title': 'Post #1',
    'content': 'The first post.',
    'date': '01.04.2021'
    },
    {'author': 'Kate',
    'title': 'Post #2',
    'content': 'The second post.',
    'date': '02.04.2021'
    }    
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title=True)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account was created for: {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful! Try it again.', 'danger')
    return render_template('login.html', title='Login', form=form)