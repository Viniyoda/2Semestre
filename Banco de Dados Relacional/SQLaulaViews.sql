use empresa;

CREATE VIEW Top10MaisCaros AS
SELECT prod_id, nome_prod, valor, qtd_estoque
FROM produtos
ORDER BY valor DESC
LIMIT 10;


SELECT * FROM top10maiscaros;

CREATE VIEW produtos_e_marcas AS
	SELECT
		produtos.nome_prod 'Nome do Produto',
		marcas.nome_marca 'Marca',
		produtos.valor 'Preço',
		produtos.qtd_estoque,
	case
		when produtos.perecivel = 0 then 'Não'
		when produtos.perecivel = 1 then 'SIM'
	end
	'Perecível'
	from produtos left join marcas
		ON produtos.marca_id = marcas.marca_id
		ORDER BY produtos.nome_prod;


SELECT * FROM produtos_e_marcas;




