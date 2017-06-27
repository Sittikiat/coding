var fs = require("fs");
var read = fs.readFileSync("./file/data.txt", "utf-8");
console.log(read);