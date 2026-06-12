let selectRegion = document.getElementById("region");
let selectComuna = document.getElementById("comuna");

let deletedFirstElement = false;

let ciudadData = new Array(16);

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

function deleteDefault(){
        if (!deletedFirstElement){
        selectRegion.removeChild(selectRegion.children[0])
        deletedFirstElement = true;
    }
}



selectRegion.oninput = (ev)=>{
    fetchCities(selectRegion.value).then(console.log)
}