<?php
include "index.html";
session_start();

if (isset($_POST['save'])) {
    $_SESSION['name'] = $_POST['name'];
    echo $_SESSION['name'];
}
if (isset($_POST['reset'])) {
    session_unset();
    echo $_SESSION['name'];
}

?>