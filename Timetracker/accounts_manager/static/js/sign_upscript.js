				
if ( err ){

$("form > input").each(function(){
	if ($(this.value != '')) {
	$(this).addClass('border-success')
	}
})
	}
else {
	$('#birthday').val('2000-01-31')
}
				
			