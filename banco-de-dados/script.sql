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

CREATE TABLE gestor(
IdGestor INT PRIMARY KEY AUTO_INCREMENT,
nomeGestor VARCHAR(45) NOT NULL,
telefone VARCHAR(12),
CPF VARCHAR(15) NOT NULL,
email VARCHAR(45) NOT NULL,
fkSetor INT, FOREIGN KEY(fkSetor) REFERENCES setor(IdSetor))AUTO_INCREMENT = 1000;

CREATE TABLE funcionario(
IdFuncionario INT PRIMARY KEY AUTO_INCREMENT,
nomeFuncionario VARCHAR(45) NOT NULL,
emailFuncionario VARCHAR(45) NOT NULL,
senhaFuncionario VARCHAR(45) NOT NULL,
fkGestor INT, FOREIGN KEY(fkGestor) REFERENCES gestor(IdGestor))AUTO_INCREMENT = 1100;

CREATE TABLE computadores(
IdComputador INT PRIMARY KEY AUTO_INCREMENT,
patrimonio VARCHAR(45),
fkFuncionario INT, FOREIGN KEY(fkFuncionario) REFERENCES funcionario(IdFuncionario))AUTO_INCREMENT = 3000;

CREATE TABLE softwares(
IdSoftwares INT PRIMARY KEY AUTO_INCREMENT,
nomeSoftware VARCHAR(45) NOT NULL,
cartegoriaSoftware VARCHAR(45))AUTO_INCREMENT = 2300;

CREATE TABLE chamados(
IdChamado INT PRIMARY KEY AUTO_INCREMENT,
cartegoriaChamado VARCHAR(45),
descricaoChamado VARCHAR(300))AUTO_INCREMENT = 3300;

CREATE TABLE computadoresSoftwares(
FKidComputador INT, FOREIGN KEY(FKidComputador) REFERENCES computadores(IdComputador),
FKidSoftware INT, FOREIGN KEY(FKidSoftware) REFERENCES softwares(IdSoftwares),
PRIMARY KEY(FKidComputador, FKidSoftware),
softwaresLiberados VARCHAR(45),
FKidChamado INT, FOREIGN KEY(FKidChamado) REFERENCES chamados(IdChamado));

CREATE TABLE peca(
IdPeca INT PRIMARY KEY AUTO_INCREMENT,
valor DOUBLE NOT NULL,
modelo VARCHAR(45) NOT NULL,
fkChamado INT, FOREIGN KEY(fkChamado) REFERENCES chamados(IdChamado))AUTO_INCREMENT = 5000;

CREATE TABLE componentes(
IdComponente INT PRIMARY KEY AUTO_INCREMENT,
tipo VARCHAR(50) NOT NULL,
fkComputadores INT, FOREIGN KEY(fkComputadores) REFERENCES computadores(IdComputador),
fkPeca INT, FOREIGN KEY(fkPeca) REFERENCES peca(IdPeca)
)AUTO_INCREMENT = 4000;




