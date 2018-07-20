<?php
 include "./connect.php";

 $id=$_POST['id'];
 $password=md5($_POST['pwd']);
 $password2=$_POST['pwd2'];
 $sql = "insert into account_info (id, pwd) values ('$id','$password')";
echo $sql;
 if($con->query($sql)){
  echo 'success inserting';
 }else{
  echo 'fail to insert sql';
 }
?>