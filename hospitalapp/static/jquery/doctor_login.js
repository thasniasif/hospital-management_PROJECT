$(document).ready(function(){
$('#bt_login').click(() =>{
var usernamel=$("#usernamel").val();
  var passwordl=$("#passwordl").val();
  console.log(usernamel,passwordl)
  var data={
        'csrfmiddlewaretoken' : '{{csrf_token}}',
        'usernamel' : usernamel,
        'passwordl' : passwordl
  }

  $.ajax({
            url : 'login_val',
            method : 'POST',
            data : data,

            success : function(data)
            {
                    if(data.exist){
                    $('#errorl_span').html('');

                    alert("Login Successfull!!! ");


                    }
                    else{
                    alert('sorry user is not authenticated');
//                     $('#errorl_span').html('sorry user is not authenticated');

                    }

            },
            error : function(data)
            {
                    alert("error");
            }

  });
  });

});





