function check_prime() {
    const n = parseInt(document.getElementById("input").value);
    const res = document.getElementById("result");

    if (isNaN(n) || n <= 1) {
        res.textContent = "Please enter a number greater than 1";
        res.style.color = "red";
        return;
    }

    let is_prime = true;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            is_prime = false;
            break;
        }
    }

    if (is_prime) {
        res.textContent = `${n} is a Prime Number.`;
        res.style.color = "green";
    }
    else {
        res.textContent = `${n} is a Non-Prime Number.`;
        res.style.color = "blue";
    }
}