const bodyParser = require('body-parser');
const find = require('./find');
const book = require('./book');
const initSubscriber = require('./subscriber');

module.exports = {
    async initApp(app){
        app.use(bodyParser.json())
        find(app);
        book(app);
        await initSubscriber(app);
    }
};
