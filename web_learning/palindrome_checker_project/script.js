document.getElementById("check").addEventListener("click", function() {
    const input = document.getElementById("input").value.trim();
    const result = document.getElementById("result");

    if (input) {
        const norm = input.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
        const rev = norm.split("").reverse().join("");

        if (norm === rev) {
            result.textContent = `"${input}" is a palindrome!`;
            result.style.color = "green";
        }
        else {
            result.textContent = `"${input}" is not a palindrome.`;
            result.style.color = "red";
        }
    }
    else {
        result.textContent = "Please enter some text.";
        result.style.color = "orange";
    }
});