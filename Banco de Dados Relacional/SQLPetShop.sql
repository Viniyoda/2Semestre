drop database if exists PetShop;  -- Remove o banco de dados, caso exista
create database PetShop;          -- Cria o banco de dados
use PetShop;                      -- Seleciona o banco para os próximos comandos

/* As linhas acima não devem ser executas em serviços online como o sqlite oline*/


create table Especies (
	id				int 			primary key identity,
	nome			varchar(50)			unique  not null,
	alimentacao		varchar(20)
);

create table Animais (
	id				int 			primary key identity,
	nome			varchar(50) 		not null,
	data_nasc		date 				not null,
	peso			decimal(10,2)		check (peso > 0),
	cor				varchar(50),

	especie_id		int					references Especies(id)
);

SELECT * FROM Animais;
SELECT * FROM Especies;

--Utilizamos INNER JOIN para juntar as tabelas
--1  Selecione o nome e a espécie de todos os animais​ VVV
SELECT A.nome, E.nome FROM Animais A INNER JOIN Especies E ON A.especie_id = E.id;

--2  Selecione todos os gatos laranja​ VVV
SELECT A.nome, E.nome, A.cor FROM Animais A INNER JOIN Especies E 
ON A.especie_id = E.id WHERE cor = 'laranja' AND E.nome = 'gato';

--3  Selecione todos os cachorros da cor amarelo​ VVV
SELECT A.nome, E.nome, A.cor FROM Animais A INNER JOIN Especies E
ON A.especie_id = E.id WHERE cor = 'amarelo' AND E.nome = 'cachorro';

--4  Selecione todos os animais aquáticos que pesam mais que 70 Kg​ VVV
SELECT A.nome, E.nome, A.peso FROM Animais A INNER JOIN Especies E
ON A.especie_id = E.id WHERE E.nome in 
('baleia', 'sardinha', 'bacalhau', 'tubarão', 'lambari', 'corvina', 'polvo', 'nautilus')
and peso > 70 ;

--5  Selecione todos os herbívoro ordenados pelos mais pesados​
SELECT A.nome, A.peso, E.nome FROM Animais A INNER JOIN Especies E
ON A.especie_id = E.id WHERE E.alimentacao = 'herbívoro' ORDER BY A.peso DESC;
--6  Selecione todos os carnívoro que são pretos e brancos​ VVV
SELECT A.nome, E.nome, A.cor, E.alimentacao FROM Animais A INNER JOIN Especies E
ON A.especie_id = E.id WHERE E.alimentacao = 'carnívoro' AND A.cor IN ('preto', 'branco');

--7  Selecione todos os onívoros que nasceram antes de 2013​ VVV
SELECT A.nome, E.nome, A.data_nasc FROM Animais A INNER JOIN Especies E
ON A.especie_id = E.id WHERE E.alimentacao = 'onívoro' AND A.data_nasc < '2013-01-01';

--8  Selecione todos os mamíferos que pesam mais que 10 quilos e são marrons ou azul​ VVV
SELECT A.nome, E.nome, E.alimentacao, A.cor, A.peso FROM Animais A INNER JOIN Especies E
ON A.especie_id = E.id WHERE A.cor in ('marrom', 'azul') and A.peso > 10;

--9  Selecione a quantidade total de animais​ VVV
SELECT count(*) FROM Animais;

--10 Se somarmos os pesos de todos os gatos, qual será o resultado? VVV
SELECT sum(peso) FROM Animais A INNER JOIN Especies E ON A.especie_id = E.id WHERE E.nome = 'gato';







-- Inserções com alimentação especificada
insert into Especies (nome, alimentacao) values ('gato', 'carnívoro');
insert into Especies (nome, alimentacao) values ('cachorro', 'carnívoro');
insert into Especies (nome, alimentacao) values ('morcego', 'onívoro');
insert into Especies (nome, alimentacao) values ('rato', 'onívoro');
insert into Especies (nome, alimentacao) values ('ramister', 'herbívoro');
insert into Especies (nome, alimentacao) values ('baleia', 'carnívoro');
insert into Especies (nome, alimentacao) values ('sardinha', 'herbívoro');
insert into Especies (nome, alimentacao) values ('bacalhau', 'herbívoro');
insert into Especies (nome, alimentacao) values ('tubarão', 'carnívoro');
insert into Especies (nome, alimentacao) values ('lambari', 'herbívoro');
insert into Especies (nome, alimentacao) values ('corvina', 'herbívoro');
insert into Especies (nome, alimentacao) values ('iguana', 'herbívoro');
insert into Especies (nome, alimentacao) values ('camaleão', 'herbívoro');
insert into Especies (nome, alimentacao) values ('lagarto', 'herbívoro');
insert into Especies (nome, alimentacao) values ('cobra', 'carnívoro');
insert into Especies (nome, alimentacao) values ('cacatua', 'herbívoro');
insert into Especies (nome, alimentacao) values ('pardal', 'onívoro');
insert into Especies (nome, alimentacao) values ('bentevi', 'herbívoro');
insert into Especies (nome, alimentacao) values ('canario', 'herbívoro');

