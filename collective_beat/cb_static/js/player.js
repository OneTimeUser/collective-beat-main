$(function () {
    $(document).ready(function() {
        jwplayer("player-block").setup({
            file: "rtmp://flash.oit.duke.edu/vod/_definst_",
            height: 0,
            width: 0
        });
    });
});