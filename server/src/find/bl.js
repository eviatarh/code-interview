const providersData = require('../providersData');

async function find({ specialty, date, minScore }) {
    const allData = providersData.findAll();


    return allData
        .filter((currProvider) => currProvider.score >= minScore &&
            currProvider.specialties.findIndex(currSpec => currSpec.toLowerCase() === specialty.toLowerCase()) > -1 &&
            currProvider.availableDates.findIndex(({from, to}) => from <= date && date <= to) > -1
        ).sort((a, b) => b.score - a.score).map(({name}) => name);
}

module.exports = {
    find,
};
