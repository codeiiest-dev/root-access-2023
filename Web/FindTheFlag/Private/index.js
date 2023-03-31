const express = require('express');
const { exec } = require('child_process');
const app = express();

app.set('view engine', 'pug');

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.render('index');
});

app.post('/ping', (req, res) => {
  const ip = req.body.ip.trim();
  const newIp = ip.replace("& ","").replace("&& ","").replace(";","").replace("|","").replace("-","").replace("$","").replace("(","").replace(")","").replace("`","").replace("||")
  const command = `ping -c 4 ${newIp}`;
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      res.render('index', { ip, output: error });
      return;
    }
    console.error(`output: ${stdout}`);
    res.render('index', { ip, output: stdout });
  });
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
