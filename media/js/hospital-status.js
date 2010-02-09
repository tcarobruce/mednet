function makeGradientSlider(element, formField){
	formField.val(5);
	element.addClass('slider');
	/*
	element.gradient({
		from:      '00FF00',
		to:        'FF0000',
		direction: 'vertical'
	});
	*/
	element.slider({
		min:0, 
		max:10, 
		step: 1,
		value:5,
		slide: function(event, ui) { formField.val(ui.value); }
	});
}

function hospitalStatusSliders() {
	$('#id_security_status').hide();
	makeGradientSlider($('#div-security-status'), $('#id_security_status'));	
	
	$('#id_backlog_status').hide();
	makeGradientSlider($('#div-backlog-status'), $('#id_backlog_status'));	
	
	$('#id_critical_backlog_status').hide();
	makeGradientSlider($('#div-critical-backlog-status'), $('#id_critical_backlog_status'));	
	
	$('#id_non_critical_backlog_status').hide();
	makeGradientSlider($('#div-non-critical-backlog-status'), $('#id_non_critical_backlog_status'));	
	
	$('#id_disease_critical_backlog_status').hide();
	makeGradientSlider($('#div-disease-critical-backlog-status'), $('#id_disease_critical_backlog_status'));	
	
	$('#id_supply_status').hide();
	makeGradientSlider($('#div-supply-status'), $('#id_supply_status'));	
	
	$('#id_supply_delivery_status').hide();
	makeGradientSlider($('#div-supply-delivery-status'), $('#id_supply_delivery_status'));	
	
	$('#id_communication_status').hide();
	makeGradientSlider($('#div-communication-status'), $('#id_communication_statu'));
}
