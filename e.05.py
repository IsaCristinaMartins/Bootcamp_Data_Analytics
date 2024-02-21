#Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Criar uma Tabela e Inserir Dados

#cursor.execute('CREATE TABLE pacientes (id INT, nome VARCHAR(100), idade INT(2), patologia VARCHAR(100), qntatendimentos INT(2)) ')

#Testando a inserção de alguns dados. 
#cursor.execute('INSERT INTO pacientes(id, nome, idade, patologia, qnt_atendimentos ) VALUES (1, "Zé", 87, "pneumonia", 2)')
#cursor.execute('INSERT INTO pacientes(id, nome, idade, patologia, qnt_atendimentos) VALUES (2, "João", 54, "reabilitação", 3)')
#cursor.execute('INSERT INTO pacientes(id, nome, idade, patologia, qnt_atendimentos) VALUES (3, "Maria", 81, "cancer", 4)')
#cursor.execute('INSERT INTO pacientes(id, nome, idade, patologia, qnt_atendimentos ) VALUES (4, "Fê", 65, "canelite", 2)')
#cursor.execute('INSERT INTO pacientes(id, nome, idade, patologia, qnt_atendimentos) VALUES (5, "Camila", 46, "dor na lombar", 3)')
#cursor.execute('INSERT INTO pacientes(id, nome, idade, patologia, qnt_atendimentos) VALUES (6, "Maria do Carmo", 15, "bronquite", 1)')





# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 



cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT(2), saldo FLOAT(1))')

# Insira alguns registros de clientes na tabela.
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Maria do Carmo", 15, 100)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Carmo", 35, 600)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "zé", 56, 450)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Socorro", 45, 2200.25)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Bia", 10, 900.36)')



conexao.commit()
conexao.close