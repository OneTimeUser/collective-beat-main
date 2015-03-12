$(function () {
    $(document).ready(function() {
        jwplayer("player-block").setup({
            file: "",
            height: 0,
            width: 0
        });
    });
});

function loadTrack(url, date, number, title, description) {
    jwplayer("player-block").stop();
    jwplayer("player-block").remove();
    jwplayer("player-block").setup({
        file: url,
        height: 0,
        width: 0
    }).play();
    $('marquee.hidden-xs').text(description);
    $('div.show-name').text('SILENCIO ' + number + ': ' + date + ' // ' + title);
}