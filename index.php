<?php
session_start(); // 세션
?>
<!DOCTYPE HTML>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/earlyaccess/notosanskr.css">
    <link rel="stylesheet" type="text/css" href="assets/css/index.css">
    <meta charset="utf8">
</head>

<body>
    <div class="container">
        <h1 class="namepan">Brievey!</h1>
        <img class="mlogo" src="assets/image/lgo.png"></img>
        <p class="intro">
            <span>여러분이 사는 도시,</span><br>
            <b>당신이 곧 시장입니다.</b>
        </p>
        <a class="start" href="<?=($_SESSION['id']==null)?"login.php":"main.php"?>">시작하기</a>
    </div>
    <script src="assets/js/index.js"></script>
</body>

</html>