var id = 0;
var models = ['Iterated Prisoner Dilemma Model', 'El Farol Bar Model', 'Macroeconomy Model', 'Dumb Model', 'model x'];
function add_list(){
	
	var button_list_item = document.createElement('button');
	var text_sample = document.createTextNode(models[id]);
	var text = document.createElement('p');
	var img = document.createElement('img');
	img.src = 'images/next.png';

	button_list_item.setAttribute('class','list-item');
	button_list_item.setAttribute('id','list-item'+id);
	text.setAttribute('class', 'list-item-text');
	img.setAttribute('class','next');
	
	text.appendChild(text_sample);
	
	button_list_item.appendChild(img);
	button_list_item.appendChild(text);
	document.getElementById('container').appendChild(button_list_item);
	id++;
}

function get_list(){
	var i;
	for (i = 0; i < models.length; i++) {
		add_list();
}
}