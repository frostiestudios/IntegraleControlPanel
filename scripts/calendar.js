function startCalendar() {
    const today = new Date();
    let d = today.getDate();
    let m = today.getMonth();
    let y = today.getFullYear();
document.getElementById('cal').innerHTML
= m+1 + "-" + d +"-"+ y;
setTimeout(startCalendar,1000)
}