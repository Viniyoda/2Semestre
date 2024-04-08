use empresa;
SELECT * FROM produtos;
SELECT * FROM marcas;

#Crie uma view que mostra todos os produtos e seus respectivos fornecedores e marcas.
CREATE VIEW prod_forn_marc AS 
	SELECT
    P.prod_id, P.nome_prod,
    P.qtd_estoque, P.estoque_mim,
    P.data_fabricacao, P.perecivel,
    P.valor, M.marca_id,
    M.nome_marca, M.origem,
    F.nome_forn, F.email
    FROM produtos P 
    INNER JOIN marcas M ON P.marca_id = M.marca_id
    INNER JOIN produto_fornecedor PF ON P.prod_id = PF.prod_id
    INNER JOIN fornecedores F ON PF.forn_id = F.forn_id;
    
SELECT * FROM prod_forn_marc;

#Crie uma view que mostra todos os produtos com estoque abaixo do mínimo.  
CREATE VIEW prod_abaxmin AS
	SELECT prod_id, nome_prod, qtd_estoque 
    FROM produtos 
    WHERE qtd_estoque < estoque_mim
    ORDER BY qtd_estoque DESC;
    
SELECT * FROM prod_abaxmin;

#Adicione o campo data de validade. Insira novos produtos com essa informação.
ALTER TABLE produtos ADD COLUMN data_validade DATE;
INSERT INTO produtos (nome_prod, valor, data_validade)
	VALUES ('Cola', 10, '2024-12-31'),
	('Cola bastao', 12, '2025-06-30'),
	('Doritos', 18, '2023-09-15');
    
SELECT * FROM produtos WHERE nome_prod in ('Cola', 'Cola bastao', 'Doritos');

#Crie uma view que mostra todos os produtos e suas respectivas marcas com validade vencida.
CREATE VIEW prod_vencido AS
	SELECT P.prod_id, P.nome_prod, P.marca_id, P.data_validade 
    FROM produtos P
    WHERE P.data_validade < CURDATE();
    
SELECT * FROM prod_vencido;

#Selecionar os produtos com preço acima da média.
CREATE VIEW prod_acimedia AS
	SELECT prod_id, nome_prod, valor 
    FROM produtos 
    WHERE valor > (SELECT AVG(valor) FROM produtos)
    ORDER BY valor DESC;
    
SELECT * FROM prod_acimedia;

#######################################################################################################################

#Crie uma SP que exibe o preço médio dos produtos.
DELIMITER //
CREATE PROCEDURE valor_medio()
BEGIN
	DECLARE preco_medio DECIMAL(10, 2); #Declara uma variavel para armazenar o valor
	SELECT AVG(valor) INTO preco_medio FROM produtos;
    SELECT CONCAT('O preço médio dos produtos é: ', preco_medio) AS 'Preço Médio';
END//
DELIMITER ;

CALL valor_medio();

#Crie uma SP que ao se passar uma marca como parâmetro retorna todos os produtos daquela marca.
DELIMITER //
CREATE PROCEDURE prod_das_marcas (IN nome_marca varchar(50))
BEGIN
	SELECT P.*
    FROM produtos P
    JOIN marcas M ON P.marca_id = M.marca_id
    WHERE M.nome_marca = nome_marca;
END//
DELIMITER ;

CALL prod_das_marcas ('Lenovo');

#Crie uma SP que receba dois valores (um menor e outro maior)
#como parâmetro e retorne todos os produtos com a quantidade dentro do intervalo dos dois valores fornecidos como parâmetros.

#Crie uma SP onde após um novo registro na tabela produto_fornecedor for criado,
#ele exibe o nome do produto e o nome do fornecedor que acabou de ser registrado.
DELIMITER //
CREATE PROCEDURE exibir_novo_registro()
BEGIN
	DECLARE produto_nome VARCHAR(50);
    DECLARE fornecedor_nome VARCHAR(50);
    
    SELECT P.nome_prod, F.nome_forn
    INTO produto_nome, fornecedor_nome
    FROM produtos P
    JOIN produto_fornecedor PF ON P.prod_id = PF.prod_id
    JOIN fornecedores F ON PF.forn_id = F.forn_id;
	
    SELECT CONCAT('Novo registro: Produto ', produto_nome, ' - Fornecedor ', fornecedor_nome) AS 'Novo Registro';
END//
DELIMITER ;

#Crie uma SP que receba como parâmetro o nome de um fornecedor e insira automaticamente o nome
#do fornecedor e um e-mail no formato nome_fornecedor@nome_fornecedor.com.br na tabela fornecedores
DELIMITER //
CREATE PROCEDURE auto_forn_email(IN nome_fornecedor varchar(50))
BEGIN
	DECLARE email_fornecedor VARCHAR(100);
    SET email_fornecedor = CONCAT(nome_fornecedor, '@', REPLACE(nome_fornecedor, ' ', ''), '.com.br');
	INSERT INTO fornecedores (nome_forn, email) VALUES (nome_fornecedor, email_fornecedor);
END//
DELIMITER ;

CALL auto_forn_email('primeinventory');
SELECT * FROM fornecedores WHERE nome_forn = 'primeinventory';