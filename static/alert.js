'use-strict';


let modal = $("#myModal");

let span = $(".close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.css("display" , "none");
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  
  if (event.target == modal) {
    modal.css("display" , "none");
  }
} 

$("#register").on("submit", (evt) => {
    evt.preventDefault();

    let input = evt.target.children;

    const data = {
        "email": input[0].children[0].value,
        "password": input[1].children[0].value
    };
    
    $.post("/users", data, (res) => {
      
      $("#modal_text").text(res);
      $("#myModal").css("display", "block");
    });
});


$("#loginForm").on("submit", (evt) => {
  evt.preventDefault();

  let input = evt.target.children;

  const data = {
      "email": input[0].children[0].value,
      "password": input[1].children[0].value
  };
  
  $.post("/login", data, (res) => {
    
    $("#modal_text").text(res);
    $("#myModal").css("display", "block");
  });
});

// element that created the event - getting the children of that - the 3 paragrahs the 1st two email and passwor
// the other is the button. get the array of childre - get the first 
