'use strict';


$('#form_search').on('submit', (evt) =>{
    evt.preventDefault();

    const formQuery = {
        'search_title': $('#search_title').val()
      
    };

    $.post('/search', formQuery, (res) =>{
    
        res.json().forEach((item) =>{
            console.log(item);
            $('#blog').append(item);
        });
    });
});

  
 