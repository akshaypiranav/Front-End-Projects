function convert(){
let cmValue=Number(document.getElementById("cm").value);
let inchValue=cmValue/2.54;
let message=document.getElementById("value");
message.innerHTML="INCH VALUE : "+inchValue;
}
