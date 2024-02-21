# Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#b) Remova um aluno pelo seu ID.

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#a) Atualize a idade de um aluno específico na tabela.

cursor.execute('UPDATE alunos SET idade = 55 WHERE nome="Isabel"')



#b) Remova um aluno pelo seu ID.

cursor.execute('DELETE FROM alunos WHERE id=2')



conexao.commit()
conexao.close