function startCalendar() {
    const today = new Date();
    let y = today.getFullYear();
document.getElementById('cal').innerHTML
= y;
setTimeout(startCalendar,1000)
}