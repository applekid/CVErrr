$(document).ready(
	function() {
	$('#feed').load('cve.html');    
	setInterval(function() {
		$('#feed').load('cve.html');
		location.reload(true);
	}, 60000);
        
});






