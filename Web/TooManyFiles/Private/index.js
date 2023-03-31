const express = require('express')
const app = express()
const port = 5000

const flag = "accessdenied{D!d_y0u_s01v3_!t_m@nu@11y?}"

const arr = [41 , 3464 , 1333 , 1495 , 4166 , 721 , 1476 , 4353 , 1957 , 4460 , 704 , 3140 , 3277 , 1824 , 4960 , 491 , 2995 , 1940 , 4827 , 435 , 2385 , 4602 , 3902 , 153 , 292 , 2380 , 2418 , 3713 , 4715 , 4892 , 446 , 1722 , 4769 , 1536 , 1869 , 4909 , 662 , 1294 , 2032 , 4893]

app.get('/', (req, res) => {
    let data = ""
    for(let i=1;i<=5000;i++){
        data += `<a href="/file/${i}">File ${i}</a> &nbsp &nbsp`
    }
    res.send(data)
})

app.get("/file/:id" ,(req,res) => {
    const fileId = req.params.id;
    const idx = arr.findIndex(element => element == fileId);
    if(idx === -1){
        res.send("<h1>Hi, Nice to meet you</h1>")
    } else {
        const data = `
            <h1>I have some data for you .But I'm not sure how you can use it.</h1>
            <h2>_${idx}_${flag[idx]}</h2>
        `
        res.send(data)
    }
})

app.listen(port, () => {
  console.log(`Listening on ${port}`)
})