const express = require('express');
const path = require('path');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const cron = require('node-cron');
const axios = require("axios")
const bodyParser = require('body-parser');
const FormData = require("form-data");
app.use(bodyParser.urlencoded({ extended: true }));

const flag = "accessdenied{w3bh00k5_5@v3d_y0u?}";
let clients = [];

app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json());

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.get('/', function (req, res) {
  res.render('index');
});

app.post('/webhook', function (req, res) {
  const webhookUrl = req.body.url;
  if (webhookUrl) {
    clients.push(webhookUrl);
    res.status(200).redirect("/");
  } else {
    res.status(500).redirect("/");
  }
});

cron.schedule('0,15,30,45 * * * *', () => {
  console.log(clients)
  clients.forEach((client,index) => {
    const form = new FormData();
    form.append("flag", flag);
    axios.post(client , form)
    .then(data => {
        console.log(`Sent to ${client}`);
        clients.splice(index, 1);
    })
    .catch(err => {
        console.log(`Error sending to ${client}`)
    })
  });
});

io.on('connection', function (socket) {
    console.log('A user connected');
    let flagIndex = 0;
    socket.emit('update flag', flag[flagIndex]);
    flagIndex = (flagIndex + 1)%flag.length;
    setInterval(() => {
        socket.emit('update flag', flag[flagIndex]);
        flagIndex = (flagIndex + 1)%flag.length;
    }, 300000);
    socket.on('disconnect', () => {
      console.log('A user disconnected');
    });
});

http.listen(3000, function () {
  console.log('Listening on *:3000');
});
