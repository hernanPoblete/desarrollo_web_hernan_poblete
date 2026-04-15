let db = mockDBHandle;

const userListElement = document.getElementById('userList');

db.users.forEach(element=>{
	userListElement.appendChild(element.getNode())
})