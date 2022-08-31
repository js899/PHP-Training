<?php
session_start();

if (isset($_POST['save'])) {
    $_SESSION['email'] = $_POST['email'];
    echo "<strong class='container'>".$_SESSION['email']."</strong>";
}
if (isset($_POST['reset'])) {
    session_unset();
    $_SESSION['email'];
    echo "<strong class='container'>Session is reset.</strong>";
}
include "index.html";
?>