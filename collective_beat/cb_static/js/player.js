$(document).ready(function() {
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

function loadTrack(url, date, number, title, description, el) {
    console.log(arguments);
    jwplayer("player-block").stop();
    jwplayer("player-block").remove();
    jwplayer("player-block").setup({
        file: url,
        height: 0,
        width: 0
    }).play();

    $('marquee.hidden-xs').text(description);
    $('div.show-name').text('SILENCIO ' + number + ': ' + date + ' // ' + title);
    $(el).hide();
    $(el).parent().find('.pause-button').show();

    jwplayer("player-block").onPlay(function() {
        $('.player-block .play-button').hide();
        $('.player-block .pause-button').show();
    });
    jwplayer("player-block").onPause(function() {
        $('.player-block .pause-button').hide();
        $('.player-block .play-button').show();
    });
}

function pause(el) {
    $(el).hide();
    $(el).parent().find('.play-button').show();
    jwplayer("player-block").pause();
}