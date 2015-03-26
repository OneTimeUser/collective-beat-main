var playingTrackAttrs = {};

/*
    function for starting playback and visual representation
    for the current playing stream/playback
 */
function loadTrack(el) {
    var showAttrs = playingTrackAttrs = $(el).parents('.podcast-block')[0].attributes;
    $(el).closest('.podcast-block').loader('show', {overlay: false, background: false});
    $('.pause-button').hide();
    $('.play-button').show();
    jwplayer("player-block").stop();
    jwplayer("player-block").remove();
    jwplayer("player-block").setup({
        sources: [
            {
                file: showAttrs['data-show-url'].value
            },
            {
                file: showAttrs['data-show-url-ios'].value
            }
        ],
        rtmp: { bufferlength: 3 },
        fallback: false,
        height: 0,
        width: 0,
        // @TODO WARNING!!! HARDCODED PRODUCTION SERVER SETTING
        flashplayer: '/static/js/jwplayer/jwplayer.flash.swf',
        image: showAttrs['data-show-image'].value
    }).play();
    $('marquee.hidden-xs').text(showAttrs['data-show-description'].value);
    $('div.show-name').text(showAttrs['data-show-number'].value
        + ': ' + showAttrs['data-show-date'].value
        + ' // ' + showAttrs['data-show-title'].value);

    jwplayer("player-block").onPlay(function() {
        $(el).hide();
        $(el).parent().find('.pause-button').show();

        $('.player-block .play-button').hide();
        $('.player-block .pause-button').show();
        $($(el).parents('.podcast-block')).loader('hide', {overlay: false, background: false});
    });
    jwplayer("player-block").onPause(function() {
        $(el).show();
        $(el).parent().find('.pause-button').hide();

        $('.player-block .play-button').show();
        $('.player-block .pause-button').hide();
    });
    jwplayer("player-block").onBuffer(function() {
        $(el).parent().find('.play-button').hide();
    });

}

/*
    pausing button functionality
 */
function pause(el) {
    $('.pause-button').hide();
    $('.play-button').show();
    $('.podcast-block[data-show-id='+ playingTrackAttrs['data-show-id'].value + ']').find('.play-button').show();
    $('.player-block .pause-button').hide();
    $('.player-block .play-button').show();
    jwplayer("player-block").pause();
}

$('.slider').slider().on('slide', function(ev) {
    jwplayer("player-block").setVolume(ev.value);
});