"use strict";

// let api_key = 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE';
// let earth_date = '2004-09-25';
// let url = new url ('https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?');
// let params = new urlSearchParams.append('api_key', 'earth_date'); 
// params.toString();
// url.search = params;
// url.href


// api_key' : 'HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE',
// 'earth_date': '2004-09-25'


const chooseDate = document.forms[0];  //to access the submit button since we had no ID so accessing form with index0
    subPress.addEventListener('submit', ()=> { //listening for submit event for callback to execute
        let alertSays = $('#alert-text').val(); //creating a object that will hold the info - from class notes
        alert(alertSays);
    });

const url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE&earth_date=2015-9-3' 
    
 

async function sendOppAPI(){
    let response = await fetch (url) //can you enter cache/no-cache here? check MDN and textbook
    let data = await response.json() //data.photos[0].img_src is where the image url is
    console.log(data) //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse
    displayOpp(data)    
}
function displayOpp(data) {
  document.querySelector('#photo').innerHTML = '<img src="' + data.photos[1].img_src + '"/>'
} //manipulating the dDOM to display the photo - 
    //why won't $('#photo') work here???  

sendOppAPI();



// async function sendOppAPI(){
//   let response = await fetch (url, {
//   method : 'POST',
//   cache : 'force-cache',
//   body: JSON.stringify (data)
//   }}) //can you enter cache/no-cache here? check MDN and textbook
//   let data = await response.json()
//   console.log(data.photos[0].img_src) //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse
//   return data.sendOppAPI;
// }