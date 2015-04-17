var playingTrackAttrs = {};

/*
    function for starting playback and visual representation
    for the current playing stream/playback
 */
function loadTrack(el) {
    var showAttrs = playingTrackAttrs = $(el).parents('.podcast-block')[0].attributes;
    $(el).closest('.podcast-block').loader('show', {overlay: false, background: false});
    $('.progress-block .slider-track').addClass('seeking-bar');
    $('.pause-button').fadeOut();
    $('.play-button').fadeIn();
    $(el).closest('.play-button').fadeOut();
    $("#player-block").jPlayer('clearMedia');
    $("#player-block").jPlayer("setMedia", {
        title: showAttrs['data-show-title'].value,
        rtmpa: showAttrs['data-show-url'].value,
        m3u8a: showAttrs['data-show-url-ios'].value,
        poster: showAttrs['data-show-image'].value
      }).jPlayer("play");

    $('marquee.hidden-xs').text(showAttrs['data-show-description'].value);
    $('div.show-name').text(showAttrs['data-show-date'].value
        + ' // ' + showAttrs['data-show-title'].value);
}

$("#play").click(function() {
   $('.progress-block .slider-track').addClass('seeking-bar');
});

$(".forward-button").click( function() {
    var currentTime = $("#player-block").data("jPlayer").status.currentTime;
    if(currentTime <= $("#player-block").data("jPlayer").status.duration - 16) {
        $("#player-block").jPlayer("play", currentTime + 15);
    }
});

$(".back-button").click( function() {
  var currentTime = $("#player-block").data("jPlayer").status.currentTime;
    if(currentTime >= 15) {
        $("#player-block").jPlayer("play", currentTime - 15);
    } else {
        $("#player-block").jPlayer("play", 0);
    }
});

$('.progress-player input.slider').slider();
$('.volume-block input.slider').slider().on('slide', function(ev){
    $("#player-block").jPlayer('volume', ev.value/100)
});