// Este archivo hace mock de la info sacada de un DB. 
// Como no tenemos acceso a apis o cualquier cosa backend, no podemos usar fetch 
// (Intente usar un json conectado con mi pagina del dcc, pero el response no incluye un encabezado cors 
// crucial para que el proceso funcione, por lo que fetch me tiraba un networkError. Esto es lo mejor que pude hacer)

class Actividad{
	constructor(nombre, tipo, horarios, archivos, links){
		this.nombre = nombre;
		this.tipo = tipo;
		this.horarios = horarios;
		this.archivos = archivos;
		this.links = links;


	}


	asJson(){
		return {
			nombre: this.nombre,
			tipo: this.tipo,
			horarios: this.horarios,
			archivos: this.archivos,
			links: this.links
		}
	}

	makeNode() {
		const node = document.createElement('li');
		node.classList.add('flex');

		const title = document.createElement('h4');
		const horarioTitle = document.createElement('h5');

		title.innerText = this.nombre;
		horarioTitle.innerText = "Horarios";


		// Nodo con informaciones de nombre y horarios
		const infoNode = document.createElement('div');
		
		infoNode.appendChild(title);
		infoNode.appendChild(horarioTitle);

		infoNode.classList.add("flex-col-25");

		const horarios = document.createElement('ul');
		const dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];


		this.horarios.forEach((dia, index)=>{

			if(dia[0] && dia[1]){
				const el = document.createElement('li');
				el.innerHTML = `${dias[index]}: ${dia[0]}-${dia[1]}`
				horarios.appendChild(el);		
			}

		})

		infoNode.appendChild(horarios);


		// Nodo con los links relacionados
		const linksNode = document.createElement('div');
		linksNode.classList.add('flex-col-25');

		linksNode.innerHTML = '<h5> Links Relacionados </h5>'

		const links = document.createElement('ol');
		this.links.forEach(link => {
			const aElement = document.createElement('a');
			aElement.href = link;
			aElement.innerText = link;

			links.appendChild(aElement);
		})
		linksNode.appendChild(links)


		// Nodo con las imagenes

		const imgNode = document.createElement('div');
		imgNode.classList.add('flex-col-50');

		this.archivos.forEach(x=>{
			const img = document.createElement('img');
			img.src = x;

			imgNode.appendChild(img);
		});

		node.appendChild(infoNode)
		node.appendChild(linksNode);
		node.appendChild(imgNode)

		return node;
	}
}

class User{
	constructor(nombre, tipo, rut, correo, telefono, actividades){
		this.nombre = nombre;
		this.rut = rut;
		this.tipo = tipo;
		this.correo = correo;
		this.telefono = telefono;
		this.actividades = actividades;


		this.node = document.createElement('li');


		this.node.innerHTML = `
		<h3> ${this.nombre} </h3>
		<h4> ${this.tipo} </h4>
		<h3> Actividades </h3>
		`

		const activitiesList = document.createElement('ul');

		this.actividades.forEach(actividad=>{
			activitiesList.appendChild(actividad.makeNode())
		})

		this.node.appendChild(activitiesList);
	}

	asJson(){
		return {
			nombre: this.nombre,
			rut: this.rut,
			tipo: this.tipo,
			actividades: this.actividades.map(x=>x.asJson()),
			correo: this.correo,
			telefono: this.telefono
		}
	}

	getNode(){
		return this.node;
	}
}



let actividades = [
	new Actividad(
		'ver reels', 
		'cultural', 
		[["9:00", "12:00"],["9:00", "12:00"],["9:00", "12:00"],["9:00", "12:00"],["9:00", "12:00"],["9:00", "12:00"],["9:00", "12:00"]],
		["https://www.lescarnetssante.fr/wp-content/uploads/2025/12/1764981989-comprendre-et-surmonter-le-doomscrolling-nos-conseils-1024x576.jpg"],
		["https://instagram.com"]
	),
	
	new Actividad(
		'ir al gimnasio', 
		'deportiva',
		[["10:00", "11:00"],[],["10:00", "11:00"],["10:00", "11:00"],[],[],[]],
		["https://thumbs.dreamstime.com/z/mirada-del-gato-con-dos-pesas-de-gimnasia-40661121.jpg", "https://i.pinimg.com/736x/73/86/35/7386355e526a9c512aa3841a54cec2a5.jpg"],
		["https://www.gimnasios.cl/cadenas/pacific-fitness/"]
	),

	new Actividad(
		'tomar tecito',
		'social',
		[[],[],[],[],[],[],["12:00", "15:45"]],
		["https://as2.ftcdn.net/jpg/06/73/31/87/1000_F_673318716_j1AAjbN54WGHcJnwydfbIT1KuKI4dHTC.webp"],
		["https://teashop.com/"]
	),

	new Actividad(
		'programacion competitiva',
		'tecnologica',
		[[],[],["12:00", "16:00"],[],[],["15:00","19:00"]],
		["https://i.imgflip.com/7fhly5.png"],
		["https://uchile.progcomp.cl"]
	),

	new Actividad(
		'observar pájaros',
		'recreativa',
		[['8:00', '11:45'], [], ['12:00', '14:30'], [], [], ['07:15', "18:30"]],
		["https://www.catster.com/wp-content/uploads/2024/03/bengal-cat-looking-at-at-bird-feeder-in-window_Steve-Heap_Shutterstock-e1711148536820.jpg.webp"],
		["https://aveschile.cl"]
	)
]


var mockDBHandle = {

	users: [
		new User(
			"Benjamín Duarte", 
			"Estudiante de Pregrado",
			"11.111.111-1",
			"benjamin.duarte@ug.uchile.cl",
			undefined,
			[actividades[0], actividades[1]]
		),

		new User(
			'Valeria Serrano',
			"Estudiante de Pregrado",
			"22.222.222-2",
			"valeria.serrano@ug.uchile.cl",
			undefined,
			[actividades[2], actividades[4]]
		),

		new User(
			'Eduardo Graells-Garrido',
			"Academico",
			"3.333.333-3",
			"egraells@dcc.uchile.cl",
			undefined,
			[actividades[1], actividades[4]]
		),

		new User(
			'Gabriel Carmona',
			"Estudiante de Pregrado",
			"44.444.444-4",
			"gcarmona@dcc.uchile.cl",
			undefined,
			[actividades[1], actividades[2], actividades[3]]
		),

		new User(
			'Lucas Villagran',
			'Estudiante de Postgrado',
			"55.555.555-5",
			'carrera@payaso.net',
			undefined,
			[actividades[0], actividades[4]]
		)
	],


	searchByName(name){
		const regex = new RegExp(name);
		return this.users.filter(x=>regex.test(x.nombre));
	},

	searchByRut(rut){
		const regex = new RegExp(name);
		return this.users.filter(x=>regex.test(x.rut));
	}
}