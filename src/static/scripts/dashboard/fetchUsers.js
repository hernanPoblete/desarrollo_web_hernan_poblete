
/**
 * Fetchea y muestra los datos y actividades de un usuario consultando al servidor con su rut
 */
function displayUser(id){

	let req = new Request(
		'/api/user',
		{
			body:{
				id:id
			},
			method: "POST"
		}
	)
	fetch(req).then(res=>{
		console.log(res.json().value)	
	})
}