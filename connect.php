<?php
$servername = "183.111.206.184";
$username = "root";
$password = "sex";
$dbname = "shorgoods";
// Create connection
$con = new mysqli($servername, $username, $password,$dbname);// Create connection
$con = new mysqli($servername, $username, $password,$dbname);
// Check connection
if ($con->connect_error) {
    die("Connection failed: " . $conn->connect_error . "::call admin");
}
?>