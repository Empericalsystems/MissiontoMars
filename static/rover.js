 

'use strict';

 
  
  
 

// let input = $(document).querySelector('input');
// input.adEventListner('keyup', function(){
//     $get('/search?q=' + input.value, function (missionposts_by_title) {
//         let html = '';
//         // for (get_posts_by_title(title) in marstest)
//         for (let id in missionposts_by_title)
//         {
//             let title = missionposts_by_title[id].title;
//             html +='<li>' + title + '</li>';

//         }
//         document.querySelector('ul').innerHTML = html;
//     });
// });



// $(document).ready(function(){
//     $('#search_query').on('input', function (evt){
//         $('#list_titles').empty();
//         $.ajax({
//             method:'post',
//             url: '/search',
//             data: {text:$('#search_query').val()},
//             success: function(res) {
//                 let data = '<ul>';
//                 $.each(res, function (index, value){
//                     data += '<li>' +value.title+'</li>';

//                 });
//                 data += '</ul>';
//                 $('#list_titles').html(data);
//             } 
//             });

//         });
//     } );


// $(document).ready(function(){
//     $('#loginForm').on('submit', (evt) => {

//         let email = $('input[name=email]').val()
        
//         $.ajax({
//              url: "/",
//              type: 'POST',
//              data: email
//             //  dataType: 'json'
//             })
//             .error(function(data) {
//                 alert('Sorry there is an error with your login. Please try again or sign up.');
            
//             })
//             .success(function(data) {
//                 alert(`Welcome back ${email}`); 
                
//             });
//             evt.preventDefault();
//         });
// });

             
        


