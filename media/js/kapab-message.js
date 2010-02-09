	$(document).ready(function() {
		
		$('#plus_link').click(function() {
			url = "/mednet/sahana/add_person/?hospital_id=" + $('#hospital_id').val();
			populateForm(url, false);
			return false
		});
		$('#hospitalactionform button.activities').click(function() {
			populateForm("/mednet/sahana/add_activities/?hospital_id=" + $('#hospital_id').val(), false, '#id_date');
			return false;
		});
		$('#hospitalactionform button.capacity').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_hbc/?hospital_id=" + $('#hospital_id').val(), false, '#id_date');
			return false
		});
		$('#hospitalactionform button.contacts').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_contact/?hospital_id=" + $('#hospital_id').val(), false);
			return false;
		});
		$('#hospitalactionform button.requests').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_request/?hospital_id=" + $('#hospital_id').val(), false);
			return false;
		});
		$('#hospitalactionform button.resources').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_resources/?hospital_id=" + $('#hospital_id').val(), false);
			return false;
		});
		$('#hospitalactionform button.services').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_services/?hospital_id=" + $('#hospital_id').val(), false);
			return false;
		});
		$('#hospitalactionform button.status').click(function() {
			populateForm('/mednet/sahana/add_status/?hospital_id=' + $('#hospital_id').val(), true, '#id_status_date'); 
			return false;
		});
		$('#messageactionform button.custom').click(function() {
			if($('#custom_message_area').css('display') == 'none') {
				$('#custom_message_area').slideDown();
			} else {
				$('#custom_message_area').slideUp()
			}
			return false
		});

		$('#messageactionform button.complete').click(function() {
			$('#hospitaldataform').text('');
			msgtype = $('#messagetype').val();
			msgid = $('#msg_id').val();
				$.ajax({ url: "/mednet/messaging/mark_message/?status=CM&msgtype=" + msgtype + "&msgid=" + msgid + "&custom_msg=" + escape($("#custom_message").val()), context: document.body, success: function(){
				$('#hospitaldataform').hide()
				$('#hospitaldataform').html('<h2>Message Complete ... Loading Next Message</h2>');
				$('#hospitaldataform').fadeIn('slow', function() {});
				setTimeout(function() { window.location = "/mednet/messaging/next_message/" + msgtype; }, 1500);
			}});
			return false
		});
		$('#messageactionform button.ignore').click(function() {
			$('#hospitaldataform').text('');
			msgtype = $('#messagetype').val();
			msgid = $('#msg_id').val();
				$.ajax({ url: "/mednet/messaging/mark_message/?status=IG&msgtype=" + msgtype + "&msgid=" + msgid, context: document.body, success: function(){
				$('#hospitaldataform').hide()
				$('#hospitaldataform').html('<h2>Message Ignored ... Loading Next Message</h2>');
				$('#hospitaldataform').fadeIn('slow', function() {});
				setTimeout(function() { window.location = "/mednet/messaging/next_message/" + msgtype; }, 1500);
			}});
			return false
		});
		$('#messageform button.capacity').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_hbc/?hospital_id=" + $('#hospital_id').val(), false, '#id_date');
			return false
		});
		$('#messageform button.contacts').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_contact/?hospital_id=" + $('#hospital_id').val(), false);
			return false;
		});
		$('#messageform button.resources').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_resources/?hospital_id=" + $('#hospital_id').val(), false);
			return false;
		});
		$('#messageform button.services').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_services/?hospital_id=" + $('#hospital_id').val(), false);
			return false;
		});
		$('#messageform button.requests').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_request/?hospital_id=" + $('#hospital_id').val(), false);
			return false;
		});
		$('#messageform button.activities').click(function() {
			$('#hospitaldataform').text('');
			populateForm("/mednet/sahana/add_activities/?hospital_id=" + $('#hospital_id').val(), false, '#id_date');
			return false;
		});
		$('#messageform button.status').click(function() {
			populateForm('/mednet/sahana/add_status/?hospital_id=' + $('#hospital_id').val(), true, '#id_status_date'); 
			hospitalStatusSliders();
			return false;
		});
	});
		
		function submitHbcForm() {
			formData = $('#hbcform').serialize();
			validForm = true;
			if($('#id_date').val().replace(/\s/g,"").length < 1) {
				$('#id_date').addClass("error");
				validForm = false;	
			}
			if(!validForm) { return false;}	
			$.ajax({  
				type: "POST",  
				url: "/mednet/sahana/add_hbc/",  
				data: formData, 
				success: function() {
					$('#hospitaldataform').text('');
					$('#hospitaldataform').html("<h2>Bed Capacity Report Submitted</h2>")  
					.append("<center><p>Thank You</p></center>")  
					.hide()  
					.fadeIn(1500, function() {  
					});
				}  
			});
			return false;
		}

		function submitContactForm() {
			formData = $('#contactform').serialize();
			validForm = true;
			if(!validForm) { return false;}	
			$.ajax({  
				type: "POST",  
				url: "/mednet/sahana/add_contact/",  
				data: formData, 
				success: function() {
					$('#hospitaldataform').text('');
					$('#hospitaldataform').html("<h2>Contact Submitted</h2>")  
					.append("<center><p>Thank You</p></center>")  
					.hide()  
					.fadeIn(1500, function() {  
					});
				}  
			});
			return false;
		}
		
		function submitResourceForm() {
			formData = $('#resourceform').serialize();
			validForm = true;
			if(!validForm) { return false;}	
			$.ajax({  
				type: "POST",  
				url: "/mednet/sahana/add_resources/",  
				data: formData, 
				success: function() {
					$('#hospitaldataform').text('');
					$('#hospitaldataform').html("<h2>Resource Report Submitted</h2>")  
					.append("<center><p>Thank You</p></center>")  
					.hide()  
					.fadeIn(1500, function() {  
					});
				}  
			});
			return false;
		}


		function submitRequestForm() {
			formData = $('#hospitalrequestform').serialize();
			validForm = true;
			if($('#id_subject').val().replace(/\s/g,"").length < 1) {
				$('#id_subject').addClass("error");
				validForm = false;	
			}
			if($('#id_message').val().replace(/\s/g,"").length < 1) {
				$('#id_message').addClass("error");
				validForm = false;	
			}
			if(!validForm) { return false;}	
			$.ajax({  
				type: "POST",  
				url: "/mednet/sahana/add_request/",  
				data: formData, 
				success: function() {
					$('#hospitaldataform').text('');
					$('#hospitaldataform').html("<h2>Request Submitted</h2>")  
					.append("<center><p>Thank You</p></center>")  
					.hide()  
					.fadeIn(1500, function() {  
						//$('#hospitaldataform').append("<img id='checkmark' src='images/check.png'/>");  
					});
				}  
			});
			return false;
		}

		function submitServicesForm() {
			formData = $('#servicesform').serialize();
			validForm = true;
			if(!validForm) { return false;}	
			$.ajax({  
				type: "POST",  
				url: "/mednet/sahana/add_services/",  
				data: formData, 
				success: function() {
					$('#hospitaldataform').text('');
					$('#hospitaldataform').html("<h2>Services Submitted</h2>")  
					.append("<center><p>Thank You</p></center>")  
					.hide()  
					.fadeIn(1500, function() {  
						//$('#hospitaldataform').append("<img id='checkmark' src='images/check.png'/>");  
					});
				}  
			});
			return false;
		}
		
		function submitActivityForm() {
			formData = $('#activityform').serialize();
			validForm = true;
			if(!validForm) { return false;}	
			$.ajax({  
				type: "POST",  
				url: "/mednet/sahana/add_activities/",  
				data: formData, 
				success: function() {
					$('#hospitaldataform').text('');
					$('#hospitaldataform').html("<h2>Activity Report Submitted</h2>")  
					.append("<center><p>Thank You</p></center>")  
					.hide()  
					.fadeIn(1500, function() {  
						//$('#hospitaldataform').append("<img id='checkmark' src='images/check.png'/>");  
					});
				}  
			});
			return false;
		}

		function submitStatusForm() {
			formData = $('#hospitalstatusform').serialize();
			validForm = true;
			if(!validForm) { return false;}	
			$.ajax({
				type: "POST",
				url: "/mednet/sahana/add_status/",
				data: formData,
				success: function() {
					$('#hospitaldataform').text('');
					$('#hospitaldataform').html("<h2>Status Report Submitted</h2>")  
					.append("<center><p>Thank You</p></center>")  
					.hide()  
					.fadeIn(1500, function() {  
						//$('#hospitaldataform').append("<img id='checkmark' src='images/check.png'/>");  
					});
					$('#hospitaldataform').text('');
				}
			});
			return false;	
		}
	
		function populateForm(url, status_form, date_picker_element){
			$('#hospitaldataform').text('');
			$.ajax({
				url: url,
				cache: false,
				success: function(html){
					$('#hospitaldataform').hide()
					$("#hospitaldataform").html(html);
					if(status_form) {
						hospitalStatusSliders();
					}
					if(date_picker_element) {
						$(date_picker_element).datepicker({dateFormat: 'yy-mm-dd'});				
					}
					$('#hospitaldataform').show()
				}
			});
		}
