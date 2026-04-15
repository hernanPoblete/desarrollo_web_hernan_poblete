let db = mockDBHandle;

const userListElement = document.getElementById('userList');

db.users.forEach(element=>{
	userListElement.appendChild(element.getNode())
})


const usertypeFilter = document.getElementById('typeFilter');
const activityFilter = document.getElementById('activityFilter')
const nameFilter = document.getElementById('usernameFilter')

function filter(){
	const types = ['','artistica', 'deportiva', 'tecnologica', 'social', 'recreativa']
	const type = types[parseInt(activityFilter.value)];

	const users = ['','Estudiante de Pregrado', 'Estudiante de Postgrado', 'Academico', 'Funcionario']
	const user = users[parseInt(usertypeFilter.value)]

	const name = nameFilter.value;


	return db.users.filter(x=>x.tipo === user)
}

function showAll (){
	db.users.forEach(x=>x.getNode().classList.remove('suppressed'));
}
