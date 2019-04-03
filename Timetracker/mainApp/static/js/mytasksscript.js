$("#mytasks_id").addClass("active");
$('.addtask').hover(
    function() {
      $( this ).addClass('bg-dark');

      $('.add_project_text').removeClass('text-muted')
      $('.add_project_text').addClass('text-white')
      
    }, 
    function() {
      $( this ).removeClass('bg-dark');

      $('.add_project_text').addClass('text-muted')
      $('.add_project_text').removeClass('text-white')
    }
  );