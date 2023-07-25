var createUserURL = "{% url 'create_user' %}"

$("#id").on("click", function(){
    $.ajax({
            type: 'POST',
            url: "http://127.0.0.1:8000/create_user/",
            data: serializedData,
            success: function (data) {

            }
                $("#id").text( data[0].username)
            },
            error: function (error){
            }
})