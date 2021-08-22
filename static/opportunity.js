"use strict";

// const imp_express = require('express');
// const https = require('https');   //https://nodejs.org/api/https.html
// const cur_app = express();


// cur_app.get('/curiosity')

// $.getJSON('https://api.nasa.gov/planetary/apod'
// , function(data){
//     console.log(data);

// });


$.ajax({
    dataType: "json",
    url: 'https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/latest_photos?api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
    data: data,
    success: success
  });