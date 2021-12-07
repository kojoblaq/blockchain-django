'use strict';
const path = require('path');
const sqlite = require('better-sqlite3');
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite(path.resolve('./nodejs-sqlite/grades.db'), { fileMustExist: true });
// const db = new sqlite(path.resolve('/home/project/blockchain-django/gradeStructure/db.sqlite3'), { fileMustExist: true });
function query(sql, params) {
    console.log(sql, params);
    return db.prepare(sql).all(params);
}

function _db() {
    // return new sqlite(path.resolve('./nodejs-sqlite/grades.db'), { fileMustExist: true });
    return new sqlite(path.resolve('../../gradeStructure/db.sqlite3'), { fileMustExist: true });
}


module.exports = {
    query,
    _db
};