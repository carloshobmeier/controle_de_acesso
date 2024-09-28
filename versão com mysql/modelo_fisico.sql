DROP DATABASE IF EXISTS controleAcesso;
CREATE DATABASE IF NOT EXISTS controleAcesso;

USE controleAcesso;

CREATE TABLE IF NOT EXISTS usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS permissoes (
    permissao_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    arquivo VARCHAR(255) NOT NULL,
    acao VARCHAR(10) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);
(2, 'notas.txt', 'escrever'),
(2, 'gabarito.txt', 'ler'),
(2, 'gabarito.txt', 'escrever');

