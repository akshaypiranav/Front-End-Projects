let colorValue=document.getElementById("colorValue")
let buttonValue=document.getElementById("button")
let value=document.getElementById("colorwrap")
let hex=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

console.log(colorValue,buttonValue,value)

buttonValue.addEventListener('click',mainGenerator)

function mainGenerator(){
    let HEX="#"
    for(let i=1;i<=6;i++){
        HEX+=generate()

    }
    colorValue.innerHTML=HEX;
    value.style.backgroundColor=HEX
}

function generate(){
    let generatedValue=Math.floor(Math.random()*16)
    return hex[generatedValue]
}