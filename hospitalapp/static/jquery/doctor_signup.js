


  $(document).ready(function(){



            $("#username").keyup(function(){

                    var username=$("#username").val()
                    console.log(username)
                    var data={

                        'username' : username
                    }

                    $.ajax({
                           url : 'validate_username',
                           method : 'POST',
                           data : data,

                           success : function (data){

                                if(data.is_taken)
                                {
                                 $('#error_span').html('username is already taken.Try again');





                                }
                                else{

                                  $('#error_span').html('');



                                }


                           },
                           error : function(data){
                           console.log('error')
                           }
                    });


            });




            $("#password").keyup(function(){
                    var password=$("#password").val()

                    var data={

                        'password' : password
                    }

                    $.ajax({
                           url : 'validate_password',
                           method : 'POST',
                           data : data,

                           success : function (data){

                                if(data.is_taken){
                                $('#pass_span').html('password is already taken.Try again');

                                }
                                else{
                                $('#pass_span').html('');

                                }
                           }

                    });



            });
            });
//
// alert("hello")
// $('#signup_btn').click(() =>{
//    alert("hi")
//    console.log('hi')
//    });
