var createUserURL = baseURL + "/create_user/"
var methodType = "POST"

$("#my-create-user").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var resultData = {
        username:$("#username").val(),
        email:$("#email").val(),
        password:$("#password").val(),
        phone_number :$("#phone_number").val()
    }
    var Callback = function(response) {
        window.location.href =  "http://127.0.0.1:8000/get_user_list/"
      };
     postAjaxCall(createUserURL, methodType, resultData,csrfToken,Callback)
})


