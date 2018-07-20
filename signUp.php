<!--
<!doctype html>
<html>
<head>
<title>sign up page</title>
</head>
<body>
<form name="join" method="post" action="memberSave.php">
 <h1>input your information</h1>
 <table border="1">
  <tr>
   <td>ID</td>
   <td><input type="text" size="30" name="id"></td>
  </tr>
  <tr>
   <td>Password</td>
   <td><input type="password" size="30" name="pwd"></td>
  </tr>
  <tr>
   <td>Confirm Password</td>
   <td><input type="password" size="30" name="pwd2"></td>
  </tr>
 
 </table>
 <input type=submit value="submit"><input type=reset value="rewrite">
</form>
</body>
</html>
-->
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
            <b class="logotext">회원 가입</b>
        </div>

        <form id="rgstform" action="memberSave.php" method="post">
        <div class="inputcontainer">
            <p>이메일</p>
            <input type="email" name="id">
        </div>

        <div class="inputcontainer">
            <p>비밀번호</p>
            <input type="password" name="pwd">
        </div>

        <div class="inputcontainer">
            <p>비밀번호 확인</p>
            <input type="password" name="pwd2">
        </div>

        <a href="#" class="login" onclick="document.getElementById('lginform').submit();">회원 가입</a>
        </form>

    </div>

</body>

</html>