#Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#b) Remova um cliente pelo seu ID.

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#a) Atualize o saldo de um cliente específico.

cursor.execute('UPDATE alunos SET saldo = 2000,87 WHERE nome="bel"')

#b) Remova um cliente pelo seu ID.


cursor.execute('DELETE FROM cliente WHERE id=4')


conexao.commit()
conexao.close