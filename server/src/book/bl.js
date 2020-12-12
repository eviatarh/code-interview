const { pubsubUrl } = require('../config');
const providersData = require('../providersData');
const request = require('request-promise');


async function book({ date, name }) {
    const allData = providersData.findAll();

    const selectedProvider = allData.find((currProv) => currProv.name === name);
    if (!selectedProvider) return false;

    const isAvailable = selectedProvider.availableDates.findIndex(({from, to}) => from <= date && date <= to) > -1;

    if (isAvailable) {
        await request({
            uri: `${pubsubUrl}/publish`,
            method: 'POST',
            body: {
                channel: 'newAppointments',
                payload: {
                    name: selectedProvider.name,
                    date: date,
                }
            },
            json: true,
        })
    }

    return isAvailable;
}

module.exports = {
    book,
};
