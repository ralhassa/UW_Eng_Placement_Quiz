$(document).ready(function() {
  $("#link0").toggleClass("activelink");
  $("#link1").toggleClass("activelink");
  $("#link2").toggleClass("activelink");
  $("#link3").toggleClass("activelink");
  $("#link4").toggleClass("activelink");
  $("#eye0").toggleClass("show");
  $("#eye1").toggleClass("show");
  $("#eye2").toggleClass("show");
  $("#eye3").toggleClass("show");
  $("#eye4").toggleClass("show");
  $("#program0").toggle();
  $("#program1").toggle();
  $("#program2").toggle();
  $("#program3").toggle();
  $("#program4").toggle();
  $(".link > a").click(function() {             
      $(this).toggleClass("activelink");          
      $(this.name).toggle();
      $("i", this).toggleClass("show hide");
      // $(".content").animate({ scrollTop: $(document).height() }, "slow");
  })
  $('#emailSubmit').bind('click', function(){
    $('#beforeSubmit').toggleClass("hide");
    $('#afterSubmit').toggleClass("show");
  });
});

function goBack() {
  window.history.go(-1);
}

