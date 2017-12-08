from flask import Flask, request

import guesswho

app = Flask(__name__)

welcome_page = "Hello, want to play?" \
               "<br><br>" \
               "<a href=\"http://localhost:5000/play/1\">Difficulty level - 1</a>" \
               "<br>" \
               "<a href=\"http://localhost:5000/play/2\">Difficulty level - 2</a>" \
               "<br>" \
               "<a href=\"http://localhost:5000/play/3\">Difficulty level - 3</a>"

game_page = "Great, lets begin!" \
            "<br><br>" \
            " So who is this person? <br><br> <img src=\"{0}\" alt=\"Guess who?\">" \
            "<br><br>" \
            "<form action=\"/guess\"> " \
            "Name: <input type=\"text\" name=\"guess_name\">" \
            "<input type=\"submit\" value=\"Submit\"> " \
            "</form>"

guessed_page = "{0} <br><br><a href=\"http://localhost:5000/play/{1}\">Try again</a>"

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


@app.route('/')
def init_game():
    guesswho.setup()
    return wrap_with_body("Lets play?", welcome_page)


@app.route('/play/<int:diff>')
def game(diff=1):
    game_name, game_link = guesswho.get_pic_link(diff)
    state.update({1: diff})
    state.update({2: game_name})
    print(game_name)
    return wrap_with_body("Game", game_page.format(game_link))


@app.route('/guess')
def guess():
    guess_name = request.args.get('guess_name')
    name_to_guess = state.get(2)
    diff_chosen = state.get(1)
    response = "Ops.. not guessed"

    print(guess_name)
    print(name_to_guess)

    if name_to_guess is None:
        response = "Can see that you even played boooooiiii"
    elif guess_name is not None and guess_name == name_to_guess:
        response = "Damn right! It really was {0}".format(name_to_guess)
    elif guess_name is None:
        response = "Can't see your answer, try again?"
    return wrap_with_body("Guess", guessed_page.format(response, diff_chosen))
