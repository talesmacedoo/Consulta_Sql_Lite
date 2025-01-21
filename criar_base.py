import sqlite3
import os

# Defina o caminho para a pasta compartilhada na rede
caminho_banco = r'C:\caminho_para_o_banco.db'

# Verifique se o caminho da pasta existe
if not os.path.exists(os.path.dirname(caminho_banco)):
    print("A pasta compartilhada não existe!")
else:
    # Conecte ou crie o banco de dados na pasta compartilhada
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    # Exemplo de criação de tabela
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        convenio TEXT,
        nome TEXT,
        cpf TEXT,
        telefone1 TEXT,
        telefone2 TEXT,
        telefone3 TEXT,
        telefone4 TEXT,
        email TEXT,
        data_nascimento TEXT,
        obito TEXT,
        data_consulta TEXT                                                                       
    )
    ''')

    # Commit e fechamento
    conexao.commit()
    conexao.close()
    print("Banco de dados e tabela criados com sucesso!")
