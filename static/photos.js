$.getJSON( "https://api.nasa.gov/mars-photos/api/v1/manifests/spirit?status&api_key=HdOBSFe1XClbPB2aK0CkdKaYXT3pORABCdKDG6aE", 
function( data ) {
    console.log(data);
});


//     const items = [];
//     $.each( data, function( key, val ) {
//       items.push( "<li id='" + key + "'>" + val + "</li>" );
//     });
   
//     $( "<ul/>", {
//       "class": "my-new-list",
//       html: items.join( "" )
//     }).appendTo( "body" );
//   });