const params = new URLSearchParams(window.location.search);

fetch(`http://localhost:8080/actividad/getById/${params.get('id')}`)
.then(async r=>{
    let json = await r.json();
    document.getElementById("nombreActividad").innerText = json["nombre"];
    document.getElementById("descripcion").innerText = json["descripcion"];
    document.getElementById("nota").innerText = json["nota"] ?  json["nota"].toString() : "Nota Vacía";

}).catch(e=>alert("Error Cargando el contenido!!!"));