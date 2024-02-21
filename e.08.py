"""
Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). Insira algumas
compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra.
"""

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


# Crie uma segunda tabela chamada "compras"
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

# Insira algumas compras associadas a clientes existentes na tabela "clientes".


cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, "Maria do Carmo", 1, "Bolsa couro", 25.67)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, "Carmo", 2,"Bolsa conchinha", 75.7)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, "zé", 3, " carteira de couro", 50.47)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, "Socorro", 4, "Bota de couro", 270.66)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (5, "Bia", 5,"sapato", 256.67)')

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

consulta = cursor.execute('SELECT nome, produto, valor FROM clientes ')
for clientes in consulta:
    print(clientes)


conexao.commit()
conexao.close