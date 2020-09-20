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

$( document ).on( 'click', '.details a', function(event) {
   if (event.target.hasAttribute('href')) {
       var link = event.target.href + 'ajax/';
       var link_array = link.split('/');
       if (link_array[4] == 'category') {
           $.ajax({
               url: link,
               success: function (data) {
                   $('.details').html(data.result);
               },
           });

           event.preventDefault();
       }
   }
});