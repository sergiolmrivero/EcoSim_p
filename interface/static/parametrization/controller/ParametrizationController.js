class ParametrizationController {

	constructor(){

		this._parameters = {simulation: [], model: [], spaces: [], agents: [], observers: []};

		this._simulationMenuEl = document.querySelector("#simulation");
		this._modelMenuEl = document.querySelector("#model");
		this._spacesMenuEl = document.querySelector("#spaces");
		this._agentsMenuEl = document.querySelector("#agents");
		this._observersMenuEl = document.querySelector("#observers");

		this._arrMainDivEl = Array.prototype.slice.call(document.querySelectorAll(".main > div"));

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

		// this._arrMainDivEl.slice(1, this._arrMainDivEl.length).forEach(divEl => {
		// 	this.hideElement(divEl.id);
		// });

		document.querySelectorAll(".sidenav > a").forEach(aEl => {
			this.addEventListenerToMenuItemToShowCorrespondingDiv(aEl, "div-" + aEl.id);			
		});

	}

	showElement(i) {

		this._arrMainDivEl.forEach(divEl => {

			// hiding displayed elements before show the clicked div corresponding
			// to clicked menu item

			divEl.style.display = "none";


		});

		document.querySelector("#" + i).style.display = "block";
	}

	hideElement(i) {
		document.querySelector("#" + i).style.display = "none";
	}
	
}