-- Inserções sem alimentação especificada
insert into Especies (nome) values ('virus');
insert into Especies (nome) values ('bactéria');

-- Inserções sem alimentação nem id especificados
insert into Especies (nome) values ('barata');
insert into Especies (nome) values ('carcará');
insert into Especies (nome) values ('polvo');
insert into Especies (nome) values ('nautilus');



-- Inserções na tabela Animais
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('ágata'         , '2015-04-09', 13.9, 'branco'  , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('félix'         , '2016-06-06', 14.3, 'preto'   , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('tom'           , '2013-02-08', 11.2, 'azul'    , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('garfield'      , '2015-07-06', 17.1, 'laranja' , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('frajola'       , '2013-08-01', 13.7, 'preto'   , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('manda-chuva'   , '2012-02-03', 12.3, 'amarelo' , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('snowball'      , '2014-04-06', 13.2, 'preto'   , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('ágata'         , '2015-08-03', 11.9, 'azul'    , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('ágata'         , '2016-03-04', 18.6, 'roxo'    , 1);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('gato de botas' , '2012-12-10', 11.6, 'amarelo' , 1);

insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('bola de pelo'  , '2020-04-06', 11.6, 'amarelo' , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('milu'          , '2013-02-04', 17.9, 'branco'  , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('pluto'         , '2012-01-03', 12.3, 'amarelo' , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('pateta'        , '2015-05-01', 17.7, 'preto'   , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('snoopy'        , '2013-07-02', 18.2, 'branco'  , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('bidu'          , '2012-09-08', 12.4, 'azul'    , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('dum dum'       , '2015-04-06', 11.2, 'laranja' , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('muttley'       , '2011-02-03', 14.3, 'laranja' , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('scooby'        , '2012-01-02', 19.9, 'marrom'  , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('rufus'         , '2014-04-05', 19.7, 'branco'  , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('costelinha'    , '2016-05-02', 13.4, 'branco'  , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('coragem'       , '2013-07-08', 12.2, 'vermelho', 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('jake'          , '2012-02-07', 11.6, 'vermelho', 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('k900'          , '2012-11-25', 11.6, 'amarelo' , 2);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('gato de botas' , '2012-11-25', 11.6, 'amarelo' , 2);

insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('jerry'         , '2010-02-04', 06.6, 'laranja' , 4);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('ligeirinho'    , '2011-05-03', 04.4, 'amarelo' , 4);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('mikey'         , '2012-07-01', 02.2, 'preto'   , 4);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('minie'         , '2013-09-03', 03.2, 'preta'   , 4);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('topo gigio'    , '2016-06-08', 05.5, 'amarelo' , 4);

insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('bafo de onça'  , '2016-06-08', 05.5, 'amarelo' , null);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('susan murphy' , '2016-06-08', 05.5, 'amarelo', null);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('insectosauro' , '2016-06-08', 05.5, 'amarelo', null);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('gallaxhar'    , '2016-06-08', 05.5, 'amarelo', null);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('hathaway'     , '2016-06-08', 05.5, 'amarelo', null);

insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('tutubarão'    , '2010-02-06', 101.9, 'branca' , 9);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('prof. pardal' , '2012-04-04', 1.7  , 'amarelo', 17);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('mobie'        , '2014-05-02', 5069.4, 'branca' , 6);
insert into Animais (nome, data_nasc, peso, cor, especie_id) values ('batman'       , '2013-07-01', 96.1 , 'preto'  , 3);

SELECT * FROM Animais;
SELECT * FROM Especies;