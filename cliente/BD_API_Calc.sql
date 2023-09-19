CREATE DATABASE apiViss;
USE apiViss;

CREATE USER 'viss'@'localhost' IDENTIFIED BY 'urubu100';
GRANT INSERT, SELECT, UPDATE, DELETE ON apiViss.* TO 'viss'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE registro(
	idRegistro INT PRIMARY KEY AUTO_INCREMENT,
    usoCpu DECIMAL(5,2),
	usoRam DECIMAL(5,2),
    usoDisco DECIMAL(5,2),
    dataRegistro DATETIME
);

SELECT * FROM registro;