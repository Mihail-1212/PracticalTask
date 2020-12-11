var datetimePicker;
const DATETIMEPICKER_FORMAT = "DD.MM.YYYY HH:mm:SS";          // format for datetime vanilla js
const DATETIMEPICKER_DEFAULT_FORMAT = "dd.mm.yyyy HH:MM:00";  // format for datetimepicker datetime
const DATEPICKER_DEFAULT_FORMAT = "dd.mm.yyyy";               // format for datetimepicker date

jQuery(document).ready(function(){
  datetimePicker = $('#datepicker-start').datetimepicker({
    uiLibrary: 'bootstrap4',
    modal: true,
    footer: true,
    format: DATETIMEPICKER_DEFAULT_FORMAT,
    change: function (e) {
        var currentValue = $('#datepicker-start').val()
        $('#datepicker-start').val(currentValue+':00');
     }
  });
});
