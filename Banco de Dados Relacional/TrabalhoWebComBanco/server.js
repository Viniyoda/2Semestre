/*comandos npm
npm init
npm instal nodemon -g 
npm install -- save express
npm install express-session
npm install --save body-parser
npm install --save mysql
npm install ejs -save
*/


//require do express e do session
const express = require('express');
const session = require("express-session");
const path = require('path');
const app = express();


//require do bodyparser responsável por capturar valores do form
const bodyParser = require("body-parser");


//require do mysql
const mysql = require("mysql"); 
const { resolveSoa } = require('dns');


//criando a sessão
app.use(session({secret: "ssshhhhh"}));


//definindo pasta pública para acesso
app.use(express.static('public'))


//config engines
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/public'));


//config bodyparser para leitura de post
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());


function conectiondb(){
    // Configurações de conexão com o banco de dados
    const connection = mysql.createConnection({
        host: 'mysql-joguinho-viniyoda360-d36d.f.aivencloud.com',
        port: '27906',
        user: 'avnadmin',
        password: 'AVNS_KPxvTUUtahG1o6-uTlV',
        database: 'joguinhodb'
    });
    connection.connect((err) => {
        if (err) {
            console.error('Erro ao conectar ao banco de dados:', err.stack);
            return;
        }
        console.log('Conexão bem-sucedida ao banco de dados.');
    });

    return connection;
}




//rota padrao
app.get('/', (req, res) => {
    var message = ' ';
    req.session.destroy();
    res.render('views/cadastro', { message: message });
});


//rota para login
app.get("/views/index", function(req, res){
    var message = ' ';
    res.render('views/index', {message:message});
});


//rota para cadastro
app.get('/views/cadastro', (req, res)=>{
    res.redirect('../');
    //res.render('views/cadastro', {message:message});
});


//método post do login
app.post('/log', function (req, res){
    //pega os valores digitados pelo usuário
    var username = req.body.username;
    var password = req.body.password;

    //conexão com banco de dados
    var con = conectiondb();

    //query de execução
    var query = 'SELECT * FROM usuarios WHERE nome_usuario = ? AND password = ?';
    
    //execução da query
    con.query(query, [username, password], function (err, results){
        if (results.length > 0){
            req.session.user = username; //seção de identificação            
            console.log("Login feito com sucesso!");
            res.render('views/joguinho', {message:results});
        }else{
            var message = 'Login incorreto!';
            res.render('views/index', { message: message });
        }
    });
});