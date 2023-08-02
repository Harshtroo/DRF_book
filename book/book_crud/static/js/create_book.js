var createBookURL = baseURL + "/create_book/"
var methodType = "POST"
var successCallBack = baseURL + "/book_list/"

$("#my-create-book").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var form_data = new FormData($("#my-create-book")[0]);
    var image = $("#book_image").prop("files")[0];
    form_data.append("image", image);
    let contentType =  false
    let processData = false
    

    var Callback = function(response) {
                         window.location.href = baseURL + "/get_book_list/";
                      };
    postAjaxCall(createBookURL, methodType, form_data,csrfToken,Callback,contentType,processData)
})


var authorURL = baseURL + "/author_list/"
var authorMethodType = "GET"
var callBack = function (data) {
            output = ""
            for (var i=0;i< data.length;i++){
             output += `
                <option value=${data[i].id}>${data[i].name}</option>
                `
            document.getElementById("author_book").innerHTML = output
            }
        }
var resultData = ''
makeAjaxCall(authorURL, authorMethodType, resultData ,callBack)