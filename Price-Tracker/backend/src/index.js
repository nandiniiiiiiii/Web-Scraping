const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

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
  // res.end(`<h1>${inputData}</h1>`)
  res.sendStatus(200);
});

dotenv.config({
  path: './env'
});

app.listen(process.env.PORT || 3000, () => {
  console.log(`Server is running on http://localhost:${process.env.PORT}`);
});
