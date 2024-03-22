drop database if exists PetShop;  -- Remove o banco de dados, caso exista
create database PetShop;          -- Cria o banco de dados
use PetShop;                      -- Seleciona o banco para os próximos comandos

/* As linhas acima não devem ser executas em serviços online como o sqlite oline*/


create table Especies (
	id				integer 			primary key auto_increment,
	nome			varchar(50)			unique  not null,
	alimentacao		varchar(20)
);

create table Animais (
	id				integer 			primary key auto_increment,
	nome			varchar(50) 		not null,
	data_nasc		date 				not null,
	peso			decimal(10,2)		check (peso > 0),
	cor				varchar(50),

	especie_id		int					references Especies(id)
);

/* Exercicios 1
Altere o nome do Pateta para Goofy;​										Altere o peso do Garfield para 10 quilogramas;​
Altere a cor de todos os gatos para laranja;​							Crie um campo altura para os animais;​
Crie um campo observação para os animais;​								Remova todos os animais que pesam mais que 200 quilogramas.​
Remova todos os animais que o nome inicie com a letra ‘C’.​				Remova o campo cor dos animais;​
Aumente o tamanho do campo nome dos animais para 80 caracteres;​			Remova todos os gatos e cachorros.​
Remova o campo data de nascimento dos animais​							Remova a tabela espécies.​											Remova todos os animais.
*/

SELECT * FROM Animais;
SELECT * FROM Especies;

UPDATE Animais SET nome = 'Goofy' WHERE nome = 'Pateta';
SELECT * FROM Animais WHERE nome = 'Goofy';

UPDATE Animais SET peso = 10 WHERE nome = 'Garfield';
SELECT * FROM Animais WHERE nome = 'Garfield';

UPDATE Animais SET cor = 'laranja' WHERE especie_id = 1;
SELECT * FROM Animais WHERE especie_id = 1;

ALTER TABLE Animais ADD COLUMN altura decimal(6,2);
SELECT * FROM Animais;

ALTER TABLE Animais ADD COLUMN observacao varchar(30);
SELECT * FROM Animais;

DELETE FROM Animais WHERE peso > 200;
SELECT * FROM Animais WHERE peso > 199;

DELETE FROM Animais WHERE nome like 'C%';
SELECT * FROM Animais WHERE nome like 'C%';

ALTER TABLE Animais DROP COLUMN cor;
SELECT * FROM Animais;

ALTER TABLE Animais MODIFY nome varchar(80);

DELETE FROM Animais WHERE especie_id in (1, 2);
SELECT * FROM Animais WHERE especie_id in (1,2);

ALTER TABLE Animais DROP COLUMN data_nasc;
SELECT * FROM Animais;

DROP TABLE Especies;

DELETE FROM Animais;
SELECT * FROM Animais;

/* Exercicios 2
Selecione quantos produtos cada marca possui.​
Selecione o preço médio dos produtos de cada marca.​
Selecione a média dos preços e total em estoque dos produtos agrupados por marca.​
Selecione quantos produtos estão cadastrados.​
Selecione o preço médio dos produtos.​
Selecione a média dos preços dos produtos em 2 grupos: perecíveis e não perecíveis.​
Selecione a média dos preços dos produtos agrupados pelo nome do produto.​
Selecione a média dos preços e total em estoque dos produtos.​
Selecione o nome, marca e quantidade em estoque do produto mais caro.​
Selecione os produtos com preço acima da média.​
Selecione a quantidade de produtos de cada nacionalidade.
*/

drop database if exists Empresa;
create database Empresa;
use Empresa;


create table marcas (
	marca_id		int 			auto_increment		primary key,
	nome_marca		varchar(50)		not null,			
	origem			varchar(50)		
);

create table produtos (

	prod_id			int 			auto_increment 		primary key,
	nome_prod		varchar(50)		not null,
	qtd_estoque		int				not null 			default 0,
	estoque_mim		int 			not null			default 0,
	data_fabricacao	timestamp 							default now(),
	perecivel		boolean,
	valor			decimal(10,2),
	
	marca_id		int		references marcas(marca_id)
);

create table fornecedores (
	forn_id			int 			auto_increment 		primary key,	
	nome_forn		varchar(50)		not null,
	email			varchar(50)		
);

create table produto_fornecedor (
	prod_id			int				not null	references produtos(prod_id),
	forn_id			int				not null	references fornecedores(forn_id),
	
	primary key (prod_id, forn_id)
);

SELECT * FROM marcas;
SELECT * FROM produtos;
SELECT * FROM fornecedores;
SELECT * FROM produto_fornecedor;

