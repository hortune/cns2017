<?php

$size = intval(trim(fgets(STDIN)));
$array = array();
for ($i = 0; $i < $size; $i += 1){   
    $key = intval(trim(fgets(STDIN)));
    $array[$key] = $i;
}

>