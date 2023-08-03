



$("#my-library-edit").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var id = $("#library_id").val();
    var bookUpdateURL = baseURL + "/library_update/" + id + "/";
    var methodType = "PUT";
    var selectedAuthor = $("#library_book option:selected").text();
    var form_data = new FormData($("#my-library-edit")[0]);
    console.log("form_data-----------",form_data)
    var Callback = function(response) {
        window.location.href = baseURL + "/get_library_list/";
      };
    postAjaxCall(bookUpdateURL, methodType, form_data,csrfToken,Callback)

})














