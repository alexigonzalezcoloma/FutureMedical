<?php
    $json = $_REQUEST['soy_la_variable'];    
    $file = fopen("archivo.json", "w");

    fwrite($file, $json . PHP_EOL);
    
    fclose($file);
    echo 'doc creado';

    /*$data = file_get_contents("archivo.json");

    print_r($data);

    $data_a=json_decode($data,true);
    print_r $data_a;*/
    
?>

<a href="conect.php">Descargar Fichero</a>