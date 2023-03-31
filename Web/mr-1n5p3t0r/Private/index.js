const expresss = require('express')

const app = expresss()

app.get('/', (req, res) => {
    // server main.html
    res.sendFile(__dirname + '/main.html')
})

app.get('/style.css', (req, res) => {
    // server main.html
    res.sendFile(__dirname + '/style.css')
})

app.get('/style1.css', (req, res) => {
    // server main.html
    res.sendFile(__dirname + '/style1.css')
})

app.listen(3000, ()=>{
    console.log("Server listening on port 3000");
})