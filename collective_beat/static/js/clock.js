function timerTick() {
  with (new Date()) {
    var h, m, s;

    h = 30 * ((getHours() % 12) + getMinutes() / 60);
    m = 6 * getMinutes();
    s = 6 * getSeconds();

    document.getElementById('h_pointer').setAttribute('transform', 'rotate(' + h + ', 50, 50)');
    document.getElementById('m_pointer').setAttribute('transform', 'rotate(' + m + ', 50, 50)');
    document.getElementById('s_pointer').setAttribute('transform', 'rotate(' + s + ', 50, 50)');

    setTimeout(timerTick, 1000);
  }
}