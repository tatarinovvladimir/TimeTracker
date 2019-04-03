 $('.myclassje').hover(
    function() {
      $( this ).addClass('shadow-lg');
    }, function() {
      $( this ).removeClass('shadow-lg');
    }
  );

$("#myprojects_id").addClass("active");


$('.addproject').hover(
    function() {
      $( this ).addClass('bg-dark');

      $('.addproject').removeClass('text-muted')
      $('.addproject').addClass('text-white')
      
    }, 
    function() {
      $( this ).removeClass('bg-dark');

      $('.addproject').addClass('text-muted')
      $('.addproject').removeClass('text-white')
    }
  );