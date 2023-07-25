
$.ajax({
        type: 'GET',
        url: "http://127.0.0.1:8000/book_list/",
        dataType: 'json',
        success: function (data) {
            output = ""
            for (var i=0;i< data.length;i++){
                output += `
                            <tr>
                                <td scope="row">${data[i].id}</td>
                                <td scope="row">${data[i].name}</td>
                                <td scope="row">${data[i].author}</td>
                                <td scope="row">${data[i].publication_date}</td>
                                <td scope="row">${data[i].rating}</td>
                            </tr>`
            }
            document.getElementById("book_list").innerHTML = output
        },
        error: function (error){
        }
    })