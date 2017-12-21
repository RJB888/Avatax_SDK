from flask import Flask, render_template
from methods import ping, create, commit

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ping')
def ping_view(resp=None):
    url, verb, resp = ping()
    return render_template(
        'index.html',
        response=resp,
        url=url,
        verb=verb)



@app.route('/create')
def create_view(resp=None):
    url, verb, request, resp = create()
    return render_template(
        'index.html',
        request=request,
        response=resp,
        url=url,
        verb=verb)


@app.route('/commit')
def commit_view(resp=None):
    url, verb, request, resp = commit()
    return render_template(
        'index.html',
        request=request,
        response=resp,
        url=url,
        verb=verb)

