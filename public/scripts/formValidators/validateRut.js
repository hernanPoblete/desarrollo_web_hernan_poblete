let idElement = document.getElementById('rut');
let numberInput = idElement.value.replace(/[^0-9]/g, '');


function formatRut(){

	if (numberInput.length === 0){
		idElement.value = '';
		return
	}

	let temp = [...numberInput];
	let dv = temp.pop()
	let division = [""]
	let i = temp.length % 3;

	if (i === 0){
		division.pop()
	}

	while (i > 0){
		division[0] += temp.shift();
		i--;
	}

	//Invariante: A partir de este punto, temp es de un tamaño múltiplo de 3.

	while(temp.length !=0){
		division.push(temp.shift() + temp.shift() + temp.shift());
	}

	idElement.value = division.join('.') + '-' + dv
}

function validateDV(){
	let rutMap = numberInput.split("")
				.map(x=>x.replace("k",'10'))
				.map(x=>parseInt(x));
	let testDV = rutMap.pop();


	let multipliers = [2,3,4,5,6,7];
	let result = 0;
	const l = rutMap.length;

	rutMap.forEach((_, index)=>{
		const mult = multipliers[index%6];

		result += (rutMap[l-index-1]*mult);
	})

	result = (11 - result % 11) % 11;

	return testDV === result;
}

idElement.onkeypress = (e)=>{
	if(/[0-9k]/.test(e.key)){
		return
	}

	e.preventDefault();
}


idElement.oninput = (e)=>{
	numberInput = idElement.value.replace(/[^0-9k]/g, '');

	if(!validateDV()){
		console.log(idElement.classList.add("err"));
	}	

	formatRut();		
}