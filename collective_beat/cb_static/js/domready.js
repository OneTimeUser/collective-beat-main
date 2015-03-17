$(function() {
    $(document).pjax(
        '.navbar a.logo, #nav a, a.archive-category-link',
        '#pjax-content',
        {timeout: 2000}
    );

    $(document).on('pjax:success', function(event, data, status, xhr, options) {
        console.log(event, data, status, xhr, options);
        $('.navbar li').removeClass('active');
        $(options.target).closest('li').addClass('active');
    });
    //$(document).on('pjax:send', function() {
    //    $('#loading').show();
    //});
    //$(document).on('pjax:complete', function() {
    //    $('#loading').hide()
    //});

    var genderOtherText = $('#id_gender_other').insertAfter($('#id_gender_2').parent().parent());

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

    $('.navbar-nav .search, .search-block .close').click(function (e) {
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

    $('.alerts .close').click(function() {
        $(this).closest('.list-group-item').remove();
    });
});