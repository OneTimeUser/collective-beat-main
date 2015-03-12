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
        file: showAttrs['data-show-url'].value,
        height: 0,
        width: 0
    }).play();

    $('marquee.hidden-xs').text(showAttrs['data-show-description'].value);
    $('div.show-name').text('SILENCIO '
        + showAttrs['data-show-number'].value
        + ': ' + showAttrs['data-show-date'].value
        + ' // ' + showAttrs['data-show-title'].value);
    $(el).hide();
    $(el).parent().find('.pause-button').show();

    $('.player-block .play-button').hide();
    $('.player-block .pause-button').show();
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