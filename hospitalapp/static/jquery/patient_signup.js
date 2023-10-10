


  $(document).ready(function(){



            $("#username_pat").keyup(function(){

                    var username=$("#username_pat").val()
                    console.log(username_pat)
                    var data={

                        'username_pat' : username_pat
                    }

                    $.ajax({
                           url : 'validate_username_pat',
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




            $("#password_pat").keyup(function(){
                    var password=$("#password_pat").val()

                    var data={

                        'password_pat' : password_pat
                    }

                    $.ajax({
                           url : 'validate_password_pat',
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
