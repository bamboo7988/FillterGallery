const express = require('express');
const fileUpload = require('express-fileupload');
const fs = require('fs');
const app = express();
const frontApp = express();
const port = 3000;
var frontPort = 8000;
var path = require('path');
const { stringify } = require('querystring');

// default options
app.use(fileUpload());
frontApp.use(express.static(path.join(__dirname)));
console.log(path.join(__dirname))

app.use((req, res, next) => {
    // Websiteyouwishtoallowtoconnect
    res.setHeader("Access-Control-Allow-Origin", "*");

    // Requestmethodsyouwishtoallow
    res.setHeader(
      "Access-Control-Allow-Methods",
      "GET,POST,OPTIONS,PUT,PATCH,DELETE"
    );

    // Requestheadersyouwishtoallow
    res.setHeader(
      "Access-Control-Allow-Headers",
      "X-Requested-With,content-type"
    );

    // Settotrueifyouneedthewebsitetoincludecookiesintherequestssent
    // totheAPI(e.g.incaseyouusesessions)
    res.setHeader("Access-Control-Allow-Credentials", true);

    // Passtonextlayerofmiddleware
    next();
  });

app.post('/upload', function(req, res) {
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send('No files were uploaded.');
  }

  // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
  let sampleFile = req.files.fileImage;

  // Use the mv() method to place the file somewhere on your server
  sampleFile.mv('./upload/filename.jpg', function(err) {
    if (err){
      return res.status(500).send(err);
    }
    if (fs.existsSync('./upload/final.jpg')){
      // Use the unlink() method to delete the existed final file
      fs.unlink('./upload/final.jpg', function(err){
        if (err){
          return res.status(500).send(err);
        }
      });
    }
    res.send('File uploaded!');
  });


});

app.get('/call/python', pythonProcess)

function pythonProcess(req, res) {
  console.log('python update')

  console.log(`sigmaBF: ${req.query.sigmaBF}, phieqCQ: ${req.query.phieqCQ}, sigmaDE: ${req.query.sigmaDE}`)

  let spawn = require("child_process").spawn

  let process = spawn('python', [
    "./imageCalculate.py",
    req.query.sigmaBF,
    req.query.phieqCQ,
    req.query.sigmaDE
  ])

  process.stdout.on('data', (data) => {
    const parsedString = JSON.parse(data)
    console.log(`stdout: ${data}`)
    // res.json(parsedString)
    res.send(parsedString)
  })

}

console.log(path.join(__dirname + '/index.html'))
frontApp.post('/',function (req, res) {
    res.sendFile(path.join(__dirname + '/index.html'));
});

app.listen(port, function () {
    console.log('Express app started on ' + port);
});

frontApp.listen(frontPort,function() {
    console.log('Express app started on ' + frontPort);
})
