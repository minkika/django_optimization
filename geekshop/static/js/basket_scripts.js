window.onload = function () {
    /*
    // можем получить DOM-объект меню через JS
    var menu = document.getElementsByClassName('menu')[0];
    menu.addEventListener('click', function () {
        console.log(event);
        event.preventDefault();
    });
    
    // можем получить DOM-объект меню через jQuery
    $('.menu').on('click', 'a', function () {
        console.log('event', event);
        console.log('this', this);
        console.log('event.target', event.target);
        event.preventDefault();
    });
   
    // получаем атрибут href
    $('.menu').on('click', 'a', function () {
        var target_href = event.target.href;
        if (target_href) {
            console.log('нужно перейти: ', target_href);
        }
        event.preventDefault();
    });
    */

    // добавляем ajax-обработчик для обновления количества товара
    $('.basket__items')
        .on('change', 'input[type="number"]', function (event) {
            let input = event.target;

            if (input) {
                $.ajax({
                    url: "/basket/edit/" + input.name + "/" + input.value + "/",
                    success: function (data) {
                        $('.basket__items').html(data.result);
                    },
                });

            }
            event.preventDefault();
        });

};