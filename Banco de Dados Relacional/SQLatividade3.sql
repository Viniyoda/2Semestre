use empresa;

#Crie uma view que mostra todos os produtos e seus respectivos fornecedores e marcas.
CREATE VIEW prod_forn_marc AS 
	SELECT 
    P.prod_id, P.nome_prod, 
    M.nome_marca, F.nome_forn  
	FROM produtos P 
    INNER JOIN marcas M ON P.marca_id = M.marca_id
    INNER JOIN fornecedores F;
    
SELECT * FROM prod_forn_marc;

#Crie uma view que mostra todos os produtos com estoque abaixo do mínimo.  
CREATE VIEW prod_abaxmin AS
	SELECT prod_id, nome_prod, qtd_estoque 
    FROM produtos 
    WHERE qtd_estoque < estoque_mim
    ORDER BY qtd_estoque DESC;
    
SELECT * FROM prod_abaxmin;

#Adicione o campo data de validade. Insira novos produtos com essa informação.

#Crie uma view que mostra todos os produtos e suas respectivas marcas com validade vencida.

#Selecionar os produtos com preço acima da média.
CREATE VIEW prod_acimedia AS
	SELECT prod_id, nome_prod, valor 
    FROM produtos 
    WHERE valor > (SELECT AVG(valor) FROM produtos)
    ORDER BY valor DESC;
    
SELECT * FROM prod_acimedia;
    
    
    
    
    
