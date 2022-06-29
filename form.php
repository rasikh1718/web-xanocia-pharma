<?php
$name= $_POST['Name'];
$visitor_email= $_POST['email'];
$product= $_POST['product'];
$message=$_POST['message'];

$email_from='info@xanocialifescience.com';
$email_product='New Form Submission';
$email_body="User Name: $name.\n".
          "User email: $email.\n".
          "User product: $product.\n".
          "User message: $message.\n";


$to ='abdulrasikh123@gmail.com';

$header="From: $email_from \r\n";
$header="Reply_to: $visitor_email \r\n";

mail($to,$email_product,$email_body,$header);
header("Loaction: contact.html");
?>