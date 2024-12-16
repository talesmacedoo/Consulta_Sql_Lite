import pandas as pd
import sqlite3
from time import sleep

# Caminho para a pasta local do db
caminho_banco = r'caminho-banco'


conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

dados = pd.read_excel(".\BASE_CREDLINK_MAKTUB_09-12.xlsx")
contador = 1

for index,row in dados.iterrows():
    

    cpf_atual = str(row["CPF"])
    if len(cpf_atual) < 11:
        #if para formatar o Cpf caso ele não tenha 11 dígitos
        cpf_atual = (11-len(cpf_atual))*"0" + cpf_atual
       
    nome_atual =  str(row["NOME"])
    celular_atual = str(row["CELULAR"])
    celular_atual = celular_atual.replace(".0","")

    


    cursor.execute('''
    INSERT INTO clientes (nome, cpf, telefone)
    VALUES (?, ?, ?)
    ''', (nome_atual, cpf_atual, celular_atual))

    conexao.commit()
    print(str(contador) + " Dados inseridos " + cpf_atual + ";" + nome_atual + ";" + celular_atual)
    contador += 1


conexao.commit()
conexao.close()

print("Todos os dados foram inseridos com sucesso!")