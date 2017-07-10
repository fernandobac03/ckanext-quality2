
function add_field_in_group(index, label, subfields){
	var next=index+1;
	var elementid = 'fields_repeating_container_'+label+'_'+index;
	var nextelementid='fields_repeating_container_'+label+'_'+next;
	document.getElementById(nextelementid).style.display = 'block';
	var buttonid='button_fields_repeating_container_'+label+'_'+index;
	document.getElementById(buttonid).style.display = 'none';
	MoverDiv(elementid, subfields, index, next);
}



function MoverDiv(elementid, subfields, index, next){
	for (i = 0; i < subfields.length; i++) {
		/**
			Agregando los actuales subcampos al div del campo principal
		**/
       		var subfield = document.getElementById('fields_repeating_container_'+subfields[i]+'_'+index);
		var groupfields = document.getElementById(elementid);
		groupfields.style.background ='#F5F5F5'
		if (groupfields && subfield)
		{
			groupfields.appendChild(subfield);
		}	
		/**mostrando los siguientes subcampos*/
		var nextsubelementid = 'fields_repeating_container_'+subfields[i]+'_'+next;
		document.getElementById(nextsubelementid).style.display = 'block';
	}
}

