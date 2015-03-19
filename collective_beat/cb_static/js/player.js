var playingTrackAttrs = {};

$(document).ready(function() {
    /*
     if we need to have an initial stream or track to play
     we put the settings here
     */
    jwplayer("player-block").setup({
        file: "",
        height: 0,
        width: 0
    });

    jwplayer("player-block").onPlay(function() {
        $('.play-button img.play-button-img').hide();
        $('.play-button img.pause-button-img').show();
    });
    jwplayer("player-block").onPause(function() {
        $('.play-button img.play-button-img').show();
        $('.play-button img.pause-button-img').hide();
    });
});

/*
    function for starting playback and visual representation
    for the current playing stream/playback
 */
function loadTrack(el) {
    var showAttrs = playingTrackAttrs = $(el).parents('.podcast-block')[0].attributes;
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
        width: 0
    }).play();
    console.log(showAttrs['data-show-description'].value);
    $('marquee.hidden-xs').text(showAttrs['data-show-description'].value);
    $('div.show-name').text('SILENCIO '
        + showAttrs['data-show-number'].value
        + ': ' + showAttrs['data-show-date'].value
        + ' // ' + showAttrs['data-show-title'].value);

    jwplayer("player-block").onPlay(function() {
        $(el).hide();
        $(el).parent().find('.pause-button').show();

        $('.player-block .play-button').hide();
        $('.player-block .pause-button').show();
    });
    jwplayer("player-block").onPause(function() {
        $(el).show();
        $(el).parent().find('.pause-button').hide();

        $('.player-block .play-button').show();
        $('.player-block .pause-button').hide();
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