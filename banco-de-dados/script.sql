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
IdFilial INT AUTO_INCREMENT,
telefoneFilial CHAR(11) NOT NULL,
fkEndereco INT, FOREIGN KEY(fkEndereco) references endereco(IdEndereco),
fkEmpresa INT, FOREIGN KEY(fkEmpresa) REFERENCES empresa(IdEmpresa))AUTO_INCREMENT = 10;

CREATE TABLE setor(
IdSetor INT AUTO_INCREMENT,
nomeSetor VARCHAR(45) NOT NULL,
fkFilial INT, FOREIGN KEY(fkFilial) REFERENCES filial(IdFilial))AUTO_INCREMENT = 200;

CREATE TABLE funcionario(
IdFuncionario INT PRIMARY KEY AUTO_INCREMENT,
nomeFuncionario VARCHAR(45) NOT NULL,
telefone VARCHAR(12),
CPF VARCHAR(15) NOT NULL,
email VARCHAR(45) NOT NULL,
fkSetor INT, FOREIGN KEY(fkSetor) REFERENCES setor(IdSetor))AUTO_INCREMENT = 1000;

CREATE TABLE usuario(
IdUsuario INT PRIMARY KEY AUTO_INCREMENT,
nomeUsuario VARCHAR(45) NOT NULL,
emailUsuario VARCHAR(45) NOT NULL,
senhaUsuario VARCHAR(45) NOT NULL,
fkFuncionario INT, FOREIGN KEY(fkFuncionario) REFERENCES funcionario(IdFuncionario))AUTO_INCREMENT = 1100;

