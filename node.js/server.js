var http = require("http");

var ip = "127.0.0.1";
var port = 1337;

http.createServer(function(req, res) {
    res.writeHead(200, {"Content-Type": "text/plain"});
    res.end("Server Running...");
}).listen(port,ip);

console.log("Server Running at http://127.0.0.1:1337/");
