$(document).ready(function() {
  $("#link0").toggleClass("activelink");
  $("#link1").toggleClass("activelink");
  $("#link2").toggleClass("activelink");
  $("#program0").toggle();
  $("#program1").toggle();
  $("#program2").toggle();
  $(".link > a").click(function() {             
      $(this).toggleClass("activelink");          
      $(this.name).toggle();
  })
});

function goBack() {
  window.history.go(-2);
}