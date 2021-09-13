'use strict';


$('#form_about').on('submit', (evt) =>{
    evt.preventDefault();

    const formQuery = {
        'nickname': $('#name_details').val(),
        'age': $('#age_year').val(),
        'hobbies':$('#hobbies').val(),
        'movie': $('#fav_movie').val(),
    };

    $.post('/about-user', formQuery, (res) =>{
        alert(res);
    });
});
 