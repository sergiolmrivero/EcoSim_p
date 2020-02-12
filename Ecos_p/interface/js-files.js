
      function hide1() {        //essas duas funções não ficarão aqui por muito mais tempo
        var checkBox = document.getElementById("check1");
        var text = document.getElementById("MinhaDiv1");
          if (checkBox.checked == true){
            text.style.display = "block";
          } else {
            text.style.display = "none";
          }
        }
      function hide2() {
        var checkBox = document.getElementById("check2");
        var text = document.getElementById("MinhaDiv2");
        if (checkBox.checked == true){
          text.style.display = "block";
          } else {
          text.style.display = "none";
          }
        }
      function update() {         //função que chama a função que criará o agente(muito provavelmente removerei em versões futuras)

        var select = document.getElementById('combo');          
        var value = select.options[select.selectedIndex].value;
        addAgent();
        }

      function addAgent(){     //funçao que adiciona o box do agente
        var div = document.createElement('div');
        div.classList.add('boxdin');        //criação da div
        div.setAttribute('id','mydiv');
        var h2 = document.createElement('h3');
        var select = document.getElementById('combo');
        var value = select.options[select.selectedIndex].value;
        var checkBoxy = document.getElementById("check2");
        var checkBox = document.getElementById("check1");
        var br = document.createElement("br");
        var br1 = document.createElement("br");
        if((checkBoxy.checked == false) && (checkBox.checked == false)){
    		alert("Please select at least one space.");
    	}else{
    	if(value == 'funny'){
			var h2text = document.createTextNode("Select space for Funny Bug");
			document.body.appendChild(div);
        	h2.appendChild(h2text);
        	document.getElementById("mydiv").appendChild(h2);
        if (checkBox.checked == true){
	        var check1 = document.createElement('input');
	        check1.setAttribute('type','checkbox');
	        var check1text = document.createTextNode("Funny Space");
	        document.getElementById("agents_slot").appendChild(div);
	        check1.appendChild(check1text);
	        document.getElementById("mydiv").appendChild(check1);
	        document.getElementById("mydiv").appendChild(check1text);
	        document.getElementById("mydiv").appendChild(br);
        }
        
        if (checkBoxy.checked == true){
            var check1 = document.createElement('input');
            check1.setAttribute('type','checkbox');
            var check1text = document.createTextNode("Boring Space");
            document.getElementById("agents_slot").appendChild(div);
            check1.appendChild(check1text);
            document.getElementById("mydiv").appendChild(check1);
            document.getElementById("mydiv").appendChild(check1text);
            
    } 
        }

		else if(value == 'circumspect'){
			var h2text = document.createTextNode("Select space for Circumspect Bug");
			document.getElementById("mydiv").appendChild(br);
			document.body.appendChild(div);
        	h2.appendChild(h2text);
        	document.getElementById("mydiv").appendChild(h2);
        	if (checkBox.checked == true){
		        var check1 = document.createElement('input');
		        check1.setAttribute('type','checkbox');
		        var check1text = document.createTextNode("Funny Space");
		        document.getElementById("agents_slot").appendChild(div);
		        check1.appendChild(check1text);
		        document.getElementById("mydiv").appendChild(check1);
		        document.getElementById("mydiv").appendChild(check1text);
		        document.getElementById("mydiv").appendChild(br);
        }
        
        if (checkBoxy.checked == true){
            var check1 = document.createElement('input');
            check1.setAttribute('type','checkbox');
            var check1text = document.createTextNode("Boring Space");
            document.getElementById("agents_slot").appendChild(div);
            check1.appendChild(check1text);
            document.getElementById("mydiv").appendChild(check1);
            document.getElementById("mydiv").appendChild(check1text);
            
    } 
        }
    }
        if(value=='null'){
			alert("Please select an agent.");
			} 	
		}

	function next1(){
		var tab2 = document.getElementById("tab2");
		tab2.checked = true;
			}

	function next2(){
		var tab3 = document.getElementById("tab3");
		tab3.checked = true;
			}

	function back1(){
		var tab1 = document.getElementById("tab1");
		tab1.checked = true;
			}

	function back2(){
		var tab1 = document.getElementById("tab2");
		tab1.checked = true;
			}