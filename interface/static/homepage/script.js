var id = 0;

// Assynchronous data request from API

var models = [];

// HTTP GET Asyncronous
function httpGetAsync(theUrl, callback) {   
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
        
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null); // https://developer.mozilla.org/pt-BR/docs/Web/API/XMLHttpRequest/send 
}


// GET models from ModelList(Resource)
httpGetAsync('http://127.0.0.1:5000/models',function (response){
	let obj = JSON.parse(response);

    for (let i = 0; i < obj.models.length; i++){
    	// console.log(obj.models[i]);
    	models[i] = obj.models[i];
    }

    // console.log(models);
});
/*--------------------------------------------*/


function add_list(){
	
	var button_list_item = document.createElement('button');
	// var button_list_item = document.createElement('input');
	var text_sample = document.createTextNode(models[id]);
	var text = document.createElement('p');
	var img = document.createElement('img');
	img.src = 'static/homepage/images/next.png';

	button_list_item.setAttribute('class','list-item');
	button_list_item.setAttribute('id','list-item'+id);

	// bruno
	button_list_item.setAttribute('type', 'submit')
	button_list_item.setAttribute('value', models[id])
	button_list_item.setAttribute('name', 'model')

	text.setAttribute('class', 'list-item-text');
	img.setAttribute('class','next');
	
	text.appendChild(text_sample);
	
	button_list_item.appendChild(img);
	button_list_item.appendChild(text);
	// document.getElementById('container').appendChild(button_list_item);
	document.getElementById('form-models').appendChild(button_list_item);

	id++;
}

function get_list(){
	var i;
	for (i = 0; i < models.length; i++) {
		add_list();
	}
}
