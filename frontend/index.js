let score = 0;
let highscore = 0;

const scoreDisplay = document.getElementById('score');
const highScoreDisplay = document.getElementById('high');
const startButton = document.getElementById('start');

function runGame() {
    fetch('http://127.0.0.1:5000/reset')
    let gameID = setInterval(async () => {
        await fetch('http://127.0.0.1:5000/advance');   // advance in the game
        fetch('http://127.0.0.1:5000/score')
            .then(res=>res.text())
            .then(res=>{
                scoreDisplay.innerText = "Score :" + res;
                highscore = Math.max(highscore, parseInt(res)); // calculate high score
                highScoreDisplay.innerText = "High score: " + highscore.toString();
            });
        fetch('http://127.0.0.1:5000/status')   // check if dead
            .then(res=>res.text())
            .then(res=> {
                if (res == "DEAD") clearInterval(gameID);   // stop loop if dead
            });
    }, 1000);
}

// detecting and 'a' and 'd' keys for left and right respectively
document.addEventListener('keypress', e => {
    if (e.code == "KeyA") fetch('http://127.0.0.1:5000/move?dir=left');
    if (e.code == "KeyD") fetch('http://127.0.0.1:5000/move?dir=right');
});