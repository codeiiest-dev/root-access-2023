const express = require('express')
const app = express()
const port = 5002

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index1.js')
})

app.get('/index2', (req, res) => {
    res.sendFile(__dirname + '/index2.js')
})

app.listen(port, () => {
    console.log(`Listening on ${port}`)
})