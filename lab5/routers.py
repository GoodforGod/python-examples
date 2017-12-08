from flask import Flask

import guesswho

app = Flask(__name__)


welcome = "Hello, Lets play?" \
          + "<br><br>" \
          + "<a href=\"http://localhost:5000/play/1\">Difficulty level - 1</a>" \
          + "<br>" \
          + "<a href=\"http://localhost:5000/play/2\">Difficulty level - 2</a>" \
          + "<br>" \
          + "<a href=\"http://localhost:5000/play/3\">Difficulty level - 3</a>"

game = "Hello, Lets play? <br><br> So who is this person? <br><br> <img src=\"{0}\"  alt=\"Guess who?\">"

body = "<html lang=\"en\"> <head> <meta charset=\"UTF-8\"> <title> {0} </title> </head> <body> {1} </body> </html>"


def wrapWithBody(title, body):
    return body.format(title, body)


@app.route('/')
def init_game():
    guesswho.setup()
    return wrapWithBody("Lets play?", welcome)


@app.route('/play/<int:diff>')
def hello_world(diff):
    print(diff)
    game_name, game_link = guesswho.get_pic_link(diff)

    print(game_name)
    print(game_link)
    return wrapWithBody("play", game.format(game_link))

