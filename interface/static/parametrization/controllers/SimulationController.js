class SimulationController {

	constructor(){

		this._modelsEl = document.getElementById("models");

		this.initializate();			

	}


	initializate() {

		this.getModels();

	}


    getModels(){
        const url = 'models';
            fetch(url)
                .then(resp => resp.json())
                .then(obj => {
                    let modelsEl = this.renderModels(obj.models);
                    this._modelsEl.appendChild(modelsEl);
                });

    }


    renderModels = (models) => {
    	let modelsEl = document.createElement("div");
    	modelsEl.innerHTML = `
    	 	<label for="models">Model: choose a model to simulate</label><br>
    		<select id="models" name="models">
				${models.map(model => `<option value="${model}">${model}</option>`).join("")}
    		</select>
    		<br><br>
    	`;
    	return modelsEl;
    }
	
}
