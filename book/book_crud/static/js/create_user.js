var createUserURL = baseURL + "/create_user/"
var methodType = "POST"

$("#my-create-user").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var contentType =  'application/json'
    var processData =  false
    var resultData = {
        username:$("#username").val(),
        email:$("#email").val(),
        password:$("#password").val(),
        phone_number :$("#phone_number").val()
    }
    resultData=JSON.stringify(resultData)
    var Callback = function(response) {
        window.location.href = baseURL + "/get_user_list/"
      };
     postAjaxCall(createUserURL, methodType, resultData,csrfToken,Callback,contentType,processData)
})


