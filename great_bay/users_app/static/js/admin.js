
$(document).on("click", "li", function () {

    $(".chat-window").show();

    $(".user-msg").html($(this).data("email"))
})
function getProducts() {
    // setInterval(function () {
       
            $.ajax({
                url: "{% url '/products/getall/' %}",
                method: "GET",
                headers: {"X-CSRFToken": getCookie("csrftoken")},
                crossDomain: false,
                success: function (data) {
                    // response_json = JSON.parse(data)
                    print(data)
                    // $('body').html(response_json.html_data);
                    //   var=response_json.variable_value; 
                }
            });
        
    // }, 1000)

}
$(document).on("click", "li", function (e) {
    $(".page-content").empty()
    print("hiii")
    getProducts()
  
})
$(document).on('click', '.panel-heading span.icon_minim', function (e) {
    var $this = $(this);
    if (!$this.hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideUp();
        $this.addClass('panel-collapsed');
        $this.removeClass('fa-minus').addClass('fa-plus');
    } else {
        $this.parents('.panel').find('.panel-body').slideDown();
        $this.removeClass('panel-collapsed');
        $this.removeClass('fa-plus').addClass('fa-minus');
    }
});
$(document).on('focus', '.panel-footer input.chat_input', function (e) {
    var $this = $(this);
    if ($('#minim_chat_window').hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideDown();
        $('#minim_chat_window').removeClass('panel-collapsed');
        $('#minim_chat_window').removeClass('fa-plus').addClass('fa-minus');
    }
});
