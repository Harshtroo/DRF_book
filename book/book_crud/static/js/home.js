var createUserURL = "http://127.0.0.1:8000/create_user/"

$("#id").on("click", function(){
    $.ajax({
            type: 'POST',
            url: createUserURL,
            data: serializedData,
            success: function (data) {

            }
                $("#id").text( data[0].username)
            },
            error: function (error){
            }
})