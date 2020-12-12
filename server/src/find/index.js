const BL = require('./bl');

function validateRequest(request){
    //todo;
    if (!request.query.specialty) return false;
    const date = parseInt(request.query.date);
    return !(date <= 0 || date != request.query.date);

}

function find(app) {
    app.get('/appointments', async (request, response) => {
        if (!validateRequest(request)) {
            response.status(400).send();
        } else {
            const { specialty, date, minScore } = request.query;

            const result = await BL.find({ specialty, date, minScore });

            response.send(result);
        }
    });
}

module.exports = find;
