<?php
// $host = $_SERVER['HTTP_HOST'];
// $uri = (dirname($_SERVER['PHP_SELF']));
// echo $uri;
$redirectTo = "testPage.php";
// can also use a button for an interaction
// header("https://$host$uri/$redirectTo");
if (isset($_GET["visitTestPage"])) {
    header("location:$redirectTo");
}
?>
<html>
    <form>
        <input type="submit" name="visitTestPage" value="Test Page">
    </form>
</html>