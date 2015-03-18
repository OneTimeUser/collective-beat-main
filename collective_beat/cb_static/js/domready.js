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
        '.navbar a.logo, #nav a, a.archive-category-link, a[data-pjax]',
        '#pjax-content',
        {timeout: 2000}
    );

    $(document).on('pjax:success', function(event, data, status, xhr, options) {
        init();
    })
        .on('pjax:send', function() {
            $('#loading').show();
        })
        .on('pjax:complete', function() {
            $('#loading').hide();
        });

    init();

    pjaxContainer.on('click', '.navbar-nav .search, .search-block .close', function (e) {
        e.preventDefault();
        if ($('.search-block').is(':hidden')) {
            $('.search-block').addClass('shown');
            $('.navbar-nav .search').hide();
        }

        else {
            $('.search-block').removeClass('shown');
            $('.navbar-nav .search').css('display','inline-block');
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

});