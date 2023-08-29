CREATE DATABASE VISS;

USE VISS;
CREATE TABLE empresa(
IdEmpresa INT PRIMARY KEY AUTO_INCREMENT,
razao VARCHAR(45) NOT NULL,
CNPJ VARCHAR(19)  NOT NULL UNIQUE,
email VARCHAR(45) NOT NULL UNIQUE) AUTO_INCREMENT = 1;

CREATE TABLE endereco(
IdEndereco INT PRIMARY KEY AUTO_INCREMENT,
logradouro VARCHAR(45) NOT NULL,
numeroEndereco INT NOT NULL,
bairro VARCHAR(45),
complemento VARCHAR(45),
cidade VARCHAR(45)) AUTO_INCREMENT = 100;

CREATE TABLE filial(
IdFilial INT PRIMARY KEY AUTO_INCREMENT,
telefoneFilial CHAR(11) NOT NULL,
fkEndereco INT, FOREIGN KEY(fkEndereco) references endereco(IdEndereco),
fkEmpresa INT, FOREIGN KEY(fkEmpresa) REFERENCES empresa(IdEmpresa))AUTO_INCREMENT = 10;

CREATE TABLE setor(
IdSetor INT PRIMARY KEY AUTO_INCREMENT,
nomeSetor VARCHAR(45) NOT NULL,
fkFilial INT, FOREIGN KEY(fkFilial) REFERENCES filial(IdFilial))AUTO_INCREMENT = 200;

CREATE TABLE funcionario(
IdFuncionario INT PRIMARY KEY AUTO_INCREMENT,
nomeFuncionario VARCHAR(45) NOT NULL,
telefoneFuncionario VARCHAR(45),
cpfGestor VARCHAR(14),
emailFuncionario VARCHAR(45) NOT NULL,
fkEmpresa INT, FOREIGN KEY(fkEmpresa) REFERENCES empresa(IdEmpresa),
senhaGestor VARCHAR(45),
fkGestor INT, FOREIGN KEY(fkGestor) REFERENCES funcionario(IdFuncionario)
)AUTO_INCREMENT = 1000;


CREATE TABLE computadores(
IdComputador INT PRIMARY KEY AUTO_INCREMENT,
patrimonio VARCHAR(45),
fkFuncionario INT, FOREIGN KEY(fkFuncionario) REFERENCES funcionario(IdFuncionario))AUTO_INCREMENT = 3000;

CREATE TABLE softwares(
IdSoftwares INT PRIMARY KEY AUTO_INCREMENT,
nomeSoftware VARCHAR(45) NOT NULL,
usuario VARCHAR(45) NOT NULL,
cartegoriaSoftware VARCHAR(45))AUTO_INCREMENT = 2300;


CREATE TABLE computadoresSoftwares(
idComputadoresSoftwares INT NOT NULL AUTO_INCREMENT,
FKidComputador INT, FOREIGN KEY(FKidComputador) REFERENCES computadores(IdComputador),
FKidSoftware INT, FOREIGN KEY(FKidSoftware) REFERENCES softwares(IdSoftwares),
PRIMARY KEY(idComputadoresSoftwares, FKidComputador, FKidSoftware),
usuario VARCHAR(45) NOT NULL,
bloqueado VARCHAR(2))AUTO_INCREMENT = 3000;


CREATE TABLE componentes(
IdComponente INT PRIMARY KEY AUTO_INCREMENT,
tipo VARCHAR(50) NOT NULL,
fkComputadores INT, FOREIGN KEY(fkComputadores) REFERENCES computadores(IdComputador)
)AUTO_INCREMENT = 4000;

CREATE TABLE chamados(
idChamado INT PRIMARY KEY AUTO_INCREMENT,
cartegoriaChamado VARCHAR(45) NOT NULL,
descricaoChamado VARCHAR(250),
fkComputadoresSoftwares INT, FOREIGN KEY(fkComputadoresSoftwares) REFERENCES computadoresSoftwares(idComputadoresSoftwares),
fkComponentes INT, FOREIGN KEY(fkComponentes) REFERENCES componentes(IdComponente))AUTO_INCREMENT = 1500;

CREATE TABLE registros(
IdRegistro INT PRIMARY KEY AUTO_INCREMENT,
emUso VARCHAR(10),
temperatura VARCHAR(5),
fkComponentes INT, FOREIGN KEY(fkComponentes) REFERENCES componentes(IdComponente))AUTO_INCREMENT = 5000;





