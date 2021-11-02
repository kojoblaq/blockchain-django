/*jshint esversion: 8 */
/* jshint -W097 */
/* jshint node: true */
'use strict';
const env = process.env;

const config = {
    listPerPage: env.LIST_PER_PAGE || 10,
};

module.exports = config;
