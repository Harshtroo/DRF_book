var homeURL = baseURL + "/create_user/"
var methodType = "POST"

$("#id").on("click", function(){
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val()
        var resultData = ''
        var Callback = function(response) {
        window.location.href =  "http://127.0.0.1:8000/get_user_list/"
      };
      postAjaxCall(homeURL, methodType, resultData,csrfToken,Callback)

})