const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');


const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const PORT = 3000;
/*
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
*/

app.use(express.json());

// Servir arquivos estáticos (como index.html)
app.use(express.static(path.join(__dirname)));

app.post('/login', (req, res) => {
    console.log("Teste", req)
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

// Rota para atualizar a vida do herói e do vilão
app.post('/atualizarVida', async (req, res) => {
    const { vidaHeroi, vidaVilao } = req.body;

    try {
        await sql.connect(config);
        const request = new sql.Request();
        await request.query(`
      MERGE INTO Personagens AS target
      USING (VALUES ('heroi', ${vidaHeroi}), ('vilao', ${vidaVilao})) AS source (Nome, Vida)
      ON target.Nome = source.Nome
      WHEN MATCHED THEN
        UPDATE SET Vida = source.Vida
      WHEN NOT MATCHED THEN
        INSERT (Nome, Vida) VALUES (source.Nome, source.Vida);
      `);
        res.status(200).send('Vida do herói e do vilão atualizada com sucesso.');
    } catch (err) {
        console.error(err);
        res.status(500).send('Erro ao atualizar a vida do herói e do vilão.');
    }
});

// Rota para fornecer os dados do herói e do vilão
app.get('/characters', async (req, res) => {
    try {
        await sql.connect(config);
        const request = new sql.Request();

        // Consulta para obter os dados do herói
        const heroResult = await request.query("SELECT * FROM Personagens WHERE Nome = 'heroi'");
        const heroi = heroResult.recordset[0];

        // Consulta para obter os dados do vilão
        const villainResult = await request.query("SELECT * FROM Personagens WHERE Nome = 'vilao'");
        const vilao = villainResult.recordset[0];

        res.json({ heroi, vilao });
    } catch (error) {
        console.error('Erro ao buscar dados do herói e do vilão:', error);
        res.status(500).json({ error: 'Erro ao buscar dados do herói e do vilão.' });
    }
});

// Rota para servir o arquivo HTML principal
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'dashboard.html'));
});

// Iniciar o servidor
app.listen(PORT, () => {
    console.log(`Servidor Express rodando na porta ${PORT}`);
});