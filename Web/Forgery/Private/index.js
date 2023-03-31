const { URL } = require('url')
const http = require('http')
const express = require('express')
const app = express()
const port = 8080
const port1 = 5002 // what is this for ?

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.js')
})

app.get('/forge', (req, res) => {
    const path = req.query.path
    if (typeof path !== 'string' || path.length === 0) {
        res.send('path must be a non-empty string')
    }
    else {
        const url = `http://localhost:${port1}${path}`
        const parsedUrl = new URL(url)
        if (parsedUrl.hostname !== 'localhost') {
            res.send('Hi, sorry we only talk with localhost!')
        }
        else {
            http.get(parsedUrl.href, forgedRes => {
                let contentType = forgedRes.headers['content-type']
                let body = ''
                forgedRes.on('data', chunk => {
                    body += chunk
                })
                forgedRes.on('end', () => {
                    if (contentType) {
                        res.setHeader('Content-Type', contentType)
                    }
                    res.send(body)
                })
            }).on('error', function(e) {
                res.send("Got error: " + e.message)
            })
        }
    }
})

app.listen(port, () => {
  console.log(`Listening on ${port}`)
})