<?php
DescargarArchivo("archivo.json");

function DescargarArchivo($fichero){
    $basefichero = basename($fichero);

    header( "Content-Type: application/octet-stream");
    header( "Content-Length: ".filesize($fichero));
    header( "Content-Disposition: attachment; filename=".$basefichero."");
    readfile($fichero);
}

?>