var createBookURL = baseURL + "/create_book/"
var methodType = "POST"
var successCallBack = baseURL + "/book_list/"


$("#my-create-book").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var resultData = {
        name:$("#book_name").val(),
        author:$("#author_book").val(),
        publication_date:$("#publication_date").val(),
        rating :$("#rating").val()
    }

    var Callback = function(response) {

                        window.location.href = "http://127.0.0.1:8000/get_book_list/";
                      };
    postAjaxCall(createBookURL, methodType, resultData,csrfToken,Callback)
})
