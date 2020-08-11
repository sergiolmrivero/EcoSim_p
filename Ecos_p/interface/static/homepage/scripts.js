// Assynchronous data request from API

var models = [];

function httpGetAsync(theUrl, callback) {   
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
        
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null); // https://developer.mozilla.org/pt-BR/docs/Web/API/XMLHttpRequest/send 
}


// GET models
httpGetAsync('http://127.0.0.1:5000/models',function (response){
	let obj = JSON.parse(response);

    for (let i = 0; i < obj.models.length; i++){
    	console.log(obj.models[i]);
    	models[i] = obj.models[i];
    }

    console.log(models);
});
