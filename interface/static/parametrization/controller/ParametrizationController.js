class ParametrizationController {

	constructor(){
		this._simulationMenuEl = document.querySelector("#simulation");	
		this.initializate();

	}

	addEventListenerToToMenuItemToHideCorrespondingDiv(menuItemEl, id_div) {
		menuItemEl.addEventListener("click", e => {
			this.hideElement(id_div);
		});		
	}

	initializate() {	

		// simulation
		this.addEventListenerToToMenuItemToHideCorrespondingDiv(this._simulationMenuEl, "div-simulation");

		// model
		// spaces
		// agents
		// observers

	}

	showElement(i) {
		document.querySelector("#" + i).style.display = "block";
	}

	hideElement(i) {
		document.querySelector("#" + i).style.display = "none";
	}
	
}
