$(document).ready(function() {

    //ВВОД ТОЛЬКО ЦИФР В ПОЛЕ ТЕЛЕФОНА
    $("#id_phone").keydown(function(event) {
        // Разрешаем: backspace, delete, tab и escape
        if ( event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 ||
             // Разрешаем: Ctrl+A
            (event.keyCode == 65 && event.ctrlKey === true) ||
             // Разрешаем: home, end, влево, вправо
            (event.keyCode >= 35 && event.keyCode <= 39)) {
                 // Ничего не делаем
                 return;
        }
        else {
            // Обеждаемся, что это цифра, и останавливаем событие keypress
            if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                event.preventDefault();
            }
        }
    });

    $(".fancybox").fancybox();

    $("#popup").fancybox({
//        'cyclic'            : true,
        'autoScale'     	: false,
        'transitionIn'		: 'none',
        'transitionOut'		: 'none',
        'type'				: 'iframe'
    });

//    $("#popup").fancybox.resize();

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

//    отложенная загрузка картинок
    $("img.lazy").lazyload({
        threshold : 200
    });

//    скролл
//    $("a.scroll").scroll(function() {
//            $('a.scroll').toggleClass('visible');
//        }
//    );
//    $( "a#scroll" ).scroll(function() {
//      $( "#log" ).append( "<div>Handler for .scroll() called.</div>" );
//    });
//    $('#portfolio').scroll(function(){
//      alert('Элемент portfolio был прокручен... скроллирован... ну как там это называется то?!');
//    });

});

//загрузка портфолио только после полной загрузки фото
function loadPage() {
    document.getElementById('portfolio_detail').style.left = '0';
}