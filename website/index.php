<html>
    <head>
        <title>thirdGroup</title>
    </head>

    <body>
        <h1>MemberList</h1>
        <ul>
            <?php

            $json = file_get_contents('http://member-service/');
            $obj = json_decode($json);
	    print_r($obj);	

 /*           foreach ($obj as $member) {
                echo "<li>SID:".$member->SID."<ul>name:".$member->name."</ul></li>";
	    }*/

            ?>
        </ul>
    </body>
</html>
