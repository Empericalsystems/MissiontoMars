'use strict';

/* <input type="date" id="mission_date_2" name="earth_date"
      min="2004-01-04" max="2010-03-22" onchange='this.form.submit()' ></input> */

$(document).ready (() =>
    $("#mission_date1").datepicker({
        minDate: "2012-08-06",
        showButtonPanel: true
    })
)


$(document).ready (() =>
    $("#mission_date2").datepicker({
        minDate: "2004-01-04",       //spirit
        maxDate: "2010-03-22",
        showButtonPanel: true
    })
)

$(document).ready (() =>
    $("#mission_date3").datepicker({
        minDate: "2004-01-25",          //opportunity
        maxDate: "2018-06-10",
        showButtonPanel: true
    })
)

// $(document).ready (() =>
//     $("#mission_date").datepicker({
//         minDate: "2012-08-06",         //curiosity
//         showButtonPanel: true
//     })
// )



