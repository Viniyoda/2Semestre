const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();

// Middleware para fazer o parse do corpo da requisição no formato JSON
app.use(bodyParser.json());

// Configurações de conexão com o banco de dados
const connection = mysql.createConnection({
    host: 'mysql-joguinho-viniyoda360-d36d.f.aivencloud.com',
    port: '27906',
    user: 'avnadmin',
    password: 'AVNS_KPxvTUUtahG1o6-uTlV',
    database: 'joguinhodb',
    connectTimeout: 100000 // 10 segundos
});

// Rota para autenticação do usuário
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const queryLogin = "SELECT * FROM usuarios WHERE nome_usuario = ? AND password = ?";
    
    connection.query(queryLogin, [username, password], function (err, results) {
        if (err) {
            console.error('Erro ao executar consulta:', err);
            res.status(500).send('Erro interno ao realizar o login');
            return;
        }

        if (results.length > 0) {
            // Redirecionar para a tela do jogo
            res.status(200).send('Login bem-sucedido! Redirecionando para a tela do jogo...');
            window.location.href = "joguinho.html";
        } else {
            res.status(401).send('Usuário ou senha incorretos.');
        }
    });
});

app.listen(3000, () => {
    console.log('Servidor iniciado na porta 3000');
});