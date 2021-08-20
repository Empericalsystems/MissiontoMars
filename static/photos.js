
import requests

res = resquests.get('https://mars.nasa.gov/rss/api/?feed=raw_images&category=mars2020&feedtype=json&page=0&num=50&order=sol+asc&search=')

$.getJSON( "https://api.nasa.gov/mars-photos/api/v1/manifests/spirit?status&api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE", 
function( data ) {
    console.log(data);
});

 