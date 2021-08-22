 "use strict";
alert('this is a test')

const press = document.forms[0];
    press.addEventListner('submit', () => {
        let alertSays=$('#alert-text').val();
        alert(alertSays)
    });

 