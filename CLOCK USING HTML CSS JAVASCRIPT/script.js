function clock(){
    let hour=document.getElementById("hour")
    let minute=document.getElementById("minute")
    let second=document.getElementById("second")
    let ampm=document.getElementById("ampm")
    let day=document.getElementById("day")
    let month=document.getElementById("month")

    let date=new Date()

    let currentHour = date.getHours()
    let currentMinute=date.getMinutes()
    let currentSeconds=date.getSeconds()
    let currentDay=date.getDay()
    let arr=["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]

    let currentMonth=date.getMonth()

    let monthArray=["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
    
    console.log()
    console.log()
    if(currentHour>12){
        ampm.innerHTML="PM"
        hour=hour-12
    }
    else{
        ampm.innerHTML="AM"
    }
    hour.innerHTML=prefixZero(currentHour)
    minute.innerHTML=prefixZero(currentMinute)
    second.innerHTML=prefixZero(currentSeconds)
    day.innerHTML=arr[currentDay]
    month.innerHTML=monthArray[currentMonth]
}

function prefixZero(value){
    return value<10?"0"+value:value
}

setInterval(clock,1)