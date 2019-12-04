<?php


//phpinfo();

/*$mng = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$stats = new MongoDB\Driver(["dbstats" => 1]);
$res = $mng->executeCommand("phpbasics", $stats);

$stats = current($res->toArray());
print_r ($stats);
*/


DescargarArchivo("archivo.json");

function DescargarArchivo($fichero){
    $basefichero = basename($fichero);

    header( "Content-Type: application/octet-stream");
    header( "Content-Length: ".filesize($fichero));
    header( "Content-Disposition: attachment; filename=".$basefichero."");
    readfile($fichero);
}

?>