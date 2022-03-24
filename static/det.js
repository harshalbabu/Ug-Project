c=1;
function c_from(){
    id="from";
    id2="to";
    if(c==2){
    document.getElementById(id2).classList.remove("bg-indigo-500");
    document.getElementById(id2).classList.remove('text-white');
    document.getElementById(id).classList.add("bg-indigo-500");
    document.getElementById(id).classList.add('text-white');
    c=1;
    document.getElementById("ctemp").innerHTML = "To&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
    }
};

function c_to(){
    id="to";
    id2="from";
    if(c==1){
    document.getElementById(id2).classList.remove("bg-indigo-500");
    document.getElementById(id2).classList.remove('text-white');
    document.getElementById(id).classList.add("bg-indigo-500");
    document.getElementById(id).classList.add('text-white');
    c=2;
    document.getElementById("ctemp").innerHTML = "From";
    }
};
