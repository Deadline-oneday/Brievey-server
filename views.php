<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>정책게시판</title>
</head>
<body>
<article class="boardArticle">
<h3>정책게시판 글쓰기</h3>
<div id="boardView">
<h3 id="boardTitle"><?php echo $row['b_title']?></h3>
<div id="boardInfo">
<span id="boardID">작성자: kangsecu </span>
<span id="boardDate">작성일: 2018-3-12</span>
<span id="boardHit">조회: 12</span>
</div>
<div id="boardContent"><?php echo $row['b_content']?></div>
	<?php
		$json = '{"Trans@1": "서울특별시 지역물류기본계획 수립 연구용역` 서울시의 물류환경 진단 및 장래 물류량 추정과 서울시 물류체계 기본구상과 서울시 물류기본계획수립을 하기위해 시행된 정책이다."}';
		
		$data=json_decode($json, true);
		
		foreach($data as $k=>$v){
			$v = str_replace("`","<br/>\n", $v);
			echo "<br>$k<br>$v";
			
		
		
		}
		?> 
</div>
</article>
</body>
</html>