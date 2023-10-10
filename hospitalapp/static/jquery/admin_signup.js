


  $(document).ready(function(){



            $("#a_uname").keyup(function(){

                    var a_uname=$("#a_uname").val()
                    console.log(a_uname)
                    var data={

                        'a_uname' : a_uname
                    }

                    $.ajax({
                           url : 'validate_a_uname',
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




            $("#a_password").keyup(function(){
                    var a_password=$("#a_password").val()

                    var data={

                        'a_password' : a_password
                    }

                    $.ajax({
                           url : 'validate_a_password',
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
