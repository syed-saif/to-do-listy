function check(){
    var inputVals = document.querySelectorAll('.input');
    var allTrue = true;
    for(i=0; i<inputVals.length; i++){
      if (inputVals[i].value.trim().length == 0){
        alert("Please fill all the form values!");
        allTrue = false;
        break;
      }
    }
    return allTrue;
}

document.getElementById('submit_btn').onclick = function(){
    var ok = check();
    if(ok==true){
    document.getElementById('form').submit();
    }
};
