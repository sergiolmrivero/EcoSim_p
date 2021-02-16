class ParametrizationController {

	constructor(){
		this._simulationMenuEl = document.querySelector("#simulation");
		this._modelMenuEl = document.querySelector("#model");
		this._spacesMenuEl = document.querySelector("#spaces");
		this._agentsMenuEl = document.querySelector("#agents");
		this._observersMenuEl = document.querySelector("#observers");

		this.initializate();

	}

	addEventListenerToMenuItemToHideCorrespondingDiv(menuItemEl, id_div) {
		menuItemEl.addEventListener("click", e => {
			this.hideElement(id_div);
		});		
	}

	addEventListenerToMenuItemToShowCorrespondingDiv(menuItemEl, id_div) {
		menuItemEl.addEventListener("click", e => {
			this.showElement(id_div);			
		});		
	}

	initializate() {	

		// hide model div
		// this.hideElement('div-model');

		// hide spaces div
		// this.hideElement('div-spaces');

		// hide agents div
		// this.hideElement('div-agents');

		// hide observers div
		// this.hideElement('div-observers');

		let arrMainDivEl = Array.prototype.slice.call(document.querySelectorAll(".main > div"));
		arrMainDivEl.slice(1, arrMainDivEl.length).forEach(divEl => {
			this.hideElement(divEl.id);
		});

		document.querySelectorAll(".sidenav > a").forEach(aEl => {
			this.addEventListenerToMenuItemToShowCorrespondingDiv(aEl, "div-" + aEl.id);
			// this.addEventListenerToMenuItemToHideCorrespondingDiv(aEl, "div-" + aEl.id);
		});



	}

	showElement(i) {
		document.querySelector("#" + i).style.display = "block";
	}

	hideElement(i) {
		document.querySelector("#" + i).style.display = "none";
	}
	
}
