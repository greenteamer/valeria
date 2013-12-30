$(document).ready(function() {
    $(".fancybox").fancybox();

    $("#popup").fancybox({
        'padding'           : 0,
        'width'             : '1200px',
        'height'            : '700px',
        'autoScale'     	: false,
        'transitionIn'		: 'none',
        'transitionOut'		: 'none',
        'type'				: 'iframe'
    });

    $('a#hide_show').click(function (e) {
        $('.hide_form').toggleClass('active');
        e.preventDefault();
    });

//    делаем активный пункт меню
    $('ul.my_nav a').each(function () {
        var location = window.location.href;
        var link = this.href;
        if(location == link) {
            $(this).addClass('active');
        }
    });

});