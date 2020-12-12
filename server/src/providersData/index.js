
let providersData;
async function init() {
    const data = require('./providers.json');
    providersData = [
        ...data,
    ];
}

async function upsert(newProvider) {
    // todo: validate provider schema
    const existsProviderIndex = providersData.findIndex(({ name })=> newProvider.name === name);
    if (existsProviderIndex > -1) {
        const currentData = providersData[existsProviderIndex];
        providersData[existsProviderIndex] = {
            ...currentData,
            ...newProvider,
        };
    } else {
        providersData.push(newProvider);
    }
}

async function deleteProvider({ name }) {
    // todo: validate provider schema
    const providerToDeleteIndex = providersData.findIndex((currProvider)=> currProvider.name === name);
    if (providerToDeleteIndex) {
        providersData.splice(providerToDeleteIndex, 1);
    } else {
        console.error('provider to delete isn\'t exists! doing nothing for now...');
    }
}

function findAll() {
    if (!providersData) throw new Error('Data provider isn\'t initialized yet!');
    return providersData;
}

module.exports = {
    init,
    findAll,
    upsert,
    deleteProvider,
};
