$(document).ready(function() {
  // getting the information from the backend
 
  $.getJSON("generated.json", function(data){
    console.log(data);
    var name;
    var programNumber = 1;
    $.each(data.programs, function(key,program){
        name = '<h3>'+ program.name + '</h3>';
        $('#name_'+ programNumber).html(name);

        minorName1 = '<h4>'+program.name +' Compared To...</h4>'
        $('#minorName1_'+ programNumber).html(minorName1);

        minorName2 = '<h4> What Other Programs Have To Say About '+program.name +' ...</h4>'
        $('#minorName2_'+ programNumber).html(minorName2);

        about = '<p>'+ program.about + '</p>';
        $('#about_'+ programNumber).html(about);

        courses = '<p>'+ program.courses + '</p>';
        $('#courses_'+ programNumber).html(courses);

        careers = '<p>'+ program.careers + '</p>';
        $('#careers_'+ programNumber).html(careers);

        comparison1 = '<p>'+ program.comparisonByTheProgram + '</p>';
        $('#comparison1_'+ programNumber).html(comparison1);

        comparison2 = '<p>'+ program.comparisonByOtherPrograms + '</p>';
        $('#comparison2_'+ programNumber).html(comparison2);
        programNumber++;
    });
});


    $("#see").click(function() {
      var elem = $("#see").text();
      if (elem == "See More") {
        //Stuff to do when btn is in the see more state
        $("#see").text("See Less");
        $("#hiddenRecommendations").slideDown();
      } else {
        //Stuff to do when btn is in the read less state
        $("#see").text("See More");
        $("#hiddenRecommendations").slideUp();
      }
    });
  });
