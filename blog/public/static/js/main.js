function showalert(message,alerttype) {

    $('#alert_placeholder').append('<div id="alertdiv" class="mt-5 alert ' +  alerttype + '"><a class="close" data-dismiss="alert">×</a><span>'+message+'</span></div>')

    setTimeout(function() { // this will automatically close the alert and remove this if the users doesnt close it in 5 secs


      $("#alertdiv").remove();

    }, 5000);
  }


function login() {
    var csrf = document.getElementById('csrf').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // if (username == '' || password == '') {
    //     alert('Enter username as well as password')
    // }

    var data = {
        'username': username,
        'password': password
    }

    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        'body': JSON.stringify(data) 
    }).then(result => result.json())
    .then(response => {
        
        if(response.status==200) {
            window.location.href = '/'
        }
        else {
            showalert(response.message, 'alert-danger')
        }
    })
}



function register() {
    var csrf = document.getElementById('csrf').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // if (username == '' || password == '') {
    //     alert('Enter username as well as password')
    // }

    var data = {
        'username': username,
        'password': password
    }

    fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        'body': JSON.stringify(data) 
    }).then(result => result.json())
    .then(response => {
        if(response.status==200) {
            window.location.href = '/'
        }
        else {
            showalert(response.message, 'alert-danger')
        }
    })
}
