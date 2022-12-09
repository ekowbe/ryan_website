from time import strftime
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
from datetime import datetime
from models.people import people as peeps
from models.articles import reads


# -----------------------------------------------------------------------

app = Flask(__name__, template_folder='templates')

# -----------------------------------------------------------------------

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html = render_template(
        'index.html',
        index=True)
    response = make_response(html)
    return response


@app.route('/people/<person>', methods=['GET'])
def people(person):
    person = peeps[person]
    # print(person)

    html = render_template(
        'people.html',
        person=person,
        index=False
    )

    response = make_response(html)
    return response

@app.route('/work/<topic>', methods=['GET'])
def work(topic):

    html = render_template(
        f'{topic}.html',
        index=False
    )
    response = make_response(html)
    return response

@app.route('/articles', methods=['GET'])
def articles():

    html = render_template(
        'articles.html',
        articles = reads,
        index=False
    )

    response = make_response(html)
    return response

@app.route('/articles/<article_title>', methods=['GET'])
def show_article(article_title):

    html = render_template(
        'article.html',
        article = reads[article_title],
        index=False
    )

    response = make_response(html)
    return response
