$(document).ready(function(){
$('#bt_plogin').click(() =>{
var usernamepl=$("#usernamepl").val();
  var passwordpl=$("#passwordpl").val();
  console.log(usernamepl,passwordpl)
  var data={
        'csrfmiddlewaretoken' : '{{csrf_token}}',
        'usernamepl' : usernamepl,
        'passwordpl' : passwordpl
  }

  $.ajax({
            url : 'login_valp',
            method : 'POST',
            data : data,

            success : function(data)
            {
                    if(data.exist){


                    alert("Login Successfull!!! ");


                    }
                    else{
                    alert('sorry user is not authenticated');

                    }

            },
            error : function(data)
            {
                    alert("error");
            }

  });
  });

});





