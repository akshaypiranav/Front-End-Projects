let check=true;
document.querySelector('button').style.backgroundColor = 'green';

function onOff(){
    if(check){
        check=false;
        document.querySelector('#img').src="on.png";
        document.querySelector('button').innerHTML='OFF';
        document.querySelector('button').style.backgroundColor='red';
    
    
    }
    else{
        check=true;
        document.querySelector('#img').src="off.png";
        document.querySelector('button').innerHTML='ON';
        document.querySelector('button').style.backgroundColor='green';
    }
}