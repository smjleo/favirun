const rowInput = document.getElementById('row');
const columnInput = document.getElementById('column');
const favicon = document.getElementById('favicon');

function displayPixel() {
    let column = columnInput.value;
    let row = rowInput.value;
    setInterval(() => {
        fetch('http://127.0.0.1:5000/render?r=' + row + '&c=' + column)
            .then(res => res.text())
            .then(body => {
                switch (body) {
                    case '0':
                        favicon.setAttribute('href', './assets/grey.ico');
                        break;
                    case '1':
                        favicon.setAttribute('href', './assets/red.ico');
                        break;
                    case '2':
                        favicon.setAttribute('href', './assets/blue.ico');
                        break;
                }
            });
    }, 100);
}

