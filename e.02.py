#Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.
import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()



cursor.execute('INSERT INTO alunos(id, nome, idade, curso ) VALUES (1, "Isabel", 35, "fisioterapia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Bela", 8, "ser linda")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Ed", 39, "engenheiro")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso ) VALUES (4, "Isabela", 5, "terapia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Bel", 80, "ser perfeita")')











conexao.commit()
conexao.close