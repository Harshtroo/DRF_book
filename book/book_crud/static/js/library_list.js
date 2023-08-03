
var bookListURL = baseURL + "/library_list/"
var methodType = "GET"

var callBack = function (data) {
            output = ""
            for (var i=0;i< data.length;i++){
                output += `
                            <tr>
                                <td scope="row">${data[i].id}</td>
                                <td scope="row">${data[i].name}</td>
                                <td scope="row">${data[i].book}</td>

                                <td><a type="button" class="btn btn-primary" href="/get_update_library/${data[i].id}" >Edit</a></td>

                                <td><button type="button" class="btn btn-primary" onclick="libraryDelete(${data[i].id})">Delete</button></td>

                            </tr>`
            }
            document.getElementById("library_list").innerHTML = output
        }

var resultData = ''
makeAjaxCall(bookListURL, methodType, resultData ,callBack)


function libraryDelete(id){
    var libraryDeleteURL = baseURL + "/library_delete/" + id + "/";
    var methodType = "DELETE";
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    resultData = ''

    var callBack = function(response) {
        window.location.reload();
      };
      postAjaxCall(libraryDeleteURL, methodType, resultData,csrfToken,callBack)

}