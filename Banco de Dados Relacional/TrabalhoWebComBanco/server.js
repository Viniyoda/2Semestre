const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const cors = require('cors');


const app = express();
app.use(cors());
const PORT = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
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
  // Conectar ao banco de dados
  connection.connect((err) => {
      if (err) {
        console.error('Erro ao conectar ao banco de dados:', err.stack);
        return;
      }
      console.log('Conexão bem-sucedida ao banco de dados.');
  });

app.use(express.json());

// Servir arquivos estáticos (como index.html)
app.use(express.static(path.join(__dirname)));



let user = '';
// Rota de login
app.post('/login', (req, res) => {
    console.log("Teste", req.body)
    const { username, password } = req.body;
    const queryLogin = `SELECT * FROM usuarios WHERE nome_usuario = '${username}' AND senha_usuario = '${password}'`;
    
    connection.query(queryLogin,function (err, results) {
        if (err) {
            console.error('Erro ao executar consulta:', err);
            res.status(500).send('Erro interno ao realizar o login');
            return;
        }

        if (results.length > 0) {
            // Redirecionar para a tela do jogo
            user = username;
            res.sendFile(path.join(__dirname, '/pages/joguinho.html'));
        } else {
            res.status(401).send('Usuário ou senha incorretos.');
        }
    });
});


// Rota de cadastro
app.post('/cadastro', (req, res) => {
    console.log("Teste", req.body)
    const { newUsername, newPassword } = req.body;
    const queryIfEquals = `SELECT * FROM usuarios WHERE nome_usuario = '${newUsername}' AND senha_usuario = '${newPassword}'`
    const queryCadastro = `INSERT INTO usuarios (nome_usuario, senha_usuario) VALUES ('${newUsername}', '${newPassword}')`;
    
    connection.query(queryIfEquals,function (err, results) {
        if (err) {
            console.error('Erro ao executar a igualdade:', err);
            res.status(500).send('Erro interno ao realizar a igualdade');
            return;
        }
        
        if (results.length > 0) {
            // Alerta de igualdade
            res.write('<script>alert("Cadastro ja realizado, tente outro usuario e senha");</script>');
            // Redirecionar para a tela de cadastro novamente
            res.write('<script>setTimeout(function() { window.location.href = "/pages/cadastro.html"; }, 400);</script>');
            res.end();
        } else{
            connection.query(queryCadastro,function (err, results) {
                if (err) {
                    console.error('Erro ao executar a insercao:', err);
                    res.status(500).send('Erro interno ao realizar a insercaoo');
                    return;
                } else {
                    // Alerta de sucesso
                    res.write('<script>alert("Cadastro realizado com sucesso!");</script>');
                    // Redirecionar para a tela de login
                    res.write('<script>setTimeout(function() { window.location.href = "/index.html"; }, 400);</script>');
                    res.end();
                }
            });
        }
    });
});




// Rota para atualizar a vida do herói e do vilão
app.post('/atualizarVida', async (req, res) => {
    const { vidaHeroi, vidaVilao } = req.body;
    try {
        await request.query(`
      MERGE INTO jogo AS target
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
        console.log("Teste se recebeu o username sendo: ", user);
        const heroQuery = `SELECT J.vida_heroi FROM jogo J INNER JOIN usuarios U ON J.usuario_id = U.usuario_id WHERE U.nome_usuario = '${user}'`;
        const villainQuery = `SELECT J.vida_vilao FROM jogo J INNER JOIN usuarios U ON J.usuario_id = U.usuario_id WHERE U.nome_usuario = '${user}'`;

        // Consulta para obter os dados do herói
        connection.query(heroQuery, function (err, heroResults) {
            if (err) {
                console.error('Erro ao buscar dados do herói:', err);
                return res.status(500).json({ error: 'Erro ao buscar dados do herói.' });
            }
            console.log("ResultQueryHeroi: ", heroResults);

            // Consulta para obter os dados do vilão
            connection.query(villainQuery, function (err, villainResults) {
                if (err) {
                    console.error('Erro ao buscar dados do vilão:', err);
                    return res.status(500).json({ error: 'Erro ao buscar dados do vilão.' });
                }
                console.log("ResultQueryVilao: ", villainResults);

                res.json({ heroResults, villainResults });
            })
        })
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