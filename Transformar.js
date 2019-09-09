var fs = require('fs');
var xml2json = require ('xml2js');

var parser = new xml2json.Parser();

fs.readfile('example.xml',function(err,data){
    parser.parseString(data,function(err,result){ 
        console.log(result);
    });
});
