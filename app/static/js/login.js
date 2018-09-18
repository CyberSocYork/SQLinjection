$(function () {

    $('#submit').click(function () {


        var username = $('#username').val();
        var password = $('#password').val();

        if(username === 'cyberSocAdmin' && password === 'password12345'){

              $.ajax({
                type: 'POST',
                url: '/authenticate',
                data: JSON.stringify('validate : true'),
                contentType: 'application/json;charset=UTF-8',
                success: function () {}
    });

            document.location.href = "/keyPage";

        }



    })
});