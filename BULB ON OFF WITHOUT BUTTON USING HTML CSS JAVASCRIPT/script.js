let check=true;
document.querySelector('button').style.backgroundColor = 'green';

function onOff(){
    if(check){
        check=false;
        document.querySelector('#img').src="on.png";

    
    }
    else{
        check=true;
        document.querySelector('#img').src="off.png";

    }
}