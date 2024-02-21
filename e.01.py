#Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#Criando a tabela Aluno
#cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT (2), curso VARCHAR(100));')


#Testando a inserção de alguns dados. 
cursor.execute('INSERT INTO alunos(id, nome, idade, curso ) VALUES (1, "Isabel", 35, "fisioterapia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Bela", 8, "ser linda")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Ed", 39, "engenheiro")')

conexao.commit()
conexao.close