
'use strict';



const url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE'

async function sendCuriosityAPI() {
    let response = await fetch (url);  //https://www.geeksforgeeks.org/how-to-use-the-javascript-fetch-api-to-get-data/
    console.log(response)
    let data = await response.json()
    console.log(data)
    filterAPI(data)

}

function filterAPI(data){
    document.querySelector("#content").innerHTML += '<img src="' + data.photos[0].img_src + '" />'

}

sendCuriosityAPI();