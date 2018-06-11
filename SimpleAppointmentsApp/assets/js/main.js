$(document).ready(function(){
    var today = new Date().toISOString().split('T')[0];
    getAppointments();

	$('#date').attr('min', today);

	$('#newBtn').click(function(){
		$('#addForm').removeClass('hidden');
		$(this).addClass('hidden');
	});
	$('#cancelBtn').click(function(){
		$('#newBtn').removeClass('hidden');
		$('#addForm').addClass('hidden');
	});
	$('#addBtn').click(function(){
		if ($('#date').val() < today){
			showError('Please pick correct date.');
			return false;
		} else if ($('#time').val() == ""){
            showError('Please enter time.');
            return false;
		} else if ($('#desc').val() == "") {
			showError('Please enter description.');
			return false;
		}
	});
	$('#searchBtn').click(function () {
		getAppointments($('#searchTxt').val());
    });
})
function showError (msg){
	$('.alert-danger').text(msg).removeClass('hidden');
			setTimeout(function(){
				$('.alert-danger').addClass('hidden')},
				3000
				);
}
function getAppointments(searchText) {
	if (!searchText)
		searchText = "";
    $.get({
        url: "http://localhost/AppointmentsApp/cgi-bin/fetchAppointments.cgi",
        data: {"searchText": searchText},
        contentType: "application/json",
        dataType: "json",
        success: function(data) {
            populateTable(data);
        },
        error: function(request, status, error) {
            console.log(error);
        }
    });
}
function populateTable(data) {
	var tr, th1, th2, th3, td1, td2, td3;

    tr = $('<tr>');
    td1 = $('<th>', {text : "DATE"});
    td2 = $('<th>', {text : "TIME"});
    td3 = $('<th>', {text : "DESCRIPTION"});
    $(tr).append(td1).append(td2).append(td3);
    $('#dataTable').html(tr);

    for (var entry in data){
        tr = $('<tr>');
        td1 = $('<td>', {text : data[entry][0]});
        td2 = $('<td>', {text : data[entry][1]});
        td3 = $('<td>', {text : data[entry][2]});
        $(tr).append(td1).append(td2).append(td3);
        $('#dataTable').append(tr);
    }
}