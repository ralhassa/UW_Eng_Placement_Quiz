$(document).ready(function() {
  $("#link0").toggleClass("activelink");
  $("#link1").toggleClass("activelink");
  $("#link2").toggleClass("activelink");
  $("#eye0").toggleClass("show");
  $("#eye1").toggleClass("show");
  $("#eye2").toggleClass("show");
  $("#program0").toggle();
  $("#program1").toggle();
  $("#program2").toggle();
  $(".link > a").click(function() {             
      $(this).toggleClass("activelink");          
      $(this.name).toggle();
      $("i", this).toggleClass("show hide");
  })
});

function goBack() {
  window.history.go(-1);
}