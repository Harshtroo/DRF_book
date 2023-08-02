
var originalDateStr = $("#hidden_public_date").val();

var originalDate = new Date(originalDateStr);
var year = originalDate.getFullYear();
var month = originalDate.getMonth() + 1;
var day = originalDate.getDate();
var formattedDate = `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}`;
$("#publication_date").val(formattedDate)

$("#my-book-edit").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var id = $("#book_id").val();
    var bookUpdateURL = baseURL + "/book_update/" + id + "/";

    var methodType = "PUT";

    var selectedAuthor = $("#author_book option:selected").text();

    var form_data = new FormData($("#my-book-edit")[0]);
    var image = $("#book_image").prop("files")[0];

    if (image) {
        form_data.append("image", image); 
    }
    var Callback = function(response) {

        window.location.href = baseURL + "/get_book_list/";
      };
    postAjaxCall(bookUpdateURL, methodType, form_data,csrfToken,Callback)

})














