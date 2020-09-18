const fetch = require('node-fetch');
var https = require('follow-redirects').https;
const fs = require('fs');
const csv = require('csv-parse');

var output = [];

fs.createReadStream('Training.csv')
    .pipe(csv())
    .on('data', (row) => {
    output.push(row)})
    .on('end', () => {
        for(let i = 1; i < 501; i++){
            var text = output[i];
            uri = encodeURI(text)

            var API_URL = `https://api.meaningcloud.com/sentiment-2.1?key=7ea5541fcc9a26dcacd98d7806d2b40c&lang=en&txt=${uri}&model=general`
            const body = { a: 1 };

            fetch(API_URL, {
                method: 'POST',
                body:    JSON.stringify(body),
                headers: {
                    'Content-Type': 'application/json'
                    },
            })
            .then(res => res.json())
            .then(json => console.log(json))
            .catch(err => console.error(err));

            // var options = {
            //     'method': 'POST',
            //     'hostname': 'api.meaningcloud.com',
            //     'path': `/sentiment-2.1?key=7ea5541fcc9a26dcacd98d7806d2b40c&lang=en&txt=${uri}&model=general`,
            //     'headers': {
            //     },
            //     'maxRedirects': 20
            //   };

            // var req = https.request(options, function (res) {
            //     var chunks = [];
            
            //     res.on("data", function (chunk) {
            //         chunks.push(chunk);
            //     });
            
            //     res.on("end", function (chunk) {
            //         var body = Buffer.concat(chunks);
            //         console.log(body.toString());
            //     });
            
            //     res.on("error", function (error) {
            //         console.error(error);
            //     });
            // });
            // req.end();
            
        }
    })




