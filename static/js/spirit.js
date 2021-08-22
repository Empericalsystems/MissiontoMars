
 const url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE&earth_date=2005-9-3'


$.getJSON (url, function (data){
    console.log(data);

    $each(data,function(index, value) {
        console.log(value);

        const name = value.rover.name;        //find this by using the value 
        console.log(name);
        const picture = value.img_src;
        console.log(picture);
        
    });
});
