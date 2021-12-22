/*jshint esversion: 8 */
/* jshint -W097 */
/* jshint node: true */
'use strict';

const express = require('express');
const router = express.Router();
const router1 = express.Router();
const router2 = express.Router();
const router3 = express.Router();
const router4 = express.Router();
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

router1.get('/', function(req, res, next) {
    try {
        res.json(quotes.getUserGrade(req.query.staff_id,req.query.page));
    } catch (err) {
        console.error('Error while getting grades ', err.message);
        next(err);
    }
});


router2.get('/', function(req, res, next) {
    try {
        res.json(quotes.createGrade(req.query.staff_id,req.query.staff_grade,req.query.institution_name, req.query.job_role, req.query.staff_name, req.query.salary,req.query.creator, req.query.status));
    } catch (err) {
        console.error('Error while creating grade ', err.message);
        next(err);
    }
});

router3.get('/', function(req, res, next) {
    try {
        res.json(quotes.updateGrade(req.query.ss_grade, req.query.inst_name, req.query.job_t, req.query.staffName,req.query.salary,req.query.creator, req.query.status,req.query.staffId ));
    } catch (err) {
        console.error('Error updating grade ', err.message);
        next(err);
    }
});
router4.get('/', function(req, res, next) {
    try {
        res.json(quotes.deleteGrade(req.query.staffId));
    } catch (err) {
        console.error('Error while getting grades ', err.message);
        next(err);
    }
});


module.exports = {
    router,
    router1,
    router2,
    router3,
    router4
} 
