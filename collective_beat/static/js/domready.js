function init() {
    var genderOtherText = $('#id_gender_other').insertAfter($('#id_gender_2').closest('.radio'));
    if ($('#id_gender input[name=gender]:checked').val() !== 'o') {
        genderOtherText.hide();
    }

    $('#id_gender input[name=gender]').change(function () {
        if ($(this).val() === 'o') {
            genderOtherText.css('display','inline-block');
        } else {
            genderOtherText.hide();
        }
    });
}

$(function() {
    var pjaxContainer = $('#pjax-content');

    $(document).pjax(
        '.navbar a.logo, #nav a:not([class*=logout]), a.archive-category-link, a[data-pjax]',
        '#pjax-content',
        {timeout: 5000}
    );

    $(document).on('pjax:success', function(event, data, status, xhr, options) {
        init();
    })
        .on('pjax:send', function() {
            $('.navbar').loader('show', {overlay: false, background: false});
        })
        .on('pjax:complete', function() {
            $('.navbar').loader('hide', {overlay: false, background: false});
        });

    init();

    pjaxContainer.on('click', '.navbar-nav .search, .search-block .close', function (e) {
        e.preventDefault();
        var $search = $('.search-block');

        if ($search.is(':hidden')) {
            $search.addClass('shown');
            $('.navbar-nav .search').hide();
            $search.find('input').css('width','200px');
        } else {
            $search.find('input').css('width','40px');
            setTimeout(function() {
                    $search.removeClass('shown');
                    $('.navbar-nav .search').fadeIn().css('display','inline-block');
                }, 300
            );
        }
    });

    pjaxContainer.on('click', '.alerts .close', function() {
        $(this).closest('.list-group-item').remove();
    });

    $(window).bind('scroll', function() {
        var topOffset = $('.top-podcast').height();
        if ($(window).scrollTop() > topOffset) {
            $('.navbar').addClass('fixed');
            $('#content').css('margin-top','92px');
        }
        else {
            $('.navbar').removeClass('fixed');
            $('#content').css('margin-top','0');
        }
    });

    /**
     * responsive sticky footer fix
     */
    var bumpIt = function() {
            console.log($('.footer').height(), $('.footer').outerHeight(), $('#player-block').outerHeight());
            $('body').css('margin-bottom', $('.footer').height());
        },
        didResize = false;

    bumpIt();

    $(window).resize(function() {
        didResize = true;
    });

    setInterval(function() {
        if(didResize) {
            didResize = false;
            bumpIt();
        }
    }, 250);

});