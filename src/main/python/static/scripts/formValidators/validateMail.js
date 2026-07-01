const mailRegex = /(\w[._-]*)+@(\w+\.)+[a-z]{1,3}/;
const mailInput = document.getElementById('correo');


let validmail = mailRegex.test(mailInput.value)
let erredInput = mailInput.classList.contains("err");

function toggleErr(){
	if(!validmail && !erredInput){
		mailInput.classList.add("err");
	}

	if(validmail && erredInput){
		mailInput.classList.remove("err");
	}

	erredInput = mailInput.classList.contains("err");
}

mailInput.oninput = (e)=>{
	validmail = mailRegex.test(mailInput.value)
	toggleErr()
}