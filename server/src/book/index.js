const BL = require('./bl');

function validateRequest(request){
    if (!request.body.name) return false;
    const date = parseInt(request.body.date);
    return !(date <= 0 || date != request.body.date);

}

function book(app) {
    app.post('/appointments', async (request, response) => {
        if (!validateRequest(request, response)) {
            response.status(400).send();
        } else {
            const { name, date } = request.body;

            const result = await BL.book({ name, date });

            if (!result) {
                response.status(400).send();
            } else {
                response.send({ success: true });
            }
        }
    });
}

module.exports = book;
