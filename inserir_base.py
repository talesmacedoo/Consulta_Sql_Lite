import pandas as pd
import sqlite3
from time import sleep

# Caminho para a pasta local do db
caminho_banco = r'C:\caminho_para_o_banco.db'


conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

dados = pd.read_excel(r'C:\caminho_para_planilha.xlsx')
contador = 1

for index,row in dados.iterrows():
    
    convenio_atual = str(row["CONVENIO"])
    cpf_atual = str(row["CPF"])
    if len(cpf_atual) < 11:
        #if para formatar o Cpf caso ele não tenha 11 dígitos
        cpf_atual = (11-len(cpf_atual))*"0" + cpf_atual
    sleep(0.2)   
    nome_atual =  str(row["NOME"])
    celular_atual1 = str(row["CELULAR1"])
    celular_atual1 = celular_atual1.replace(".0","")

    celular_atual2 = str(row["CELULAR2"])
    celular_atual2 = celular_atual2.replace(".0","")    

    celular_atual3 = str(row["CELULAR3"])
    celular_atual3 = celular_atual3.replace(".0","")

    celular_atual4 = str(row["CELULAR4"])
    celular_atual4 = celular_atual4.replace(".0","")

    email_atual = str(row["EMAIL1"])

    data_nascimento_atual = str(row["DATA DE NASCIMENTO"])
    obito_atual = str(row["OBITO"])
    data_higienizacao_atual = str(row["DATA HIGIENIZACAO"])

    cursor.execute('''
    INSERT INTO clientes (convenio, nome, cpf, telefone1, telefone2, telefone3, telefone4, email, data_nascimento, obito, data_consulta)
    VALUES (?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?)
    ''', (convenio_atual ,nome_atual, cpf_atual, celular_atual1, celular_atual2, celular_atual3, celular_atual4, email_atual, data_nascimento_atual, obito_atual, data_higienizacao_atual))
 
    conexao.commit()
    print(str(contador) + " Dados inseridos " + cpf_atual + ";" + nome_atual + ";" + celular_atual1 + ";" + celular_atual2 + ";" + celular_atual3 + ";" + celular_atual4 + ";" + email_atual + ";" + data_nascimento_atual + ";" + obito_atual + ";" + data_higienizacao_atual)
    contador += 1


conexao.commit()
conexao.close()

print("Todos os dados foram inseridos com sucesso!")