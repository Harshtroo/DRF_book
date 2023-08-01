var createBookURL = baseURL + "/create_book/"
var methodType = "POST"
var successCallBack = baseURL + "/book_list/"


$("#my-create-book").on("submit",function(event){
//    debugger()
    event.preventDefault()
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();


//    var file = $('#book_image').prop('files')
//    console.log("file------------",$("#book_image").value)
    var chooseFile = document.getElementById("book_image");
    chooseFile.addEventListener("change", function () {
      getImgData();
    });
    function getImgData() {
      const files = chooseFile.files[0];
      if (files) {
        const fileReader = new FileReader();
        fileReader.readAsDataURL(files);
        }
    }



    var resultData = {
        image:$("#book_image").value,
        name:$("#book_name").val(),
        author:$("#author_book").val(),
        publication_date:$("#publication_date").val(),
        rating :$("#rating").val()
    }
    console.log("helloo------------",resultData)
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

        }
var resultData = ''
makeAjaxCall(authorURL, authorMethodType, resultData ,callBack)