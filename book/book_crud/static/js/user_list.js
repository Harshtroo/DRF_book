
$.ajax({
        type: 'GET',
        url: "http://127.0.0.1:8000/user_list/",
        dataType: 'json',
        success: function (data) {
            output = ""
            for (var i=0;i< data.length;i++){
                output += `
                            <tr>

                                <td scope="row">${data[i].username}</td>
                                <td scope="row">${data[i].email}</td>
                                <td scope="row">${data[i].phone_number}</td>
                            </tr>`
            }
            document.getElementById("user_list").innerHTML = output
        },
        error: function (error){
        }
    })