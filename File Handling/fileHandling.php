<?php
$filePath = "File Handling/read.txt";
$file = fopen($filePath, "r") or die("Unable To Open File");
// echo fread($file, filesize($filePath));
$i = 1;
while (!(feof($file))) {
    $lineString = fgets($file);
    // $lineLength = strlen($lineString);
    // if ($lineString[-1] == "\n") {
    //     echo substr($lineString, 0, $lineLength-1)."$".$i."\n";
    // }
    // else {
    //     echo $lineString."$".$i;
    // }
    // $i += 1;
    if (strpos($lineString, "Aaka") !== false){
        echo $lineString;
        break;
    }
}
fclose($file);
?>