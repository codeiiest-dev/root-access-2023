const express = require('express');
const { exec } = require('child_process');
const app = express();

const randomString = "Nothing Usefull here, Pay no attention to it"

app.set('view engine', 'pug');

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.render('index');
});

app.post('/ping', (req, res) => {
  const ip = req.body.ip;
  const command = `ping -c 2 ${ip}`;
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      res.render('index', { ip, output: error });
      return;
    }
    const newOutput = stdout.toString().slice(0,1000)
    res.render('index', { ip, output: newOutput});
  });
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
