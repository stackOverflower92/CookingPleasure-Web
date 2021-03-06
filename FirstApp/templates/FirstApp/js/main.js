
$(document).ready(function() {

    // Init tooltips
    $(function () {
      $('[data-toggle="tooltip"]').tooltip();
    });
    // Ingredients div hidden by default
    $("#ingredients-well").hide();
    $('input[id=inputIngredients]').keyup(function() {
        var content = $("#inputIngredients").val();
        var lastChar = content.substr(content.length-1);

        if (lastChar === ";") {
            $("#ingredients-well").show();
                    // If last char is delimiter
                    // Reset textbox content
            $("#inputIngredients").val("");
                    // Remove delimiter from tag
            content = content.replace(";", "");
            var tempContent = content.split(",");
            tempContent[0] = tempContent[0].trim();
            tempContent[1] = tempContent[1].trim();

            tempContent[0] = tempContent[0].replace(/\s+/g, ' ').trim();
            content = (tempContent[0] + ', ' + tempContent[1]);
                    // Insert ingredient into tag
            content= "<div class=\"badgeHolder\"style=\"margin: 1px 1px 1px 1px;\"><span class=\"btn badge badge-primary badge-btn\"><span class=\"badge badge-success badge-xs\">"+ content +"</span><span aria-hidden=\"true\">&times;</span></span></div>"
                    // Ad this to well
            $("#ingredients-well").append(content);
        }
    });
    $(document).on("click", ".badge-primary", function(e) {
        console.log("ciao");
        $(this).closest('.badgeHolder').remove();
    });
    $('#frmRecipe').ajaxForm(function() { // catch the form's submit event
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        var badgenum = 0;
        var name=[];
        var quant=[];
        $.ajax({ // create an AJAX call...
            data: $(this).serialize() , // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function (data) {
                $('#ingredients-well').children().each(function () {
                    val = $(this).text();
                    console.log(val);
                    nam = val.substr(0,val.indexOf(","));
                    console.log(nam);
                    q = val.substr(val.indexOf(",")+2);
                    q = q.replace("×"," ");
                    console.log(q);
                    name[badgenum]=nam;
                    quant[badgenum]=q;
                    badgenum=badgenum+1;
                });
            },
            complete: function(data) {
                recipe = $('#inputName').val();
                $("#ingredients-well").html(" ");
                date={name: name, q: quant ,recipe:recipe,ingrn:badgenum, csrfmiddlewaretoken: token} ;
                $.ajax({ // create an AJAX call...
                    data: date , // get the form data
                    type: "POST", // GET or POST
                    url: "add_ingredients/", // the file to call
                    complete: function(data){
                        window.location.href = "/FirstApp/dashboard/";
                        return false;
                    }
                });

                return false;
            }
        });
        badgenum=0;
        name.length = 0;
        quant.lenght = 0;
        return false;
    });

    $('#frmcontact').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize() , // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success : function(response,status) {
                         window.location.href = "/FirstApp/dashboard/";
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
        return false;
    });

    $('#frmMenu').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize() , // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success : function(response,status) {
                         window.location.href = "/FirstApp/dashboard/";
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
        return false;
    });
    $('#btnMailRecipe').click( function(e){
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        recipename = $('#frmViewRecipe').find('#inputName').text();
        recipename = recipename.substr(recipename.indexOf(":")+1);
        date={recipename:recipename, csrfmiddlewaretoken: token} ;
        $.ajax({ // create an AJAX call...
            data: date , // get the form data
            type: "POST", // GET or POST
            url: "mail_recipe/", // the file to call
            success: function(data){
                window.location.href = "/FirstApp/dashboard/";
            },
            complete: function(data){
                return false;
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
    $('#btnMailMenu').click( function(e){
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        menuname = $('#frmViewMenu').find('#inputName').text();
        menuname = menuname.substr(menuname.indexOf(":")+2);
        console.log(menuname);
        date1={menuname:menuname, csrfmiddlewaretoken: token} ;
        $.ajax({ // create an AJAX call...
            data: date1 , // get the form data
            type: "POST", // GET or POST
            url: "mail_menu/", // the file to call
            success: function(data){
                window.location.href = "/FirstApp/dashboard/";
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
     $('#btnMailList').click( function(e){
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        listname = $('#frmViewList').find('#listname').text();
        listname = listname.substr(0,listname.length-1);
        console.log(listname);
        date1={listname:listname, csrfmiddlewaretoken: token} ;
        $.ajax({ // create an AJAX call...
            data: date1 , // get the form data
            type: "POST", // GET or POST
            url: "mail_list/", // the file to call
            success: function(data){
                window.location.href = "/FirstApp/dashboard/";
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
    $('#btnListRecipe').click( function(e){
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        list = $('#frmViewRecipe').find('#inputName').text();
        list = list.substr(list.indexOf(":")+1);
        console.log(list);
        date={list:list, csrfmiddlewaretoken: token} ;
        $.ajax({ // create an AJAX call...
            data: date , // get the form data
            type: "POST", // GET or POST
            url: "add_list/", // the file to call
            success: function(data){
                window.location.href = "/FirstApp/dashboard/";
            },
            complete: function(data){
                return false;
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
    $('#btnListMenu').click( function(e){
        console.log("button list_menu")
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        list = $('#frmViewMenu').find('#inputName').text();
        list = list.substr(list.indexOf(":")+2);
        console.log(list);
        date1={list:list, csrfmiddlewaretoken: token} ;
        $.ajax({ // create an AJAX call...
            data: date1 , // get the form data
            type: "POST", // GET or POST
            url: "add_list_menu/", // the file to call
            success: function(data){
                window.location.href = "/FirstApp/dashboard/";
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });

     $('#btnDeleteRecipe').click( function(e){
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        recipe = $('#frmViewRecipe').find('#inputName').text();
        recipe = recipe.substr(recipe.indexOf(":")+1);
        console.log(recipe);
        date1={recipe:recipe, csrfmiddlewaretoken: token} ;
        $.ajax({ // create an AJAX call...
            data: date1 , // get the form data
            type: "POST", // GET or POST
            url: "delete_recipe/", // the file to call
            success: function(data){
                window.location.href = "/FirstApp/dashboard/";
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
    $('#btnDeleteMenu').click( function(e){
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        menu = $('#frmViewMenu').find('#inputName').text();
        menu = menu.substr(menu.indexOf(":")+2);;
        date1={menu:menu, csrfmiddlewaretoken: token} ;
        $.ajax({ // create an AJAX call...
            data: date1 , // get the form data
            type: "POST", // GET or POST
            url: "delete_menu/", // the file to call
            success: function(data){
                window.location.href = "/FirstApp/dashboard/";
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });

    $('#btnDeleteList').click( function(e){
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        list = $('#frmViewList').find('#listname').text();
        list = list.substr(0,list.length-1)
        console.log(list)
        date1={list:list, csrfmiddlewaretoken: token} ;
        $.ajax({ // create an AJAX call...
            data: date1 , // get the form data
            type: "POST", // GET or POST
            url: "delete_list/", // the file to call
            success: function(data){
                window.location.href = "/FirstApp/dashboard/";
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });

    $('#recipeplace').on('click', '#btnGetRecipe', function(e){
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        e.preventDefault();
        recipe = $(this).closest('div').children('h4').first().text();
        $.ajax({
            type: "POST",
            url: "get_recipe/",
            data: { recipename : recipe ,csrfmiddlewaretoken: token
                },
            success : function(response,status) {
                if (status == 'success'){
                    $('#frmViewRecipe').html(response);
                }
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
    $('#menuplace').on('click', '#btnGetMenu', function(e){
        console.log("catch btngetmenu");
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        e.preventDefault();
        menu = $(this).closest('div').children('h4').first().text();
        $.ajax({
            type: "POST",
            url: "get_menu/",
            data: { menuname : menu ,csrfmiddlewaretoken: token
                },
            success : function(response,status) {
                if (status == 'success'){
                    $('#frmViewMenu').html(response);
                }
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
    $('#listplace').on('click', '#btnGetList', function(e) {
        token = $('input[name="csrfmiddlewaretoken"]').prop('value');
        e.preventDefault();
        list = $(this).closest('div').children('h4').first().text();
        $.ajax({
            type: "POST",
            url: "get_list/",
            data: {
                listname: list, csrfmiddlewaretoken: token
            },
            success: function (response, status) {
                if (status == 'success') {
                    $('#frmViewList').html(response);
                }
            },
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });
    cont=0;
    word="";
    $('#SEARCH').keyup(function(){
        console.log("prova");
        var valThis = $(this).val();
        $('.placeholders').children('.placeholder').each(function(){
            var text = $(this).children('h4').text().toLowerCase();
            (text.indexOf(valThis) == 0) ? $(this).show() : $(this).hide();
   });
    });


});