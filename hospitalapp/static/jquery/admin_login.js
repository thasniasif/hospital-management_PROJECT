$(document).ready(function(){
$('#bt_logina').click(() =>{
var a_unamel=$("#a_unamel").val();
  var a_passwordl=$("#a_passwordl").val();
  console.log(a_unamel,a_passwordl)
  var data={
        'csrfmiddlewaretoken' : '{{csrf_token}}',
        'a_unamel' : a_unamel,
        'a_passwordl' : a_passwordl
  }

  $.ajax({
            url : 'login_a_vala',
            method : 'POST',
            data : data,

            success : function(data)
            {
                    if(data.exist){


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





