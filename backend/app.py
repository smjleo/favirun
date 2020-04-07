from game import Game
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
game = Game()

CORS(app)

@app.route('/')
def hello_world():
    return 'alamak wrong page sia'

@app.route('/move')
def move():
    direction = request.args.get('dir') # direction of movement
    if direction == 'left':
        game.moveleft()
        return 'OK'
    if direction == 'right':
        game.moveright()
        return 'OK'
    return 'INVALID DIRECTION'  # wasn't left nor right

@app.route('/score')
def score():
    return str(game.score)

@app.route('/render')
def render():
    r = int(request.args.get('r'))   # row number (0 - 3)
    c = int(request.args.get('c'))   # column number (0 - 2)
    return str(game.board[r][c])

@app.route('/advance')
def advance():
    game.advance()
    return 'OK'

@app.route('/reset')
def reset():
    game.reset()
    return 'OK'

@app.route('/status')
def status():
    if game.alive:
        return "ALIVE"
    return "DEAD"