/*
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const NewGradeContract = require('./lib/new-grade-contract');



const express = require('express');
const app = express();
const port = 3000 || process.env.PORT;
const quotesRouter = require('./routes/grades');
var bodyParser = require('body-parser');  


app.get('/', (req, res) => {
    res.json({ message: 'Welcome to the homepage' });
    
});
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "http://127.0.0.1:8000"); // update to match the domain you will make the request from
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });
  
app.use('/get-grades', quotesRouter.router);
app.use('/get-grade', quotesRouter.router1);
app.use('/create-grade', quotesRouter.router2);
app.use('/update-grade', quotesRouter.router3);
app.use('/delete-grade', quotesRouter.router4);


app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});

module.exports.NewGradeContract = NewGradeContract;
module.exports.contracts = [NewGradeContract];
