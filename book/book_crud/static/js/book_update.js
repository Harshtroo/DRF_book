
const originalDateStr = $("#hidden_public_date").val();
const originalDate = new Date(originalDateStr);
const year = originalDate.getFullYear(); 
const month = originalDate.getMonth() + 1; 
const day = originalDate.getDate(); 
const formattedDate = `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
$("#publication_date").val(formattedDate) 

$("#my-book-edit").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var id = $("#book_id").val();
    var bookUpdateURL = baseURL + "/book_update/" + id + "/";

    var methodType = "PUT";

    var selectedAuthor = $("#author_book option:selected").text();
    var resultData = {
        name:$("#book_name").val(),
        author:$("#author_book").val(),
        publication_date:$("#publication_date").val(),
        rating :$("#rating").val()
    }
    resultData=JSON.stringify(resultData)
    var Callback = function(response) {

        window.location.href = "http://127.0.0.1:8000/get_book_list/";
      };
    postAjaxCall(bookUpdateURL, methodType, resultData,csrfToken,Callback)

})














