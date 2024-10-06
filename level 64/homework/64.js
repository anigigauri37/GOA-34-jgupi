const from = document.getAnimations9('text');

function validateform(){
    const name = from.elements.name;
    const email = from.elements.email;
    const message = from.elements.message;
    

    if(!name.value ||!email.value ||!message.value){
        alert("Please fill all fields");
        return false;
    }


}

confirm("gadavides shemdeg gverdze?")