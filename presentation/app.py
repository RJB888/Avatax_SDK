"""Flask App Module."""
from flask import Flask, render_template
from methods import ping, create, commit
from client import AvataxClient
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template, flash, redirect
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
client = AvataxClient('test_app', '0', 'machine', 'sandbox')
client.add_credentials(os.environ.get('USERNAME', ''), os.environ.get('PASSWORD', ''))


class CreateForm(FlaskForm):
    model = StringField('model', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    submit = SubmitField('call_api')


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
    js = None
    if form.validate_on_submit():
        # import pdb; pdb.set_trace()
        js = client.create_transaction(None, json.loads(form.model.data)).json()
        js = json.dumps(js, indent=4, sort_keys=True)
        import pdb; pdb.set_trace()
    return render_template('create.html', title='api_call', form=form, response=js)


@app.route('/commit')
def commit_view(resp=None):
    """Commit route function."""
    url, verb, request, resp = commit()
    return render_template(
        'index.html',
        request=request,
        response=resp,
        url=url,
        verb=verb)
