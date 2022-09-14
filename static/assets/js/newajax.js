function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


jQuery(window).on("load", function(){
    optText = 'Maincategory';
    optValue = 'selected';
    $('#id_main_category').prepend(`<option value ${optValue}>${optText}</option>`);
    optText1 = 'Category';
    optValue1 = 'selected';
    $('#id_category').prepend(`<option value ${optValue1}>${optText1}</option>`);
    optText1 = 'Subcategory';
    optValue1 = 'selected';
    $('#id_sub_category').prepend(`<option value ${optValue1}>${optText1}</option>`);
    cols = document.getElementById("id_category");
    cols.options.length = 1;
    // cols.options.add(new Option("Category", "Category"));
    

    cols1 = document.getElementById("id_sub_category");
    cols1.options.length = 1;

    // cols1.options.add(new Option("Subcategory", "Subcategory"));
    
   
  });
  $("#id_category").change(function() {   
    // $("select option[value='Category']").attr("disabled","disabled");
    $("select option[value = 'Category' ]").prop('disabled',true);

});
//   jQuery(window).on("click", function(){

    
//   });


jQuery(function($){

    


    $(document).ready(function(){
      

        $("#id_main_category").change(function(){
            
            $.ajax({
                url:"/Products/category/",
                type:"POST",
                data:{maincategories: $(this).val(),},
                success: function(result) {
                    console.log(result);

                    cols = document.getElementById("id_category");
                    if  (cols.options.length = 0){

                    }
                    else{
                        optText1 = 'Category';
                        optValue1 = 'selected';
                        $('#id_category').prepend(`<option value ${optValue1}>${optText1}</option>`); 
                    }
                    // cols.options.add(new Option("Category", "Category"));
                    cols1 = document.getElementById("id_sub_category");
                    if (cols1.options.length = 0){

                    }
                    else{
                        optText1 = 'Subcategory';
                        optValue1 = 'selected';
                        $('#id_sub_category').prepend(`<option value ${optValue1}>${optText1}</option>`);
                    }
                    // cols1.options.add(new Option("Subcategory", "Subcategory"));
                    
                    for(var k in result){
                        cols.options.add(new Option(k, result[k]));
                    }
                },
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        });
            $("#id_category").change(function(){
            $.ajax({
                url:"/Products/subcategory/",
                type:"POST",
                data:{categories: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_sub_category");
                    if (cols1.options.length = 0){

                    }
                    else{
                        optText1 = 'Subcategory';
                        optValue1 = 'selected';
                        $('#id_sub_category').prepend(`<option value ${optValue1}>${optText1}</option>`);
                    }
                    for(var k in result){
                        cols.options.add(new Option(k, result[k]));
                    }
                },
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        });

      





        });
    }); 
