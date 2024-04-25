const express = require('express');
const server = express();

    //localhot:3000/curso
//server.get('/curso', () => {
//    console.log('ALGUEM DEU UM GET NA ROTA CURSO');
//});

    //localhost:3000/curso
server.get('/curso', (req, res) => {
    return res.json({ curso: 'NodeJS'});
});

server.listen(3000);
