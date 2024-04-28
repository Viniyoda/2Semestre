const express = require('express');
const path = require('path');
const sql = require('mssql');

const app = express();
const PORT = 3000;

const config = {
    user: 'joguinhoadmin',
    password: 'Joguinho1',
    server: 'joguinhoserver.database.windows.net',
    database: '',
    options: {
        encrypt: true
    }
};