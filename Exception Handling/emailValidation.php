<?php
# creating a custom exception class, inherited from PHP Exception class
class customException extends Exception {
    # a custom function for practicing exception handling
    public function errorMessage() {
        $error = "Not a valid email address";
        return $error;
    }
}
$email = "abrac@dabra.com";
try {
    if (filter_var($email, FILTER_VALIDATE_EMAIL) === False) {
        throw new customException($email);
    }
    else{
        echo "Valid email address";
    }
} catch (customException $cE) {
    echo $cE->errorMessage();
}
?>