
$("#my-book-edit").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var id = $("#book_id").val();
    var bookUpdateURL = baseURL + "/book_update/" + id + "/";
    var methodType = "PUT";
    var resultData = {
        name:$("#book_name").val(),
        author:$("#author_book").val(),
        publication_date:$("#publication_date").val(),
        rating :$("#rating").val()
    }
    var Callback = function(response) {
        console.log("response======", response);
        window.location.href = "http://127.0.0.1:8000/get_book_list/";
      };
    postAjaxCall(bookUpdateURL, methodType, resultData,csrfToken,Callback)

})