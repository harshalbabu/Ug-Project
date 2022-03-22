let s = 1;
let c = 1;
let econ;
let bus;
let seat="e";
window.onload = function() {
    first();
    econ = document.getElementById("econ_c").textContent.trim();
    bus = document.getElementById("econ_b").textContent.trim();
  };
function first(){
    select('step1');
    s=1;
    document.getElementById("one").style.display = "block";
    document.getElementById("two").style.display = "none";
    document.getElementById("three").style.display = "none";
    document.getElementById("four").style.display = "none";
};
function second(){
    select('step2');
    s=2;
    document.getElementById("one").style.display = "none";
    document.getElementById("two").style.display = "block";
    document.getElementById("three").style.display = "none";
    document.getElementById("four").style.display = "none";
};
function third(){
    select('step3');
    s=3;
    document.getElementById("one").style.display = "none";
    document.getElementById("two").style.display = "none";
    document.getElementById("three").style.display = "block";
    document.getElementById("four").style.display = "none";
};
function fourth(){
    select('step4');
    s=4;
    document.getElementById("one").style.display = "none";
    document.getElementById("two").style.display = "none";
    document.getElementById("three").style.display = "none";
    document.getElementById("four").style.display = "block";
};
function select(id){
    if(s==1){
        deselect("step1");
    }
    if(s==2){
        deselect("step2");
    }
    if(s==3){
        deselect("step3");
    }
    if(s==4){
        deselect("step4");
    }
    document.getElementById(id).classList.remove('hover:text-gray-900');
    document.getElementById(id).classList.remove('border-gray-200');
    document.getElementById(id).classList.add('bg-gray-100');
    document.getElementById(id).classList.add('border-indigo-500');
    document.getElementById(id).classList.add('text-indigo-500');
    document.getElementById(id).classList.add('rounded-t');
};
function deselect(id){
    document.getElementById(id).classList.remove('bg-gray-100');
    document.getElementById(id).classList.remove('border-indigo-500');
    document.getElementById(id).classList.remove('text-indigo-500');
    document.getElementById(id).classList.remove('rounded-t');
    document.getElementById(id).classList.add('hover:text-gray-900');
    document.getElementById(id).classList.add('border-gray-200');
};
function continue1(){
    second();
};
function continue2(){
        data = "";
        n = document.getElementById("number").value;
        for (let i = 1; i <= n; i++) {
          text = `<div class="p-4 border-2 my-1">
        <div class="relative flex-grow">
          <label for="full-name" class="leading-7 text-sm text-gray-600">Name and gender</label><br>
          <input type="text" id="f_name` + i + `" name="f_name` + i + `" placeholder="First Name" class="bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-transparent focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out inline">
          <input type="text" id="l_name` + i + `" name="l_name` + i + `" placeholder="Last Name" class="bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-transparent focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out inline">
    
        </div>
        <br>
        <div class="relative flex-grow">
          <label for="email" class="leading-7 text-sm text-gray-600">Gender</label><br>
      <select name="gender` + i + `" id="gender` + i + `">
         <option value="" disabled selected>--Select--</option>
      <option value="M">Male</option>
      <option value="F">Female</option>
      <option value="O">Other</option>
    </select>
        </div><br></div>`
        data += text;
        }
    document.getElementById("temp1").innerHTML = data;
    third();
};
function continue3(){
    let cost;
    if(c==1){
        cost=econ;
    }
    else{
        cost=bus;
    }
    
    data = "";
        n = document.getElementById("number").value;
        for (let i = 1; i <= n; i++) {
        t = document.getElementById("f_name"+ i).value + " " + document.getElementById("l_name"+i).value;
        g=document.getElementById("gender"+i).value;
          text = `<tr>
          <td class="px-4 py-3">` + i + `</td>
          <td class="px-4 py-3">`+t+`</td>
          <td class="px-4 py-3">`+g+`</td>
          <td class="px-4 py-3 text-lg text-gray-900">`+cost+`</td>
        </tr>`
        data += text;
        }
        data = data+`<tr>
        <td class="border-t-8 border-b-8 border-gray-200 px-4 py-3" colspan="3">TOTAL</td>
        <td class="border-t-8 border-b-8 border-gray-200 px-4 py-3 text-lg text-gray-900">`+cost*n+`</td>
      </tr>`
    document.getElementById("temp2").innerHTML = data;
    fourth();
};
function economy(){
    c = 1;
    seat="e";
    data = `<div id="econ" class="p-4 xl:w-1/4 md:w-1/2 w-full ml-60 price" onclick="economy()">
        <div class="h-full p-6 rounded-lg border-2 border-indigo-500 flex flex-col relative overflow-hidden">
          <span class="bg-indigo-500 text-white px-3 py-1 tracking-widest text-xs absolute right-0 top-0 rounded-bl">SELECTED</span>
          <h2 class="text-sm tracking-widest title-font mb-1 font-medium">Economy class</h2>
          <h1 id="econ_c" class="text-5xl text-gray-900 leading-none flex items-center pb-4 mb-4 border-b border-gray-200">
            <span>`+econ+`</span>
          </h1>
         </div>
      </div>
      <div id="busi" class="p-4 xl:w-1/4 md:w-1/2 w-full price" onclick="business()">
        <div class="h-full p-6 rounded-lg border-2 border-gray-300 flex flex-col relative overflow-hidden">
          <h2 class="text-sm tracking-widest title-font mb-1 font-medium">Business class</h2>
          <h1 id="econ_b" class="text-5xl text-gray-900 pb-4 mb-4 border-b border-gray-200 leading-none">`+bus+`</h1>
        </div>
      </div>
      <br>`;
      document.getElementById("tempe").innerHTML = data;
      document.getElementById("costId").setAttribute("value", econ);
      document.getElementById("seat_temp").setAttribute("value", seat);
};
function business(){
    c = 2;
    seat="b";
    data = `<div id="econ" class="p-4 xl:w-1/4 md:w-1/2 w-full ml-60 price" onclick="economy()">
        <div class="h-full p-6 rounded-lg border-2 border-gray-300 flex flex-col relative overflow-hidden">
          <h2 class="text-sm tracking-widest title-font mb-1 font-medium">Economy class</h2>
          <h1 id="econ_c" class="text-5xl text-gray-900 pb-4 mb-4 border-b border-gray-200 leading-none">`+econ+`</h1>
         </div>
      </div>
      <div id="busi" class="p-4 xl:w-1/4 md:w-1/2 w-full price" onclick="business()">
        <div class="h-full p-6 rounded-lg border-2  border-indigo-500 flex flex-col relative overflow-hidden">
        <span class="bg-indigo-500 text-white px-3 py-1 tracking-widest text-xs absolute right-0 top-0 rounded-bl">SELECTED</span>
          <h2 class="text-sm tracking-widest title-font mb-1 font-medium">Business class</h2>
          <h1 id="econ_b" class="text-5xl text-gray-900 leading-none flex items-center pb-4 mb-4 border-b border-gray-200"><span>`+bus+`</span></h1>
        </div>
      </div>
      <br>`;
      document.getElementById("tempe").innerHTML = data;
      document.getElementById("costId").setAttribute("value", bus);
      document.getElementById("seat_temp").setAttribute("value", seat);
};
