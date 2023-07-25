$("#my-create-book").on("submit",function(event){
    event.preventDefault()
    console.log("hello")
    var formData ={
        name:$("#book_name").val(),
        author:$("#author_book").val(),
        publication_date:$("#publication_date").val(),
        rating :$("#rating").val()
    }

    $.ajax({
      type: 'POST',
      url: "http://127.0.0.1:8000/create_book/",
      data: formData,
      dataType: "JSON",
      success: function(resultData) {
        window.location.href = "http://127.0.0.1:8000/get_book_list/"
        }
});



})