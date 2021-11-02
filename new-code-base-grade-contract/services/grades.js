/*jshint esversion: 8 */
/* jshint -W097 */
/* jshint node: true */
'use strict';
const path = require('path');
const sqlite = require('better-sqlite3');
const db = new sqlite(path.resolve('./nodejs-sqlite/grades.db'), { fileMustExist: true });
const config = require('../config');

function getMultiple(page = 1) {
    const offset = (page - 1) * config.listPerPage;
    const data = db.prepare('SELECT * FROM grade LIMIT ?,?').all(offset, config.listPerPage);
    const meta = { page };
    return {
        data,
        meta
    };
}

module.exports = {
    getMultiple
};
