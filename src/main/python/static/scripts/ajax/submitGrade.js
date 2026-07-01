let form = document.getElementById("grade");
let inp = document.getElementById("nota_eval");

form.onsubmit = (e)=>{

    let val = parseInt(inp.value);

    if (1<=val<=7){
        fetch("http://localhost:8080/actividad/agregarNota",{
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "idActividad": parseInt(params.get("id")),
                "nota": val 
            })
        }).then(async res =>{
            window.location.reload();
        })
    }


    e.preventDefault();
}