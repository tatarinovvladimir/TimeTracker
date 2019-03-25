$("#mytasks_id").addClass("active");
$('title').html("Tt - " + mytitle);


 $('.commbut').hover(
    function() {
      $( this ).addClass('shadow-lg');
    }, function() {
      $( this ).removeClass('shadow-lg');
    }
  );


$('#showcomm').click(showhide)

var flag = 0;
function showhide(){

	if (flag == 1) {
	$('#showcomm').html('Hide comments')
	flag = 0;
	}
	else {$('#showcomm').html('Show comments')
		flag = 1;
		}
}
