document.addEventListener('DOMContentLoaded', function() {
    const change_Color_Btn = document.getElementById('change-colour-btn');
    const reset_color_btn = document.getElementById('reset_colour_btn');
    const current_color_span = document.getElementById('current_colour')

    const colors = [
            '#f0f8ff', '#faebd7', '#7fffd4', '#f0ffff', '#f5f5dc', 
            '#ffe4c4', '#ffebcd', '#8a2be2', '#a52a2a', '#deb887',
            '#5f9ea0', '#7fff00', '#d2691e', '#ff7f50', '#6495ed',
            '#ff69b4', '#cd5c5c', '#f08080', '#e6e6fa', '#ffa07a'
        ];

    const original_colour = '#f0f8ff';

    function get_random_colour() {
        const random_index = Math.floor(Math.random() * colors.length);
        return colors[random_index]
    }

    function reset_background_colour() {
        document.body.style.backgroundColor = original_colour;
        current_color_span.textContent = original_colour;
        current_color_span.className = '';
    }

    change_Color_Btn.addEventListener('click', function() {
        const new_colour = get_random_colour();
        document.body.style.backgroundColor = new_colour;
        current_color_span.textContent = new_colour;
        current_color_span.className = 'hex-code';
    });

    reset_color_btn.addEventListener('click', reset_background_colour);

});