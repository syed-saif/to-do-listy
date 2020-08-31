$(document).ready( function(){

$(document).on('change', '.cb', function() {
    console.log("function triggered irespctive of state");
    if(this.checked){
      var task_id =  $(this).parent().parent().attr('id');
      if($(this).hasClass('completed')){
        $('#action').val('completed')
      }
      else{
        $('#action').val('incompleted')
      }
      $('#tid').val(task_id)
      $('#change').submit();
    }
});

$(document).on('click', '#delete', function() {
      var task_id =  $(this).parent().parent().attr('id');
      $('#del_tid').val(task_id)
      $('#del_form').submit();

});


});
