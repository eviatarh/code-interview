const config = require('./config');
const { initApp } = require('./initApp');
const providersData = require('./providersData');

const express = require('express');

const app = express();

providersData.init()
    .then(()=>initApp(app))
    .then(()=>{
        app.listen(config.port, () => {
            console.log(`Example app listening on port ${config.port}!`)
        });
    });
