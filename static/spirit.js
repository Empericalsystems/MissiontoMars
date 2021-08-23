'use strict';
 

const url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE&earth_date=2005-9-3' 
    
 

async function sendSpiritAPI(){
    let response = await fetch (url)
    let data = await response.json()
    console.log(data)
    filterSpiritAPI(data)
}

function filterSpiritAPI(data){
    document.querySelector("#content").innerHTML += '<img src="' + data.photos[0].img_src + '" />'
}

sendSpiritAPI();