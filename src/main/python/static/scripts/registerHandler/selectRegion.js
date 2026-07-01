let selectRegion = document.getElementById("region");
let selectComuna = document.getElementById("comuna");

let deletedFirstElement = false;

let ciudadData = new Array(16);


/*
Busca las ciudades dado un id de región. Si ya se buscó previamente 
(y la búsqueda fue buena), se almacena de forma local
*/
async function fetchCities(region_id){
    if (ciudadData[region_id]) return ciudadData[region_id];
    let list;

    try{
        list = await (await fetch(`/api/cities_by_region/${region_id}`)).json();
        ciudadData[region_id] = list;
    }catch (e){
        list = []
    }

    return list
}

/*
Elimina la opcion "seleccionar region al momento de elegir una region"
*/
function deleteDefault(){
        if (!deletedFirstElement){
        selectRegion.removeChild(selectRegion.children[0])
        deletedFirstElement = true;
    }
}


/*
Reinicia el select de comunas
*/
function resetCities(){
    selectComuna.value="";

    for (let child of selectComuna.children){
        selectComuna.removeChild(child)
    }

    selectComuna.setAttribute('disabled','');
}

/*
Cambia las opciones de comuna disponibles en el formulario de inscripción
*/
async function toggleCities() {
    resetCities();

    let cities = await fetchCities(parseInt(selectRegion.value));
    deleteDefault()

    
    for (let city of cities){
        let city_node = document.createElement('option')
        city_node.value = city.id;
        city_node.innerText = city.comuna;

        selectComuna.append(city_node);
    }

    if (cities.length>0){
        selectComuna.removeAttribute('disabled');
    }
}


selectRegion.oninput = toggleCities;

//Recarga automatica de comunas
window.onload=(ev)=>{
    if(selectRegion.value){
        toggleCities()
    }
}