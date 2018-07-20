<?php
session_start(); // 세션
if($_SESSION['id']==null) { // 로그인 하지 않았다면
?>

<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf8">
    <link rel="stylesheet" href="assets/css/index.css">
    <link rel="stylesheet" href="assets/css/signin.css">
</head>

<body>
    <div class="mobcontainer">
        <div class="titlecontainer">
            <img src="assets/image/lgo.png" class="logoimage">
            <b class="logotext">로그인</b>
        </div>

        <form id="lginform" action="logincheck.php" method="post">
            <div class="inputcontainer">
                <p>이메일</p>
                <input type="email" name="id">
            </div>
            <div class="inputcontainer">
                <p>비밀번호</p>
                <input type="password" name="pwd">
            </div>
            <a href="#" class="login" onclick="document.getElementById('lginform').submit();">로그인</a>
        </form>
       
        <a class="register" href="signup.php">계정 만들기</a>

        <a class="forgetpass" href="#">비밀번호를 잊어버리셨나요?</a>

    </div>

</body>

</html>
<!--
<center><br><br><br>
<form name="login_form" action="logincheck.php" method="post"> 
   ID : <input type="text" name="id"><br> 
   PW:<input type="password" name="pwd"><br><br>
   <input type="submit" name="login" value="Login"> 
</form>
	
<form name="register" action="signUp.php" method="post">
	<input type="submit" name="register" value="register">
	</form>
</center>
-->
<?php
}else{ // 로그인 했다면
   echo "<center><br><br><br>";
   echo $_SESSION['name']."(".$_SESSION['id'].")님이 로그인 하였습니다.";
   echo "&nbsp;<a href='logout.php'><input type='button' value='Logout'></a>";
   echo "</center>";
}
?>