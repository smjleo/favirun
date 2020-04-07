# Favirun
Favirun is an extremely simple infinite runner game with a slight twist: the game is displayed on a 3x4 grid of favicons. [Video demo](https://youtu.be/oyQh9jWlNg0)

## How it works
The game runs on a Flask server, which communicates the current game information to all the tabs. Each individual 'pixel' websites receive what to display, and changes its favicon accordingly. Additionally, there is a 'master' website that starts the game and displays the score.

## Why?
Why not?

## Try it yourself
First, clone the repo. To start the Flask server, go to `favirun/backend` and type in `flask run`. For the 'pixels', open 12 tabs of `display.html` on Google Chrome and arrange it as shown in the video. You can pin the tabs on Chrome to make the tabs only show the favicon. Open `index.html` and press the button to start the game.
