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

    var genderInput = $('<input type="text" style="display:none;" class="form-control">');

    genderInput.insertAfter($('#id_gender_2').parent().parent());

    $('#id_gender input[name=gender]').change(function () {
        if ($(this).val() === 'o') {
            genderInput.css('display','inline-block');
        }

        else {
            genderInput.hide();
        }
    });
});