use empresa;

DELIMITER //

CREATE PROCEDURE estoqueBaixo (IN estoque INT)
BEGIN
    SELECT p.*, m.nome_marca
    FROM produtos p 
    LEFT JOIN marcas m ON m.marca_id = p.prod_id
    WHERE qtd_estoque < estoque;
END//

DELIMITER ;

call estoqueBaixo(100);

SET @estoqueMinimo_int := 100;
call estoqueBaixo(@estoqueMinimo_int);

