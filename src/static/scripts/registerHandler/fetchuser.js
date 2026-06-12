


let idInput = document.getElementById("rut")
let nameSpan = document.getElementById("uname");

let timeout;


idInput.oninput = ()=>{
    nameSpan.innerText = "";

    clearTimeout(timeout);
    t=undefined;


    timeout = setTimeout(()=>{
        fetch(`/api/user_by_id/${idInput.value}`)
        .then(async (r)=>{
            let result = (await r.json())[0]

            if (result.length === 0){
                nameSpan.innerText = "¡No se encontró este rut en la base de datos!"
            } else {
                nameSpan.innerText = result;
            }
            
        }).catch(e=> nameSpan.innerText = "¡Ocurrio un error al comunicar con la base de datos!")
    }, 2000);
}
