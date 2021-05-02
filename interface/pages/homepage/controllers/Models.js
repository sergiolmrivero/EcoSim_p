class Models {

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

        function captilize(string){
            return string.replace(/^./, string[0].toUpperCase());
        }

        function split_names(string){
            return string.split("_").map(name => captilize(name)).join(" ");
        }    

    	modelsEl.innerHTML = `
    	 	<label for="select-model">Model: choose a model to simulate</label><br>
    		<select id="select-model" name="model">
				${
                    models.map(model => `<option value="${model}">${split_names(model)}</option>`).join("")
                }
    		</select>
    		<br><br>
    	`;
    	return modelsEl;
    }
	
}
