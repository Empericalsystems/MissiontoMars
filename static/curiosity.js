
'use strict';



const url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE'

async function sendCuriosityAPI() {
    let response = await fetch (url); 
    console.log(response)
    let data = await response.json()
    console.log(data)
    displayCur(data)

}

function displayCur(data){
    document.querySelector("#cur_pic").innerHTML ='<img src="' + data.photos[0].img_src + '" />'

}
sendCuriosityAPI();