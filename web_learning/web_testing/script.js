const colours = [];

function change_background_colour() {
	const input = document.getElementById('colour_input').value.trim();
	if (input) {
		document.body.style.backgroundColor = input;
	}
}

document.addEventListener('DOMContentLoaded', function() {
	const btn = document.querySelector('button[type="submit"]');
	if (btn) {
		btn.addEventListener('click', change_background_colour);
	}
});