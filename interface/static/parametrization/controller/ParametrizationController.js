class ParametrizationController {

	constructor(){
		
		this.initializate();

	}

	initializate() {	

		// ok
		let simulationMenuEl = document.querySelector("#simulation");

		// ok
		// simulationMenuEl.addEventListener("click", e => {console.log('click');});

		// ok
		// this.hideElement("div-simulation");

		//
		simulationMenuEl.addEventListener("click", e => {
			this.hideElement("div-simulation");
		});
		this.showElement("simulation");		

	}

	showElement(i) {
		document.querySelector("#" + i).style.display = "block";
	}

	hideElement(i) {
		document.querySelector("#" + i).style.display = "none";
	}
	
}
