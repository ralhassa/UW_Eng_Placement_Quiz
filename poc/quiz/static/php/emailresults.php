<?php 
$useremail		= $_POST['email'];
$welcomecopy	= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">Thank you for taking the Waterloo Engineering Type Quiz. We hope you find your results helpful in discovering the program that best fits your needs and interests.';
// $programlist	= '<div style="border:1px solid #ccc;padding:10px;width:780px;"><p style="font-family:Verdana, Helvetica, Arial, sans-serif;font-size:16px;font-weight:bold;color:#57068C;margin-bottom:-5px;">' . $_POST['onetitle'] . '</p>';$onelink		= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">' . $_POST['onelink'] . '</p>';
$uwatlogo		= '<div style="width:800px;height:40px;position:relative;background-color:#000;"><img src="http://uwaterloo.ca/images/template/uw_wordmark.gif" /></div>';
$headers  = "MIME-Version: 1.0\r\n"; 
$headers .= "Content-type: text/html; charset=iso-8859-1\r\n";
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 1) Edit the first line below to match your email address////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
$headers .= "From: Engineering @ The University of Waterloo <> \n";
$headers .= "Reply-To: admissions@engmail.uwaterloo.ca \n\n";
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 2) Then edit the following two lines to match your site name and email address////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
$siteName		= "https://waterlooengineeringquiz.herokuapp.com";
$to 			= $useremail;
$toSubject 		= "Here are your results";
$emailBody 		= "$uwatlogo $welcomecopy";
$message 		= $emailBody;
// echo "Result have been emailed to $youremail";
mail($to, $toSubject, $message, $headers);?>
