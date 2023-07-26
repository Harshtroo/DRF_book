var userListURL = baseURL + "/user_list/"
var methodType = "GET"
var callBack = function (data) {
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
        }

var resultData = ''

makeAjaxCall(userListURL, methodType, resultData ,callBack)



//$.ajax({
//        type: 'GET',
//        url: userListURL,
//        dataType: 'json',
//        success: function (data) {
//            output = ""
//            for (var i=0;i< data.length;i++){
//                output += `
//                            <tr>
//
//                                <td scope="row">${data[i].username}</td>
//                                <td scope="row">${data[i].email}</td>
//                                <td scope="row">${data[i].phone_number}</td>
//                            </tr>`
//            }
//            document.getElementById("user_list").innerHTML = output
//        },
//        error: function (error){
//        }
//    })