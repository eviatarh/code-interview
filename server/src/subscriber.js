const request = require('request-promise');
const providersData = require('./providersData');
const { pubsubUrl, serverUrl } = require('./config');
async function initSubscriber(app){
    const route = 'providerUpdates';
    await request({
        uri: `${pubsubUrl}/subscribe`,
        method: 'POST',
        body: {
            channel: 'addProvider',
            address: `${serverUrl}/${route}`,
        },
        json: true,
    });
    app.post(`/${route}`, async (req, res) => {
        await providersData.upsert(req.body.payload);
        res.send();
    });

    const deleteRoute = 'providerDeletes';
    await request({
        uri: `${pubsubUrl}/subscribe`,
        method: 'POST',
        body: {
            channel: 'deleteProvider',
            address: `${serverUrl}/${deleteRoute}`,
        },
        json: true,
    });
    app.post(`/${deleteRoute}`, async (req, res) => {
        await providersData.deleteProvider(req.body.payload);
        res.send();
    });
}

module.exports = initSubscriber;
