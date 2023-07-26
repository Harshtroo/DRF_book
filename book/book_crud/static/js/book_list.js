
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
                                <td><button type="button" class="btn btn-primary" id="bookbtn_${data[i].id}" onclick="bookEdit()">Edit</button></td>

                                <td><button type="button" class="btn btn-primary">Delete</button></td>

                            </tr>`
            }
            document.getElementById("book_list").innerHTML = output
        }

var resultData = ''

makeAjaxCall(bookListURL, methodType, resultData ,callBack)


function bookEdit(){
    console.log("data")
    var bookUpdateURL = baseURL + "/book_update/<int:pk>/"
    var methodType = "GET"
    var callBack = function (data) {
        console.log("data",data)
    }
}