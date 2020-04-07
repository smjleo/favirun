# Favirun
Favirun is an extremely simple infinite runner game with a slight twist: the game is displayed on a 3x4 grid of favicons. [Video demo](https://youtu.be/oyQh9jWlNg0)

## How it works
The game runs on a Flask server, which communicates the current game information to all the tabs. Each individual 'pixel' websites receive what to display, and changes its favicon accordingly. Additionally, there is a 'master' website that starts the game and displays the score.

## Why?
Why not?

## Dependencies
* Python 3

* Flask

## Try it yourself
1. Clone the repo:   
```
git clone https://github.com/smjleo/favirun
```

2. Start the Flask server:  
```
cd favirun/backend
flask run
```
3. For the 'pixels', open 12 tabs of `display.html` on Google Chrome and arrange it as shown in the video. You can pin the tabs on Chrome to make the tabs only show the favicon. 

4. For each pixel, set the row and column values. The top left corner is `(0, 0)` and the bottom right corner is `(3, 2)`.

5. Open `index.html` and press the 'Start game' button to start the game.
