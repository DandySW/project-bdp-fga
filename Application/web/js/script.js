window.addEventListener('contextmenu', function (e) {
    e.preventDefault();
}, false);

document.onkeydown = function (e) {

    // disable F12 key
    if (e.keyCode == 123) {
        return false;
    }

    // disable I key
    if (e.ctrlKey && e.shiftKey && e.keyCode == 73) {
        return false;
    }

    // disable J key
    if (e.ctrlKey && e.shiftKey && e.keyCode == 74) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 74) {
        return false;
    }

    // disable U key
    if (e.ctrlKey && e.keyCode == 85) {
        return false;
    }

    // disable S key
    if (e.ctrlKey && e.keyCode == 83) {
        return false;
    }
}


function get_prediction() {
    user_input = []
    const elements = document.getElementById("form-prediction").elements
    for (let element = 0; element < elements.length - 1; element++) {
        user_input.push(elements[element].value)
    }
    console.log(user_input)
    eel.prediction(user_input)(set_prediction)
}


function set_prediction(predict) {
    document.getElementById("label").innerHTML = "Tingkat stres anda termasuk dalam kategori " + predict[0] + " (" + predict[1] + ")"
}