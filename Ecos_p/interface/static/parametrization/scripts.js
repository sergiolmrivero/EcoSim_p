// Assynchronous data request from API

var spaces = [];
var agents = [];
var scenarios = [];

function httpGetAsync(theUrl, callback) {   
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
        
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null); // https://developer.mozilla.org/pt-BR/docs/Web/API/XMLHttpRequest/send 
}


// GET spaces
httpGetAsync('http://127.0.0.1:5000/spaces',function (response){
	let obj = JSON.parse(response);

    for (let i = 0; i < obj.spaces.length; i++){
    	console.log(obj.spaces[i]);
    	spaces[i] = obj.spaces[i];
    }

    console.log(spaces);
});

// GET agents
httpGetAsync('http://127.0.0.1:5000/agents',function (response){
    let obj = JSON.parse(response);

    for (let i = 0; i < obj.agents.length; i++){
        console.log(obj.agents[i]);
        agents[i] = obj.agents[i];
    }

    console.log(agents);
});

// GET scenarios
httpGetAsync('http://127.0.0.1:5000/scenarios',function (response){
    let obj = JSON.parse(response);

    for (let i = 0; i < obj.scenarios.length; i++){
        console.log(obj.scenarios[i]);
        scenarios[i] = obj.scenarios[i];
    }

    console.log(scenarios);
});
