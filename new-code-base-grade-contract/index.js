/*
 * SPDX-License-Identifier: Apache-2.0
 */
/*jshint esversion: 8 */
/* jshint -W097 */
/* jshint node: true */
'use strict';

const NewGradeContract = require('./lib/new-grade-contract');
const express = require('express');
const app = express();
const port = 3000 || process.env.PORT;
const quotesRouter = require('./routes/grades');

app.get('/', (req, res) => {
    res.json({ message: 'Welcome to the homepage' });
});

app.use('/grades', quotesRouter);

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});

module.exports.NewGradeContract = NewGradeContract;
module.exports.contracts = [NewGradeContract];
