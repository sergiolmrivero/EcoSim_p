class ParametrizationController {

	constructor(){
		
		this.initializate();

	}

	initializate() {	

		// ok
		let simulationMenuEl = document.querySelector("#simulation");

		// ok
		simulationMenuEl.addEventListener("click", e => {console.log('click');});

	}

	showElement(id) {
		document.getElementById(id).style.display = "block";
	}

	hideElement(id) {
		document.getElementById(id).style.display = "none";
	}
	
}
