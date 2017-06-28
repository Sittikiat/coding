var fs = require("fs");
fs.mkdir("./file/folder1", function(err) {
    if (err) throw console.log(err);
    fs.writeFileSync("./file/folder1/write.txt", "HelloWorld");
})