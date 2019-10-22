<?php
    $json = $_REQUEST['soy_la_variable'];    
    $file = fopen("archivo.json", "a");

    fwrite($file, $json . PHP_EOL);
    
    fclose($file);
    echo 'doc creado';

   /* $data = file_get_contents("archivo.json");
    $products = json_decode($data, true);
 
    foreach ($products as $product) {
        echo '<pre>';
        print_r($product);
        echo '</pre>';
    }*/

?>