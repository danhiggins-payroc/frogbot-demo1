const express = require('express');
const app = express();
const exec = require('child_process').exec;

app.get('/exec', function (req, res) {
    // Vulnerability: User input passed directly to the command line without validation
    exec(req.query.cmd, function (error, stdout, stderr) {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.send(`Error: ${stderr}`);
        }
        res.send(`Output: ${stdout}`);
    });
});

app.listen(3000, function () {
    console.log('App listening on port 3000!');
});
