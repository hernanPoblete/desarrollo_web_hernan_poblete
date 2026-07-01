let form = document.getElementById("grade");
let inp = document.getElementById("nota_eval");

form.onsubmit = (e)=>{

    let val = parseInt(inp.innerText);

    if (1<=val<=7){
        //Armar acá logica de insercion de nota
    }


    e.preventDefault();
}