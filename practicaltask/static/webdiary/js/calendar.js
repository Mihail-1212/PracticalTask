(function () {
    'use strict';

    var dict_status_icon = {
      'Done': 'fa-check',
      'Not_done': 'fa-clock-o',
    }
    var dict_status_text = {
      'Done': 'Выполнено',
      'Not_done': 'Не выполнено',
    }

    // ------------------------------------------------------- //
    // Calendar
    // ------------------------------------------------------ //

	jQuery(function() {
		// page is ready
		  jQuery('#calendar').fullCalendar({
			themeSystem: 'bootstrap4',
      timeZone: 'Asia/Yekaterinburg', // TIme zone
      locale: 'ru',
      // emphasizes business hours
			businessHours: false,
			defaultView: 'month',
			// event dragging & resizing
			editable: true,
			// header
			header: {
				left: 'title',
				center: 'month,agendaWeek,agendaDay',
				right: 'today prev,next'
			},
      editable : false,

			eventAfterRender: function(event, element) {
        element.find(".fc-event-title").remove();
        element.find(".fc-event-time").remove();
        var status;
        var title;
        if(event.status == 'Done'){
          status = '<span class="fa fa-1x float-right '+dict_status_icon[event.status]+' fc-event-status" title="'+dict_status_text[event.status]+'"></span>';
          title = "Выполнено";
        }else {
          status = '<span class="fa fa-1x float-right '+dict_status_icon[event.status]+' fc-event-status" title="'+dict_status_text[event.status]+'"></span>';
          title = "Не выполнено";
        }
        element.append(status);
        element.prop('title', title);
	    },
			dayClick: function(date, jsEvent, view) {
          datetimePicker.value(date.format(DATETIMEPICKER_FORMAT));
			    jQuery('#modal-view-event-add').modal();
			},
			eventClick: function(event, jsEvent, view) {
        $('.event-title').html(event.title);
        $('.event-datetime').html('Дата задачи: '+event.start.format(DATETIMEPICKER_FORMAT));
        $('.event-body').html(event.description?event.description:"Описания нет.");
        $('.event-icon').find('span').attr('class','fa fa-2x '+dict_status_icon[event.status]).attr('title', dict_status_text[event.status]);
        $('.edit-button').attr('href', url_edit.replace('0', event.id));
        //edit-button
        //  event-datetime
        $('#modal-view-event').modal();
			},

      eventSources: [
        {
            url: 'tasks/',
            type: 'get', // This is the default though, you don't actually need to always mention it
            success: function(data) {
              var new_data = ((data) => {
                let new_array = [];
                $(data['tasks']).each(function( index, elem ){
                  //  elem = elem['tasks'][0];
                  new_array.push({
                    'id': elem.id,
                    'title': elem.name,
                    'description': elem.text,
                    'start': elem.date_start,
                    'status': elem.status,
                    'allDay' : false
                  });
                  // '<span class="badge badge-pill badge-primary">'
                });
                return new_array;
              })(data);
              return new_data;
            },
            failure: function(data) {
                console.log(data.statusText);
                throw new Exception('Fail request!');
            },
            error: function(data){
              console.log(data.statusText);
              throw new Exception('Error request!');
            }
        }
      ]
		});

	});
})(jQuery);
