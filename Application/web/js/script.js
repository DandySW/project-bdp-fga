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
    console.log(predict)
}