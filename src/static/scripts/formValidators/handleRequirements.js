const form = document.getElementById('mainForm')
const requirements = form.querySelectorAll('[required]')

function checkNotEmpty(){
	requirements.forEach(r=>{
		if (! r.value) return false;
	});

	return true;
}

function errEmpty(){
	requirements.forEach(r=>{
		if (! r.value){
			r.classList.add('err');
		}
	});
}

form.onsubmit = (e)=>{
	if(checkNotEmpty()){
		errEmpty();
		e.preventDefault();		
	};

	form.submit()
}