import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


#cursor.execute('CREATE TABLE produtos (id INT, nome VARCHAR(100), endereco VARCHAR (100), email VARCHAR(100));')
#cursor.execute('DROP TABLE produtos')
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR (100), email VARCHAR(100));')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT')

#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1, "Isabel", "Fortaleza", "nemligo@gmail.com", 654321)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1, "Isabel", "Fortaleza", "nemligo@gmail.com", 654321)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (2, "Bela", "Fortaleza", "nemligo@gmail.com", 654321)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (3, "Ed", "Fortaleza", "nemligo@gmail.com", 654321)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (4, "Mabely", "Fortaleza", "nemligo@gmail.com", 654321)')
#cursor.execute('DELETE FROM usuario WHERE id=1')

dados = cursor.execute('SELECT * FROM usuario')
for usuario in dados:
	print(usuario)




conexao.commit()
conexao.close