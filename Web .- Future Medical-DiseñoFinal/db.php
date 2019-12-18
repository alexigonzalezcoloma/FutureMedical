<?php

//phpinfo();

/*$mng = new MongoDB\Driver\Manager("mongodb://localhost:27017");
$stats = new MongoDB\Driver(["dbstats" => 1]);
$res = $mng->executeCommand("phpbasics", $stats);

$stats = current($res->toArray());
print_r ($stats);
*/


$filename = 'archivo.json';
$lines = file($filename, FILE_IGNORE_NEW_LINES);

$bulk = new MongoDB\Driver\BulkWrite;

foreach ($lines as $line) {
    echo $line;
    $bson = MongoDB\BSON\fromJSON($line);
    $document = MongoDB\BSON\toPHP($bson);
    $bulk->insert($document);
}

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1/');

$result = $manager->executeBulkWrite('test.arq', $bulk);
printf("Inserted %d documents\n", $result->getInsertedCount());



?>