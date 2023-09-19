USE VISS;
INSERT INTO empresa (razao, CNPJ, email)
VALUES
    ('Empresa 1', '12345678901234', 'empresa1@email.com'),
    ('Empresa 2', '23456789012345', 'empresa2@email.com'),
    ('Empresa 3', '34567890123456', 'empresa3@email.com'),
    ('Empresa 4', '45678901234567', 'empresa4@email.com'),
    ('Empresa 5', '56789012345678', 'empresa5@email.com'),
    ('Empresa 6', '67890123456789', 'empresa6@email.com'),
    ('Empresa 7', '78901234567890', 'empresa7@email.com'),
    ('Empresa 8', '89012345678901', 'empresa8@email.com'),
    ('Empresa 9', '90123456789012', 'empresa9@email.com'),
    ('Empresa 10', '01234567890123', 'empresa10@email.com');
    
    
INSERT INTO endereco (logradouro, numeroEndereco, bairro, complemento, cidade)VALUES
    ('Rua Principal', 123, 'Bairro A', 'Apto 101', 'Cidade X'),
    ('Avenida Central', 456, 'Bairro B', 'Casa 202', 'Cidade Y'),
    ('Rua Secundária', 789, 'Bairro C', 'Sala 303', 'Cidade Z');


 INSERT INTO filial (telefoneFilial, fkEndereco, fkEmpresa)VALUES
    ('98765432101', 100, 1),
    ('98765432102', 101, 2),
    ('98765432119', 102, 3);    
    
INSERT INTO setor (nomeSetor, fkFilial)VALUES
    ('Departamento de Vendas', 19),
    ('Departamento de RH', 20),
    ('Departamento de TI', 21);
  
INSERT INTO funcionario (nomeFuncionario, telefoneFuncionario, cpfGestor, emailFuncionario, fkEmpresa, senhaGestor, fkGestor)VALUES
    ('João Silva', '987654321', NULL, 'joao@email.com', 1, 'senha123', NULL),
    ('Maria Santos', '987654322', NULL, 'maria@email.com', 2, 'senha456', NULL),
    ('Pedro Rocha', '987654339', NULL, 'pedro@email.com', 3, 'senha789', NULL);
    
INSERT INTO computadores (patrimonio, fkFuncionario)VALUES
    ('PC001', 1003),
    ('PC002', 1004),
    ('PC019', 1005);
    
INSERT INTO softwares (nomeSoftware, usuario, cartegoriaSoftware)VALUES
    ('Microsoft Office', 'user1', 'Produtividade'),
    ('Adobe Photoshop', 'user2', 'Design'),
    ('AutoCAD', 'user19', 'Engenharia');
    
INSERT INTO computadoresSoftwares (FKidComputador, FKidSoftware, usuario, bloqueado)VALUES
    (3006, 2300, 'user1', 'N'),
    (3007, 2301, 'user2', 'N'),
    (3008, 2302, 'user19', 'N');

INSERT INTO componentes (tipo, modelo, fkComputadores)VALUES
    ('CPU', 'Intel Core i7', 3006),
    ('GPU', 'NVIDIA 1060 3GB',3006),
    ('RAM', '8GB HyperX DDR4',3006),
    ('CPU', 'Celeron', 3007),
    ('GPU', 'NVIDIA GeForce RTX 3080', 3007),
    ('RAM', '16GB DDR4', 3008);
    
INSERT INTO registros (emUso, temperatura, dataRegistro, fkComponentes) VALUES
    (23, '72°C', '2023-09-16 10:00:00', 4000),
    (54, '55°C', '2023-09-16 11:00:00', 4001),
    (44, '', '2023-09-16 12:00:00', 4002),
    (43, '65°C', '2023-09-16 13:00:00', 4003),
    (75, '75°C', '2023-09-16 14:00:00', 4004);

INSERT INTO registros (temperatura, dataRegistro, fkComponentes) VALUES
    (50, '2023-09-16 15:00:00', 4005);

