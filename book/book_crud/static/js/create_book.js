var createBookURL = baseURL + "/create_book/"
var methodType = "POST"
var successCallBack = baseURL + "/book_list/"


$("#my-create-book").on("submit",function(event){
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    var resultData = {
        name:$("#book_name").val(),
        author:$("#author_book").val(),
        publication_date:$("#publication_date").val(),
        rating :$("#rating").val()
    }
    resultData=JSON.stringify(resultData)

    var Callback = function(response) {
                        window.location.href = "http://127.0.0.1:8000/get_book_list/";
                      };
    postAjaxCall(createBookURL, methodType, resultData,csrfToken,Callback)
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
            console.log("output====================",output)
        }
var resultData = ''
makeAjaxCall(authorURL, authorMethodType, resultData ,callBack)