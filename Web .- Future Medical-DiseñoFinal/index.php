<?php
require 'vendor/autoload.php' ;
$uri="mongodb://usuario:password@host_base_datos/base_de_datos?ssl=false";
$client=new MongoDB\Client($uri);

$data = file_get_contents("archivo.json");

//print_r($data);

$data_a=json_decode($data,true);

//print_r($data_a);

foreach($data_a as $row){
    print_r($row);
}

?>