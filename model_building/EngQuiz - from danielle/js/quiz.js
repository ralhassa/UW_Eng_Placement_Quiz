$(document).ready(function(){
	var answerHolder = [],
		tabindex = 1,
	// Question Weight
		q1weight = .20,
		q2weight = .15,
		q3weight = .12,
		q4weight = .10,
		q5weight = .10,
		q6weight = .08,
		q7weight = .07,
		q8weight = .07,
		q9weight = .06,
		q10weight = .05,
	// Disciplines
		chemical = 0,
		civil = 0,
		computer = 0,
		electrical = 0,
		environment = 0,
		geological = 0,
		management = 0,
		mechanical = 0,
		mechatronics = 0,
		nanotechnology = 0,
		software = 0,
		systemsdesign = 0;
	// dynamically gives elements proper tabindexes (buttons and answers)
	$('#quiz li.answer, a.next, a.start').each(function() {
        var $input = $(this);
        $input.attr("tabindex", tabindex);
        tabindex++;
	});
	// initially hides all questions but the intro
	$('#quiz div').not('#intro, .logo, .notice').each(function() {
		$(this).addClass('starthidden')
	})
	// start the quiz
	$('.start').keypress(function(e) {
	    $(this).closest('div').eq(0).fadeToggle(function(){
			$(this).closest('div').nextAll('div').eq(0).fadeToggle()
		})	
	}).on('click', function() {
		$(this).closest('div').eq(0).fadeToggle(function(){
			$(this).closest('div').nextAll('div').eq(0).fadeToggle()
		})
	})
	// click highlights your answer
	$('.answer').keypress(function(e) {
	    if(e.which == 13) {
	        // $(this).toggleClass('selected')
			$('.answer').not(this).removeClass('selected')
	    }
	}).on('click', function() {
		$(this).toggleClass('selected')
		$('.answer').not(this).removeClass('selected')
	});
	//
	// The business!
	//
	function business() {
		if ($('.selected').hasClass('q1a1')) {
			mechanical = mechanical + ((58 * .10) + 12) * q1weight;
			environment = environment + ((36 * .10) + 11) * q1weight;
			civil = civil + ((35 * .10) + 10) * q1weight;
			management = management + ((22 * .10) + 9) * q1weight;
			geological = geological + ((20 * .10) + 8) * q1weight;
			chemical = chemical + ((19 * .10) + 7) * q1weight;
			electrical = electrical + ((18 * .10) + 6) * q1weight;
			mechatronics = mechatronics + ((17 * .10) + 5) * q1weight;
			systemsdesign = systemsdesign + ((16 * .10) + 4) * q1weight;
			nanotechnology = nanotechnology + ((7 * .10) + 3) * q1weight;
			software = software + ((3 * .10) + 2) * q1weight;
			computer = computer + ((3 * .10) + 1) * q1weight;
		}
		if ($('.selected').hasClass('q1a2')) {
			electrical = electrical + ((34 * .10) + 12) * q1weight;
			computer = computer + ((23 * .10) + 11) * q1weight;
			management = management + ((22 * .10) + 10) * q1weight;
			nanotechnology = nanotechnology + ((20 * .10) + 9) * q1weight;
			systemsdesign = systemsdesign + ((18 * .10) + 8) * q1weight;
			chemical = chemical + ((17 * .10) + 7) * q1weight;
			mechatronics = mechatronics + ((10 * .10) + 6) * q1weight;
			civil = civil + ((10 * .10) + 5) * q1weight;
			environment = environment + ((9 * .10) + 4) * q1weight;
			software = software + ((8 * .10) + 3) * q1weight;
			mechanical = mechanical + ((5 * .10) + 2) * q1weight;
			geological = geological + ((0 * .10) + 1) * q1weight;
		}
		if ($('.selected').hasClass('q1a3')) {
			software = software + ((66 * .10) + 12) * q1weight;
			computer = computer + ((46 * .10) + 11) * q1weight;
			environment = environment + ((27 * .10) + 10) * q1weight;
			management = management + ((25 * .10) + 9) * q1weight;
			civil = civil + ((23 * .10) + 8) * q1weight;
			systemsdesign = systemsdesign + ((23 * .10) + 7) * q1weight;
			electrical = electrical + ((19 * .10) + 6) * q1weight;
			nanotechnology = nanotechnology + ((15 * .10) + 5) * q1weight;
			geological = geological + ((13 * .10) + 4) * q1weight;
			mechanical = mechanical + ((11 * .10) + 3) * q1weight;
			mechatronics = mechatronics + ((11 * .10) + 2) * q1weight;
			chemical = chemical + ((8 * .10) + 1) * q1weight;
		}
		if ($('.selected').hasClass('q1a4')) {
			geological = geological + ((54 * .10) + 12) * q1weight;
			chemical = chemical + ((47 * .10) + 11) * q1weight;
			nanotechnology = nanotechnology + ((41 * .10) + 10) * q1weight;
			civil = civil + ((15 * .10) + 9) * q1weight;
			environment = environment + ((14 * .10) + 8) * q1weight;
			systemsdesign = systemsdesign + ((11 * .10) + 7) * q1weight;
			mechatronics = mechatronics + ((3 * .10) + 6) * q1weight;
			management = management + ((3 * .10) + 5) * q1weight;
			mechanical = mechanical + ((3 * .10) + 4) * q1weight;
			electrical = electrical + ((2 * .10) + 3) * q1weight;
			computer = computer + ((2 * .10) + 2) * q1weight;
			software = software + ((1 * .10) + 1) * q1weight;
		}
		if ($('.selected').hasClass('q1a5')) {
			mechatronics = mechatronics + ((61 * .10) + 12) * q1weight;
			systemsdesign = systemsdesign + ((32 * .10) + 11) * q1weight;
			management = management + ((28 * .10) + 10) * q1weight;
			electrical = electrical + ((27 * .10) + 9) * q1weight;
			computer = computer + ((26 * .10) + 8) * q1weight;
			mechanical = mechanical + ((23 * .10) + 7) * q1weight;
			software = software + ((22 * .10) + 6) * q1weight;
			civil = civil + ((17 * .10) + 5) * q1weight;
			nanotechnology = nanotechnology + ((17 * .10) + 4) * q1weight;
			environment = environment + ((14 * .10) + 3) * q1weight;
			geological = geological + ((13 * .10) + 2) * q1weight;
			chemical = chemical + ((9 * .10) + 1) * q1weight;
		}
		if ($('.selected').hasClass('q2a1')) {
			management = management + ((72 * .10) + 12) * q2weight;
			nanotechnology = nanotechnology + ((68 * .10) + 11) * q2weight;
			chemical = chemical + ((59 * .10) + 10) * q2weight;
			systemsdesign = systemsdesign + ((58 * .10) + 9) * q2weight;
			software = software + ((56 * .10) + 8) * q2weight;
			mechatronics = mechatronics + ((40 * .10) + 7) * q2weight;
			computer = computer + ((30 * .10) + 6) * q2weight;
			civil = civil + ((27 * .10) + 5) * q2weight;
			electrical = electrical + ((26 * .10) + 4) * q2weight;
			environment = environment + ((25 * .10) + 3) * q2weight;
			geological = geological + ((18 * .10) + 2) * q2weight;
			mechanical = mechanical + ((17 * .10) + 1) * q2weight;
		}
		if ($('.selected').hasClass('q2a2')) {
			computer = computer + ((30 * .10) + 12) * q2weight;
			software = software + ((21 * .10) + 11) * q2weight;
			management = management + ((20 * .10) + 10) * q2weight;
			geological = geological + ((18 * .10) + 9) * q2weight;
			nanotechnology = nanotechnology + ((12 * .10) + 8) * q2weight;
			electrical = electrical + ((11 * .10) + 7) * q2weight;
			mechatronics = mechatronics + ((9 * .10) + 6) * q2weight;
			chemical = chemical + ((9 * .10) + 5) * q2weight;
			civil = civil + ((9 * .10) + 4) * q2weight;
			environment = environment + ((8 * .10) + 3) * q2weight;
			mechanical = mechanical + ((8 * .10) + 2) * q2weight;
			systemsdesign = systemsdesign + ((6 * .10) + 1) * q2weight;
		}
		if ($('.selected').hasClass('q2a3')) {
			mechanical = mechanical + ((75 * .10) + 12) * q2weight;
			environment = environment + ((67 * .10) + 11) * q2weight;
			electrical = electrical + ((64 * .10) + 10) * q2weight;
			civil = civil + ((64 * .10) + 9) * q2weight;
			geological = geological + ((64 * .10) + 8) * q2weight;
			mechatronics = mechatronics + ((51 * .10) + 7) * q2weight;
			computer = computer + ((41 * .10) + 6) * q2weight;
			systemsdesign = systemsdesign + ((35 * .10) + 5) * q2weight;
			chemical = chemical + ((32 * .10) + 4) * q2weight;
			software = software + ((23 * .10) + 3) * q2weight;	
			nanotechnology = nanotechnology + ((21 * .10) + 2) * q2weight;
			management = management + ((8 * .10) + 1) * q2weight;
		}
		if ($('.selected').hasClass('q3a1')) {
			mechanical = mechanical + ((62 * .10) + 12) * q3weight;
			mechatronics = mechatronics + ((49 * .10) + 11) * q3weight;
			civil = civil + ((48 * .10) + 10) * q3weight;
			systemsdesign = systemsdesign + ((45 * .10) + 9) * q3weight;
			environment = environment + ((42 * .10) + 8) * q3weight;
			electrical = electrical + ((40 * .10) + 7) * q3weight;
			geological = geological + ((36 * .10) + 6) * q3weight;
			software = software + ((27 * .10) + 5) * q3weight;
			computer = computer + ((24 * .10) + 4) * q3weight;
			chemical = chemical + ((18 * .10) + 3) * q3weight;
			nanotechnology = nanotechnology + ((18 * .10) + 2) * q3weight;
			management = management + ((16 * .10) + 1) * q3weight;
		}
		if ($('.selected').hasClass('q3a2')) {
			management = management + ((48 * .10) + 12) * q3weight;
			chemical = chemical + ((48 * .10) + 11) * q3weight;
			environment = environment + ((33 * .10) + 10) * q3weight;
			nanotechnology = nanotechnology + ((32 * .10) + 9) * q3weight;
			civil = civil + ((30 * .10) + 8) * q3weight;
			mechatronics = mechatronics + ((28 * .10) + 7) * q3weight;
			electrical = electrical + ((28 * .10) + 6) * q3weight;
			software = software + ((27 * .10) + 5) * q3weight;
			geological = geological + ((27 * .10) + 4) * q3weight;
			computer = computer + ((27 * .10) + 3) * q3weight;
			systemsdesign = systemsdesign + ((26 * .10) + 2) * q3weight;
			mechanical = mechanical + ((17 * .10) + 1) * q3weight;
		}
		if ($('.selected').hasClass('q3a3')) {
			nanotechnology = nanotechnology + ((50 * .10) + 12) * q3weight;
			computer = computer + ((49 * .10) + 11) * q3weight;
			software = software + ((46 * .10) + 10) * q3weight;
			geological = geological + ((36 * .10) + 9) * q3weight;
			management = management + ((36 * .10) + 8) * q3weight;
			chemical = chemical + ((34 * .10) + 7) * q3weight;
			electrical = electrical + ((32 * .10) + 6) * q3weight;
			systemsdesign = systemsdesign + ((29 * .10) + 5) * q3weight;
			environment = environment + ((25 * .10) + 4) * q3weight;
			mechatronics = mechatronics + ((23 * .10) + 3) * q3weight;
			civil = civil + ((21 * .10) + 2) * q3weight;
			mechanical = mechanical + ((21 * .10) + 1) * q3weight;
		}
		if ($('.selected').hasClass('q4a1')) {
			mechatronics = mechatronics + ((44 * .10) + 12) * q4weight;
			computer = computer + ((38 * .10) + 11) * q4weight;
			management = management + ((36 * .10) + 10) * q4weight;
			systemsdesign = systemsdesign + ((32 * .10) + 9) * q4weight;
			mechanical = mechanical + ((32 * .10) + 8) * q4weight;
			software = software + ((28 * .10) + 7) * q4weight;
			civil = civil + ((27 * .10) + 6) * q4weight;
			electrical = electrical + ((26 * .10) + 5) * q4weight;
			environment = environment + ((25 * .10) + 4) * q4weight;
			nanotechnology = nanotechnology + ((21 * .10) + 3) * q4weight;
			geological = geological + ((18 * .10) + 2) * q4weight;
			chemical = chemical + ((11 * .10) + 1) * q4weight;
		}
		if ($('.selected').hasClass('q4a2')) {
			environment = environment + ((42 * .10) + 12) * q4weight;
			chemical = chemical + ((39 * .10) + 11) * q4weight;
			mechatronics = mechatronics + ((26 * .10) + 10) * q4weight;
			management = management + ((24 * .10) + 9) * q4weight;
			electrical = electrical + ((21 * .10) + 8) * q4weight;
			nanotechnology = nanotechnology + ((21 * .10) + 7) * q4weight;
			civil = civil + ((18 * .10) + 6) * q4weight;
			geological = geological + ((18 * .10) + 5) * q4weight;
			mechanical = mechanical + ((15 * .10) + 4) * q4weight;
			software = software + ((15 * .10) + 3) * q4weight;
			computer = computer + ((14 * .10) + 2) * q4weight;
			systemsdesign = systemsdesign + ((13 * .10) + 1) * q4weight;
		}
		if ($('.selected').hasClass('q4a3')) {
			computer = computer + ((22 * .10) + 12) * q4weight;
			electrical = electrical + ((19 * .10) + 11) * q4weight;
			nanotechnology = nanotechnology + ((15 * .10) + 10) * q4weight;
			mechanical = mechanical + ((11 * .10) + 9) * q4weight;
			software = software + ((11 * .10) + 8) * q4weight;
			systemsdesign = systemsdesign + ((10 * .10) + 7) * q4weight;
			civil = civil + ((9 * .10) + 6) * q4weight;
			management = management + ((8 * .10) + 5) * q4weight;
			chemical = chemical + ((7 * .10) + 4) * q4weight;
			environment = environment + ((0 * .10) + 3) * q4weight;
			geological = geological + ((0 * .10) + 2) * q4weight;
			mechatronics = mechatronics + ((0 * .10) + 1) * q4weight;
		}
		if ($('.selected').hasClass('q4a4')) {
			geological = geological + ((64 * .10) + 12) * q4weight;
			software = software + ((46 * .10) + 11) * q4weight;
			civil = civil + ((45 * .10) + 10) * q4weight;
			systemsdesign = systemsdesign + ((45 * .10) + 9) * q4weight;
			nanotechnology = nanotechnology + ((44 * .10) + 8) * q4weight;
			chemical = chemical + ((43 * .10) + 7) * q4weight;
			mechanical = mechanical + ((42 * .10) + 6) * q4weight;
			electrical = electrical + ((34 * .10) + 5) * q4weight;
			environment = environment + ((33 * .10) + 4) * q4weight;
			management = management + ((32 * .10) + 3) * q4weight;
			mechatronics = mechatronics + ((30 * .10) + 2) * q4weight;
			computer = computer + ((27 * .10) + 1) * q4weight;
		}
		if ($('.selected').hasClass('q5a1')) {
			computer = computer + ((46 * .10) + 12) * q5weight;
			electrical = electrical + ((40 * .10) + 11) * q5weight;
			software = software + ((36 * .10) + 10) * q5weight;
			civil = civil + ((33 * .10) + 9) * q5weight;
			nanotechnology = nanotechnology + ((32 * .10) + 8) * q5weight;
			mechatronics = mechatronics + ((23 * .10) + 7) * q5weight;
			chemical = chemical + ((20 * .10) + 6) * q5weight;
			environment = environment + ((17 * .10) + 5) * q5weight;
			mechanical = mechanical + ((15 * .10) + 4) * q5weight;
			management = management + ((12 * .10) + 3) * q5weight;
			systemsdesign = systemsdesign + ((10 * .10) + 2) * q5weight;
			geological = geological + ((9 * .10) + 1) * q5weight;
		}
		if ($('.selected').hasClass('q5a2')) {
			geological = geological + ((91 * .10) + 12) * q5weight;
			systemsdesign = systemsdesign + ((90 * .10) + 11) * q5weight;
			management = management + ((88 * .10) + 10) * q5weight;
			mechanical = mechanical + ((85 * .10) + 9) * q5weight;
			environment = environment + ((83 * .10) + 8) * q5weight;
			chemical = chemical + ((80 * .10) + 7) * q5weight;
			mechatronics = mechatronics + ((77 * .10) + 6) * q5weight;
			nanotechnology = nanotechnology + ((68 * .10) + 5) * q5weight;
			civil = civil + ((67 * .10) + 4) * q5weight;
			software = software + ((64 * .10) + 3) * q5weight;
			electrical = electrical + ((60 * .10) + 2) * q5weight;
			computer = computer + ((54 * .10) + 1) * q5weight;
		}
		if ($('.selected').hasClass('q6a1')) {
			civil = civil + ((18 * .10) + 12) * q6weight;
			environment = environment + ((8 * .10) + 11) * q6weight;
			electrical = electrical + ((4 * .10) + 10) * q6weight;
			management = management + ((4 * .10) + 9) * q6weight;
			mechanical = mechanical + ((4 * .10) + 8) * q6weight;
			systemsdesign = systemsdesign + ((3 * .10) + 7) * q6weight;
			computer = computer + ((3 * .10) + 6) * q6weight;
			mechatronics = mechatronics + ((2 * .10) + 5) * q6weight;
			chemical = chemical + ((2 * .10) + 4) * q6weight;
			geological = geological + ((0 * .10) + 3) * q6weight;
			nanotechnology = nanotechnology + ((0 * .10) + 2) * q6weight;
			software = software + ((0 * .10) + 1) * q6weight;
		}
		if ($('.selected').hasClass('q6a2')) {
			nanotechnology = nanotechnology + ((44 * .10) + 12) * q6weight;
			mechatronics = mechatronics + ((21 * .10) + 11) * q6weight;
			electrical = electrical + ((19 * .10) + 10) * q6weight;
			mechanical = mechanical + ((17 * .10) + 9) * q6weight;
			computer = computer + ((16 * .10) + 8) * q6weight;
			chemical = chemical + ((16 * .10) + 7) * q6weight;
			systemsdesign = systemsdesign + ((13 * .10) + 6) * q6weight;
			civil = civil + ((6 * .10) + 5) * q6weight;
			software = software + ((1 * .10) + 4) * q6weight;
			environment = environment + ((0 * .10) + 3) * q6weight;
			geological = geological + ((0 * .10) + 2) * q6weight;
			management = management + ((0 * .10) + 1) * q6weight;
		}
		if ($('.selected').hasClass('q6a3')) {
			chemical = chemical + ((30 * .10) + 12) * q6weight;
			management = management + ((24 * .10) + 11) * q6weight;
			mechatronics = mechatronics + ((19 * .10) + 10) * q6weight;
			mechanical = mechanical + ((17 * .10) + 9) * q6weight;
			nanotechnology = nanotechnology + ((6 * .10) + 8) * q6weight;
			computer = computer + ((5 * .10) + 7) * q6weight;
			electrical = electrical + ((4 * .10) + 6) * q6weight;
			systemsdesign = systemsdesign + ((3 * .10) + 5) * q6weight;
			software = software + ((2 * .10) + 4) * q6weight;
			civil = civil + ((0 * .10) + 3) * q6weight;
			environment = environment + ((0 * .10) + 2) * q6weight;
			geological = geological + ((0 * .10) + 1) * q6weight;
		}
		if ($('.selected').hasClass('q6a4')) {
			software = software + ((76 * .10) + 12) * q6weight;
			electrical = electrical + ((55 * .10) + 11) * q6weight;
			computer = computer + ((54 * .10) + 10) * q6weight;
			management = management + ((48 * .10) + 9) * q6weight;
			civil = civil + ((45 * .10) + 8) * q6weight;
			systemsdesign = systemsdesign + ((42 * .10) + 7) * q6weight;
			mechatronics = mechatronics + ((42 * .10) + 6) * q6weight;
			mechanical = mechanical + ((30 * .10) + 5) * q6weight;
			chemical = chemical + ((30 * .10) + 4) * q6weight;
			nanotechnology = nanotechnology + ((29 * .10) + 3) * q6weight;
			geological = geological + ((18 * .10) + 2) * q6weight;
			environment = environment + ((8 * .10) + 1) * q6weight;
		}
		if ($('.selected').hasClass('q6q5')) {
			environment = environment + ((83 * .10) + 12) * q6weight;
			geological = geological + ((82 * .10) + 11) * q6weight;
			systemsdesign = systemsdesign + ((39 * .10) + 10) * q6weight;
			mechanical = mechanical + ((32 * .10) + 9) * q6weight;
			civil = civil + ((30 * .10) + 8) * q6weight;
			management = management + ((24 * .10) + 7) * q6weight;
			chemical = chemical + ((23 * .10) + 6) * q6weight;
			computer = computer + ((22 * .10) + 5) * q6weight;
			nanotechnology = nanotechnology + ((21 * .10) + 4) * q6weight;
			software = software + ((21 * .10) + 3) * q6weight;
			electrical = electrical + ((17 * .10) + 2) * q6weight;
			mechatronics = mechatronics + ((16 * .10) + 1) * q6weight;
		}
		if ($('.selected').hasClass('q7a1')) {
			systemsdesign = systemsdesign + ((94 * .10) + 12) * q7weight;
			management = management + ((88 * .10) + 11) * q7weight;
			mechatronics = mechatronics + ((74 * .10) + 10) * q7weight;
			nanotechnology = nanotechnology + ((68 * .10) + 9) * q7weight;
			mechanical = mechanical + ((64 * .10) + 8) * q7weight;
			geological = geological + ((64 * .10) + 7) * q7weight;
			electrical = electrical + ((62 * .10) + 6) * q7weight;
			computer = computer + ((59 * .10) + 5) * q7weight;
			chemical = chemical + ((59 * .10) + 4) * q7weight;
			environment = environment + ((58 * .10) + 3) * q7weight;
			software = software + ((52 * .10) + 2) * q7weight;
			civil = civil + ((48 * .10) + 1) * q7weight;
		}
		if ($('.selected').hasClass('q7a2')) {
			civil = civil + ((52 * .10) + 12) * q7weight;
			software = software + ((48 * .10) + 11) * q7weight;
			environment = environment + ((42 * .10) + 10) * q7weight;
			chemical = chemical + ((41 * .10) + 9) * q7weight;
			computer = computer + ((41 * .10) + 8) * q7weight;
			electrical = electrical + ((38 * .10) + 7) * q7weight;
			geological = geological + ((36 * .10) + 6) * q7weight;
			mechanical = mechanical + ((36 * .10) + 5) * q7weight;
			nanotechnology = nanotechnology + ((32 * .10) + 4) * q7weight;
			mechatronics = mechatronics + ((26 * .10) + 3) * q7weight;
			management = management + ((12 * .10) + 2) * q7weight;
			systemsdesign = systemsdesign + ((6 * .10) + 1) * q7weight;
		}
		if ($('.selected').hasClass('q8a1')) {
			nanotechnology = nanotechnology + ((85 * .10) + 12) * q8weight;
			chemical = chemical + ((75 * .10) + 11) * q8weight;
			environment = environment + ((75 * .10) + 10) * q8weight;
			civil = civil + ((64 * .10) + 9) * q8weight;
			geological = geological + ((64 * .10) + 8) * q8weight;
			mechanical = mechanical + ((62 * .10) + 7) * q8weight;
			management = management + ((60 * .10) + 6) * q8weight;
			mechatronics = mechatronics + ((51 * .10) + 5) * q8weight;
			electrical = electrical + ((47 * .10) + 4) * q8weight;
			computer = computer + ((46 * .10) + 3) * q8weight;
			systemsdesign = systemsdesign + ((32 * .10) + 2) * q8weight;
			software = software + ((52 * .10) + 1) * q8weight;
		}
		if ($('.selected').hasClass('q8a2')) {
			systemsdesign = systemsdesign + ((68 * .10) + 12) * q8weight;
			computer = computer + ((54 * .10) + 11) * q8weight;
			electrical = electrical + ((53 * .10) + 10) * q8weight;
			mechatronics = mechatronics + ((49 * .10) + 9) * q8weight;
			management = management + ((40 * .10) + 8) * q8weight;
			mechanical = mechanical + ((38 * .10) + 7) * q8weight;
			civil = civil + ((36 * .10) + 6) * q8weight;
			geological = geological + ((36 * .10) + 5) * q8weight;
			chemical = chemical + ((25 * .10) + 4) * q8weight;
			environment = environment + ((25 * .10) + 3) * q8weight;
			nanotechnology = nanotechnology + ((15 * .10) + 2) * q8weight;
			software = software + ((48 * .10) + 1) * q8weight;
		}
		if ($('.selected').hasClass('q9a1')) {
			environment = environment + ((42 * .10) + 12) * q9weight;
			management = management + ((36 * .10) + 11) * q9weight;
			computer = computer + ((32 * .10) + 10) * q9weight;
			civil = civil + ((27 * .10) + 9) * q9weight;
			mechanical = mechanical + ((25 * .10) + 8) * q9weight;
			electrical = electrical + ((21 * .10) + 7) * q9weight;
			chemical = chemical + ((20 * .10) + 6) * q9weight;
			systemsdesign = systemsdesign + ((19 * .10) + 5) * q9weight;
			nanotechnology = nanotechnology + ((15 * .10) + 4) * q9weight;
			mechatronics = mechatronics + ((5 * .10) + 3) * q9weight;
			geological = geological + ((0 * .10) + 2) * q9weight;
			software = software + ((17 * .10) + 1) * q9weight;
		}
		if ($('.selected').hasClass('q9a2')) {
			mechatronics = mechatronics + ((63 * .10) + 12) * q9weight;
			systemsdesign = systemsdesign + ((61 * .10) + 11) * q9weight;
			nanotechnology = nanotechnology + ((56 * .10) + 10) * q9weight;
			electrical = electrical + ((53 * .10) + 9) * q9weight;
			mechanical = mechanical + ((53 * .10) + 8) * q9weight;
			chemical = chemical + ((50 * .10) + 7) * q9weight;
			geological = geological + ((45 * .10) + 6) * q9weight;
			civil = civil + ((42 * .10) + 5) * q9weight;
			computer = computer + ((41 * .10) + 4) * q9weight;
			environment = environment + ((33 * .10) + 3) * q9weight;
			management = management + ((32 * .10) + 2) * q9weight;
			software = software + ((51 * .10) + 1) * q9weight;
		}
		if ($('.selected').hasClass('q9a3')) {
			geological = geological + ((55 * .10) + 12) * q9weight;
			mechatronics = mechatronics + ((33 * .10) + 11) * q9weight;
			management = management + ((32 * .10) + 10) * q9weight;
			civil = civil + ((30 * .10) + 9) * q9weight;
			chemical = chemical + ((30 * .10) + 8) * q9weight;
			nanotechnology = nanotechnology + ((29 * .10) + 7) * q9weight;
			computer = computer + ((27 * .10) + 6) * q9weight;
			electrical = electrical + ((26 * .10) + 5) * q9weight;
			environment = environment + ((25 * .10) + 4) * q9weight;
			mechanical = mechanical + ((23 * .10) + 3) * q9weight;
			systemsdesign = systemsdesign + ((19 * .10) + 2) * q9weight;
			software = software + ((31 * .10) + 1) * q9weight;
		}
		if ($('.selected').hasClass('q10a1')) {
			electrical = electrical + ((77 * .10) + 12) * q10weight;
			mechanical = mechanical + ((74 * .10) + 11) * q10weight;
			mechatronics = mechatronics + ((65 * .10) + 10) * q10weight;
			computer = computer + ((65 * .10) + 9) * q10weight;
			management = management + ((64 * .10) + 8) * q10weight;
			systemsdesign = systemsdesign + ((58 * .10) + 7) * q10weight;
			civil = civil + ((55 * .10) + 6) * q10weight;
			geological = geological + ((55 * .10) + 5) * q10weight;
			nanotechnology = nanotechnology + ((53 * .10) + 4) * q10weight;
			environment = environment + ((50 * .10) + 3) * q10weight;
			chemical = chemical + ((48 * .10) + 2) * q10weight;
			software = software + ((67 * .10) + 1) * q10weight;
		}
		if ($('.selected').hasClass('q10a2')) {
			chemical = chemical + ((52 * .10) + 12) * q10weight;
			environment = environment + ((50 * .10) + 11) * q10weight;
			nanotechnology = nanotechnology + ((47 * .10) + 10) * q10weight;
			mechanical = mechanical  + ((45 * .10) + 9) * q10weight;
			geological = geological + ((45 * .10) + 8) * q10weight;
			systemsdesign = systemsdesign + ((42 * .10) + 7) * q10weight;
			management = management + ((36 * .10) + 6) * q10weight;
			computer = computer + ((35 * .10) + 5) * q10weight;
			mechatronics = mechatronics + ((35 * .10) + 4) * q10weight;
			mechanical = mechanical + ((26 * .10) + 3) * q10weight;
			electrical = electrical + ((23 * .10) + 2) * q10weight;
			software = software + ((33 * .10) + 1) * q10weight;
		}
		//
		// If nothing is seleted, show an error.
		//
		if ($('.selected').length == 0) {
			$('.message').text('Please select an answer').fadeIn(function() {
				$('.message').delay(1000).fadeOut()
			})
		} else {
			$(this).closest('div').eq(0).fadeToggle(function(){
				$(this).closest('div').nextAll('div').eq(0).fadeToggle()
				$('.answer').removeClass('selected')
			})
		}
		//
		// Final outcome
		//
		answerHolder = [
			{name:'Chemical',value:chemical,description:'<h1>Chemical</h1><p class=\"small\">Be a transformation expert</p><p>Chemical engineers are in charge of all aspects involved from the manipulation of raw materials into every product that we use, wear, live in and around, and rely on every day. Making products and processes safe, cost-effective and energy efficient are all elements of being a Chemical Engineer.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/chemical-engineering"},
			{name:'Civil',value:civil,description:'<h1>Civil</h1><p class=\"small\">Influence the infrastructure the world relies on</p><p>Civil engineers design, consult and advise on, and oversee the major infrastructure that all societies need to function, stay safe, thrive - and usually take for granted! Things like water supply networks, bridges and roadways, even airports.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/civil-engineering"},
			{name:'Computer',value:computer,description:'<h1>Computer</h1><p class=\"small\">Get the big tech picture for the 21st century.</p><p>Computer engineers are on the cutting edge of design, application and integration of software and hardware components to create the newest and most helpful technology. Anywhere and anything that focuses on information processing, transfer or storage involves a Computer Engineer.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/computer-engineering"},
			{name:'Electrical',value:electrical,description:'<h1>Electrical</h1><p class=\"small\">Think information, power and energy</p><p>Electrical engineers are experts in the fundamentals of electricity allowing them to harness its potential to improve the way we function, interact, and develop in society around the world. Creating faster, innovative, more reliable, and safer technologies - from giant power generators to Bluetooth devices - is what Electrical Engineering is all about.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/electrical-engineering"},
			{name:'Environment',value:environment,description:'<h1>Environment</h1><p class=\"small\">Think global impact.</p><p>Environmental engineers are experts in the management, protection, and rehabilitation of our natural environment. This highly consultative field of engineering is in demand in all areas of industry and government. Whether it\'s protecting an endangered species\' habitat or preventing leaching of toxins into drinking water, environmental engineers are involved.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/environmental-engineering"},
			{name:'Geological',value:geological,description:'<h1>Geological</h1><p class=\"small\">Manage high-risks by understanding how the Earth works.</p><p>Geological engineers know just how successful any infrastructural project will be by their deep understanding of the Earth\'s surface and sub-surface properties. Choosing the right location to build the next skyscraper or drill for oil without disastrous results comes down to geological engineers.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/geological-engineering"},
			{name:'Management',value:management,description:'<h1>Management</h1><p class=\"small\">Influence optimization in any industry.</p><p>Management engineers use the combination of analytical problem solving, savvy software skills and management experience to increase efficiencies and decrease losses in industry. Any CEO who wants to optimize their business will look to a management engineer who "gets" both the technical and business sides of their company.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/management-engineering"},
			{name:'Mechanical',value:mechanical,description:'<h1>Mechanical</h1><p class=\"small\">Design and invent things that move.</p><p>Mechanical engineers work from the ground up to develop and lead projects that involve anything that moves - from wind turbines to medical implants. Choosing the right material for any product and function saves time, money, and resources, and there\'s no one savvier in this than mechanical engineers.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/mechanical-engineering"},
			{name:'Mechatronics',value:mechatronics,description:'<h1>Mechatronics</h1><p class=\"small\">Integrate mechanical design with electronics, computers and software.</p>Mechatronics engineers are ready to take on the challenges of the modern world where every process, device, and vehicle is expected to be "smart" and multi-functional. Think laparoscopic tools that can mimic a surgeons\' movements at a miniaturized level or automated vehicles that can "learn" preferred routes.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/mechatronics-engineering"},
			{name:'Nanotechnology',value:nanotechnology,description:'<h1>Nanotechnology</h1><p class=\"small\">Focus on a billionth of a metre.</p><p>Nanotechnology engineers are focused on the potential of advanced materials - at the atomic level. Combining theoretical research with quantum mechanics, they\'re creating new materials that will make airplanes lighter, cosmetics more personalized, and life-saving devices as small as a blood cell.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/nanotechnology-engineering"},
			{name:'Software',value:software,description:'<h1>Software</h1><p class=\"small\">Influence human-computer interaction.</p><p>Software engineers really understand how to develop and test software so that it meets the needs of its users. Combining the applied approach of computer engineering with computer programming, software engineers are always in demand to create the next best program with the user in mind.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/software-engineering"},
			{name:'Systemsdesign',value:systemsdesign,description:'<h1>Systemsdesign</h1><p class=\"small\">Be a big-picture problem solver.</p><p>Systems Design engineers understand that all things are integrated, and so use a systems-based approach to problem solving partnered with a keen sense of design to lead well-functioning teams across a variety of disciplines. These engineers understand how a pacemaker effects a human\'s biological system over time or the impact of replacing traffic lights with roundabouts in transportation systems.</p>',link:"http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options/systems-design-engineering"}
		]
		// sort by score in descending order
		function SortByValue(a,b) { 
			return a.value - b.value
		}
		answerHolder.sort(SortByValue).reverse()
		// write the outcome html
		$('.outcome').html('<a href="mailto:?subject=Check%20out%20this%20awesome%20quiz&body=Check out this great engineering survey from the University of Waterloo!%0A%0Ahttp://engineering.uwaterloo.ca/survey%0A%0AIt\'s a great starting point for deciding what discipline you might want to apply for!" class="more">E-mail quiz to a friend</a><a href="http://www.studiographic.ca/quiz" class="more">Take the quiz again</a><h1>You\'re done!</h1><p>Your responses tell us that you might want to consider these engineering careers:</p><div style="clear:both;"></div><div class="choice"><p>' + answerHolder[0].description + '</p><a href="' + answerHolder[0].link +'" class="more" target="blank">Find out more</a></div><div class="choice"><p>' + answerHolder[1].description + '</p><a href="' + answerHolder[1].link +'" class="more" target="blank">Find out more</a></div><div class="choice"><p>' + answerHolder[2].description + '</p><a href="' + answerHolder[2].link +'" class="more" target="blank">Find out more</a></div><div style="clear:both;"></div><p>Not sure if you\'ve found your fit? <a href="http://uwaterloo.ca/engineering/future-undergraduate-students/undergraduate-programs-options" target="blank">Click here</a> to learn more about other engineering careers.</p><h1 class="notice">Important Notice:</h1><p>This quiz has been developed based on research conducted of current Waterloo Engineering students. It is intended to be a fun and interactive starting point to your exploration of the program(s) that is/are right for you and not a conclusive decision-making tool.</p>')
	};
	//
	// Do the business on next button ENTER or CLICK
	//
	$('.next').keypress(function(e) {
	    if(e.which == 13) { //ENTER is pressed
	        $(this).trigger('click', business)
	    }
	}).on('click', business)
	$('#quiz').removeClass('starthidden')
)};