from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
import requests
import dotenv
import os


dotenv.load_dotenv()
GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')
APP_SECRET = os.getenv('APP_SECRET')

app = Flask(__name__)
app.secret_key = APP_SECRET
oauth = OAuth(app)

oauth.register(
    name='github',
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET,
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)


@app.route('/')
def root():
    user = session.get('user')
    return render_template('index.html', user=user)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.github.authorize_redirect(redirect_uri)


@app.route('/authorize')
def auth():
    token = oauth.github.authorize_access_token()
    bearer = token['access_token']
    headers = {"Authorization": "Bearer {}".format(bearer)}
    data = requests.get('https://api.github.com/user', headers=headers).json()
    session['user'] = data['login']
    session['repo_name'] = 'foo'
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/home')
def home():
    user = session.get('user')
    repo_name = session.get('repo_name')
    return render_template('home.html', user=user, repo_name=repo_name)


@app.route('/step1')
def step1():
    user = session.get('user')
    return render_template('step1.html', user=user)


@app.route('/step2')
def step2():
    user = session.get('user')
    return render_template('step2.html', user=user)


if __name__ == '__main__':
    app.run()
