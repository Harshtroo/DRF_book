var createLibraryURL = baseURL + "/create_library/"
var methodType = "POST"


$("#my-create-library").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var form_data = new FormData($("#my-create-library")[0]);
    console.log("form_data=========",form_data)
    var Callback = function(response) {
                         window.location.href = baseURL + "/get_library_list/";
                      };
    postAjaxCall(createLibraryURL, methodType, form_data,csrfToken,Callback)
})

