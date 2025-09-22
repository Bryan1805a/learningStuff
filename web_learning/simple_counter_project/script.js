let c = 0;
let ci = 0;
let cd = 0;

const count = document.getElementById("count");
const inc_count = document.getElementById("inc_count");
const dec_count = document.getElementById("dec_count");

function inc() {
    c++;
    ci = (ci >= 10) ? 0: ci + 1;
    update();
}

function dec() {
    c = c > 0 ? c - 1 : 0;
    cd = (cd >= 10) ? 0 : cd + 1;
    update();
}

function update() {
    count.textContent = c;
    inc_count.textContent = ci;
    dec_count.textContent = cd;
}