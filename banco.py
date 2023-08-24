import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("cadastro.db")
cur = conn.cursor()

# Verificar se a tabela já existe
cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='cadastroUsuario'")
table_exists = cur.fetchone()[0]

# Criar a tabela apenas se ela não existir
if not table_exists:
    cur.execute("CREATE TABLE cadastroUsuario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, data DATE, cidade TEXT, creci INTEGER, assunto TEXT)")

# Fechar a conexão com o banco de dados
conn.close()
