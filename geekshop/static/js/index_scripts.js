window.onload = function () {

    $('.section-tabs__tab')
        .on('click', 'span', function (event) {
            let tab = event.target;

            if (tab) {
                $.ajax({
                    url: "/new/",
                    success: function (data) {
                        $('.basket__items').html(data.result);
                    },
                });

            }
            event.preventDefault();
        });

};