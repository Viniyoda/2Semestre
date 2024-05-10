CREATE DATABASE joguinhodb;

USE joguinhodb;

CREATE TABLE usuarios (
	usuario_id				INT AUTO_INCREMENT PRIMARY KEY,
    nome_usuario			varchar(100),
    senha_usuario			varchar(100)
);

CREATE TABLE jogo (
	jogo_id					INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id				INT,
    vida_heroi				DOUBLE,
    vida_vilao				DOUBLE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);

DELIMITER //
CREATE TRIGGER after_usuarios_insert
AFTER INSERT ON usuarios
FOR EACH ROW
BEGIN
    INSERT INTO jogo (usuario_id, vida_heroi, vida_vilao)
    VALUES (NEW.usuario_id, 100, 100);
END//
DELIMITER ;