function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    var ampm = h >= 12 ? 'pm' : 'am';
    h = h % 12;
    h = h ? h : 12; // the hour '0' should be '12'
    m = checkTime(m)
    s = checkTime(s)
document.getElementById('clock').innerHTML
= h + ":" + m + ":" + s + "  "+ ampm;
    setTimeout(startTime,1000) ;
}  
function checkTime(i) {
    if (i < 10) {i="0"+i}
    return i;
}