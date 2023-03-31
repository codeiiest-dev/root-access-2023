const express = require('express')
const app = express()
const port = 50022

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index2.js')
})

app.get('/flag', (req, res) => {
    res.sendFile(__dirname + '/flag.txt')
})

app.listen(port, () => {
    console.log(`Listening on ${port}`)
})