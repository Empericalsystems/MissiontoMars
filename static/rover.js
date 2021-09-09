'use strict';

$("#login").on("submit", (evt) =>{
    evt.preventDefault();
    
    $.get("/",  (res)=> {
        alert('You are now logged in');
    });


 
 
// $('form'[0]).on('submit', (evt) => {      
//     evt.preventDefault();   
    
//     let alertSays = document.getElementbyID('alert-text').val();  
//     console.log('alertSays')
//     $.get('/', alertSays, (res) => {
//         alert(res);
//     });
// });