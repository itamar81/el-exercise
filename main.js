var fs = require('fs');

var SERVER_PORT=process.env.SERVER_PORT || 3000;
var data = fs.readFileSync('rickandmorty.json');
var elements = JSON.parse(data);
const express = require("express");


const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.get('/api', (req, res) => {
    res.json(books);
});
// this is where we'll handle our various routes from
const routes = require('./routes.js')(app, fs);

// finally, launch our server on port 3001.
const server = app.listen(SERVER_PORT, () => {
  console.log('listening on port %s...', server.address());
});