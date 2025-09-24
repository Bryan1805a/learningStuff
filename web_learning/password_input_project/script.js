let input = document.getElementById("pass");
let eye_icon = document.getElementById("eye-icon");

eye_icon.addEventListener("click", function() {
    if (input.type === "password") {
        input.type = "text";
        eye_icon.textContent = "";
    }
    else {
        input.type = "password";
        eye_icon.textContent = "";
    }
})