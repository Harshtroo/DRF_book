var baseURL = "http://127.0.0.1:8000"
function makeAjaxCall(url, methodType, resultData, callback){

 $.ajax({
    url : url,
    method : methodType,
    dataType : "json",
    data: resultData,
    success : callback,
    error : function (reason, xhr){
     console.log("error in processing your request", reason);
    }
   });
 }

function postAjaxCall(url, methodType, resultData,csrfToken, callback){
    $.ajax({
    url : url,
    method : methodType,
    headers: {'X-CSRFToken': csrfToken},
    contentType: "application/json",
    dataType: "text",
    data: resultData,
    success : callback,
    error : function (reason, xhr){
     console.log("error in processing your request", reason);
    }
   });
}