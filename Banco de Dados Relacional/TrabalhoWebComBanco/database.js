const mysql = require('mysql');

// Configurações de conexão com o banco de dados
const connection = mysql.createConnection({
  host: 'mysql-joguinho-viniyoda360-d36d.f.aivencloud.com',
  port: '27906',
  user: 'avnadmin',
  password: 'AVNS_KPxvTUUtahG1o6-uTlV',
  database: 'joguinhodb',
  connectTimeout: 100000 // 10 segundos
});

// Conectar ao banco de dados
connection.connect((err) => {
    if (err) {
      console.error('Erro ao conectar ao banco de dados:', err.stack);
      return;
    }
    console.log('Conexão bem-sucedida ao banco de dados.');
});


connection.query("SELECT * FROM usuarios", function (err, result, fields) {
    if (err) {
        console.log(err);
    };
    console.log(result);
});
