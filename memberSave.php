<?php
 include "./connect.php";

 $id=$_POST['id'];
 $password=md5($_POST['pwd']);
 $password2=$_POST['pwd2'];
 $name=$_POST['name'];
 $address=$_POST['addr'];
 $sex=$_POST['sex'];
 $birthDay=$_POST['birthDay'];
 $email=$_POST['email'];
 $sql = "insert into account_info (id, pwd, name,addr,sex,birthDay,email) values ('$id','$password','$name','$address','$sex',$birthDay,'$email')";
echo $sql;
 if($con->query($sql)){
  echo 'success inserting';
 }else{
  echo 'fail to insert sql';
 }
?>