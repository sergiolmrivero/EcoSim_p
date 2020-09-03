var space_id = 0;
var scenario_id = 0;
var agent_id = 0;
var y = 100;

var models = ['ipd model', 'el farol bar model', 'macroeconomy model', 'dumb model'];
var spaces = ['space 1', 'space 2', 'space 3', 'space 4'];
var agents = ['agent 1', 'agent 2', 'agent 3', 'agent 4'];
var scenarios = ['scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'];
var selected_spaces = [];

function change_header(){
	var random = Math.floor(Math.random()*4);
	document.getElementById('header_text').innerHTML = models[random];
	
}

function get_parameters(){
	get_spaces();
	get_scenario();
	get_agents();
	change_header();
	}

function add_space(){

var select = document.getElementById('spaces_combo');
var option = document.createElement('option');
	option.value = "spc"+ space_id;
	option.text  = spaces[space_id];
	select.appendChild(option);

	space_id++;
}


function get_spaces(){
var i;
	for (i = 0; i < spaces.length; i++) {
		add_space();
	}
}


function add_scenario(){
var select = document.getElementById('scenarios_combo');
var option = document.createElement('option');
	option.value = "scn"+ scenario_id;
	option.text  = scenarios[scenario_id];
	select.appendChild(option);

	space_id++;

	scenario_id++;
}


function get_scenario(){
var i;
	for (i = 0; i < scenarios.length; i++) {
		add_scenario();
	}
}

function add_agents(){
var select = document.getElementById('agents_combo');
var option = document.createElement('option');
	option.value = "agt"+ agent_id;
	option.text  = agents[agent_id];
	select.appendChild(option);
	agent_id++;
}

function get_agents(){
var i;
	for (i = 0; i < scenarios.length; i++) {
		add_agents();
	}
}
var counter = 0;
function append_space(){
	
var select = document.getElementById('spaces_combo');
var option = select.options[select.selectedIndex].text;
var text = document.createElement('p');
var list_item = document.createElement('div');
var x = document.createElement('img');

    x.src = "images/x.png";
    x.setAttribute('class','img');
    list_item.setAttribute('value', option)
    x.setAttribute('onclick','remove_space(this.parentNode.value);');
    list_item.setAttribute('class','list_item');
    list_item.setAttribute('id','list_item'+counter);
    
    text.setAttribute('value', option);
    selected_spaces.push(""+option+"");

var text_sample = document.createTextNode(option);
var spaces_div = document.getElementById('spaces');
    

    text.appendChild(text_sample);
   
    list_item.appendChild(x);
    list_item.appendChild(text);
    spaces_div.appendChild(list_item);
    counter++;

}

function append_scenario(){
	
var select = document.getElementById('scenarios_combo');
var option = select.options[select.selectedIndex].text;
var text = document.createElement('p');
var list_item = document.createElement('div');
var x = document.createElement('img');
    x.src = "images/x.png";
    x.setAttribute('class','img');
    x.setAttribute('onclick','this.parentNode.parentNode.removeChild(this.parentNode);');
    list_item.setAttribute('class','list_item');
    list_item.setAttribute('id','list_item'+counter);
var text_sample = document.createTextNode(option);
var scenarios_div = document.getElementById('scenarios_container');

    text.appendChild(text_sample);
   
    list_item.appendChild(x);
    list_item.appendChild(text);
    scenarios_div.appendChild(list_item);
    counter++;

}

function append_agent(){
	
var select = document.getElementById('agents_combo');
var option = select.options[select.selectedIndex].text;
var text = document.createElement('p');
var list_item = document.createElement('div');
var x = document.createElement('img');
var no_of_agents = document.getElementById("number_input").value;
var number = document.createTextNode(" ("+no_of_agents+")");
var toggle_div = document.createElement('div');
var toggle_label = document.createElement('label')
var toggle_checkbox = document.createElement('input');

	toggle_checkbox.setAttribute('type','checkbox');
	toggle_div.setAttribute('class', 'toggle');

    x.src = "images/x.png";
    x.setAttribute('class','img');
    x.setAttribute('onclick','this.parentNode.parentNode.removeChild(this.parentNode);');
    list_item.setAttribute('class','agent_list_item');
    list_item.setAttribute('id','list_item'+counter);
	


var text_sample = document.createTextNode(option);
var agents_div = document.getElementById('agents');

    text.appendChild(text_sample);
    text.appendChild(number);
   
    list_item.appendChild(x);
    list_item.appendChild(text);
var i;
	for (i = 0; i < selected_spaces.length; i++) {
		
	var space_text = document.createElement('p');
	var space_text_sample = document.createTextNode(selected_spaces[i]);
	var checkbox = document.createElement('input');
	checkbox.setAttribute('type', 'checkbox');
	checkbox.setAttribute('class', 'checkbox');


		space_text.appendChild(space_text_sample);
		list_item.appendChild(checkbox);
		list_item.appendChild(space_text);
		
		y++;
	   	}
    agents_div.appendChild(list_item);
    counter++;

}

function remove_space(y){
	alert(y);
}

