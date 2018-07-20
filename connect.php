<?php
$servername = "183.111.206.184";
$username = "flumbe";
$password = "blumeprimes";
$dbname = "shorgoods";
// Create connection
$con = new mysqli($servername, $username, $password,$dbname);// Create connections
// Check connection
if ($con->connect_error) {
    die("Connection failed: " . $conn->connect_error . "::call admin");
}
?>