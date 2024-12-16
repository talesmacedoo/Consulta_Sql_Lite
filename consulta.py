import sqlite3

class Consulta():
    def __init__(self, telefone):
        self.caminho_banco =  r'\\server-mkt\DOC.DIGITAIS\CPD_B.I\arquivo de dados\telefones_maktub.db'
        self.telefone_consulta = telefone


    def consultar(self):
        """
        Realiza a consulta no banco de dados da rede para um determinado telefone
        """
        conexao = sqlite3.connect(self.caminho_banco)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM clientes WHERE telefone='"+str(self.telefone_consulta)+"'")
        dados = cursor.fetchall()

        conexao.close()

        return dados
    

    def tratar_dados(self, dados):
        try:
            print(dados)
            nome_cliente = dados[0][1]
            cpf_cliente = dados[0][2]
            celular_cliente = dados[0][3]
            dados_tratados = "NOME: " + nome_cliente + "\nCPF: " +  cpf_cliente + "\nCELULAR: " + celular_cliente
        except:
            dados_tratados = "CLIENTE NÃO ENCONTRADO"
        return dados_tratados
