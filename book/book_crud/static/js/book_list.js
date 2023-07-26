
var bookListURL = baseURL + "/book_list/"
var methodType = "GET"

var callBack = function (data) {
            output = ""
            for (var i=0;i< data.length;i++){
                output += `
                            <tr>
                                <td scope="row">${data[i].id}</td>
                                <td scope="row">${data[i].name}</td>
                                <td scope="row">${data[i].author}</td>
                                <td scope="row">${data[i].publication_date}</td>
                                <td scope="row">${data[i].rating}</td>
                                <td><a type="button" class="btn btn-primary" href="/get_update_data/${data[i].id}" >Edit</a></td>

                                <td><button type="button" class="btn btn-primary" onclick="bookDelete(${data[i].id})">Delete</button></td>

                            </tr>`
            }
            document.getElementById("book_list").innerHTML = output
        }

var resultData = ''

makeAjaxCall(bookListURL, methodType, resultData ,callBack)


function bookDelete(id){

    var bookDeleteURL = baseURL + "/book_delete/" + id + "/";
    var methodType = "DELETE"; 
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    
    resultData = ''
    
    var callBack = function(response) {
        console.log("response======", response);
        window.location.href = "http://127.0.0.1:8000/get_book_list/";
      };
      postAjaxCall(bookDeleteURL, methodType, resultData,csrfToken,callBack)

}