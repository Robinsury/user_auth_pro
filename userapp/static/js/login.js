let user= document.forms['myFame']['user'];
let pass= document.forms['myFame']['pass'];
let user_error=document.getElementById("error-user");
let pass_error=document.getElementById("error-pass");
function validated(){

    if(user.value.length >=4 ||
        user.value.length <=15){
        user_error.style.display="block";
        user.style.border="1px solid red";
        user.focus();
        return false
    }

    if(pass.value.length >=4 ||
        pass.value.length <=15){
        pass_error.style.display="block";
        pass.style.border="1px solid red";
        pass.focus();
        return false;
    }


}
