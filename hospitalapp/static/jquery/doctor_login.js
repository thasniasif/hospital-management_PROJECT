$(document).ready(function(){
$('#bt_login').click(() =>{
var username=$("#username").val();
  var password=$("#password").val();
  var data={
        'csrfmiddlewaretoken' : '{{csrf_token}}',
        'username' : username,
        'password' : password
  }
  if(username==''){
  alert("enter valid username");
  }
  else if(password==''){
  alert("enter valid password");
  }
  else{
  alert("not authenticated");
  console.log(username,password);
//  $.ajax({
//            url : 'login_val',
//            method : 'POST',
//            data : data,
//
//            success : function(data)
//            {
//                    if(data.exist){
//                    alert("user logged in ");
//
//                    window.location.replace('doctor_login2')
//                    }
//                    else{
//                    alert("user not authenticated ");
//                    }
//
//            },
//            error : function(data)
//            {
//                    alert("error");
//            }
//
//  });
  }

});

});



