var express = require('express');
var cookieParser = require('cookie-parser');
var escape = require('escape-html');
var serialize = require('node-serialize');
var app = express();
app.use(cookieParser())
 
app.get('/', function(req, res) {
    try {
        if (req.cookies.profile) {
            var str = new Buffer.from(req.cookies.profile, 'base64').toString();
            console.log(str)
            var obj = serialize.unserialize(str);
            if (obj.username) {
                res.send("Hello " + escape(obj.username));
            }
            } else {
                res.cookie('profile', "eyJ1c2VybmFtZSI6ImhAY2szciIsImNvdW50cnkiOiJpbmRpYSIsImNpdHkiOiJob3dyYWgifQ", {
                    maxAge: 900000,
                    httpOnly: false
                });
                res.send("Hello World");
            }
    } catch(e) {
        console.log(e)
    }
});
app.listen(3000 , () => {
    console.log("Listening")
});