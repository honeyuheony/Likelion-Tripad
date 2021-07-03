window.onload = function() {
    // Get the modal
    var mobile_modal = document.getElementById('mobileModal');
    var pay_modal = document.getElementById('payModal');
    var icon_modal = document.getElementById('iconModal');
    
    // Get the button that opens the modal
    var mobile_btn = document.getElementById('mobile_btn');
    var pay_btn = document.getElementById('pay_btn');
    var icon_btn = document.getElementById('icon_btn');

    // Get the <span> element that closes the modal
    var mobile_span = document.getElementById("mobile_close");
    var pay_span = document.getElementById("pay_close");
    var icon_span = document.getElementById("icon_close");                                       

    // When the user clicks on the button, open the modal 

    mobile_btn.onclick = function() {
        mobile_modal.style.display = "block";
    }
    pay_btn.onclick = function() {
        pay_modal.style.display = "block";
    }
    icon_btn.onclick = function() {
        icon_modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    mobile_span.onclick = function() {
        mobile_modal.style.display = "none";
    }
    pay_span.onclick = function() {
        pay_modal.style.display = "none";
    }
    icon_span.onclick = function() {
        icon_modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == mobile_modal) {
            mobile_modal.style.display = "none";
        }
        if (event.target == pay_modal) {
            pay_modal.style.display = "none";
        }
        if (event.target == icon_modal) {
            icon_modal.style.display = "none";
        }
    }
}