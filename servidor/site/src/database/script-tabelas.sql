-- Arquivo de apoio, caso você queira criar tabelas como as aqui criadas para a API funcionar.
-- Você precisa executar os comandos no banco de dados para criar as tabelas,
-- ter este arquivo aqui não significa que a tabela em seu BD estará como abaixo!

/*
comandos para mysql - banco local - ambiente de desenvolvimento
*/

CREATE DATABASE teste1;

USE teste1;

create table usuario(
    -> id int primary key auto_increment ,
    -> nome varchar(80) ,
    -> email varchar(80) ,
    -> senha varchar(30) ,
    -> cpf char(11) ,
    -> telefone char(9));


