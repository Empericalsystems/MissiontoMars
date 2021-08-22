 "use strict";


const press = document.forms[0];
    press.addEventListner('submit', () => {
        let alertSays=$('#alert-text').val();
        alert(alertSays)
    });

 
//  const imp_express = require('express');
//  const https = require('https');   //https://nodejs.org/api/https.html
//  const app = express();

const url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE'

//  app.get('/curiosity', function (req, res){
//      htpps.get(url, function(response){
//          console.log (response);

//      })
//  })

//https://api.jquery.com/jQuery.getJSON/

$.getJSON(url, function(data){
    console.log(data);

});

 


// $.ajax({
//   dataType: "json",
//   url: url,
//   data: data,
//   success: success
// });


