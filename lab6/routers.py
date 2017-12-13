from flask import Flask

app = Flask(__name__)

stream_page = "Hello, want to play?" \
               "<br><br>" \
               "<a href=\"http://localhost:5000/play/1\">Difficulty level - 1</a>" \
               "<br>" \
               "<a href=\"http://localhost:5000/play/2\">Difficulty level - 2</a>" \
               "<br>" \
               "<a href=\"http://localhost:5000/play/3\">Difficulty level - 3</a>"

config_page = "Great, lets begin!" \
            "<br><br>" \
            " So who is this person? <br><br> <img src=\"{0}\" alt=\"Guess who?\">" \
            "<br><br>" \
            "<form action=\"/guess\"> " \
            "Name: <input type=\"text\" name=\"guess_name\">" \
            "<input type=\"submit\" value=\"Submit\"> " \
            "</form>"

body_template = "<html lang=\"en\"><head><meta charset=\"UTF-8\"><title> {0} </title></head><body> {1} </body></html>"

state = dict()

"""
START WITH

$ export FLASK_APP=routers.py
$ export FLASK_DEBUG=1
$ flask run

"""


def wrap_with_body(title, body):
    return body_template.format(title, body)


@app.route('/stream')
def config():
    print("STREAM")
    return wrap_with_body("RSS Config", stream_page)


@app.route('/config')
def config():
    print("CONFIG")
    return wrap_with_body("RSS Config", stream_page)


@app.route('/rss/<int:id>')
def view_rss(id=1):
    print("VIEW")
    return wrap_with_body("RSS Config", stream_page)


@app.route('/rss/<int:id>')
def add_rss(id=1):
    print("ADD")
    return wrap_with_body("RSS Config", stream_page)


@app.route('/rss/<int:id>')
def del_rss(id=1):
    print("DEL")
    return wrap_with_body("RSS Config", stream_page)

