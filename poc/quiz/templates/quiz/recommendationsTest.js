$(document).ready(function() {
    $("#link0").toggleClass("activelink");
    $("#link1").toggleClass("activelink");
    $("#program0").toggle();
    $("#program1").toggle();
    $(".link > a").click(function() {             // when clicking any of these links
        // $(".link > a").removeClass("activelink"); // remove highlight from all links
        $(this).toggleClass("activelink");          // add highlight to clicked link
        $(this.hash).toggle();
    })
    
});
