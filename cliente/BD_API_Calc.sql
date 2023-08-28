create database apiViss;
use apiViss;

CREATE USER 'viss'@'localhost' identified by 'urubu100';
GRANT INSERT, SELECT, UPDATE, DELETE ON apiViss.* to 'viss'@'localhost';
flush privileges;	

CREATE TABLE registro(
	idRegistro INT PRIMARY KEY AUTO_INCREMENT,
    usoCpu DECIMAL(5,2),
	usoRam DECIMAL(5,2),
    usoDisco DECIMAL(5,2),
    dataRegistro DATETIME
);

select * from registro;