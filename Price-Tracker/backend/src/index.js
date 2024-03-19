const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const {pythonShell, PythonShell} = require('python-shell');
const app = express();

app.use(cors({
    origin: process.env.CORS_ORIGIN,
    Credential: true
}))
app.use(express.json());

app.get('/',(req,res)=>{
  res.send('Hello world');
})

app.post('/data', (req, res) => {
  // console.log("hello")
  const inputData = req.body.value;
  console.log('Received input:', inputData);
  //connecting python
  let options = {
    scriptPath: "C:/Users/Manoj/Dropbox/My PC (LAPTOP-DT2730KE)/Desktop/git1/Web-Scraping/Price-Tracker/backend/WebScraping",
    args: [inputData]
  }
  PythonShell.run("demo.py",options).then(res=>{
    // if(error) console.log(error)
    // if(res) console.log(res)
    console.log(res)
  })
  // console.log("hogaya");
  // res.end(`<h1>${inputData}</h1>`)
  res.sendStatus(200);
});

dotenv.config({
  path: './env'
});

app.listen(process.env.PORT || 3000, () => {
  console.log(`Server is running on http://localhost:${process.env.PORT}`);
});
