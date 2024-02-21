#  Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#c) Selecionar os alunos do curso de "Engenharia" em ordem
#alfabética.
#d) Contar o número total de alunos na tabela

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


#a) Selecionar todos os registros da tabela "alunos".

dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
	print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
	

dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade >20 ')
for alunos in dados:
	print(alunos)


#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética. obs: Mudei o nome pra engenheiro pq por acaso eu tinha colocado engenheiro...
	

dados = cursor.execute('SELECT nome FROM alunos WHERE curso ="engenheiro" ')
for alunos in dados:
	print(alunos)

#d) Contar o número total de alunos na tabela


contagem = cursor.execute('SELECT COUNT(id) FROM alunos')
for alunos in contagem:
    print(alunos)


conexao.commit()
conexao.close