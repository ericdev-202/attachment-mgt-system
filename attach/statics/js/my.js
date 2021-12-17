$("form#updateEvent").submit(function() {
    var idInput = $('input[name="formId"]').val().trim();
    var titleInput = $('input[name="formTitle"]').val().trim();
    var descriptionInput = $('input[name="formDescription"]').val().trim();
    var venueInput = $('input[name="formVenue"]').val().trim();
    var mdateInput = $('input[name="formDate"]').val().trim();
    var mtimeInput = $('input[name="formTime"]').val().trim();
    if (titleInput && descriptionInput && venueInput && mdateInput && mtimeInput) {
    	$.ajax({
            url: '{% url "event_update" %}',
            data: {
                'id': idInput,
                'title': titleInput,
                'description': descriptionInput,
                'venue': venueInput,
                'mdate': mdateInput,
                'mtime': mtimeInput
            },
            dataType: 'json',
            success: function (data) {
                if (data.event) {
                  updateTomy_event(data.event);
                }
            }
        });
    }else{
    	alert("All fields must have a valid value.");
    }
    $('form#updateEvent').trigger("reset");
    $('#myModal').modal('hide');
    return false;

});
function editEvent(id) {
	if (id) {
		tr_id = "#event-" + id;
		title = $(tr_id).find(".eventTitle").text();
		description = $(tr_id).find(".eventDescription").text();
		venue = $(tr_id).find(".eventVenue").text();
		mdate = $(tr_id).find(".eventDate").text();
		mtime = $(tr_id).find(".eventTime").text();
		$('#form-id').val(id);
		$('#form-title').val(title);
		$('#form-description').val(description);
		$('#form-venue').val(venue);
		$('#form-mdate').val(mdate);
		$('#form-mtime').val(mtime);
	}
}
function updateTomy_event(event){
	$("#my_event #event-" +event.id).children(".eventData").each(function (){
		var attr = $(this).attr("title");
		if (attr == "title") {
			$(this).text(event.title);
		}else if (attr == "description") {
			$(this).text(event.description);
		}else if (attr == "venue") {
			$(this).text(event.venue);
		}else if (attr == "mdate") {
			$(this).text(event.mdate);
		}else{
			$(this).text(event.mtime);
		}
	});
}

