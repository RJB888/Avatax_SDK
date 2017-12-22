"""Flask App Module."""
from flask import Flask, render_template
from methods import ping, create, commit
from client import AvataxClient
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask import render_template, flash, redirect
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
client = AvataxClient('test_app', '0', 'machine', 'sandbox')
client.add_credentials(os.environ.get('USERNAME', ''), os.environ.get('PASSWORD', ''))
comp_code = 'DEFAULT'
trans_code = ''


class CreateForm(FlaskForm):
    model = TextAreaField('Request Body', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    submit = SubmitField('call_api')


class CommitForm(FlaskForm):
    model = TextAreaField('Transaction Code', validators=[DataRequired()])
    submit = SubmitField('commit_call')


@app.route('/')
def home():
    """Home route function."""
    return render_template('index.html')


@app.route('/ping')
def ping_view(resp=None):
    """Ping route function."""
    js = client.ping().json()
    return render_template(
        'index.html',
        response=js)


@app.route('/create', methods=['GET', 'POST'])
def create_view(resp=None):
    """Create route function."""
    form = CreateForm()
    js = ''
    if form.validate_on_submit():
        js = client.create_transaction(None, json.loads(form.model.data)).json()
        js = json.dumps(js, indent=4)
    return render_template('create.html', title='api_call', form=form, response=js)


@app.route('/commit', methods=['GET', 'POST'])
def commit_view(resp=None):
    """Commit route function."""
    form = CommitForm()
    js = ''
    if form.validate_on_submit():
        js = client.commit_transaction('DEFAULT', form.model.data).json()
        js = json.dumps(js, indent=4)
    return render_template('create.html', title='api_call', form=form, response=js)
