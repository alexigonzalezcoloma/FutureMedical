<?php
    //var json = $_REQUEST['soy_la_variable'];
    //echo(json);
    
    $file = fopen("archivo.txt", "a");

    fwrite($file, "Añadimos línea 1" . PHP_EOL);
    
    fwrite($file, "Añadimos línea 2" . PHP_EOL);
    
    fclose($file);

    echo 'archivo creado';

?>