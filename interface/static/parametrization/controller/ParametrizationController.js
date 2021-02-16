class ParametrizationController {

	constructor(){
		this._simulationMenuEl = document.querySelector("#simulation");		
		this.initializate();

	}

	initializate() {	

		// simulation
		this._simulationMenuEl.addEventListener("click", e => {
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
