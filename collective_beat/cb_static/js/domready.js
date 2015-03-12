$(function() {
    $(document).pjax(
        '.navbar a.logo, #nav a, a.archive-category-link',
        '#content',
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
});