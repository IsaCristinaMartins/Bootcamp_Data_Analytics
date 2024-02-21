#Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a
#30 anos.
#b) Calcule o saldo médio dos clientes.
#c) Encontre o cliente com o saldo máximo.
#d) Conte quantos clientes têm saldo acima de 1000.

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

idade = cursor.execute('SELECT nome, idade FROM clientes WHERE idade >30 ')
for clientes in idade:
	print(clientes)

# b) Calcule o saldo médio dos clientes.

cursor.execute('SELECT AVG(saldo) FROM clientes')



# c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT cliente_id, AVG(saldo) AS saldo_medio FROM transacoes GROUP BY cliente_id')


# d) Conte quantos clientes têm saldo acima de 1000.

saldo = cursor.execute('SELECT nome, idade FROM clientes WHERE saldo > 1000 ')
for clientes in saldo:
	print(clientes)



conexao.commit()
conexao.close