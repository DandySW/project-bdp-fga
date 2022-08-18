function get_prediction() {
    // var sr = document.getElementById("sr").value;
    // var rr = document.getElementById("rr").value;
    // var t = document.getElementById("t").value;
    // var lm = document.getElementById("lm").value;
    // var bo = document.getElementById("bo").value;
    // var rem = document.getElementById("rem").value;
    // var sr1 = document.getElementById("sr1").value;
    // var hr = document.getElementById("hr").value;

    // const form = document.getElementById("form-prediction").elements[0].value;
    user_input = []
    const elements = document.getElementById("form-prediction").elements;
    for (let element = 0; element < elements.length - 1; element++) {
        user_input.push(elements[element].value);
    }
    console.log(user_input)
    eel.prediction(user_input)

    // console.log([sr, rr, t, lm, bo, rem, sr1, hr])
}
// BENARKAN JAVASCRIPTNYA!!