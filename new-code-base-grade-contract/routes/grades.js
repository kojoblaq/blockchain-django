/*jshint esversion: 8 */
/* jshint -W097 */
/* jshint node: true */
'use strict';

const express = require('express');
const router = express.Router();
const quotes = require('../services/grades');

/* GET quotes listing. */
router.get('/', function(req, res, next) {
    try {
        res.json(quotes.getMultiple(req.query.page));
    } catch (err) {
        console.error('Error while getting grades ', err.message);
        next(err);
    }
});

module.exports = router;
